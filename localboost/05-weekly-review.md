# Weekly Review (every Sunday)

## Step 1 — Hadi produces the scorecard (Grok)

Prompt to schedule in Grok every Sunday at 09:00 Riyadh time:

```
Hadi — produce the LocalBoost weekly scorecard for [last Sun]–[last Thu] from the LocalBoost CRM sheet. Use only data in the sheet. Write "no data" where something wasn't tracked. Format exactly:

WEEKLY SCORECARD — week ending [date]

SALES
- New leads discovered: x (target 10)
- Audits completed: x (target 5–10)
- Messages approved / sent: x / x
- Replies: x · Interested: x · Opt-outs: x
- Proposals sent: x · Won: x · Lost: x (top reason)

DELIVERY
- Active projects: x (max 2) — [Project ID: status]
- Delivered this week: x
- Projects past target date: x

MONEY (Finance tab, Confirmed by founder only)
- Collected this week: SAR x
- Collected this month: SAR x
- Stay Current active: x clients = SAR x/month
- Unverified / pending: SAR x

FOUNDER TIME
- Hours on LocalBoost this week (founder's own number): x (cap 12)
- Hours per delivered customer: x

PROBLEMS
- [max 3, each with a Record ID]

NEXT WEEK
- ONE priority:
- Research batch: [categories, area]
- Approvals the founder must clear by Tuesday: [IDs]
```

## Step 2 — The founder pastes it into ChatGPT

```
Here's this week's LocalBoost scorecard. What's the single biggest bottleneck, and what ONE change should I make next week? Use only these numbers.
[paste]
```

## Step 3 — The founder decides (5 minutes)

Write one line in the `Approvals` tab: `Week [date] decision: [what changes]`. Hadi reads it on Monday and adjusts the bot tasks.

## Health thresholds (Hadi flags any of these in red)

- Founder hours > 12/week for 2 weeks in a row
- 0 replies from 15 or more sent messages, which means the message or channel needs work
- Any project more than 5 days past its target date
- An unverified payment more than 3 days old
- More than 2 active projects
