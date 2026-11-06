# LocalBoost website

A static site with no build step. Deploy this folder (`localboost/site/`), or `localboost/localboost-website.zip`, as the site root. The design is the founder's version: map hero, scroll-driven rocket launch, before/after, packages, FAQ, and contact.

```
index.html            Arabic home (RTL, default at /)
en/index.html         English home (LTR, at /en/)
policies.html         Arabic policies
en/policies.html      English policies
assets/css/home.css   Home page styles (brand tokens at the top)
assets/css/style.css  Policies page styles
assets/js/home.js     Rocket scroll animation (the page works without it)
assets/fonts/         Self-hosted IBM Plex Sans Arabic + Inter (OFL licences included)
assets/logo.png       Header/footer logo (real rocket logo)
assets/logo-large.png Large logo
assets/favicon.png    Rocket icon, cropped from the logo
assets/og-image.png   1200×630 share image
```

All paths are relative, so the site works at a domain root, in a subfolder (GitHub Pages), or opened locally.

## Hosting on GitHub Pages

Address: **https://crashbook2014.github.io/newme-/**. The workflow `.github/workflows/pages.yml` publishes this folder on every push to `main` that changes it.

One-time setup: on GitHub, open the repo's **Settings → Pages**, set **Source** to **GitHub Actions**, then open **Actions → "Deploy LocalBoost site to GitHub Pages" → Run workflow**.

Own domain later: **Settings → Pages → Custom domain**. Then replace `https://crashbook2014.github.io/newme-` with your domain in the four HTML files (canonical, hreflang, og:image).

## Still to fill in

| Where | Text now | Replace with |
|---|---|---|
| Home `#contact` (AR + EN) | الرقم قريب / Number coming soon | WhatsApp number, as a `https://wa.me/966…` link |
| Home `#contact` | كل يوم (الأوقات تتأكد قريب) | Real contact hours |
| Packages, Get Found | Launch price 750 … "we confirm availability during the check" | Remove the line when the offer ends |
| Policies | Deposit % / milestones placeholder | Payment terms |
| Policies | Privacy policy placeholder | A real privacy policy |
| Hero + before/after | Gradient photo placeholders | Real (permitted) shop photos, when you have a client |

When you edit text, change **both** `index.html` and `en/index.html`.

## Live on WebsitePublisher

The site is live at **https://project27483.websitepublisher.ai/** (project 27483), with English at `/en/index.html` and the policies pages at `/policies.html` and `/en/policies.html`.

- Fonts, CSS, JS and images are uploaded to `https://cdn.websitepublisher.ai/custom/wid27483/` under `fonts/`, `css/`, `js/` and `img/`.
- To republish after editing, run `python3 localboost/tools/websitepublisher-build.py localboost/site <out>` and upload the generated pages.
- The free plan serves every page with `noindex`, so Google won't list the site until you move to a paid plan.
