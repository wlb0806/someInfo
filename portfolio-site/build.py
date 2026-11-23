"""Render the English and Simplified Chinese portfolio and sitemap from catalog.json."""
import json
from html import escape as h
from pathlib import Path
from posixpath import relpath
from urllib.parse import urljoin

from idmint import APP_STORE as IDMINT_STORE, product_page as idmint_page

ROOT = Path(__file__).resolve().parent
BASE = "https://wlb0806.github.io/someInfo/portfolio-site/"
APPS = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
BY_SLUG = {app["slug"]: app for app in APPS}
GROUPS = {
    "everyday": {"en": "Everyday tools", "zh": "日常工具"},
    "studio": {"en": "Photos & storage", "zh": "照片与空间"},
    "games": {"en": "Puzzle games", "zh": "益智游戏"},
}
COPY = {
    "en": {
        "lang": "en", "site": "Lingbo Wang · Independent Apps",
        "title": "Independent Apps for iPhone, iPad & Mac | Lingbo Wang",
        "description": "Explore 11 independent iPhone, iPad and Mac apps by Lingbo Wang. Find photo and Mac cleanup tools, rental and receipt trackers, habit and savings apps, and daily logic puzzles.",
        "intro": "I’m Lingbo Wang. I build apps for the things you do every day, from keeping track of a receipt to unwinding with a logic puzzle.",
        "hero1": "Apps for daily life", "hero2": "and a little play.",
        "platforms": "iPhone, iPad & Mac", "browse": "Explore apps",
        "directory": "The app collection", "skip": "Skip to content",
        "about": "About", "about_title": "Made by Lingbo Wang",
        "about_body": "Most of my apps keep your records and processing on your device. Some offer optional private iCloud sync. Each app’s page explains what it does and links to its store listing and privacy policy where available.",
        "home": "All apps", "features": "What you can do", "more": "More in this collection",
        "store": "View on the App Store", "mac_store": "View on the Mac App Store",
        "privacy": "Privacy policy", "support": "Support", "website": "Product website",
        "availability": "The public App Store link is pending.",
        "store_name": "Listed as {name} on the U.S. App Store.",
    },
    "zh": {
        "lang": "zh-CN", "site": "Lingbo Wang · 独立应用",
        "title": "iPhone、iPad 与 Mac 独立应用作品集 | Lingbo Wang",
        "description": "浏览 Lingbo Wang 的 11 款 iPhone、iPad 与 Mac 独立应用，涵盖照片和磁盘清理、租房验房、收据保修、习惯打卡、省钱挑战和每日逻辑谜题。",
        "intro": "我是 Lingbo Wang，一名独立开发者。这里有整理收据、清理照片的实用工具，也有适合休息时玩一局的逻辑谜题。",
        "hero1": "让日常轻一点，", "hero2": "让闲暇有趣一点。",
        "platforms": "iPhone、iPad 与 Mac", "browse": "浏览应用",
        "directory": "应用作品集", "skip": "跳到正文",
        "about": "关于", "about_title": "关于开发者",
        "about_body": "我是 Lingbo Wang。多数应用在你的设备上保存记录和处理数据，部分提供可选的私人 iCloud 同步。每款应用的页面都有功能介绍，并提供已有的商店和隐私政策链接。",
        "home": "全部应用", "features": "主要功能", "more": "同类应用",
        "store": "前往 App Store", "mac_store": "前往 Mac App Store",
        "privacy": "隐私政策", "support": "使用支持", "website": "产品网站",
        "availability": "公开 App Store 链接待补充。",
        "store_name": "美区 App Store 上的名称为 {name}。",
        "outside_cn": "已在美区上架，中国大陆 App Store 暂未提供。",
    },
}
LANGUAGES = tuple(COPY)
FEATURED = ("stayframe", "eos", "trio", "dewday")


def route(lang, slug=""):
    prefix = "zh/" if lang == "zh" else ""
    return prefix + (f"apps/{slug}/" if slug else "")


def relative(page, target):
    path = relpath(target or ".", page or ".")
    return f"{path}/" if not target or target.endswith("/") else path


def icon_path(slug):
    return f"../assets/app-icons/{slug}.png"


def icon(page, app, size, *, lazy=False, alt=""):
    src = h(relative(page, icon_path(app["slug"])))
    loading = ' loading="lazy"' if lazy else ""
    return f'<img src="{src}" alt="{h(alt)}" width="{size}" height="{size}" decoding="async"{loading}>'


