const MAX_FILES = 20;
const MAX_FILE_SIZE = 20 * 1024 * 1024;
const STANDALONE_BUILD = __LIGHTPRESS_STANDALONE__;
const ACCEPTED_TYPES = new Set(["image/jpeg", "image/png", "image/webp"]);
const EXTENSION_TYPES = new Map([
  ["jpg", "image/jpeg"], ["jpeg", "image/jpeg"], ["jfif", "image/jpeg"],
  ["png", "image/png"], ["webp", "image/webp"]
]);

const translations = {
  zh: {
    pageTitle: "轻压图 · 本地图片压缩",
    metaDescription: "在浏览器本地完成图片有损或无损压缩，快速、安全、无需上传。",
    brandName: "轻压图", homeAria: "轻压图首页", navAria: "主导航", navCompress: "开始压缩", navFeatures: "产品特点", navHow: "工作原理",
    privacy: "图片仅在本地处理", switchLanguage: "Switch to English", languageButton: "EN",
    heroTitle: "让图片更轻，<br />让分享更快。", heroDescription: "支持 JPG、PNG 与 WebP，最多一次处理 20 张。",
    compressorAria: "图片压缩工具", modeAria: "压缩模式",
    lossy: "有损压缩", lossyDescription: "体积更小，画质可调", lossless: "无损压缩", losslessDescription: "像素不变，深度优化",
    chooseImages: "选择图片", dropTitle: "把图片拖到这里", dropDescription: "或 <span>点击选择图片</span> · 单张最大 20 MB",
    quality: "压缩质量", smallerFile: "文件更小", higherQuality: "画质更高", outputFormat: "输出格式", smartChoice: "智能选择",
    losslessNoteTitle: "格式专用无损优化", losslessNoteDescription: "PNG 使用最高级编码，JPEG / WebP 清理冗余元数据；保留方向与色彩信息。",
    pendingImages: "待处理图片", clear: "清空", startCompress: "开始压缩", processingButton: "正在压缩…", recompress: "重新压缩", downloadAll: "全部下载",
    originalSize: "原始大小", compressedSize: "压缩后", totalSaved: "共节省", savedSpace: "节省空间", optimizationCount: "{count} 项优化",
    featuresTitle: "更聪明的图片压缩", featuresDescription: "无需上传，也不牺牲你在意的细节。",
    localProcessing: "本地处理", localProcessingDescription: "所有计算都在浏览器内完成，原图不会离开你的设备。",
    dualModes: "双压缩模式", dualModesDescription: "按场景选择高效有损，或像素不变的格式专用无损优化。",
    batchEfficient: "批量高效", batchEfficientDescription: "一次添加最多 20 张图片，集中查看结果并快速下载。",
    howTitle: "简单三步，<br />释放存储空间。", stepAdd: "添加图片", stepAddDescription: "拖拽或选择 JPG、PNG、WebP 图片。",
    stepChoose: "选择模式", stepChooseDescription: "调节有损质量，或开启格式专用无损优化。", stepDownload: "下载结果", stepDownloadDescription: "对比体积后单独或批量保存。",
    footerTagline: "更小的图片，更轻的网络。",
    waiting: "等待压缩", reading: "正在读取", pngOptimizing: "最高级别 PNG 无损优化", jpegOptimizing: "清理 JPEG 冗余元数据", webpOptimizing: "清理 WebP 冗余元数据",
    compressed: "压缩完成", minimal: "已是最小", failed: "处理失败", download: "下载", remove: "移除", removeFile: "移除 {name}",
    ignoredFiles: "已忽略 {count} 个重复、不支持或超限文件", completedToast: "图片处理完成", noDropFiles: "没有识别到可用的图片文件", downloadedToast: "已开始下载 {count} 张图片"
  },
  en: {
    pageTitle: "LightPress · Local Image Compressor",
    metaDescription: "Compress images locally in your browser with lossy or lossless optimization. Fast, private, and upload-free.",
    brandName: "LightPress", homeAria: "LightPress home", navAria: "Main navigation", navCompress: "Compress", navFeatures: "Features", navHow: "How it works",
    privacy: "Images stay on your device", switchLanguage: "切换到中文", languageButton: "中文",
    heroTitle: "Lighter images.<br />Faster sharing.", heroDescription: "Compress up to 20 JPG, PNG, or WebP images at once.",
    compressorAria: "Image compressor", modeAria: "Compression mode",
    lossy: "Lossy", lossyDescription: "Smaller files, adjustable quality", lossless: "Lossless", losslessDescription: "Same pixels, deeper optimization",
    chooseImages: "Choose images", dropTitle: "Drop images here", dropDescription: "or <span>click to choose</span> · Up to 20 MB each",
    quality: "Quality", smallerFile: "Smaller file", higherQuality: "Higher quality", outputFormat: "Output format", smartChoice: "Smart choice",
    losslessNoteTitle: "Format-specific lossless optimization", losslessNoteDescription: "Highest-level PNG encoding and JPEG / WebP metadata cleanup, with orientation and color preserved.",
    pendingImages: "Images to process", clear: "Clear", startCompress: "Compress", processingButton: "Compressing…", recompress: "Compress again", downloadAll: "Download all",
    originalSize: "Original", compressedSize: "Compressed", totalSaved: "Total saved", savedSpace: "Space saved", optimizationCount: "{count} optimization(s)",
    featuresTitle: "Smarter image compression", featuresDescription: "No uploads and no unnecessary compromises.",
    localProcessing: "Local processing", localProcessingDescription: "Everything runs in your browser, so originals never leave your device.",
    dualModes: "Two compression modes", dualModesDescription: "Choose efficient lossy compression or format-specific, pixel-preserving optimization.",
    batchEfficient: "Efficient batches", batchEfficientDescription: "Add up to 20 images, compare results, and download them quickly.",
    howTitle: "Three simple steps.<br />More space to spare.", stepAdd: "Add images", stepAddDescription: "Drop or choose JPG, PNG, and WebP images.",
    stepChoose: "Choose a mode", stepChooseDescription: "Adjust lossy quality or use format-specific lossless optimization.", stepDownload: "Download results", stepDownloadDescription: "Compare sizes, then save one image or the whole batch.",
    footerTagline: "Smaller images. A lighter web.",
    waiting: "Ready", reading: "Reading", pngOptimizing: "Highest-level PNG optimization", jpegOptimizing: "Cleaning JPEG metadata", webpOptimizing: "Cleaning WebP metadata",
    compressed: "Compressed", minimal: "Already optimized", failed: "Failed", download: "Download", remove: "Remove", removeFile: "Remove {name}",
    ignoredFiles: "Ignored {count} duplicate, unsupported, or oversized file(s)", completedToast: "Image processing complete", noDropFiles: "No supported image files found", downloadedToast: "Started downloading {count} image(s)"
  }
};

