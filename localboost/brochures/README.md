# LocalBoost service brochures

Three A4 brochures (2 pages each, Arabic), one per package. Print double-sided or send as PDF on WhatsApp.

| File | Package | Price |
|---|---|---|
| `01-get-found.pdf` | خلّهم يلقونك · Get Found | 900 SAR (launch 750, confirmed during the check) |
| `02-get-chosen.pdf` | خلّهم يختارونك · Get Chosen | 2,200 SAR + domain/hosting at cost |
| `03-stay-current.pdf` | خلّك محدّث · Stay Current | 299 SAR/month, add-on only |

Each one covers who it's for, what's included, the step-by-step process (who does what), what the owner provides, what's not included, the honesty rules, payment and cancellation, and a QR code to the website.

All facts come from `localboost/01-offer.md`. The Stay Current monthly report example is labelled as illustrative.

## Rebuild after a change

```
python3 localboost/brochures/build.py localboost/brochures/qr-website.svg <out-dir>
node localboost/brochures/render.js <out-dir>      # needs Playwright; warns if a page overflows
```

Then copy the PDFs here. If the website address changes, regenerate `qr-website.svg` (npm package `qrcode`) and update `SITE_URL` in `build.py`.

**When the WhatsApp number is live:** add it to the CTA in `build.py` and rebuild.
