const JPEG_MARKER_PREFIX = 0xff;

function matchesAscii(bytes, offset, text) {
  if (offset + text.length > bytes.length) return false;
  for (let index = 0; index < text.length; index += 1) {
    if (bytes[offset + index] !== text.charCodeAt(index)) return false;
  }
  return true;
}

function readExifOrientation(bytes, offset = 0) {
  let tiffOffset = offset;
  if (matchesAscii(bytes, offset, "Exif\0\0")) tiffOffset += 6;
  if (tiffOffset + 8 > bytes.length) return null;

  const littleEndian = bytes[tiffOffset] === 0x49 && bytes[tiffOffset + 1] === 0x49;
  const bigEndian = bytes[tiffOffset] === 0x4d && bytes[tiffOffset + 1] === 0x4d;
  if (!littleEndian && !bigEndian) return null;

  const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  const read16 = (position) => view.getUint16(position, littleEndian);
  const read32 = (position) => view.getUint32(position, littleEndian);
  if (read16(tiffOffset + 2) !== 42) return null;

  const ifdOffset = tiffOffset + read32(tiffOffset + 4);
  if (ifdOffset + 2 > bytes.length) return null;
  const entryCount = read16(ifdOffset);
  for (let index = 0; index < entryCount; index += 1) {
    const entryOffset = ifdOffset + 2 + index * 12;
    if (entryOffset + 12 > bytes.length) return null;
    if (read16(entryOffset) === 0x0112 && read16(entryOffset + 2) === 3 && read32(entryOffset + 4) === 1) {
      const orientation = read16(entryOffset + 8);
      return orientation >= 1 && orientation <= 8 ? orientation : null;
    }
  }
  return null;
}

function makeMinimalExif(orientation, includeExifPrefix) {
  const prefixLength = includeExifPrefix ? 6 : 0;
  const bytes = new Uint8Array(prefixLength + 26);
  if (includeExifPrefix) bytes.set([0x45, 0x78, 0x69, 0x66, 0, 0]);
  const offset = prefixLength;
  const view = new DataView(bytes.buffer);
  bytes[offset] = 0x4d;
  bytes[offset + 1] = 0x4d;
  view.setUint16(offset + 2, 42);
  view.setUint32(offset + 4, 8);
  view.setUint16(offset + 8, 1);
  view.setUint16(offset + 10, 0x0112);
  view.setUint16(offset + 12, 3);
  view.setUint32(offset + 14, 1);
  view.setUint16(offset + 18, orientation);
  view.setUint32(offset + 22, 0);
  return bytes;
}

function concatBytes(parts) {
  const length = parts.reduce((total, part) => total + part.byteLength, 0);
  const output = new Uint8Array(length);
  let offset = 0;
  for (const part of parts) {
    output.set(part, offset);
    offset += part.byteLength;
  }
  return output;
}

function makeJpegExifSegment(orientation) {
  const payload = makeMinimalExif(orientation, true);
  const segment = new Uint8Array(payload.length + 4);
  segment.set([0xff, 0xe1]);
  new DataView(segment.buffer).setUint16(2, payload.length + 2);
  segment.set(payload, 4);
  return segment;
}

