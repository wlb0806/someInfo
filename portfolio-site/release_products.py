"""Render localized product pages using app copy and release screenshots."""
import json
from html import escape as h
from pathlib import Path

PRODUCTS = {
    "stayframe": {
        "brand": "Stayframe",
        "hero_image": ("journey", 560, 1217),
        "example_image": ("report", 760, 1651),
        "en": {
            "platform": "iPhone · iOS 17 or later",
            "headline": "Rental inspection & condition reports",
            "lead": "Make a room-by-room record when you get the keys. Compare it at move-out and share a clear condition report with your landlord.",
            "store": "Download on the App Store",
            "store_url": "https://apps.apple.com/us/app/stayframe/id6791833165",
            "note": "Records stay on your iPhone. No account required.",
            "jump": "See a sample report",
            "hero_alt": "Stayframe tenancy timeline showing move-in records, report sharing, living notes and move-out steps",
            "features_title": "What to record at each stage",
            "features_intro": "Start with the spaces you rent and use the same rooms again when you move out.",
            "features": [
                ("Move-in inspection", "Record cleanliness and physical condition separately. Photograph existing marks, wear and damage, and add videos or written notes."),
                ("Repairs during the tenancy", "Add dated observations and keep communication attachments with the relevant record. Revisit earlier versions when a condition changes."),
                ("Move-out comparison", "Compare move-in and move-out observations for the same space. Choose relevant rooms for a difference report and record your handover and deposit outcome."),
            ],
            "example_title": "A sample move-in condition report",
            "example_text": "This preview uses an example home. A Stayframe report groups observations by room and includes photos and notes. Export it as a PDF or image so your landlord can review the same record you see.",
            "example_points": [
                "A living-room entry can show cleanliness, physical condition and a note about existing wear.",
                "Share video attachments separately. Mark the report as sent after you share it.",
            ],
            "example_alt": "Sample Stayframe PDF preview for a fictional rental, showing the living-room condition record, photos and export options",
            "enlarge": "Open the full report preview",
            "faq_title": "Rental inspection questions",
            "questions": [
                ("What should I photograph at move-in?", "Start with a wide photo of each room, then capture close-ups of existing marks, damaged fixtures or other conditions you want to discuss. Add notes so it’s clear where each item was found."),
                ("Can I share a report with my landlord?", "Yes. Preview and export the report as a PDF or image. Share video files separately and confirm in Stayframe once you’ve sent the report."),
                ("Can Stayframe decide a deposit dispute?", "Stayframe organizes records for discussion. The report does not determine responsibility, provide legal advice or guarantee a deposit outcome."),
            ],
            "closing": "Start a record for your rental",
            "privacy": "Privacy policy",
        },
        "zh": {
            "platform": "iPhone · iOS 17 或更高版本",
            "headline": "从入住验房到退租交接",
            "lead": "拿到钥匙时逐间记录房况，退租时对照同一房间，并导出清晰的验房报告和房东沟通。",
            "store": "查看美区 App Store",
            "store_url": "https://apps.apple.com/us/app/stayframe/id6791833165",
            "note": "记录保存在 iPhone 上，无需注册账号。",
            "jump": "查看报告示例",
            "hero_alt": "Stayframe 租住流程界面，展示入住记录、发送报告、居住笔记和退租步骤",
            "features_title": "租房各阶段，分别记录什么",
            "features_intro": "先选出租住空间，退租时按同一房间逐一对照。",
            "features": [
                ("入住验房", "把清洁度和物品状况分开记录。为已有的污渍、磨损或破损拍照，也可补充视频和文字说明。"),
                ("居住期间的维修", "记录问题发现和维修的日期，把沟通附件保存在对应记录中。房况发生变化时，可以回看之前保存的版本。"),
                ("退租房况对比", "将入住和退租记录按房间对照。选取相关空间生成差异报告，并保留交接和押金处理结果。"),
            ],
            "example_title": "入住验房报告示例",
            "example_text": "截图来自虚构房屋的报表示例。Stayframe 按房间汇总照片和备注，可导出 PDF 或图片，让房东查看同一份记录。",
            "example_points": [
                "例如，客厅记录可以分别展示清洁度、物品状况和入住前的磨损。",
                "视频附件可单独分享。发送后，可以在 Stayframe 标记已发送。",
            ],
            "example_alt": "Stayframe 虚构租屋的入住报告预览，展示客厅房况、照片与导出选项",
            "enlarge": "查看完整报告截图",
            "faq_title": "租房验房常见问题",
            "questions": [
                ("入住时要拍哪些照片？", "可以先拍每个房间的全景，再拍已有刮痕、破损或值得说明的地方。加上位置和现象说明，方便日后回看。"),
                ("怎样把验房报告发给房东？", "在 Stayframe 预览报告后选择导出 PDF 或图片。视频文件单独分享，发送完成后可以在应用中确认。"),
                ("Stayframe 能判定押金纠纷责任吗？", "Stayframe 用于整理沟通所需的记录。报告不能认定责任、提供法律意见或保证押金退还。"),
            ],
            "closing": "为你的租住房屋建一份记录",
            "privacy": "隐私政策",
        },
    },
    "eos": {
        "brand": "Eos",
        "hero_image": ("results", 1229, 768),
        "example_image": ("review", 1229, 768),
        "en": {
            "platform": "Mac · macOS 14 or later",
            "headline": "See what’s taking up space on your Mac",
            "lead": "Find Xcode caches, large files, duplicates and app leftovers. Eos explains what each result is so you can decide what to remove.",
            "store": "Download on the Mac App Store",
            "store_url": "https://apps.apple.com/us/app/eos-disk-cleanup/id6794152421?mt=12",
            "note": "Free · No ads or subscriptions · Scans run on your Mac",
            "jump": "See what Eos finds",
            "hero_alt": "Eos Mac storage scan results showing system junk, developer caches and files grouped by what needs review",
            "features_title": "Mac storage, sorted by what it holds",
            "features_intro": "Run a scan, open a category, and review the files and consequences before you clear anything.",
            "features": [
                ("Xcode and developer caches", "Find Xcode Derived Data, simulator caches and old device support, along with Homebrew, npm, CocoaPods and other package manager caches."),
                ("Large files and exact duplicates", "Sort large video, audio and other files by size. Eos verifies exact duplicates by matching file content, so you can choose which copies to keep."),
                ("Old apps and leftovers", "Review unused apps, their associated files, logs and user caches. Eos also surfaces supported terminal tools and startup items for inspection."),
            ],
            "example_title": "Review what will change",
            "example_text": "Open a scan result to see why it can be removed and what will happen afterward. Some caches are rebuilt by the app that created them, and some package files may need to be downloaded again.",
            "example_points": [
                "Eos separates straightforward cleanup from items that need your review.",
                "Files go to the Trash by default. Running apps and protected paths are skipped.",
            ],
            "example_alt": "Eos system junk tab with cache results and an explanation of the selected item",
            "enlarge": "Open the full screenshot",
            "faq_title": "Mac disk cleanup questions",
            "questions": [
                ("Can Eos help clear Xcode storage?", "Yes. Eos identifies Derived Data, simulator caches and old device support. Review the details before removing anything you may need for a future build or device."),
                ("How does Eos find duplicate files?", "Eos checks file content using hashes so it can surface exact copies. Review their locations and choose which files to keep."),
                ("Does Eos delete files automatically?", "You choose which items to remove and confirm cleanup. Files go to the Trash by default."),
                ("Does Eos upload information about my files?", "Eos runs scans and cleanup locally on your Mac and does not use a developer server, analytics or an app account."),
            ],
            "closing": "Make room on your Mac",
            "support": "Support",
            "privacy": "Privacy policy",
        },
        "zh": {
            "platform": "Mac · macOS 14 或更高版本",
            "headline": "看清 Mac 磁盘占用",
            "lead": "查找 Xcode 缓存、大文件、完全重复的文件和应用残留。Eos 会说明每项结果是什么，再由你决定是否清理。",
            "store": "在 Mac App Store 下载",
            "store_url": "https://apps.apple.com/cn/app/eos-%E7%A3%81%E7%9B%98%E6%B8%85%E7%90%86/id6794152421?mt=12",
            "note": "免费 · 无广告和订阅 · 扫描在 Mac 上完成",
            "jump": "查看可清理项目",
            "hero_alt": "Eos 的 Mac 磁盘扫描结果，按类别列出系统垃圾、开发缓存和需要复核的项目",
            "features_title": "按类别查看磁盘占用",
            "features_intro": "扫描后打开任意类别，先确认文件用途和清理影响，再决定要清哪些。",
            "features": [
                ("Xcode 与开发缓存", "查找 Xcode Derived Data、模拟器缓存、旧设备支持文件，以及 Homebrew、npm 和 CocoaPods 等工具的缓存。"),
                ("大文件与完全重复的文件", "按大小查看视频、音频和其他文件。Eos 按内容识别完全相同的文件，由你决定保留哪个副本。"),
                ("应用卸载与残留", "查看很少使用的 App、相关残留、日志和用户缓存，也可以检查受支持的命令行工具和启动项。"),
            ],
            "example_title": "清理前先看会发生什么",
            "example_text": "点开扫描结果，查看可清理的原因以及清理后的影响。有些缓存会由应用重新生成，有些依赖文件下次使用时需要重新下载。",
            "example_points": [
                "可直接清理的内容与需要复核的文件分开列出。",
                "默认移入废纸篓。运行中的应用和受保护路径会被跳过。",
            ],
            "example_alt": "Eos 的系统垃圾页面，展示缓存列表和所选项目的清理说明",
            "enlarge": "查看完整截图",
            "faq_title": "Mac 磁盘清理常见问题",
            "questions": [
                ("Eos 能清理 Xcode 占用的空间吗？", "可以查找 Derived Data、模拟器缓存和旧设备支持文件。建议先查看每项说明，确认后续构建或连接设备是否还需要它。"),
                ("Eos 如何判断文件重复？", "Eos 会用内容哈希核对文件，找出完全相同的副本。你可以查看各副本所在位置，再决定保留哪一个。"),
                ("Eos 会自动删除文件吗？", "由你选择并确认清理项目。默认将清理的文件移入废纸篓。"),
                ("扫描结果会上传吗？", "扫描和清理都在 Mac 上运行。Eos 无需账号，也不使用开发者服务器或分析服务。"),
            ],
            "closing": "给 Mac 腾出空间",
            "support": "使用支持",
            "privacy": "隐私政策",
        },
    },
}
PRODUCTS.update(json.loads(Path(__file__).with_name("app_websites.json").read_text(encoding="utf-8")))


