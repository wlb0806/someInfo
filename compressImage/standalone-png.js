import initCodec, { optimise as optimiseRawPng } from "@jsquash/oxipng/codec/pkg/squoosh_oxipng.js";
import codecUrl from "@jsquash/oxipng/codec/pkg/squoosh_oxipng_bg.wasm?url";

let codecReady;

export async function optimiseStandalonePng(buffer, options) {
  codecReady ||= initCodec(codecUrl);
  await codecReady;
  return optimiseRawPng(
    new Uint8Array(buffer),
    options.level,
    options.interlace,
    options.optimiseAlpha
  ).buffer;
}