export function optimiseJpegMetadata(buffer) {
  const bytes = new Uint8Array(buffer);
  if (bytes.length < 4 || bytes[0] !== 0xff || bytes[1] !== 0xd8) return buffer;

  const parts = [bytes.subarray(0, 2)];
  let offset = 2;
  let orientationWritten = false;

  while (offset < bytes.length) {
    const markerStart = offset;
    if (bytes[offset] !== JPEG_MARKER_PREFIX) return buffer;
    while (offset < bytes.length && bytes[offset] === JPEG_MARKER_PREFIX) offset += 1;
    if (offset >= bytes.length) return buffer;
    const marker = bytes[offset];

    // The scan payload is entropy-coded and may contain escaped marker bytes. Copy it
    // verbatim so image samples and the original Huffman coding remain untouched.
    if (marker === 0xda) {
      parts.push(bytes.subarray(markerStart));
      return concatBytes(parts).buffer;
    }

    const standalone = marker === 0xd8 || marker === 0xd9 || marker === 0x01 || (marker >= 0xd0 && marker <= 0xd7);
    if (standalone) {
      const markerEnd = offset + 1;
      parts.push(bytes.subarray(markerStart, markerEnd));
      offset = markerEnd;
      if (marker === 0xd9) return concatBytes(parts).buffer;
      continue;
    }

    if (offset + 2 >= bytes.length) return buffer;
    const segmentLength = (bytes[offset + 1] << 8) | bytes[offset + 2];
    if (segmentLength < 2) return buffer;
    const segmentEnd = offset + 1 + segmentLength;
    if (segmentEnd > bytes.length) return buffer;
    const payloadOffset = offset + 3;

    let keep = true;
    if (marker === 0xe0 || marker === 0xfe || (marker >= 0xe3 && marker <= 0xed) || marker === 0xef) {
      keep = false;
    } else if (marker === 0xe1) {
      keep = false;
      if (matchesAscii(bytes, payloadOffset, "Exif\0\0") && !orientationWritten) {
        const orientation = readExifOrientation(bytes.subarray(payloadOffset, segmentEnd));
        if (orientation && orientation !== 1) {
          parts.push(makeJpegExifSegment(orientation));
          orientationWritten = true;
        }
      }
    } else if (marker === 0xe2) {
      // ICC profiles affect displayed colours. Other APP2 payloads are removable metadata.
      keep = matchesAscii(bytes, payloadOffset, "ICC_PROFILE\0");
    }

    if (keep) parts.push(bytes.subarray(markerStart, segmentEnd));
    offset = segmentEnd;
  }

  return buffer;
}

function makeWebpChunk(type, payload) {
  const paddedLength = payload.length + (payload.length % 2);
  const chunk = new Uint8Array(8 + paddedLength);
  for (let index = 0; index < 4; index += 1) chunk[index] = type.charCodeAt(index);
  new DataView(chunk.buffer).setUint32(4, payload.length, true);
  chunk.set(payload, 8);
  return chunk;
}

export function optimiseWebpMetadata(buffer) {
  const bytes = new Uint8Array(buffer);
  if (bytes.length < 12 || !matchesAscii(bytes, 0, "RIFF") || !matchesAscii(bytes, 8, "WEBP")) return buffer;

  const chunks = [];
  let offset = 12;
  let hasExif = false;
  let vp8xPayload = null;

  while (offset + 8 <= bytes.length) {
    const type = String.fromCharCode(...bytes.subarray(offset, offset + 4));
    const size = new DataView(bytes.buffer, bytes.byteOffset + offset + 4, 4).getUint32(0, true);
    const chunkEnd = offset + 8 + size;
    const paddedEnd = chunkEnd + (size % 2);
    if (chunkEnd > bytes.length || paddedEnd > bytes.length) return buffer;

    if (type === "VP8X") {
      vp8xPayload = bytes.slice(offset + 8, chunkEnd);
      chunks.push({ type, payload: vp8xPayload });
    } else if (type === "EXIF") {
      const payload = bytes.subarray(offset + 8, chunkEnd);
      const orientation = readExifOrientation(payload);
      if (orientation && orientation !== 1 && !hasExif) {
        chunks.push({ type, payload: makeMinimalExif(orientation, matchesAscii(payload, 0, "Exif\0\0")) });
        hasExif = true;
      }
    } else if (type !== "XMP ") {
      chunks.push({ type, payload: bytes.slice(offset + 8, chunkEnd) });
    }
    offset = paddedEnd;
  }

  if (offset !== bytes.length) return buffer;
  if (vp8xPayload && vp8xPayload.length >= 1) {
    vp8xPayload[0] &= ~0x04;
    if (hasExif) vp8xPayload[0] |= 0x08;
    else vp8xPayload[0] &= ~0x08;
  }

  const body = concatBytes(chunks.map(({ type, payload }) => makeWebpChunk(type, payload)));
  const output = new Uint8Array(12 + body.length);
  output.set([0x52, 0x49, 0x46, 0x46]);
  new DataView(output.buffer).setUint32(4, output.length - 8, true);
  output.set([0x57, 0x45, 0x42, 0x50], 8);
  output.set(body, 12);
  return output.buffer;
}
