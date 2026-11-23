# My Apps — Privacy-First Utilities, Puzzles & Productivity Apps

This workspace contains **12 native Apple-platform app projects** (11 iOS projects and one macOS project) and **one portfolio website**. The collection covers rental-home records, receipts and maintenance, personal memories, photo editing and cleanup, perfume samples, habits, savings, disk cleanup, and games. Foliover combines five utility services in a single app project.

Last updated: **November 23, 2026**. This inventory reflects the folders currently present, local source code, project documentation, and English Fastlane metadata. Some project folders retain earlier working names. App Store links come from project records; the descriptions reflect local development and may differ from a published version. Store availability and commercial terms are determined by each App Store listing. An App Store Connect record does not by itself mean an app is publicly available.

## Apps at a Glance

| Icon | App | Platform | What it does | Links |
| :---: | --- | :---: | --- | :---: |
| <img src="./receiptguard/ReceiptGuard/Resources/Assets.xcassets/AppIcon.appiconset/AppIcon-1024.png" width="64" alt="Stayframe app icon"> | **Stayframe** | iOS / iPhone | Rental-home condition records, move-in/out comparisons, and reports | [App Store record](https://apps.apple.com/app/id6791833165) · [Project](receiptguard/) |
| <img src="./calendar/CalendarKiller/CalendarKiller/Assets.xcassets/AppIcon.appiconset/Foliover-1024.png" width="64" alt="Foliover app icon"> | **Foliover: Photos & Space** | iOS / iPhone & iPad | Photo cleanup, timestamp camera, photo & print, image compression, and calendar cleanup | [App Store](https://apps.apple.com/app/id6787564566) · [Project](calendar/CalendarKiller/) |
| <img src="./assets/app-icons/trio.png" width="64" alt="Trio Daily Logic Puzzles app icon"> | **Trio: Daily Logic Puzzles** | iOS / iPhone | Three fresh logic puzzles every day, each verified to have one solution | [App Store](https://apps.apple.com/app/id6791609588) · [Project](game/trio/) |
| <img src="./assets/app-icons/knots.png" width="64" alt="Knots Connect Puzzle app icon"> | **Knots: Connect Puzzle** | iOS / iPhone & iPad | A cozy connect-the-dots puzzle with full-grid Perfect goals | [App Store](https://apps.apple.com/app/id6790466420) · [Project](game/killAI/) |
| <img src="./Spruce/Spruce/Resources/Assets.xcassets/AppIcon.appiconset/icon_128.png" width="64" alt="Eos Mac disk cleaner app icon"> | **Eos: Disk Cleanup** | macOS / Mac | Private disk-space analyzer, junk cleaner, and app uninstaller | [Mac App Store](https://apps.apple.com/app/id6794152421) · [Project](Spruce/) |
| <img src="./Scentory/Scentory/Support/Assets.xcassets/AppIcon.appiconset/icon_1024.png" width="64" alt="Scentory Perfume Samples app icon"> | **Scentory: Perfume Samples** | iOS / iPhone | Sample boxes, scent trials, impressions, decisions, and private iCloud sync | [App Store](https://apps.apple.com/app/id6793348562) · [Project](Scentory/) |
| <img src="./assets/app-icons/daily-quest.png" width="64" alt="Daily Quest Habit and Goals app icon"> | **Daily Quest: Habit & Goals** | iOS / iPhone & iPad | Habit tracker, goal planner, streaks, and Live Activities | [App Store](https://apps.apple.com/app/id6797427767) · [Project](DailyQuest/) |
| <img src="./HomeCue/HomeCue/Resources/Assets.xcassets/AppIcon.appiconset/HomeCue-AppIcon-1024.png" width="64" alt="HomeCue app icon"> | **HomeCue: Receipts & Care** | iOS / iPhone & iPad | Item care, receipts, returns, warranties, and maintenance history | [App Store](https://apps.apple.com/app/id6810898865) · [Project](HomeCue/) |
| <img src="./importantPeople/Dearfolk/Assets.xcassets/AppIcon.appiconset/AppIcon.png" width="64" alt="Family & Friends Journal app icon"> | **Family & Friends Journal** | iOS / iPhone | Private people profiles, memories, birthdays, and personal documents | [App Store Connect](https://appstoreconnect.apple.com/apps/6835294742/distribution) · [Project](importantPeople/) |
| <img src="./PassportPhotoMaker/PassportPhotoMaker/Support/Assets.xcassets/AppIcon.appiconset/AppIcon.png" width="64" alt="Photo Maker app icon"> | **Photo Maker: Standard Sizes** | iOS / iPhone | Standard and custom photo sizes, background editing, and multipage print sheets | [App Store](https://apps.apple.com/app/id6798896113) · [Project](PassportPhotoMaker/) |
| <img src="./Nada/Nada/Support/Assets.xcassets/AppIcon.appiconset/icon_1024.png" width="64" alt="Dewday app icon"> | **Dewday: Daily Savings** | iOS / iPhone | Daily spending check-ins, savings challenges, plant growth, badges, and a widget | [Project](Nada/) |
| — | **Nightblade · 夜刃** | iOS / landscape game | Playable ninja action prototype with platforming, enemies, and bosses | [Project](game/Nightblade/) |

### Web Projects

| Project | Platform | What it does | Folder |
| --- | --- | --- | --- |
| **Independent App Portfolio** | Web browser | Bilingual app showcase with icons, categories, and store links | [portfolio-site](portfolio-site/) |

## Stayframe

### Rental-Home Records from Move-in to Move-out

Stayframe is the current native UIKit app in the `receiptguard` folder. It replaces the earlier receipt tracker with a rental-home workflow while retaining the `ReceiptGuard` project and existing bundle identifier.

Choose a property type and the spaces you rent, then capture photos, videos, and notes about cleanliness and physical condition. Keep move-in revisions, living notes, repairs, and communication attachments together. Compare the same spaces at move-out, review disagreements when needed, and retain handover and deposit outcomes in the rental archive.

Preview saved reports and export PDFs or images; video attachments are shared separately. Report sending requires explicit confirmation from the user, and local reminders can help follow up on sending the move-in report. Records stay on-device, with no account or current iCloud sync. English and Simplified Chinese are supported. The app organizes records for communication and does not determine responsibility or guarantee a deposit outcome.

[Existing App Store record](https://apps.apple.com/app/id6791833165) · [Project folder](receiptguard/) · [Project README](receiptguard/README.md)

## Foliover: Photos & Space

### Five Services for Photos, Exports & Calendar Cleanup

Foliover lives in the `calendar/CalendarKiller` folder, which previously contained Calendar Spam Cleaner. The current app brings five services into one workspace:

- **Photo Cleanup:** review duplicate and similar photos, screenshots, large items, and videos before confirming removal. Deleted items move to Photos' Recently Deleted.
- **Timestamp Camera:** capture or import a photo, add a date, time, optional location, and note, then save a new JPG copy.
- **Photo & Print:** replace portrait backgrounds, crop and size photos, and arrange copies on A4, Letter, or 4 × 6 paper. Preview and export JPG, PNG, or PDF.
- **Image Compression:** reduce file size, resize images, convert formats, compare results, and export a copy.
- **Calendar Cleanup:** inspect unwanted invitations, duplicate events, and unfamiliar subscriptions with explanations before cleanup. Read-only subscriptions may need removal in Apple's Calendar app.

Completed image exports remain available in **Your work** for later sharing. Photo and calendar analysis, editing, and stamp rendering run on-device; no app account is required, and permissions are requested when a chosen feature needs them.

Each service includes one free successful use. Afterwards, a completed optional share grants one additional use of that service, or a one-time purchase unlocks an individual service or all five for lifetime use. A cleanup batch counts as one use regardless of item count; sharing does not grant unlimited access. Restore Purchases is available.

[Foliover App Store link](https://apps.apple.com/app/id6787564566) · [Project folder](calendar/CalendarKiller/) · [Current product description](calendar/CalendarKiller/fastlane/metadata/en-US/description.txt)

## Trio: Daily Logic Puzzles

### Three Daily Brain Teasers — Trace, Lumen & Crowns

Trio is a daily puzzle habit that fits into a coffee break. Everyone receives the same three puzzles each day:

- **Trace:** draw one path through every numbered cell.
- **Lumen:** balance suns and moons while following line and clue rules.
- **Crowns:** place one crown in each row, column, and color region without touching.

Every puzzle is verified to have exactly one solution. Trio includes streaks, solve times, personal bests, shareable result cards, practice mode, hints, and private iCloud progress sync. Core play works offline with no account, ads, or tracking. The daily puzzles are free; an optional one-time Pro unlock expands the archive, practice, hints, and statistics.

[Download Trio: Daily Logic Puzzles on the App Store](https://apps.apple.com/app/id6791609588) · [Project folder](game/trio/)

## Knots: Connect Puzzle

### A Cozy Connect-the-Dots Logic Game

Knots is a relaxing flow-style puzzle: connect every matching pair of colored dots without crossing lines. Filling the entire grid earns a **Perfect** result. There are no timers and no pressure—just a quiet board and the satisfaction of making every connection fit.

Play through 999 hand-tuned levels from 5×5 to 12×12, take on the same Daily Challenge as everyone else, build a streak, use gentle hints, and play offline. An optional one-time Knots Pro purchase unlocks all levels, unlimited hints, Endless Mode, and future updates. There are no ads or subscriptions.

The current project also supports private iCloud progress sync, puzzle invitations that reward hints, and branded result cards.

[Download Knots: Connect Puzzle on the App Store](https://apps.apple.com/app/id6790466420) · [Project folder](game/killAI/)

## Eos: Disk Cleanup

### A Private Mac Cleaner with Clear Cleanup Decisions

Eos, formerly Spruce, shows exactly what is using your Mac storage and lets you clean only what you approve. It finds caches, logs, diagnostic reports, large media files, exact duplicates, application leftovers, startup items, and developer files from tools such as Xcode, npm, CocoaPods, and Homebrew. Results explain why an item is removable and what happens after cleanup.

Eos works entirely on your Mac with no account, ads, subscription, analytics, or network access. Nothing is deleted without review, protected paths and running apps are skipped, and cleanup uses the Trash by default. Individual results and safe categories can be cleaned directly after confirmation.

[Eos: Disk Cleanup on the Mac App Store](https://apps.apple.com/app/id6794152421) · [Project folder](Spruce/)

## Scentory: Perfume Samples

### Organize Samples, Record Trials & Remember Decisions

Scentory now centers on perfume samples and the experience of trying them. Browse a bundled offline perfume catalog or add a sample manually, organize samples into boxes, and record position numbers. On a personal box photo, manually mark where each sample is stored; samples without a position remain usable in the list.

Choose what to try from samples you own, record first impressions and later observations in the same trial, and add feelings, scent tags, notes, and optional local reminders. Keep a decision history—buy a bottle, keep the sample, try again, or pass—and review trials, exploration progress, and current decisions in the timeline and statistics.

The free tier includes ten samples, the default box, and one custom box. Pro removes sample and custom-box limits through monthly or yearly subscriptions or a lifetime purchase. The app works offline without a Scentory account or developer-operated data server, supports optional private iCloud sync, and can export JSON backups and merge restored data. Legacy wardrobe data, purchases, and earned slots are preserved by the rebuild.

[Scentory on the App Store](https://apps.apple.com/app/id6793348562) · [Project folder](Scentory/) · [Project README](Scentory/README.md) · [Rebuild implementation](Scentory/REBUILD_IMPLEMENTATION.md)

## Daily Quest: Habit & Goals

### Habit Tracker, Goal Planner & Mochi Growth Journey

Daily Quest turns daily progress into a visible growth journey on iPhone and iPad. Create recurring habits that repeat daily, on selected weekdays, or every few days. For finite goals, create an expedition with a target and deadline, then move it forward one step at a time. Each action helps Mochi grow and brings new life to Mochi World.

Track streaks, achievements, calendars, and progress rings; receive local reminders; create milestone share cards; and see today's tasks through Live Activities on the Lock Screen and Dynamic Island. Daily Quest has no account, server, ads, or in-app purchases—your tasks and progress stay on your device.

[Download Daily Quest: Habit & Goals on the App Store](https://apps.apple.com/app/id6797427767) · [Project folder](DailyQuest/)

## HomeCue: Receipts & Care

### Item Care, Purchase Proof, Returns & Warranties

HomeCue keeps maintenance, receipts, return deadlines, and warranties close to the things you own. Start with 48 illustrated item templates across eight categories, review suggested details and care tasks, then save only the items you choose. Unknown purchase details and model-specific care intervals remain unset until confirmed.

Schedule care by date, mileage, or whichever comes first. Scan multipage receipts, import images or PDFs, recognize text on-device, and link one receipt to several items. Track partial returns, warranties, maintenance, and one-time repairs with dates, costs, currencies, providers, and attachments. Share records as PDFs or export and restore a complete local backup.

The current version supports iPhone and iPad, seven interface languages, local reminders, and adaptive layouts. The free tier includes three active items, all templates, scanning, reminders, and exports; one optional non-consumable purchase unlocks unlimited active items. There is no subscription, account, advertising, analytics, or cross-device cloud sync in this version.

[HomeCue on the App Store](https://apps.apple.com/app/id6810898865) · [Project folder](HomeCue/) · [Project README](HomeCue/README.md)

## Family & Friends Journal

### Remember People, Moments & Meaningful Dates

Family & Friends Journal is the current name of the app in `importantPeople`; the source project and scheme remain `Dearfolk`. Build private profiles for family and friends with relationship tags, closeness, interests, contact details, notes, and custom fields. Add photos, videos, and Live Photos, record moments, and choose a cover for each person. A full-screen media browser supports automatic playback and slideshow controls. Videos can also be transferred directly from a computer over the same Wi-Fi through a temporary local transfer page.

Keep Gregorian and lunar birthdays and other important dates together, schedule local reminders, and optionally add dates to Apple Calendar. Scan, photograph, or import personal documents and organize them by person. Selected profiles can be hidden behind a private-record password. The free tier supports three people and ten media items per person; the optional one-time Family & Friends Pro purchase removes these limits. Records stay on the iPhone, with no account, developer server, ads, analytics, tracking, or enabled iCloud sync in the current version.

The renamed app has a separate App Store Connect record, created on November 16, 2026, with Apple ID `6835294742` and bundle identifier `com.wanglingbo.familyfriends`. Release preparation is documented in the project README; public availability is not verified by this inventory.

[App Store Connect](https://appstoreconnect.apple.com/apps/6835294742/distribution) · [Project folder](importantPeople/) · [Project README](importantPeople/README.md)

## Photo Maker: Standard Sizes

### Private Photo Sizing, Background Editing & Print Sheets

Photo Maker, previously called IDMint, lives in the `PassportPhotoMaker` project folder. Import or capture a photo, choose a common portrait or print size, or save custom dimensions in millimeters, inches, or pixels with your preferred DPI. Adjust crop, position, and zoom, replace the background with a solid color, and preview the result before export.

Export JPEG or PNG, set a JPEG file-size limit while keeping output dimensions, or save directly to Photos. Arrange multiple copies on 4 × 6 inch, A5, A4, or Letter paper at 300 DPI, with spacing and cut lines; additional copies continue onto new pages. Exported work remains in the local Creations gallery. Layouts adapt to folded and unfolded iPhone Duo displays.

Creating and editing photos is available before purchase; export requires a monthly subscription or lifetime purchase. Processing and creations stay on-device, with no account, photo upload, advertising, tracking, or watermark. The app provides photo editing tools and does not guarantee official document-photo acceptance.

[Photo Maker on the App Store](https://apps.apple.com/app/id6798896113) · [Project folder](PassportPhotoMaker/) · [Project README](PassportPhotoMaker/README.md) · [Current product description](PassportPhotoMaker/fastlane/metadata/en-US/description.txt)

## Dewday: Daily Savings

### Daily Check-ins, Savings Challenges & Plant Growth

Dewday lives in the `Nada` project folder. Record each day as no spending, essentials only, or other spending; set a daily reference amount, review estimated money kept and streaks, and record purchases you chose to skip. Calendar records can be corrected or filled in for missed dates.

Create a savings challenge for 7 days, one calendar month, or one calendar year, choose a daily amount and personal completion reward, then earn virtual growth and badges as a plant grows. Progress cards and receipts, optional local reminders, a home-screen widget, light and dark appearance, and seven interface languages support the daily habit. Savings totals are estimates and records; the app does not connect to a bank or transfer money.

The current implementation offers 24 hours of full access from first launch. Afterwards, yearly, monthly, or weekly subscriptions provide continued access, while a completed optional share unlocks the current local calendar day. Repeated shares on the same day do not extend access, and historical records remain viewable without an active pass. There is no developer account or advertising. Records stay on-device unless private iCloud sync is enabled.

[Project folder](Nada/) · [Current product description](Nada/fastlane/metadata/en-US/description.txt) · [Local support page](Nada/Nadaweb/support.html)

## Nightblade · 夜刃

### A Playable Ninja Action Prototype

Nightblade is an original landscape action game built with Swift and SpriteKit. Move through scrolling terrain and tree platforms, jump and double-jump, use ranged attacks against enemies, collect pickups, and face a boss. The prototype includes touch controls, a lives system, a main menu, and a result screen.

This project is a playable prototype. The design document also describes possible future progression, game modes, and monetization; those plans are separate from the current implementation.

[Project folder](game/Nightblade/) · [Game design document](game/Nightblade/DESIGN.md)

## Independent App Portfolio

### A Bilingual Website for the App Collection

The portfolio website showcases apps with icons, descriptions, platform and app/game categories, and App Store links. It follows the visitor's browser language and offers a manual English/Chinese switch. Built with plain HTML, CSS, and JavaScript, it can be served locally or published as a static site.

Its app catalogue is maintained separately in `portfolio-site/app.js`; the current website presents six entries under earlier names, including ReceiptGuard, CalendarKiller, Spruce, and Scentory: Fragrance Wardrobe. This README inventories all current app projects; the website catalogue has not yet been updated to match these product changes.

[Project folder](portfolio-site/) · [Website README](portfolio-site/README.md) · [App catalogue](portfolio-site/app.js)

## Privacy at a Glance

Most utility apps keep their working data on the device and do not require a developer-operated account. Sync behavior varies by project:

- **On-device working data:** Stayframe, Foliover, Eos, Daily Quest, HomeCue, Family & Friends Journal, and Photo Maker. Stayframe, HomeCue, and Family & Friends Journal do not currently provide iCloud sync. Foliover analyzes photos and calendars locally and requests access only for the selected service. Family & Friends Journal's optional computer video transfer runs over the local network.
- **Local data with iCloud support:** Trio, Knots, Scentory, and Dewday. Sync settings and implementation vary by app; Scentory's private iCloud sync defaults to off.
- **Local image processing:** Foliover and Photo Maker perform photo editing and output generation on-device.

See each app's privacy policy and App Store listing for its complete disclosures.

## Workspace Support Files

- [assets/app-icons](assets/app-icons/): shared icons used by this README; several rows link directly to their project's current app icon.
- [somefile/privacy.html](somefile/privacy.html): a standalone privacy-policy page, not a separate app.
- [iOS App Store / Fastlane playbook](IOS_APP_STORE_FASTLANE_PLAYBOOK.md): shared release-process documentation.
- App-specific marketing sites, widgets, screenshots, store metadata, and build artifacts live inside their parent app folders.

---

Search topics: iOS apps, macOS apps, indie apps, privacy-first apps, Stayframe, rental inspection, move-in records, move-out comparison, rental reports, receipt tracker, warranty tracker, return reminder, Foliover, calendar spam remover, daily logic puzzle, connect puzzle, Mac cleaner, disk cleanup, app uninstaller, perfume samples, scent trials, fragrance impressions, habit tracker, goal planner, Live Activities, HomeCue, home maintenance, vehicle maintenance, Family & Friends Journal, people journal, personal documents, birthday reminders, local video transfer, Photo Maker, custom photo sizes, photo print sheets, photo cleanup, timestamp camera, daily savings, no-spend check-ins, savings challenges, ninja action game, local image compression, app portfolio.
