import { defineConfig } from "vite";

export default defineConfig({
  define: {
    __LIGHTPRESS_STANDALONE__: "true"
  },
  plugins: [{
    name: "make-oxipng-iife-safe",
    transform(code, id) {
      if (!id.endsWith("/codec/pkg/squoosh_oxipng.js")) return null;
      return code.replace(
        /\n  if \(import\.meta\.url === undefined\) \{\n    import\.meta\.url = 'https:\/\/localhost';\n  \}\n/,
        "\n"
      );
    }
  }],
  build: {
    target: "es2020",
    assetsInlineLimit: 1024 * 1024,
    emptyOutDir: false,
    outDir: ".",
    lib: {
      entry: "./app.js",
      name: "LightPressApp",
      formats: ["iife"],
      fileName: () => "app.bundle.js"
    },
    rollupOptions: {
      output: {
        inlineDynamicImports: true
      }
    }
  }
});
