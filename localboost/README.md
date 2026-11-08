# LocalBoost — Implementation Pack

The operating manual for LocalBoost. Each bot (Grok, Claude, ChatGPT) gets its instructions from this folder, and the Google Sheet is the single source of truth for all records.

**Founder:** Abdulelah Alshanqiti, final authority on everything external, financial, or contractual.
**Current version:** offer sheet v2026-11-08 (5 services: LB-GF 900 · LB-GC 2,200 · LB-SC 299/mo · LB-CHK 3,300 · LB-MC 1,700/mo). Website: https://crashbook2014.github.io/newme-/ · Repo-wide summary: [`../CLAUDE.md`](../CLAUDE.md)

## How to use this pack

1. **Create the Google Sheet.** Make one sheet called `LocalBoost CRM` and import each file in [`crm/`](crm/) as its own tab, keeping the same tab names. The columns and statuses are explained in [`02-crm.md`](02-crm.md).
2. **Set up each Grok bot.** Paste [`00-operating-rules.md`](00-operating-rules.md) first, then that bot's file from [`bots/`](bots/).
3. **Set up Claude.** Paste [`00-operating-rules.md`](00-operating-rules.md) and then [`bots/claude-production.md`](bots/claude-production.md) into a Claude Project's instructions (or at the start of a chat).
4. **Set up ChatGPT.** Paste [`bots/chatgpt-review.md`](bots/chatgpt-review.md).
5. **Move work between bots** using the copy-paste prompts in [`03-handoffs.md`](03-handoffs.md).
6. **Before any outreach**, finish the checklist in [`04-contact-and-consent.md`](04-contact-and-consent.md).

## Files

| File | What it is |
|---|---|
| `00-operating-rules.md` | Rules every bot follows. Paste these first, always. |
| `01-offer.md` | The single offer sheet: 5 services, prices, inclusions, WhatsApp AI wording, approved FAQ |
| `02-crm.md` | Sheet tabs, IDs, statuses, package codes, and the rules for updating them |
| `03-handoffs.md` | Exact prompts that pass work from one stage to the next |
| `04-contact-and-consent.md` | Compliant outreach process and Arabic opt-in/opt-out wording |
| `05-weekly-review.md` | Sunday scorecard covering both sides (Maps packages and shop visits) |
| `06-roadmap.md` | 30-day build plan and success checks |
| `07-chrome-setup-prompt.md` | Prompt for the Claude Chrome extension to organize the bots, Drive, and the CRM sheet |
| `bots/` | Instructions for Hadi, Saad, the Delivery coordinator, QC, Claude production and ChatGPT review |
| `crm/` | CSV headers to import into Google Sheets, plus `Packages.csv` (the 5 package codes) |
| `templates/` | Audit, proposal, onboarding, QA, handover, monthly report and Shop Check report templates |
| `brand/STYLE.md` | The "launch" visual style: colours, fonts, icons, sizes |
| `site/` | The LocalBoost website (Arabic + English, static, GitHub Pages) |
| `brochures/` | Four A4 service brochures (PDF) and the script that builds them |
| `playbook/` | Delivery playbook in English and Arabic (PDF) and the scripts that build them |
| `_archive/` | Obsolete files, kept for reference only. Never quote from them. |

## Decisions waiting on the founder

These are marked `[FOUNDER DECISION]` or «قريب» in the files. Bots must not fill them in themselves.

1. **Official WhatsApp number** (the site shows «الرقم قريب»)
2. **Business email** (used for first contact and Google Business Profile manager invites)
3. **Contact hours** (the site shows «تتأكد قريب»)
4. **Payment terms:** deposit %, payment schedule, and Monthly Care cancellation terms
5. **Launch offer end date** for the Get Found launch price (750 for the first 2 clients)
