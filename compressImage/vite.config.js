import { defineConfig } from "vite";
import { readFileSync } from "node:fs";

export default defineConfig({
  base: "./",
  define: {
    __LIGHTPRESS_STANDALONE__: "false"
  },
  plugins: [
    {
      name: "use-module-app-in-vite",
      transformIndexHtml: {
        order: "pre",
        handler(html) {
          const moduleEntry = `<script>
      window.__loadLightpressFallback = function () {
        if (window.__LIGHTPRESS_READY__ || window.__LIGHTPRESS_FALLBACK_LOADING__) return;
        window.__LIGHTPRESS_FALLBACK_LOADING__ = true;
        var fallback = document.createElement("script");
        fallback.src = "./app.bundle.js";
        document.body.appendChild(fallback);
      };
      document.addEventListener("DOMContentLoaded", window.__loadLightpressFallback);
    </script>
    <script type="module" src="./app.js"></script>`;
          return html.replace('<script src="./app.bundle.js"></script>', moduleEntry);
        }
      }
    },
    {
      name: "include-standalone-fallback",
      generateBundle() {
        this.emitFile({
          type: "asset",
          fileName: "app.bundle.js",
          source: readFileSync(new URL("./app.bundle.js", import.meta.url))
        });
      }
    }
  ],
  optimizeDeps: {
    exclude: ["@jsquash/oxipng"]
  }
});
