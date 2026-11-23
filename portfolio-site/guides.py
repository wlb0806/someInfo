"""Render illustrated guides and links to them from the corresponding product pages."""
import json
from html import escape as h
from pathlib import Path

GUIDES = json.loads(Path(__file__).with_name("guides.json").read_text(encoding="utf-8"))

LABELS = {
    "en": {
        "guide": "Illustrated guide", "read": "Read the guide", "contents": "In this guide",
        "screenshot": "Open full screenshot", "product": "Back to product", "store": "View in the App Store",
    },
    "zh": {
        "guide": "图文教程", "read": "阅读教程", "contents": "本篇内容",
        "screenshot": "查看完整截图", "product": "返回产品页", "store": "前往 App Store",
    },
}


def teaser(lang, guide, href):
    copy, labels = guide[lang], LABELS[lang]
    title = h(copy["title"])
    return f"""    <aside class="guide-promo" aria-label="{labels['guide']}">
      <div>
        <p class="guide-promo-label">{labels['guide']}</p>
        <p class="guide-promo-title"><a href="{h(href)}">{title}</a></p>
        <p class="guide-promo-description">{h(copy['teaser'])}</p>
      </div>
      <a class="guide-promo-action" href="{h(href)}" aria-label="{labels['read']} · {title}">{labels['read']} <span aria-hidden="true">→</span></a>
    </aside>"""


def figure(step, guide, lang, asset_prefix, first):
    if "image" not in step:
        return ""
    image = step["image"]
    width, height = guide["images"][image][lang]
    src = h(f"{asset_prefix}/{image}-{lang}.webp")
    portrait = " guide-portrait" if height > width else ""
    loading = "" if first else ' loading="lazy"'
    description = h(step["alt"])
    return f"""
          <figure class="guide-figure{portrait}">
            <img src="{src}" width="{width}" height="{height}" alt="{description}"{loading} decoding="async">
            <figcaption>{h(step["caption"])} <a href="{src}" aria-label="{LABELS[lang]['screenshot']} · {description}">{LABELS[lang]['screenshot']} <span aria-hidden="true">↗</span></a></figcaption>
          </figure>"""


def reference_table(table):
    columns = "".join(f'<th scope="col">{h(label)}</th>' for label in table["headers"])
    rows = []
    for name, *values in table["rows"]:
        cells = []
        for value in values:
            if isinstance(value, list):
                label, url = value
                cells.append(f'<td><a href="{h(url)}">{h(label)}</a></td>')
            else:
                cells.append(f"<td>{h(value)}</td>")
        rows.append(f'<tr><th scope="row">{h(name)}</th>{"".join(cells)}</tr>')
    body = "\n".join(f"            {row}" for row in rows)
    return f"""      <section id="reference" class="guide-reference" aria-labelledby="reference-title">
        <h2 id="reference-title">{h(table['title'])}</h2>
        <div class="guide-table">
          <table>
            <thead><tr>{columns}</tr></thead>
            <tbody>
{body}
            </tbody>
          </table>
        </div>
      </section>"""


def guide_content(slug, lang, *, guide, product_url, store_url, asset_prefix):
    copy, labels = guide[lang], LABELS[lang]
    contents = []
    steps = []
    for n, step in enumerate(copy["steps"], 1):
        step_id = f"step-{n}"
        title = h(step["title"])
        contents.append(f'          <li><a href="#{step_id}">{title}</a></li>')
        paragraphs = "\n".join(f"            <p>{h(text)}</p>" for text in step["body"])
        picture = figure(step, guide, lang, asset_prefix, first=n == 1)
        steps.append(f"""        <section class="guide-step" id="{step_id}" aria-labelledby="{step_id}-title">
          <div class="guide-step-copy">
            <h2 id="{step_id}-title"><span>{n}.</span> {title}</h2>
{paragraphs}
          </div>{picture}
        </section>""")

    reference = ""
    if "table" in copy:
        reference = reference_table(copy["table"]) + "\n"
    after_steps = ""
    if "checklist" in copy:
        checklist = copy["checklist"]
        items = "\n".join(f"          <li>{h(item)}</li>" for item in checklist["items"])
        after_steps = f"""      <section id="checklist" class="guide-checklist" aria-labelledby="checklist-title">
        <h2 id="checklist-title">{h(checklist['title'])}</h2>
        <ul>
{items}
        </ul>
      </section>
"""

    contents_html = "\n".join(contents)
    steps_html = "\n".join(steps)
    return f"""  <main class="frame guide guide-{slug}" id="main">
    <article aria-labelledby="guide-title">
      <header class="guide-header">
        <div>
          <p class="guide-label">{labels['guide']}</p>
          <h1 id="guide-title">{h(copy['title'])}</h1>
          <p class="guide-intro">{h(copy['intro'])}</p>
        </div>
        <nav class="guide-contents" aria-label="{labels['contents']}">
          <p>{labels['contents']}</p>
          <ol>
{contents_html}
          </ol>
        </nav>
      </header>
{reference}      <div class="guide-steps">
{steps_html}
      </div>
{after_steps}      <div class="guide-end">
        <a href="{h(product_url)}"><span aria-hidden="true">←</span> {labels['product']}</a>
        <a class="button" href="{h(store_url)}">{labels['store']} <span aria-hidden="true">↗</span></a>
      </div>
    </article>
  </main>"""