def shell(lang, content, structured_data, app=None, *, product=False):
    t = COPY[lang]
    slug = app["slug"] if app else ""
    page = route(lang, slug)
    canonical = BASE + page
    home = relative(page, route(lang))
    en, zh = (relative(page, route(key, slug)) for key in LANGUAGES)
    en_current = ' aria-current="page"' if lang == "en" else ""
    zh_current = ' aria-current="page"' if lang == "zh" else ""
    title = t["title"]
    description = t["description"]
    image = ""
    brand = '<span class="wordmark" aria-hidden="true">LW</span> Lingbo Wang'
    brand_url = home
    favicon = "trio"
    styles = ""
    if app:
        copy = app[lang]
        title = copy["seo_title"] if product else f'{copy["name"]} | {copy["tagline"]}'
        description = copy["summary"]
        image_url = urljoin(BASE, icon_path(slug))
        image = f'\n  <meta property="og:image" content="{h(image_url)}">'
    if product:
        brand = f"{icon(page, app, 36)} IDMint"
        brand_url = "./"
        favicon = slug
        styles = f'\n  <link rel="stylesheet" href="{relative(page, "idmint.css")}">'
    data = json.dumps(structured_data, ensure_ascii=False, indent=2).replace("<", "\\u003c")
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{h(title)}</title>
  <meta name="description" content="{h(description)}">
  <meta name="theme-color" content="#f7f6f0">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{BASE + route('en', slug)}">
  <link rel="alternate" hreflang="zh-CN" href="{BASE + route('zh', slug)}">
  <link rel="alternate" hreflang="x-default" href="{BASE + route('en', slug)}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{h(t['site'])}">
  <meta property="og:locale" content="{'zh_CN' if lang == 'zh' else 'en_US'}">
  <meta property="og:title" content="{h(title)}">
  <meta property="og:description" content="{h(description)}">
  <meta property="og:url" content="{canonical}">{image}
  <link rel="icon" href="{relative(page, icon_path(favicon))}">
  <link rel="stylesheet" href="{relative(page, 'styles.css')}">{styles}
  <script type="application/ld+json">
{data}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">{t['skip']}</a>
  <header class="site-header frame">
    <a class="brand" href="{brand_url}">{brand}</a>
    <nav aria-label="{'主导航' if lang == 'zh' else 'Main navigation'}">
      <a class="nav-link" href="{home}#apps">{t['browse']}</a>
      <div class="languages">
        <a href="{en}" lang="en" hreflang="en"{en_current}>EN</a>
        <a href="{zh}" lang="zh-CN" hreflang="zh-CN"{zh_current}>中文</a>
      </div>
    </nav>
  </header>
{content}
  <footer class="site-footer frame">
    <span>© 2026 Lingbo Wang</span>
    <a href="{home}#about">{t['about']}</a>
  </footer>
