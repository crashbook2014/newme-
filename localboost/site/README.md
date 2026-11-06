# LocalBoost website

A static site with no build step. Deploy this folder (`localboost/site/`) as the publish directory.

```
site/
  index.html            Arabic home (RTL, default at /)
  policies.html         Arabic policies
  en/index.html         English home (LTR)
  en/policies.html      English policies
  assets/css/style.css  All styles (brand tokens at the top)
  assets/js/site.js     Mobile menu + package picker (page works without it)
  assets/fonts/         Self-hosted IBM Plex Sans Arabic + Inter (OFL licences included)
  assets/logos/         ⚠ PLACEHOLDERS — replace with the approved logo files
  assets/img/og-image.png  ⚠ PLACEHOLDER — 1200×630 share image
```

Paths are root-relative (`/assets/...`), so the site must be served from the domain root, as Netlify does. To preview it locally, run `python3 -m http.server` in this folder.

## Replace before going live

| File | What to put there |
|---|---|
| `assets/logos/localboost-lockup.png` | Full rocket lockup, colour, transparent background (header) |
| `assets/logos/localboost-lockup-reversed.png` | Reversed lockup for the navy footer |
| `assets/logos/localboost-icon.png` | Flat orange rocket on navy, 512×512 (favicon / app icon) |
| `assets/img/og-image.png` | 1200×630 share image: lockup + Arabic tagline on navy |

Keep the same file names and nothing else needs to change.

## Visible placeholders (dashed orange boxes, CSS class `ph`)

Search the HTML for `class="ph"` to find them all.

| Where | Placeholder | Replace with |
|---|---|---|
| Home `#contact` (AR + EN) | WhatsApp number coming soon | Number. Then also turn the disabled button into `<a class="btn btn--primary" href="https://wa.me/966…">`, and point the hero and package buttons straight to it if you like |
| Home `#contact` | Contact hours | Real hours |
| Home `#contact` | Email | Business email |
| Home `#packages` | Meta Business AI price | Price outside the launch offer |
| Home `#packages` | Launch offer availability | Remove the line, or the whole `.launch` box when the offer ends |
| Policies | Deposit % / milestones | Payment terms |
| Policies | Privacy policy | A real privacy policy (needed once you collect any customer data) |