function initialLanguage() {
  try {
    const saved = localStorage.getItem("lightpress-language");
    if (saved === "zh" || saved === "en") return saved;
  } catch {}
  return navigator.language?.toLowerCase().startsWith("zh") ? "zh" : "en";
}

const state = { mode: "lossy", language: initialLanguage(), items: [], processing: false };
let pngOptimiserPromise;
let standalonePngOptimiserPromise;
let losslessCodecsPromise;

function getPngOptimiser() {
  pngOptimiserPromise ||= import("@jsquash/oxipng").then((module) => module.optimise);
  return pngOptimiserPromise;
}

function getStandalonePngOptimiser() {
  standalonePngOptimiserPromise ||= import("./standalone-png.js").then((module) => module.optimiseStandalonePng);
  return standalonePngOptimiserPromise;
}

function getLosslessCodecs() {
  losslessCodecsPromise ||= import("./lossless-codecs.js");
  return losslessCodecsPromise;
}

const $ = (selector) => document.querySelector(selector);
const els = {
  tabs: [...document.querySelectorAll(".mode-tab")],
  languageToggle: $("#languageToggle"),
  dropZone: $("#dropZone"), fileInput: $("#fileInput"),
  lossySettings: $("#lossySettings"), losslessNote: $("#losslessNote"),
  qualityRange: $("#qualityRange"), qualityValue: $("#qualityValue"), formatSelect: $("#formatSelect"),
  workspace: $("#workspace"), fileList: $("#fileList"), clearButton: $("#clearButton"),
  compressButton: $("#compressButton"), downloadAllButton: $("#downloadAllButton"),
  summary: $("#summary"), originalTotal: $("#originalTotal"), compressedTotal: $("#compressedTotal"),
  savedTotal: $("#savedTotal"), toast: $("#toast")
};