</body>
</html>
"""


def directory_card(lang, page, app, heading="h4"):
    copy = app[lang]
    name = h(copy["name"])
    link = relative(page, route(lang, app["slug"]))
    return f"""        <article class="app-card">
          {icon(page, app, 64, lazy=True)}
          <div class="card-copy">
            <p class="platform">{app['platform']}</p>
            <{heading}><a href="{link}">{name}</a></{heading}>
            <p class="app-summary">{h(copy['summary'])}</p>
          </div>
          <span class="card-arrow" aria-hidden="true">↗</span>
        </article>"""


def directory_group(lang, group):
    page = route(lang)
    cards = "\n".join(directory_card(lang, page, app) for app in APPS if app["group"] == group)
    return f"""      <section class="app-group" id="{group}" aria-labelledby="{group}-title">
        <h3 id="{group}-title">{GROUPS[group][lang]}</h3>
        <div class="app-grid">
{cards}
        </div>
      </section>"""


def landing(lang):
    t = COPY[lang]
    page = route(lang)
    tiles = "\n".join(
        f'        <a class="hero-tile tile-{key}" href="{relative(page, route(lang, key))}" '
        f'aria-label="{h(BY_SLUG[key][lang]["name"])}">{icon(page, BY_SLUG[key], 124)}</a>'
        for key in FEATURED
    )
    categories = "".join(f'<a href="#{key}">{labels[lang]}</a>' for key, labels in GROUPS.items())
    groups = "\n".join(directory_group(lang, group) for group in GROUPS)
    content = f"""  <main class="frame" id="main">
    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-copy">
        <p class="eyebrow">{t['platforms']}</p>
        <h1 id="hero-title">{t['hero1']}<br><span>{t['hero2']}</span></h1>
        <p class="hero-intro">{t['intro']}</p>
        <a class="button" href="#apps">{t['browse']} <span aria-hidden="true">↓</span></a>
      </div>
      <div class="hero-art">
{tiles}
      </div>
    </section>
    <section class="directory" id="apps" aria-labelledby="directory-title">
      <div class="directory-heading">
        <h2 id="directory-title">{t['directory']}</h2>
        <nav class="category-nav" aria-label="{'应用分类' if lang == 'zh' else 'App categories'}">{categories}</nav>
      </div>
{groups}
    </section>
    <section class="about" id="about">
      <h2>{t['about_title']}</h2>
      <p>{t['about_body']}</p>
    </section>
  </main>"""
    structured_data = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "url": BASE + page,
        "name": t["title"],
        "description": t["description"],
        "inLanguage": t["lang"],
        "author": {"@type": "Person", "name": "Lingbo Wang"},
        "mainEntity": {
            "@type": "ItemList",
            "itemListElement": [
                {"@type": "ListItem", "position": i, "url": BASE + route(lang, app["slug"]), "name": app[lang]["name"]}
                for i, app in enumerate(
                    (entry for group in GROUPS for entry in APPS if entry["group"] == group), 1
                )
            ],
        },
    }
    return shell(lang, content, structured_data)


def detail(lang, app):
    t, copy = COPY[lang], app[lang]
    page = route(lang, app["slug"])
    home = relative(page, route(lang))
    group = app["group"]
    name = h(copy["name"])
    store_id = app.get("store")
    storefront = (
        "cn/" if app.get("listed_in_cn") else "us/"
    ) if lang == "zh" else ""
    store = f"https://apps.apple.com/{storefront}app/id{store_id}" if store_id else ""
    store_label = t["mac_store"] if app["platform"] == "Mac" else t["store"]
    action = (
        f'<a class="button" href="{store}">{store_label} <span aria-hidden="true">↗</span></a>'
        if store else f'<p class="availability">{t["availability"]}</p>'
    )
    store_notes = []
    if "us_store_name" in app:
        store_notes.append(t["store_name"].format(name=app["us_store_name"]))
    if store and lang == "zh" and not app.get("listed_in_cn"):
        store_notes.append(t["outside_cn"])
    availability = f'\n        <p class="store-notes">{h(" ".join(store_notes))}</p>' if store_notes else ""
    links = "".join(
        f'<a href="{h(relative(page, "../" + app[key]))}">{t[key]} <span aria-hidden="true">↗</span></a>'
        for key in ("website", "support", "privacy") if key in app
    )
    resources = f'\n      <div class="resource-links">{links}</div>' if links else ""
    features = "\n".join(f"        <li>{h(feature)}</li>" for feature in copy["features"])
    related = [item for item in APPS if item["group"] == group and item != app][:3]
    related_cards = "\n".join(directory_card(lang, page, item, "h3") for item in related)
    content = f"""  <main class="frame detail" id="main">
    <nav class="breadcrumbs" aria-label="{'当前位置' if lang == 'zh' else 'Breadcrumb'}">
      <a href="{home}#apps">{t['home']}</a><span aria-hidden="true">/</span>
      <a href="{home}#{group}">{GROUPS[group][lang]}</a>
    </nav>
    <section class="detail-hero" aria-labelledby="app-title">
      <div class="detail-art group-{group}">{icon(page, app, 190)}</div>
      <div class="detail-copy">
        <p class="eyebrow">{app['platform']}</p>
        <h1 id="app-title">{name}</h1>
        <p class="tagline">{h(copy['tagline'])}</p>
        <p class="detail-summary">{h(copy['summary'])}</p>
        {action}{availability}
      </div>
    </section>
    <section class="features" aria-labelledby="features-title">
      <h2 id="features-title">{t['features']}</h2>
      <ul>
{features}
      </ul>{resources}
    </section>
    <section class="related" aria-labelledby="related-title">
      <h2 id="related-title">{t['more']}</h2>
      <div class="app-grid">
{related_cards}
      </div>
    </section>
  </main>"""
    structured_data = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": copy["name"],
        "description": copy["summary"],
        "url": BASE + page,
        "inLanguage": t["lang"],
        "operatingSystem": {"Mac": "macOS", "iPhone": "iOS", "iPhone · iPad": "iOS, iPadOS"}[app["platform"]],
        "applicationCategory": "GameApplication" if group == "games" else "LifestyleApplication" if group == "everyday" else "UtilitiesApplication",
        "author": {"@type": "Person", "name": "Lingbo Wang"},
    }
    if store:
        structured_data["installUrl"] = store
    return shell(lang, content, structured_data, app)


def idmint_detail(lang, app):
    page = route(lang, app["slug"])
    copy = app[lang]
    content = idmint_page(
        lang,
        icon=icon(page, app, 54),
        assets=relative(page, "assets/idmint"),
        support=relative(page, "../" + app["support"]),
        privacy=relative(page, "../" + app["privacy"]),
    )
    structured_data = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": copy["name"],
        "alternateName": "IDMint",
        "description": copy["summary"],
        "url": BASE + page,
        "image": urljoin(BASE, icon_path(app["slug"])),
        "inLanguage": COPY[lang]["lang"],
        "operatingSystem": "iOS",
        "applicationCategory": "MultimediaApplication",
        "author": {"@type": "Person", "name": "Lingbo Wang"},
        "installUrl": IDMINT_STORE,
    }
    return shell(lang, content, structured_data, app, product=True)


def write(path, content):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def build():
    urls = []
    for lang in LANGUAGES:
        home = route(lang)
        write(home + "index.html", landing(lang))
        urls.append(BASE + home)
        for app in APPS:
            page = route(lang, app["slug"])
            render = idmint_detail if app["slug"] == "photo-maker" else detail
            write(page + "index.html", render(lang, app))
            urls.append(BASE + page)
    entries = "\n".join(f"  <url><loc>{h(url)}</loc></url>" for url in urls)
    write("sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
""")


if __name__ == "__main__":
    build()
