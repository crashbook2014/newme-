# Claude in Chrome — Bot Organization Prompt

Paste the block below into the Claude extension in Chrome. Before you paste it, open the Grok bot dashboard in one tab and this GitHub folder in another, and stay logged in to both, plus Google.

```
You are helping me (Abdulelah, founder of LocalBoost) organize my AI bot team in this browser. Work carefully, step by step, and STOP at every checkpoint marked ⛔ to show me what you plan to do and wait for my "go".

SOURCE OF TRUTH
All bot instructions live in my GitHub repo:
https://github.com/crashbook2014/newme-/tree/main/localboost
Read these files first (open each one, use the "Raw" view to copy text exactly):
- 00-operating-rules.md  (shared rules — goes FIRST in every bot)
- 01-offer.md             (prices and packages)
- bots/hadi.md, bots/saad.md, bots/delivery-coordinator.md, bots/quality-controller.md
- 02-crm.md and the crm/ folder (Google Sheet structure)
Copy only the text inside the ``` code blocks of each file, never the markdown around them.

SAFETY RULES (never break these)
- Do NOT send any message, email, or WhatsApp to anyone.
- Do NOT buy, subscribe, upgrade, or enter payment details.
- Do NOT delete any bot, file, chat, or memory. To retire something, rename it with the prefix "ZZ Archive · " and leave it.
- Do NOT touch my personal assistant bot "Abady" except to rename it to "Personal · Abady".
- Do NOT change sharing or permissions on anything.
- Do NOT enter passwords or approve login or 2FA prompts — stop and ask me.
- If a page looks different from what you expect, stop and describe it. Don't guess.

STEP 1 — INVENTORY (read only)
Open my Grok bot dashboard. List every bot that exists: its current name, a 1-line summary of its current instructions, any schedules or routines attached, and the files or apps it has access to. Show me this as a table.
⛔ CHECKPOINT 1: show the table and wait.

STEP 2 — RENAME AND RESTRUCTURE
Target structure (number prefixes keep them sorted in order):
| New name                          | Instructions to install                                    | Replaces old bot(s)                       |
| LB · 01 Hadi — Manager            | 00-operating-rules + bots/hadi.md                          | Hadi · LocalBoost Coach                   |
| LB · 02 Saad — Outreach           | 00-operating-rules + bots/saad.md                          | Saad                                      |
| LB · 03 Delivery — Coordinator    | 00-operating-rules + bots/delivery-coordinator.md          | LocalBoost Delivery + Projects Manager    |
| LB · 04 QC — Quality Control      | 00-operating-rules + bots/quality-controller.md            | (new bot — create it)                     |
| ZZ Archive · Product Developer    | leave instructions unchanged                               | LocalBoost Product Developer (role moved to ChatGPT) |
| ZZ Archive · Projects Manager     | leave instructions unchanged                               | Projects Manager (merged into 03)         |
| Personal · Abady                  | leave instructions unchanged                               | Abady                                     |

For each LB bot:
a) BEFORE editing, copy its current instructions into a Google Doc called "LocalBoost — Old Bot Instructions Backup", under a heading with the bot's old name.
b) Rename it.
c) Replace its instructions with: the 00-operating-rules block, a blank line, then its own bot block. If there is a character limit, tell me the limit and the overflow. Don't trim anything yourself.
d) Attach 01-offer.md as a knowledge file if the platform supports files; otherwise append its contents after the bot block.
⛔ CHECKPOINT 2: before you save ANY bot, show me the backup doc link and the exact final name and instructions for bot 01. After I approve, do 02–04 the same way, pausing once more before saving them.

STEP 3 — SCHEDULES (set up, but leave OFF)
If the platform supports scheduled routines, create these and leave them DISABLED/paused:
- LB · 01 Hadi: "Daily brief" — Sun–Thu 09:30 Asia/Riyadh — prompt: "Produce today's daily brief per your instructions."
- LB · 01 Hadi: "Weekly scorecard" — Sunday 09:00 Asia/Riyadh — prompt: the Step 1 block from 05-weekly-review.md
⛔ CHECKPOINT 3: show me the schedules. I'll switch them on myself.

STEP 4 — GOOGLE WORKSPACE
a) Google Drive: create the folder structure
   LocalBoost/
     00 Admin/            (put the backup doc here)
     01 Leads/
     02 Customers/
     03 Templates/
     04 Reports/
b) Google Sheets: in "LocalBoost/00 Admin", create the sheet "LocalBoost CRM". Create one tab per CSV in the repo's crm/ folder (same tab names, in this order: Leads, Audits, Outreach, Customers, Projects, Deliverables, Recurring, Finance, Log, Approvals), with each CSV's header row as row 1. Freeze row 1 and make it bold.
c) Add an 11th tab "Bot Directory" with columns: Bot name | Platform | Role | Instructions source file | Last updated | Schedules | Notes. Fill one row per bot from Step 2, plus:
   Claude — Production | claude.ai | Websites, Arabic copy, proposals, reports | bots/claude-production.md
   ChatGPT — Review    | chatgpt.com | Strategy & weekly review | bots/chatgpt-review.md
⛔ CHECKPOINT 4: give me the Drive folder link and the Sheet link.

STEP 5 — FINAL REPORT
Give me:
1. A table of every bot: old name → new name, what changed, saved yes/no
2. Links: Backup doc, Drive folder, CRM sheet
3. Anything you could NOT do and why (limits, missing features, errors)
4. Anything you noticed that looks risky or confusing
```

## After it finishes

- Switch on the schedules yourself once you're happy with them.
- Paste the final report back into Claude Code so the repo can be updated to match. For example, if Grok has an instruction length limit, the bot files can be shortened.
