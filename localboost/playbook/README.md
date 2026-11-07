# LocalBoost Delivery Playbook (internal)

| File | Language | For |
|---|---|---|
| `localboost-delivery-playbook.pdf` | English | Founder |
| `localboost-delivery-playbook-ar.pdf` | العربية | Founder and new team members (roles named: المؤسس / البوتات / العميل) |

Both are 14 pages. Each shows how to deliver Get Found, Get Chosen and Stay Current from start to finish, has a one-page final review checklist, Arabic message templates, and fixes for common problems.

Keep the two versions in sync: when you change one build script, change the other.

```
python3 localboost/playbook/build.py    <out-dir> && node localboost/playbook/render.js <out-dir>
python3 localboost/playbook/build_ar.py <out-dir> && node localboost/playbook/render.js <out-dir> localboost-delivery-playbook-ar
```

Then copy the PDFs here.
