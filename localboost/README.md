# LocalBoost — Implementation Pack

The operating manual for LocalBoost. Each bot (Grok, Claude, ChatGPT) gets its instructions from this folder, and the Google Sheet is the single source of truth for all records.

**Founder:** Abdulelah — final authority on everything external, financial, or contractual.

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
| `01-offer.md` | Official packages and prices. Bots quote from here only. |
| `02-crm.md` | Sheet tabs, IDs, statuses, and the rules for updating them |
| `03-handoffs.md` | Exact prompts that pass work from one stage to the next |
| `04-contact-and-consent.md` | Compliant outreach process and Arabic opt-in/opt-out wording |
| `05-weekly-review.md` | Sunday review prompt and scorecard format |
| `06-roadmap.md` | 30-day build plan and success checks |
| `07-chrome-setup-prompt.md` | Prompt for the Claude Chrome extension to organize the bots, Drive, and the CRM sheet |
| `bots/` | Instructions for each bot |
| `crm/` | CSV headers to import into Google Sheets |
| `templates/` | Audit, proposal, onboarding, QA, handover, and monthly report templates |

## Decisions waiting on the founder

These are marked `[FOUNDER DECISION]` in the files. Bots must not fill them in themselves.

1. **Prices and package names.** Your website and the new plan don't match (see `01-offer.md`).
2. **Payment terms.** Upfront percentage and payment method.
3. **The launch-price end date.**
4. **The LocalBoost business email address** used for first contact and for Google Business Profile manager invites.
