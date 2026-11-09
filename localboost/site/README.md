# LocalBoost website

A static site with no build step. Deploy this folder (`localboost/site/`), or `localboost/localboost-website.zip`, as the site root. The design is the founder's version: map hero, scroll-driven rocket launch, before/after, an animated journey panel (`#journey`: sign → launch → pass the alien → moon, 12 s loop, static final frame for reduced-motion users), packages (`#packages`, stage ١), shop-visit section (`#orbit`, stage ٢), FAQ, and contact. **Keep the `#packages` and `#orbit` anchors stable**: the WhatsApp catalog links to them. Prices and wording follow `localboost/01-offer.md` v2026-11-08; visuals follow `localboost/brand/STYLE.md`.

```
index.html            Arabic home (RTL, default at /)
en/index.html         English home (LTR, at /en/)
policies.html         Arabic policies
en/policies.html      English policies
assets/css/home.css   Home page styles (brand tokens at the top)
assets/css/style.css  Policies page styles
assets/js/home.js     Rocket scroll animation (the page works without it)
assets/fonts/         Self-hosted Readex Pro (headlines), IBM Plex Sans Arabic, Inter (OFL licences included)
assets/logo.png       Header/footer logo (real rocket logo)
assets/logo-large.png Large logo
assets/favicon.png    Rocket icon, cropped from the logo
assets/og-image.png   1200×630 share image
```

All paths are relative, so the site works at a domain root, in a subfolder (GitHub Pages), or opened locally.

## Hosting on GitHub Pages

Address: **https://crashbook2014.github.io/newme-/**. The workflow `.github/workflows/pages.yml` publishes this folder on every push to `main` that changes it. **Deploy only when Abdulelah says deploy**, which means don't merge to `main` without that instruction.

One-time setup: on GitHub, open the repo's **Settings → Pages**, set **Source** to **GitHub Actions**, then open **Actions → "Deploy LocalBoost site to GitHub Pages" → Run workflow**.

Own domain later: **Settings → Pages → Custom domain**. Then replace `https://crashbook2014.github.io/newme-` with your domain in the four HTML files (canonical, hreflang, og:image).

## Contact (live)

WhatsApp **+966 55 789 1433**. Buttons open `https://wa.me/966557891433` with the pre-filled free-check request (Arabic on `/`, English on `/en/`). The Linktree `https://linktr.ee/localboost.sa` appears in the contact section and every footer, and as `sameAs` in the structured data. Hours: every day 8:00 AM – midnight (`openingHours: Mo-Su 08:00-24:00`).

## Still to fill in

| Where | Text now | Replace with |
|---|---|---|
| Packages, Get Found | Launch price 750 … "we confirm availability during the check" | Remove the line when the offer ends |
| Policies | Deposit % / milestones, Monthly Care cancellation terms | Payment terms `[FOUNDER DECISION]` |
| Policies | Privacy policy placeholder | A real privacy policy |
| Hero + before/after | Gradient photo placeholders | Real (permitted) shop photos, when you have a client |

When you edit text, change **both** `index.html` and `en/index.html`.
