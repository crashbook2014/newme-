# CLAUDE.md — LocalBoost

This repo holds LocalBoost's website (`localboost/site/`, published on GitHub Pages) and its AI-team instruction pack (`localboost/`).

**Deploy only when Abdulelah says deploy.** (Merging into `main` publishes the site automatically through `.github/workflows/pages.yml`, so don't merge without that instruction either.)

## 1. Brand facts
- **LocalBoost**: an independent service for local shops in Riyadh (barbershops, salons, cafés, restaurants, clinics, gyms, auto, retail). Don't list specific districts in profiles or bios.
- **Founder:** Abdulelah Alshanqiti (Saudi). Background, only as: aviation, luxury automotive, real estate, ESSEC hospitality training. Never mention his current employer or personal phone number.
- **Tagline:** «سهل يلقونك. واضح. وجاهز لزبائنك.» / "Findable. Clear. Ready for customers."
- **Slogan:** «وجهتك الأولى قبل ما تطلق صاروخك للنجاح»
- **Two sides of one offer:** ١ «خلّهم يلقونك ويختارونك»: Google Maps profile + simple website. ٢ «نشوف محلك بعين زبونك»: secret-shopper visits, shop appearance, visible money leaks, light SOPs.
- Not affiliated with Google or Meta. Clients own all their accounts.
- **The link to share (QR codes, brochures, bios, outreach, catalog):** https://linktr.ee/localboost.sa
- **Official WhatsApp (business):** +966 55 789 1433 · click-to-chat https://wa.me/966557891433
- **Website:** https://crashbook2014.github.io/newme-/ (it stays hosted here; older hosting links are dead). The Linktree points people to it.
- **Email, hours:** not decided yet. Write «قريب» / "coming soon".

## 2. Services and prices (the only prices allowed anywhere)
| Code | Service | Arabic | Price |
|---|---|---|---|
| LB-GF | Get Found | خلّهم يلقونك | SAR 900 one-time (launch 750 for the first 2 clients) |
| LB-GC | Get Chosen | خلّهم يختارونك | SAR 2,200 one-time; domain/hosting at cost |
| LB-SC | Stay Current | خلّك محدّث | SAR 299/month; add-on only after Get Found or Get Chosen |
| LB-CHK | Shop Check | زيارة التقييم | SAR 3,300, one visit |
| LB-MC | Monthly Care | المتابعة الشهرية | SAR 1,700/month |

What each includes, and the retired offers, are in `localboost/01-offer.md`. The shop-visit side has no accounting, no sales or bank data, no supplier contracts, and no profit promises.

## 3. WhatsApp AI
Not confirmed available in Saudi Arabia. Never write that it's available. Only:
«مهتم بمساعد ذكي يرد على عملائك في واتساب؟ اسألنا عنه — نتأكد من توفّره لحسابك أول، والحساب يبقى باسمك.»

## 4. Rules
- Never guarantee rankings, customers, bookings, revenue or profit.
- No fake reviews, testimonials or invented results. Before/after examples are labelled «مثال توضيحي».
- Money examples are labelled «مثال حسابي، مو وعد» and show a gain bigger than the fee (a 10-riyal add-on × 10 customers a day × 30 days = 3,000 riyals vs the 1,700 monthly fee).
- Never ask for passwords, card details or bank access.
- No message goes to any shop without Abdulelah approving the exact text.
- Don't invent facts, numbers, testimonials, phone numbers, emails or hours. Use `[FOUNDER DECISION]` or «قريب».

## 5. Website (GitHub Pages, `localboost/site/`)
- Arabic RTL by default at `/`, English at `/en/` (the EN button switches between them; every string exists in both files).
- Sections: map hero, rocket launch scroll, before/after, packages (`#packages`), shop-visit section (`#orbit`), FAQ, contact. **Keep `#packages` and `#orbit` stable**: the WhatsApp catalog links to them.
- Contact: WhatsApp +966 55 789 1433 (buttons open https://wa.me/966557891433 with the pre-filled free-check request), Linktree https://linktr.ee/localboost.sa, hours «تتأكد قريب». No other phone number.
- Test at 390 px wide (no sideways scroll) before committing.

## 6. Instruction pack (`localboost/`)
`00-operating-rules.md` (shared rules, pasted first into every bot) · `01-offer.md` (offer sheet) · `02-crm.md` + `crm/` (CRM, package codes) · `03-handoffs.md` · `04-contact-and-consent.md` · `05-weekly-review.md` · `bots/` (Hadi, Saad, Delivery coordinator, QC, Claude production, ChatGPT review) · `templates/` · `brochures/` · `playbook/` · `_archive/` (obsolete; never quote from it).

## 7. Visual style
"Launch" style, documented in `localboost/brand/STYLE.md`:
- night sky `#010d1f → #022754` with an orange sunrise
- the logo's rocket on a glowing moon with a dashed yellow orbit ring
- stages ١ · الانطلاقة / ٢ · المدار
- the full logo on a white badge

Colours: navy `#022754`, orange `#EA5C0A`, amber `#F6880F`, yellow `#FFD332`; never teal. Fonts: Readex Pro (headlines), IBM Plex Sans Arabic (body), Inter (numbers). No emojis in product posts or catalog images. Sizes: 1080×1920, 1080×1350, A4.