function t(key, values = {}) {
  const template = translations[state.language][key] ?? translations.zh[key] ?? key;
  return String(template).replace(/\{(\w+)\}/g, (_, name) => values[name] ?? "");
}

function updateCompressButtonLabel() {
  const key = state.processing
    ? "processingButton"
    : state.items.some((item) => item.result)
      ? "recompress"
      : "startCompress";
  els.compressButton.querySelector("span").textContent = t(key);
}

function applyLanguage() {
  document.documentElement.lang = state.language === "zh" ? "zh-CN" : "en";
  document.title = t("pageTitle");
  document.querySelectorAll("[data-i18n]").forEach((element) => { element.textContent = t(element.dataset.i18n); });
  document.querySelectorAll("[data-i18n-html]").forEach((element) => { element.innerHTML = t(element.dataset.i18nHtml); });
  document.querySelectorAll("[data-i18n-aria-label]").forEach((element) => { element.setAttribute("aria-label", t(element.dataset.i18nAriaLabel)); });
  document.querySelectorAll("[data-i18n-content]").forEach((element) => { element.setAttribute("content", t(element.dataset.i18nContent)); });
  els.languageToggle.textContent = t("languageButton");
  els.languageToggle.setAttribute("aria-label", t("switchLanguage"));
  try { localStorage.setItem("lightpress-language", state.language); } catch {}
  render();
}

let toastTimer;
function toast(message) {
  els.toast.textContent = message;
  els.toast.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => els.toast.classList.remove("show"), 2400);
}

function formatBytes(bytes) {
  if (!Number.isFinite(bytes) || bytes === 0) return "0 KB";
  const units = ["B", "KB", "MB", "GB"];
  const index = Math.min(Math.floor(Math.log(bytes) / Math.log(1024)), units.length - 1);
  const value = bytes / 1024 ** index;
  return `${value.toFixed(index > 1 ? 2 : index ? 1 : 0)} ${units[index]}`;
}

