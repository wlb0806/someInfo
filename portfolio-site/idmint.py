"""Localized content and markup for the public IDMint product page."""
from html import escape as h

APP_STORE = "https://apps.apple.com/us/app/idmint-passport-photo-maker/id6798896113"
# Size references from the publicly listed IDMint version and PhotoSpecification.swift.
FORMATS = [
    ("United States", "美国", "Passport photo", "护照照片", "2 × 2 in", "2 × 2 英寸",
     "https://travel.state.gov/content/travel/en/passports/how-apply/photos.html"),
    ("United States", "美国", "Visa photo", "签证照片", "2 × 2 in", "2 × 2 英寸",
     "https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/photos.html"),
    ("Canada", "加拿大", "Passport photo", "护照照片", "50 × 70 mm", "50 × 70 毫米",
     "https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-passports/photos.html"),
    ("United Kingdom", "英国", "Printed passport photo", "纸质护照照片", "35 × 45 mm", "35 × 45 毫米",
     "https://www.gov.uk/photos-for-passports/photo-requirements"),
    ("United Kingdom", "英国", "Online passport photo", "在线护照照片", "600 × 750 px", "600 × 750 像素",
     "https://www.gov.uk/photos-for-passports"),
    ("Ireland", "爱尔兰", "Online passport photo", "在线护照照片", "715 × 951 px", "715 × 951 像素",
     "https://www.ireland.ie/en/dfa/passports/photo-guidelines/"),
    ("France", "法国", "Passport & national ID photos", "护照及身份证照片", "35 × 45 mm", "35 × 45 毫米",
     "https://www.service-public.gouv.fr/particuliers/vosdroits/F10619"),
    ("Netherlands", "荷兰", "Passport, ID & driving licence photos", "护照、身份证及驾照照片", "35 × 45 mm", "35 × 45 毫米",
     "https://www.government.nl/topics/identification-documents/requirements-for-photos"),
    ("Austria", "奥地利", "Passport, ID & driving licence photos", "护照、身份证及驾照照片", "35 × 45 mm", "35 × 45 毫米",
     "https://www.oesterreich.gv.at/de/lexicon/P/Seite.991253"),
    ("Belgium", "比利时", "Passport & Kids-ID photos", "护照及儿童身份证照片", "35 × 45 mm", "35 × 45 毫米",
     "https://diplomatie.belgium.be/en/belgians-abroad/belgian-passport/quality-requirements-photo"),
    ("Italy", "意大利", "Passport & national ID photos", "护照及身份证照片", "35 × 45 mm", "35 × 45 毫米",
     "https://www.esteri.it/it/servizi-opportunita/italiani-all-estero/documenti_di_viaggio/linee-guida-foto-icao/"),
    ("Spain", "西班牙", "Passport & DNI photos", "护照及 DNI 身份证照片", "26 × 32 mm", "26 × 32 毫米",
     "https://www.interior.gob.es/opencms/es/servicios-al-ciudadano/tramites-y-gestiones/pasaporte/procedimiento-de-expedicion/"),
    ("Poland", "波兰", "Passport & national ID photos", "护照及身份证照片", "35 × 45 mm", "35 × 45 毫米",
     "https://www.gov.pl/web/gov/zdjecie-do-dowodu-lub-paszportu"),
    ("Schengen area", "申根区", "Short-stay visa photo", "短期签证照片", "35 × 45 mm", "35 × 45 毫米",
     "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02009R0810-20240628"),
]