def product_page(slug, lang, *, icon, assets, resources):
    product = PRODUCTS[slug]
    copy = product[lang]
    image_language = product.get("image_language", lang)
    cards = "\n".join(
        f"        <article><h3>{h(title)}</h3><p>{h(text)}</p></article>"
        for title, text in copy["features"]
    )
    points = "\n".join(f"          <li>{h(text)}</li>" for text in copy["example_points"])
    questions = "\n".join(
        f"        <details><summary>{h(question)}</summary><p>{h(answer)}</p></details>"
        for question, answer in copy["questions"]
    )
    links = "".join(f'<a href="{h(url)}">{h(copy[key])}</a>' for key, url in resources.items())
    link = h(copy["store_url"])
    action = f'<a class="button release-cta" href="{link}">{h(copy["store"])} <span aria-hidden="true">↗</span></a>'
    jump = "example" if slug == "stayframe" else "features"
    hero, hero_width, hero_height = product["hero_image"]
    example, example_width, example_height = product["example_image"]
    portrait = " release-portrait" if hero_width < hero_height and slug != "stayframe" else ""
    return f"""  <main id="main" class="release-product release-{slug}{portrait} frame">
    <section class="release-hero" aria-labelledby="product-title">
      <div class="release-intro">
        <div class="release-platform">{icon}<p>{h(copy['platform'])}</p></div>
        <h1 id="product-title">{h(copy['headline'])}</h1>
        <p class="release-lead">{h(copy['lead'])}</p>
        <div class="release-actions">
          {action}
          <a class="release-jump" href="#{jump}">{h(copy['jump'])} <span aria-hidden="true">↓</span></a>
        </div>
        <p class="release-note">{h(copy['note'])}</p>
      </div>
      <div class="release-showcase">
        <img src="{assets}/{hero}-{image_language}.webp" width="{hero_width}" height="{hero_height}" fetchpriority="high" alt="{h(copy['hero_alt'])}">
      </div>
    </section>
    <section class="release-section" id="features" aria-labelledby="features-title">
      <div class="release-section-heading">
        <h2 id="features-title">{h(copy['features_title'])}</h2>
        <p>{h(copy['features_intro'])}</p>
      </div>
      <div class="release-features">
{cards}
      </div>
    </section>
    <section class="release-section release-example" id="example" aria-labelledby="example-title">
      <div class="release-example-copy">
        <h2 id="example-title">{h(copy['example_title'])}</h2>
        <p>{h(copy['example_text'])}</p>
        <ul>
{points}
        </ul>
      </div>
      <figure>
        <img src="{assets}/{example}-{image_language}.webp" width="{example_width}" height="{example_height}" loading="lazy" decoding="async" alt="{h(copy['example_alt'])}">
        <figcaption>
        <a href="{assets}/{example}-{image_language}.webp">
          {h(copy['enlarge'])} <span aria-hidden="true">↗</span>
        </a>
        </figcaption>
      </figure>
    </section>
    <section class="release-section release-faq" aria-labelledby="faq-title">
      <h2 id="faq-title">{h(copy['faq_title'])}</h2>
      <div>
{questions}
      </div>
    </section>
    <section class="release-closing" aria-labelledby="closing-title">
      <h2 id="closing-title">{h(copy['closing'])}</h2>
      <div class="release-actions">{action}<div class="release-resources">{links}</div></div>
    </section>
  </main>"""
