# Independent App Portfolio

The public portfolio features 11 Apple-platform apps. The English and Simplified Chinese homepages and app pages are served as static HTML.

- [Live portfolio](https://wlb0806.github.io/someInfo/portfolio-site/)
- [Chinese homepage](https://wlb0806.github.io/someInfo/portfolio-site/zh/)
- [XML sitemap](https://wlb0806.github.io/someInfo/portfolio-site/sitemap.xml)

## Update and preview

Edit `catalog.json` for app names, descriptions, and links. Edit `build.py` for shared page copy and markup, and `styles.css` for the layout. Icons are shared with the repository README in `assets/app-icons/`.

The IDMint product page uses `idmint.py` for its country size guides and bilingual copy, and `idmint.css` for its layout. The images in `assets/idmint/` are web-sized copies of the English and Simplified Chinese screenshots from the publicly listed IDMint release.

From the repository root, run:

```bash
python3 portfolio-site/build.py
python3 -m http.server 8080
```

Open [the local portfolio](http://localhost:8080/portfolio-site/). Commit both the source and regenerated HTML and sitemap. GitHub Pages serves the committed files.

## Google Search Console

With access to the site's verified Search Console property, submit the sitemap URL above. Use URL Inspection to check coverage or request indexing for the homepage and priority app pages.