COPY = {
    "en": {
        "platform": "For iPhone",
        "title": "Passport & ID photo maker",
        "intro": "Prepare photos for U.S., Canadian and European passport, visa and ID applications. Pick a size, frame your portrait, and export a digital photo or print sheet.",
        "store": "View on the App Store",
        "formats_link": "Find your photo size",
        "privacy_line": "On-device editing · No account or photo uploads",
        "formats_alt": "IDMint’s photo format search on iPhone, showing U.S., Canadian, British and European references",
        "custom_alt": "The IDMint custom size editor with width and height settings in millimeters",
        "featured": [("U.S. passport", "2 × 2 in"), ("UK printed passport", "35 × 45 mm"), ("Canadian passport", "50 × 70 mm")],
        "formats_title": "Passport and ID photo sizes",
        "formats_intro": "IDMint includes searchable references for these formats. Dimensions are the app’s width × height settings. Digital presets are starting points, and each authority sets its own rules for acceptable photos.",
        "columns": ("Country or region", "Photo type", "Size in IDMint", "Authority"),
        "guidance": "Official guidance",
        "requirements": "Some authorities require a professional photographer or prohibit digital edits, including background replacement. Check the current requirements for your application before using an edited or self-taken photo.",
        "workflow_title": "From portrait to print",
        "steps": [
            ("Choose a format", "Search by country, document type or size. Enter millimeters or pixels and a DPI for a custom size you can save."),
            ("Frame the portrait", "Import a photo or take a new one. Use the crop guide, zoom and on-device checks for framing, pose and photo quality."),
            ("Export your photo", "Save a JPEG or PNG, set an optional JPEG file-size target, or arrange copies on a 4 × 6 inch print sheet with cut lines."),
        ],
        "faq_title": "Common questions",
        "faqs": [
            ("What size is a U.S. passport photo?", "The U.S. passport reference in IDMint is 2 × 2 inches (51 × 51 mm when rounded). That creates a 600 × 600 px image at 300 DPI. For online applications, check the separate upload instructions."),
            ("Are printed and online UK passport photos the same size?", "Printed UK passport photos are 35 × 45 mm. For online passport applications, the UK specifies at least 600 pixels wide by 750 pixels tall. IDMint provides a separate reference for each."),
            ("Can I take a Canadian passport photo myself?", "Canada generally requires passport photos to be taken in person by a commercial photographer or studio. Check the official instructions. Use IDMint’s size reference to understand the dimensions."),
            ("Does IDMint make passports, visas or ID cards?", "IDMint prepares the portrait photo you may submit with an application. Issuing authorities make official documents and decide whether submitted photos are accepted."),
            ("Does IDMint upload my photos?", "Cropping, checks and export run on your iPhone. IDMint does not require an app account or upload your photos to a developer-operated server."),
        ],
        "closing": "Prepare your next application photo",
        "paid": "Photo export requires a monthly subscription or a one-time lifetime purchase.",
        "support": "Support",
        "privacy": "Privacy policy",
    },
    "zh": {
        "platform": "适用于 iPhone",
        "title": "护照与证件照制作",
        "intro": "制作适用于美国、加拿大、欧洲等地申请的护照、签证与身份证照片。选择规格、调整人像构图，导出电子照片或打印排版。",
        "store": "查看美区 App Store",
        "formats_link": "查看证件照尺寸",
        "privacy_line": "照片在本机处理 · 无需账号或上传",
        "formats_alt": "IDMint 的证件照规格搜索界面，展示美国、加拿大、英国及其他欧洲国家的规格",
        "custom_alt": "IDMint 的自定义照片尺寸界面，可按毫米填写宽度和高度",
        "featured": [("美国护照", "2 × 2 英寸"), ("英国纸质护照", "35 × 45 毫米"), ("加拿大护照", "50 × 70 毫米")],
        "formats_title": "护照与证件照尺寸",
        "formats_intro": "以下规格可以在 IDMint 中搜索。尺寸按宽 × 高列出。电子照片预设可作为制作起点，照片是否符合要求取决于申请机构的规定。",
        "columns": ("国家或地区", "照片类型", "IDMint 规格", "官方要求"),
        "guidance": "官方指引",
        "requirements": "部分机构要求由专业摄影师拍摄，或禁止更换背景等数字修改。使用自拍或编辑过的照片前，请先查看本次申请的最新规定。",
        "workflow_title": "从人像照片到打印排版",
        "steps": [
            ("选择照片规格", "按国家、证件类型或尺寸搜索。也可以按毫米或像素输入自定义尺寸和 DPI，并保存规格备用。"),
            ("调整人像构图", "从相册导入或拍摄一张照片。用裁剪参考线和缩放工具调整构图，在本机检查姿态和照片质量。"),
            ("导出电子照或排版", "保存 JPEG 或 PNG，可为 JPEG 设置目标文件大小，也可将多张照片排在一张 4 × 6 英寸纸上并添加裁切线。"),
        ],
        "faq_title": "常见问题",
        "faqs": [
            ("美国护照照片是几寸？", "IDMint 中的美国护照照片参考为 2 × 2 英寸，约 51 × 51 毫米，300 DPI 下为 600 × 600 像素。在线申请请另外核对上传要求。"),
            ("英国纸质和在线护照照片的尺寸一样吗？", "纸质照片为 35 × 45 毫米。英国在线护照申请要求至少 600 像素宽、750 像素高。IDMint 分别提供了两个参考规格。"),
            ("加拿大护照照片可以自拍吗？", "加拿大通常要求本人到商业摄影师或照相馆拍摄。请按官方申请指引准备，IDMint 的规格仅供了解所需尺寸。"),
            ("IDMint 可以制作护照、签证或身份证吗？", "IDMint 仅用于制作申请时可能用到的人像照片。证件由有关机构签发，照片也由该机构审核。"),
            ("IDMint 会上传我的照片吗？", "裁剪、照片检查和导出都在 iPhone 上运行。使用 IDMint 无需注册账号，照片不会上传到开发者服务器。"),
        ],
        "closing": "开始准备你的证件照",
        "paid": "导出照片需要月度订阅或一次性购买。中国大陆 App Store 暂未提供。",
        "support": "使用支持",
        "privacy": "隐私政策",
    },
}


