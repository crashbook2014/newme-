# LocalBoost service brochures

Four A4 brochures (2 pages each, Arabic) in the "launch" style (night sky, orange sunrise, the rocket on a glowing moon, stage badges ١ · الانطلاقة / ٢ · المدار). Offer sheet v2026-11-08; style per `localboost/brand/STYLE.md` (orbit ring, Readex Pro headlines). Print double-sided or send as PDF on WhatsApp.

| File | Package | Price |
|---|---|---|
| `01-get-found.pdf` | خلّهم يلقونك · Get Found | 900 SAR (launch 750 for the first 2 clients) |
| `02-get-chosen.pdf` | خلّهم يختارونك · Get Chosen | 2,200 SAR + domain/hosting at cost |
| `03-stay-current.pdf` | خلّك محدّث · Stay Current | 299 SAR/month, add-on only |
| `04-shop-experience.pdf` | نشوف محلك بعين زبونك · Shop Check + Monthly Care | Shop Check 3,300 (one visit) · Monthly Care 1,700/month |

Each one covers who it's for, what's included, the step-by-step process (who does what), what the owner provides, what's not included, the honesty rules, payment and cancellation, and a QR code to the website.

All facts come from `localboost/01-offer.md`. The Stay Current monthly report example is labelled as illustrative.

## Rebuild after a change

```
python3 localboost/brochures/build.py localboost/brochures/qr-linktree.svg <out-dir>
node localboost/brochures/render.js <out-dir>      # needs Playwright; warns if a page overflows
```

Then copy the PDFs here. The QR code and the printed link point to the Linktree **linktr.ee/localboost.sa** (`qr-linktree.svg`, `SITE_URL` in `build.py`). If it ever changes, regenerate the QR with the npm package `qrcode`.

The CTA shows the business WhatsApp **+966 55 789 1433** (`WA_TEXT` in `build.py`).
