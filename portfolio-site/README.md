# Independent App Portfolio

A bilingual, dependency-free portfolio for six Apple-platform apps. It can be published directly with GitHub Pages.

## Preview locally

```bash
python3 -m http.server 8080 --directory portfolio-site
```

Then open `http://localhost:8080`.

## Publish with GitHub Pages

1. Create a GitHub repository and copy the contents of this folder to its root.
2. Push to the `main` branch.
3. Open **Settings → Pages** in GitHub.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select `main` and `/ (root)`, then save.

The language automatically follows the visitor's browser and can be switched manually. App data and links live in `app.js`.
