# Independent App Portfolio

The public portfolio has a dedicated product website in English and Simplified Chinese for each of its 11 Apple-platform apps. The homepages and product pages are served as static HTML.

- [Live portfolio](https://wlb0806.github.io/someInfo/portfolio-site/)
- [Chinese homepage](https://wlb0806.github.io/someInfo/portfolio-site/zh/)
- [XML sitemap](https://wlb0806.github.io/someInfo/portfolio-site/sitemap.xml)

## Update and preview

Edit `catalog.json` for app names, descriptions, and links. Edit `build.py` for shared page copy and markup, and `styles.css` for the layout. Icons are shared with the repository README in `assets/app-icons/`.

The IDMint product page uses `idmint.py` for its country size guides and bilingual copy, and `idmint.css` for its layout. The images in `assets/idmint/` are web-sized copies of the English and Simplified Chinese screenshots from the publicly listed IDMint release. The other app websites use `release_products.py` for shared markup and `release-products.css` for layout. The bilingual copy for the eight newer sites lives in `app_websites.json`. The web images come from the projects’ App Store screenshots or the captures used to prepare them. Daily Quest uses the published English screenshots on both pages.

From the repository root, run:

```bash
python3 portfolio-site/build.py
python3 -m http.server 8080
```

Open [the local portfolio](http://localhost:8080/portfolio-site/). When a page changes substantially, update its date in `UPDATED` in `build.py`. Commit both the source and regenerated HTML and sitemap. GitHub Pages serves the committed files.

## Google Search Console

With access to the site's verified Search Console property, submit the sitemap URL above. Use URL Inspection to check coverage or request indexing for the homepage and priority app pages.
