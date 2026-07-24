const copy = {
  zh: {
    skip: "跳到作品",
    brand: "独立开发者",
    navApps: "作品",
    navAbout: "关于",
    eyebrow: "为 Apple 平台打造 · 持续更新中",
    heroLine1: "小而专注的应用，",
    heroLine2: "认真做得更好。",
    heroIntro: "我是一名独立开发者，喜欢把日常里不够顺手的事，做成简单、漂亮、真正有用的产品。",
    seeApps: "查看全部作品",
    stageNote: "六个想法，六种日常。",
    statApps: "款独立应用",
    statLanguages: "种网站语言",
    selectedWork: "精选作品",
    appsHeading: "我的作品",
    appsIntro: "工具让生活轻一点，游戏让空闲有趣一点。",
    iOSSummary: "5 款为 iPhone 与 iPad 打造的作品",
    macOSSummary: "1 款为 Mac 打造的效率工具",
    applicationGroup: "应用",
    gameGroup: "游戏",
    applicationHint: "解决日常里的具体问题",
    gameHint: "让空闲的片刻更有趣",
    behindApps: "作品背后",
    aboutHeading: "独立制作，认真打磨。",
    aboutBody: "从一个具体的小问题出发，完成设计、开发和发布的每一步。没有庞大的团队，只有对清晰体验、可靠功能和细节的坚持。",
    principle1: "专注",
    principle2: "隐私",
    principle3: "品质",
    footerLine: "为有用的时刻，也为放松的片刻。",
    footerRights: "用心制作",
    appStore: "前往 App Store",
    storeLabel: "App Store",
  },
  en: {
    skip: "Skip to work",
    brand: "Independent Maker",
    navApps: "Apps",
    navAbout: "About",
    eyebrow: "Made for Apple platforms · Always evolving",
    heroLine1: "Small, focused apps.",
    heroLine2: "Made with big care.",
    heroIntro: "I’m an independent developer turning everyday friction into simple, thoughtful products that are genuinely useful.",
    seeApps: "Explore the apps",
    stageNote: "Six ideas for everyday life.",
    statApps: "independent apps",
    statLanguages: "site languages",
    selectedWork: "SELECTED WORK",
    appsHeading: "The app collection",
    appsIntro: "Tools to make life lighter. Games to make quiet moments brighter.",
    iOSSummary: "5 products made for iPhone and iPad",
    macOSSummary: "1 focused utility made for Mac",
    applicationGroup: "Apps",
    gameGroup: "Games",
    applicationHint: "Useful answers to everyday problems",
    gameHint: "A little more play in quiet moments",
    behindApps: "BEHIND THE APPS",
    aboutHeading: "Independently made. Carefully refined.",
    aboutBody: "Each app begins with one specific problem, then moves through design, development and launch. No huge team—just a belief in clear experiences, dependable features and thoughtful details.",
    principle1: "Focused",
    principle2: "Private",
    principle3: "Polished",
    footerLine: "For useful moments and playful breaks.",
    footerRights: "Made with care",
    appStore: "View on the App Store",
    storeLabel: "App Store",
  },
};

const apps = [
  {
    name: "ReceiptGuard: Returns",
    os: "ios",
    kind: "application",
    icon: "assets/icons/receiptguard.png",
    url: "https://apps.apple.com/cn/app/id6791833165",
    platform: { zh: "iPhone · 生活", en: "iPhone · Lifestyle" },
    subtitle: { zh: "退货与保修追踪", en: "Return & Warranty Tracker" },
    description: {
      zh: "集中保存收据、退货日期、保修信息、商品照片和序列号，让每一次购买都更安心。",
      en: "Keep receipts, return dates, warranties, product photos and serial numbers together—so every purchase stays covered.",
    },
  },
  {
    name: "CalendarKiller",
    os: "ios",
    kind: "application",
    icon: "assets/icons/calendarkiller.png",
    url: "https://apps.apple.com/cn/app/id6787564566",
    platform: { zh: "iPhone & iPad · 工具", en: "iPhone & iPad · Utility" },
    subtitle: { zh: "删除日历广告与垃圾邀请", en: "Remove Calendar Spam & Viruses" },
    description: {
      zh: "在本机发现日历广告、垃圾邀请和重复事件，删除前逐项确认，干净又安心。",
      en: "Find calendar spam, suspicious invitations and duplicate events on device. Review every item before cleanup.",
    },
  },
  {
    name: "Trio: Daily Logic Puzzles",
    os: "ios",
    kind: "game",
    icon: "assets/icons/trio.png",
    url: "https://apps.apple.com/cn/app/id6791609588",
    platform: { zh: "iPhone & iPad · 游戏", en: "iPhone & iPad · Game" },
    subtitle: { zh: "每天三道，全球同题", en: "Three puzzles, every day" },
    description: {
      zh: "画一笔路径、平衡一张格子、为棋盘加冕。每天三道小谜题，每道题都保证唯一解。",
      en: "Draw a path, balance a grid and crown a board. Three fresh daily puzzles, each with exactly one solution.",
    },
  },
  {
    name: "Knots: Connect Puzzle",
    os: "ios",
    kind: "game",
    icon: "assets/icons/knots.png",
    url: "https://apps.apple.com/cn/app/id6790466420",
    platform: { zh: "iPhone & iPad · 游戏", en: "iPhone & iPad · Game" },
    subtitle: { zh: "惬意的连点解谜", en: "Cozy connect-the-dots puzzle" },
    description: {
      zh: "连接同色圆点、填满网格、解开思绪。999 关加每日谜题，没有计时、压力和广告。",
      en: "Link matching dots and fill the grid across 999 levels plus a daily puzzle. No timers, pressure or ads.",
    },
  },
  {
    name: "Spruce: Mac Cleaner",
    os: "macos",
    kind: "application",
    icon: "assets/icons/spruce.png",
    url: "https://apps.apple.com/cn/app/id6794152421",
    platform: { zh: "Mac · 工具", en: "Mac · Utility" },
    subtitle: { zh: "清垃圾、卸载应用、找重复", en: "Clean junk, uninstall apps" },
    description: {
      zh: "看清磁盘被什么占满，只清理你确认的内容。一切移入废纸篓，随时可以恢复。",
      en: "See exactly what fills your disk and clean only what you approve. Everything goes to Trash and stays recoverable.",
    },
  },
  {
    name: "Scentory: Fragrance Wardrobe",
    os: "ios",
    kind: "application",
    icon: "assets/icons/scentory.png",
    url: "https://apps.apple.com/cn/app/id6793348562",
    platform: { zh: "iPhone · 生活", en: "iPhone · Lifestyle" },
    subtitle: { zh: "收藏、记录与分享香气", en: "Collect, rate & share scents" },
    description: {
      zh: "为你的香水收藏打造一个私密而漂亮的家。记录穿香、管理愿望清单，并分享精美收藏卡。",
      en: "A private, beautiful home for your fragrance collection. Log what you wear, build a wishlist and share it beautifully.",
    },
  },
];