function escapeHtml(value) {
  return value.replace(/[&<>'"]/g, (character) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[character]));
}

function switchMode(mode) {
  if (state.processing) return;
  state.mode = mode;
  els.tabs.forEach((tab) => {
    const active = tab.dataset.mode === mode;
    tab.classList.toggle("active", active);
    tab.setAttribute("aria-selected", String(active));
  });
  els.lossySettings.hidden = mode !== "lossy";
  els.losslessNote.hidden = mode !== "lossless";
  resetResults();
}

function imageTypeFor(file) {
  const mime = file.type.toLowerCase();
  if (mime === "image/jpg" || mime === "image/pjpeg") return "image/jpeg";
  if (ACCEPTED_TYPES.has(mime)) return mime;
  const extension = file.name.split(".").pop()?.toLowerCase();
  return EXTENSION_TYPES.get(extension) || "";
}

function addFiles(fileList) {
  const files = Array.from(fileList || []);
  let rejected = 0;
  for (const file of files) {
    const imageType = imageTypeFor(file);
    if (state.items.length >= MAX_FILES) { rejected += 1; continue; }
    if (!imageType || file.size > MAX_FILE_SIZE) { rejected += 1; continue; }
    const duplicate = state.items.some((item) => item.file.name === file.name && item.file.size === file.size && item.file.lastModified === file.lastModified);
    if (duplicate) { rejected += 1; continue; }
    const normalizedFile = file.type === imageType
      ? file
      : new File([file], file.name, { type: imageType, lastModified: file.lastModified });
    state.items.push({
      id: crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random()}`,
      file: normalizedFile, originalUrl: URL.createObjectURL(normalizedFile), resultUrl: null, result: null,
      status: "ready", messageKey: "waiting", rounds: 0
    });
  }
  if (rejected) toast(t("ignoredFiles", { count: rejected }));
  render();
  if (state.items.length) setTimeout(() => els.workspace.scrollIntoView({ behavior: "smooth", block: "start" }), 80);
}

function cleanupItem(item) {
  URL.revokeObjectURL(item.originalUrl);
  if (item.resultUrl) URL.revokeObjectURL(item.resultUrl);
}

function resetResults() {
  state.items.forEach((item) => {
    if (item.resultUrl) URL.revokeObjectURL(item.resultUrl);
    item.resultUrl = null; item.result = null; item.status = "ready"; item.messageKey = "waiting"; item.rounds = 0;
  });
  render();
}

function removeItem(id) {
  if (state.processing) return;
  const index = state.items.findIndex((item) => item.id === id);
  if (index < 0) return;
  cleanupItem(state.items[index]);
  state.items.splice(index, 1);
  render();
}

function render() {
  els.workspace.hidden = state.items.length === 0;
  const completed = state.items.filter((item) => item.status === "done" && item.result);
  els.fileList.innerHTML = state.items.map((item) => {
    const savedRaw = item.result ? (1 - item.result.size / item.file.size) * 100 : 0;
    const saved = savedRaw > 0 ? savedRaw : 0;
    const statusClass = item.status === "done" ? "done" : item.status === "processing" ? "processing" : item.status === "error" ? "error" : "";
    return `<article class="file-row" data-id="${item.id}">
      <img class="thumb" src="${item.originalUrl}" alt="" />
      <div class="file-info"><strong title="${escapeHtml(item.file.name)}">${escapeHtml(item.file.name)}</strong><span>${item.file.type.replace("image/", "").toUpperCase()}</span></div>
      <div class="file-stat"><strong>${formatBytes(item.file.size)}</strong><span>${t("originalSize")}</span></div>
      <div class="file-stat"><strong>${item.result ? formatBytes(item.result.size) : "—"}</strong><span>${t("compressedSize")}</span></div>
      <div class="file-stat saving"><strong>${item.result ? (saved > 0 && saved < 0.1 ? "-&lt;0.1%" : `-${saved.toFixed(1)}%`) : "—"}</strong><span>${item.rounds > 0 ? t("optimizationCount", { count: item.rounds }) : t("savedSpace")}</span></div>
      <span class="status ${statusClass}">${t(item.messageKey)}</span>
      <div class="row-actions">
        ${item.result ? `<button class="download-button" data-action="download">${t("download")}</button>` : ""}
        <button class="remove-button" data-action="remove" aria-label="${escapeHtml(t("removeFile", { name: item.file.name }))}">${t("remove")}</button>
      </div>
    </article>`;
  }).join("");

  els.summary.hidden = completed.length === 0;
  els.downloadAllButton.hidden = completed.length === 0 || completed.length !== state.items.length;
  if (completed.length) {
    const original = completed.reduce((sum, item) => sum + item.file.size, 0);
    const compressed = completed.reduce((sum, item) => sum + item.result.size, 0);
    els.originalTotal.textContent = formatBytes(original);
    els.compressedTotal.textContent = formatBytes(compressed);
    const savedPercent = (1 - compressed / original) * 100;
    els.savedTotal.textContent = savedPercent > 0 && savedPercent < 0.1
      ? "<0.1%"
      : `${(savedPercent > 0 ? savedPercent : 0).toFixed(1)}%`;
  }
  updateCompressButtonLabel();
}

async function decodeImage(file) {
  if ("createImageBitmap" in window) return createImageBitmap(file, { imageOrientation: "from-image" });
  return new Promise((resolve, reject) => {
    const image = new Image();
    const url = URL.createObjectURL(file);
    image.onload = () => { URL.revokeObjectURL(url); resolve(image); };
    image.onerror = () => { URL.revokeObjectURL(url); reject(new Error("图片解码失败")); };
    image.src = url;
  });
}

function canvasToBlob(canvas, type, quality) {
  return new Promise((resolve, reject) => canvas.toBlob((blob) => blob ? resolve(blob) : reject(new Error("浏览器无法编码该图片")), type, quality));
}

async function encodeImage(file, type, quality) {
  const source = await decodeImage(file);
  const width = source.width || source.naturalWidth;
  const height = source.height || source.naturalHeight;
  const canvas = document.createElement("canvas");
  canvas.width = width; canvas.height = height;
  const context = canvas.getContext("2d", { alpha: type !== "image/jpeg" });
  if (type === "image/jpeg") { context.fillStyle = "#fff"; context.fillRect(0, 0, width, height); }
  context.drawImage(source, 0, 0, width, height);
  if (source.close) source.close();
  return canvasToBlob(canvas, type, quality);
}

async function lossyCompress(file) {
  const requested = els.formatSelect.value;
  let type = requested === "auto" ? (file.type === "image/png" ? "image/webp" : file.type) : requested;
  if (type !== "image/jpeg" && type !== "image/webp") type = "image/webp";
  const quality = Number(els.qualityRange.value) / 100;
  const blob = await encodeImage(file, type, quality);
  return blob.size < file.size ? blob : file;
}

async function losslessCompress(file, onRound) {
  const source = await file.arrayBuffer();
  let output;

  if (file.type === "image/png") {
    onRound(1, "pngOptimizing");
    if (STANDALONE_BUILD) {
      const optimisePng = await getStandalonePngOptimiser();
      output = await optimisePng(source, { level: 6, interlace: false, optimiseAlpha: false });
    } else {
      const optimisePng = await getPngOptimiser();
      output = await optimisePng(source, { level: 6, interlace: false, optimiseAlpha: false });
    }
  } else if (file.type === "image/jpeg") {
    onRound(1, "jpegOptimizing");
    const { optimiseJpegMetadata } = await getLosslessCodecs();
    output = optimiseJpegMetadata(source);
  } else if (file.type === "image/webp") {
    onRound(1, "webpOptimizing");
    const { optimiseWebpMetadata } = await getLosslessCodecs();
    output = optimiseWebpMetadata(source);
  } else {
    return file;
  }

  const outputBuffer = output instanceof ArrayBuffer
    ? output
    : output.buffer.slice(output.byteOffset, output.byteOffset + output.byteLength);
  const next = new Blob([outputBuffer], { type: file.type });
  return next.size < file.size ? next : file;
}

function extensionFor(blob, fallbackName) {
  const ext = blob.type === "image/webp" ? "webp" : blob.type === "image/png" ? "png" : blob.type === "image/jpeg" ? "jpg" : (fallbackName.split(".").pop() || "img");
  return ext;
}

function resultName(item) {
  const base = item.file.name.replace(/\.[^.]+$/, "");
  return `${base}-lightpress.${extensionFor(item.result, item.file.name)}`;
}

function downloadItem(item) {
  if (!item.resultUrl) return;
  const anchor = document.createElement("a");
  anchor.href = item.resultUrl; anchor.download = resultName(item);
  document.body.append(anchor); anchor.click(); anchor.remove();
}

async function compressAll() {
  if (!state.items.length || state.processing) return;
  state.processing = true;
  els.compressButton.disabled = true;
  updateCompressButtonLabel();
  const mode = state.mode;
  for (const item of state.items) {
    item.status = "processing"; item.messageKey = "reading"; render();
    try {
      const blob = mode === "lossy"
        ? await lossyCompress(item.file)
        : await losslessCompress(item.file, (round, messageKey) => { item.rounds = round; item.messageKey = messageKey; render(); });
      if (item.resultUrl) URL.revokeObjectURL(item.resultUrl);
      item.result = blob;
      item.resultUrl = blob === item.file ? item.originalUrl : URL.createObjectURL(blob);
      item.status = "done";
      item.messageKey = blob.size < item.file.size ? "compressed" : "minimal";
    } catch (error) {
      console.error(error);
      item.status = "error"; item.messageKey = "failed";
    }
    render();
    await new Promise((resolve) => requestAnimationFrame(resolve));
  }
  state.processing = false;
  els.compressButton.disabled = false;
  updateCompressButtonLabel();
  toast(t("completedToast"));
}

els.tabs.forEach((tab) => tab.addEventListener("click", () => switchMode(tab.dataset.mode)));
els.languageToggle.addEventListener("click", () => {
  state.language = state.language === "zh" ? "en" : "zh";
  applyLanguage();
});
els.qualityRange.addEventListener("input", () => { els.qualityValue.textContent = `${els.qualityRange.value}%`; resetResults(); });
els.formatSelect.addEventListener("change", resetResults);
els.fileInput.addEventListener("change", (event) => { addFiles(event.target.files); event.target.value = ""; });

function containsDraggedFiles(event) {
  return [...(event.dataTransfer?.types || [])].includes("Files");
}

function filesFromDrop(event) {
  const directFiles = [...(event.dataTransfer?.files || [])];
  if (directFiles.length) return directFiles;
  return [...(event.dataTransfer?.items || [])]
    .filter((item) => item.kind === "file")
    .map((item) => item.getAsFile())
    .filter(Boolean);
}

// Prevent the browser from navigating to a dropped image when the pointer misses
// the drop-zone by a few pixels. The drop-zone handler below performs the import.
["dragover", "drop"].forEach((name) => window.addEventListener(name, (event) => {
  if (containsDraggedFiles(event)) event.preventDefault();
}));

["dragenter", "dragover"].forEach((name) => els.dropZone.addEventListener(name, (event) => {
  event.preventDefault();
  event.stopPropagation();
  if (event.dataTransfer) event.dataTransfer.dropEffect = "copy";
  els.dropZone.classList.add("dragging");
}));
els.dropZone.addEventListener("dragleave", (event) => {
  event.preventDefault();
  if (!els.dropZone.contains(event.relatedTarget)) els.dropZone.classList.remove("dragging");
});
els.dropZone.addEventListener("drop", (event) => {
  event.preventDefault();
  event.stopPropagation();
  els.dropZone.classList.remove("dragging");
  const files = filesFromDrop(event);
  if (files.length) addFiles(files);
  else toast(t("noDropFiles"));
});
els.clearButton.addEventListener("click", () => { if (state.processing) return; state.items.forEach(cleanupItem); state.items = []; render(); });
els.compressButton.addEventListener("click", compressAll);
els.downloadAllButton.addEventListener("click", async () => {
  const completed = state.items.filter((item) => item.resultUrl);
  for (const item of completed) { downloadItem(item); await new Promise((resolve) => setTimeout(resolve, 180)); }
  toast(t("downloadedToast", { count: completed.length }));
});
els.fileList.addEventListener("click", (event) => {
  const button = event.target.closest("button[data-action]");
  if (!button) return;
  const item = state.items.find((entry) => entry.id === button.closest(".file-row").dataset.id);
  if (!item) return;
  if (button.dataset.action === "remove") removeItem(item.id);
  if (button.dataset.action === "download") downloadItem(item);
});
window.addEventListener("beforeunload", () => state.items.forEach(cleanupItem));
applyLanguage();
window.__LIGHTPRESS_READY__ = true;