def product_page(lang, *, icon, assets, support, privacy, guide_promo=""):
    copy = COPY[lang]
    is_zh = lang == "zh"
    offset = int(is_zh)
    highlights = "\n".join(
        f'          <li><span>{h(label)}</span><strong>{h(size)}</strong></li>'
        for label, size in copy["featured"]
    )
    columns = "".join(f'<th scope="col">{h(label)}</th>' for label in copy["columns"])
    rows = "\n".join(
        f'            <tr><th scope="row">{h(row[offset])}</th><td>{h(row[2 + offset])}</td>'
        f'<td class="mint-size">{h(row[4 + offset])}</td>'
        f'<td><a href="{h(row[6])}" aria-label="{h(row[offset])} · {h(row[2 + offset])} · {h(copy["guidance"])}">'
        f'{h(copy["guidance"])}<span aria-hidden="true"> ↗</span></a></td></tr>'
        for row in FORMATS
    )
    steps = "\n".join(
        f'          <li><h3>{h(title)}</h3><p>{h(text)}</p></li>'
        for title, text in copy["steps"]
    )
    faqs = "\n".join(
        f'        <details><summary>{h(question)}</summary><p>{h(answer)}</p></details>'
        for question, answer in copy["faqs"]
    )
    action = f'<a class="button mint-download" href="{APP_STORE}">{h(copy["store"])} <span aria-hidden="true">↗</span></a>'
    return f"""  <main id="main" class="mint frame">
    <section class="mint-hero" aria-labelledby="mint-title">
      <div class="mint-intro">
        <div class="mint-brand">{icon}<span>IDMint<small>{h(copy['platform'])}</small></span></div>
        <h1 id="mint-title">{h(copy['title'])}</h1>
        <p class="mint-lead">{h(copy['intro'])}</p>
        <div class="mint-actions">
          {action}
          <a class="mint-jump" href="#formats">{h(copy['formats_link'])} <span aria-hidden="true">↓</span></a>
        </div>
        <p class="mint-note">{h(copy['privacy_line'])}</p>
      </div>
      <div class="mint-showcase">
        <ul class="mint-highlights">
{highlights}
        </ul>
        <div class="mint-phone">
          <img src="{assets}/formats-{lang}.webp" width="560" height="1216" fetchpriority="high" alt="{h(copy['formats_alt'])}">
        </div>
      </div>
    </section>{guide_promo}
    <section class="mint-section" id="formats" aria-labelledby="formats-title">
      <h2 id="formats-title">{h(copy['formats_title'])}</h2>
      <p class="mint-section-intro">{h(copy['formats_intro'])}</p>
      <div class="mint-table-wrap">
        <table>
          <thead><tr>{columns}</tr></thead>
          <tbody>
{rows}
          </tbody>
        </table>
      </div>
      <p class="mint-caution">{h(copy['requirements'])}</p>
    </section>
    <section class="mint-section mint-workflow" aria-labelledby="workflow-title">
      <div class="mint-workflow-copy">
        <h2 id="workflow-title">{h(copy['workflow_title'])}</h2>
        <ol>
{steps}
        </ol>
      </div>
      <div class="mint-workflow-image">
        <img src="{assets}/custom-size-{lang}.webp" width="560" height="1216" loading="lazy" decoding="async" alt="{h(copy['custom_alt'])}">
      </div>
    </section>
    <section class="mint-section mint-faq" aria-labelledby="faq-title">
      <h2 id="faq-title">{h(copy['faq_title'])}</h2>
      <div>
{faqs}
      </div>
    </section>
    <section class="mint-closing" aria-labelledby="closing-title">
      <div>
        <h2 id="closing-title">{h(copy['closing'])}</h2>
        <p>{h(copy['paid'])}</p>
      </div>
      <div class="mint-closing-actions">
        {action}
        <div class="mint-resources">
          <a href="{support}">{h(copy['support'])}</a>
          <a href="{privacy}">{h(copy['privacy'])}</a>
        </div>
      </div>
    </section>
  </main>"""