const portfolioGroups = document.querySelector("#portfolio-groups");
const languageButtons = [...document.querySelectorAll("[data-lang]")];
let currentLanguage = getInitialLanguage();

function getInitialLanguage() {
  const saved = localStorage.getItem("portfolio-language");
  if (saved === "zh" || saved === "en") return saved;
  return navigator.language.toLowerCase().startsWith("zh") ? "zh" : "en";
}

function externalLinkIcon() {
  return '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M7 5h8v8M15 5l-9 9" /></svg>';
}

function renderApps(lang) {
  const platforms = [
    { id: "ios", label: "iOS", summary: copy[lang].iOSSummary },
    { id: "macos", label: "macOS", summary: copy[lang].macOSSummary },
  ];
  const kinds = [
    { id: "application", label: copy[lang].applicationGroup, hint: copy[lang].applicationHint },
    { id: "game", label: copy[lang].gameGroup, hint: copy[lang].gameHint },
  ];

  const cardMarkup = (app, index) => `
        <article class="app-card card-${index + 1}">
          <div class="card-top">
            <img class="app-icon" src="${app.icon}" alt="${app.name} icon" loading="lazy" />
            <span class="app-meta">${app.platform[lang]}</span>
          </div>
          <h5>${app.name}</h5>
          <p class="app-subtitle">${app.subtitle[lang]}</p>
          <p class="app-description">${app.description[lang]}</p>
          <a class="app-link" href="${app.url}" target="_blank" rel="noopener noreferrer" aria-label="${copy[lang].appStore}: ${app.name}">
            ${copy[lang].appStore} ${externalLinkIcon()}
          </a>
          <span class="card-index" aria-hidden="true">${String(index + 1).padStart(2, "0")}</span>
        </article>
      `;

  let cardIndex = 0;
  portfolioGroups.innerHTML = platforms
    .map((platform) => {
      const platformApps = apps.filter((app) => app.os === platform.id);
      const categoryMarkup = kinds
        .map((kind) => {
          const categoryApps = platformApps.filter((app) => app.kind === kind.id);
          if (!categoryApps.length) return "";
          const cards = categoryApps.map((app) => cardMarkup(app, cardIndex++)).join("");
          return `
            <section class="category-block" aria-labelledby="${platform.id}-${kind.id}-heading">
              <div class="category-heading reveal">
                <div>
                  <span class="category-line" aria-hidden="true"></span>
                  <h4 id="${platform.id}-${kind.id}-heading">${kind.label}</h4>
                </div>
                <p>${kind.hint}</p>
              </div>
              <div class="app-grid${categoryApps.length === 1 ? " is-single" : ""}">${cards}</div>
            </section>
          `;
        })
        .join("");

      return `
        <section class="platform-section" aria-labelledby="${platform.id}-heading">
          <header class="platform-heading reveal">
            <div class="platform-name">
              <span class="platform-badge" aria-hidden="true">${platform.id === "ios" ? "●" : "◆"}</span>
              <h3 id="${platform.id}-heading">${platform.label}</h3>
            </div>
            <p>${platform.summary}</p>
          </header>
          ${categoryMarkup}
        </section>
      `;
    })
    .join("");

  observeReveals(document.querySelectorAll(".app-card"));
  observeReveals(portfolioGroups.querySelectorAll(".reveal"));
}

function setLanguage(lang) {
  currentLanguage = lang;
  document.documentElement.lang = lang === "zh" ? "zh-CN" : "en";
  document.title = lang === "zh" ? "独立应用作品集" : "Independent App Portfolio";
  document.querySelectorAll("[data-i18n]").forEach((element) => {
    element.textContent = copy[lang][element.dataset.i18n];
  });
  languageButtons.forEach((button) => {
    button.setAttribute("aria-pressed", String(button.dataset.lang === lang));
  });
  localStorage.setItem("portfolio-language", lang);
  renderApps(lang);
}

function observeReveals(elements) {
  if (!("IntersectionObserver" in window)) {
    elements.forEach((element) => element.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.12 },
  );

  elements.forEach((element, index) => {
    if (element.classList.contains("app-card")) {
      element.style.transitionDelay = `${(index % 2) * 90}ms`;
    }
    observer.observe(element);
  });
}

languageButtons.forEach((button) => {
  button.addEventListener("click", () => setLanguage(button.dataset.lang));
});

document.querySelector("#year").textContent = new Date().getFullYear();
setLanguage(currentLanguage);
observeReveals(document.querySelectorAll(".reveal"));
