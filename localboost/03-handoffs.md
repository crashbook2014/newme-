# Handoff Prompts

Copy-paste prompts that pass work between stages. Fill in the `[brackets]`. Every handoff names its record IDs so the receiver can find everything in the CRM.

---

## H1 · Hadi → Saad: research batch (weekly, Sunday)

```
Saad — research batch for week of [date].
Target: [N, default 10] new leads.
Categories: [e.g. barbershops, cafés]
Area: [Riyadh area set by Hadi]
For each lead: add to Leads (check duplicates), audit with templates/audit.md, save evidence to Drive, set Status and Score.
Report back: list of Lead IDs with score and suggested package, sorted lowest score first.
Deadline: [date]. No outreach drafts yet. I'll pick which ones to draft.
```

## H2 · Hadi → Saad: draft outreach

```
Saad — draft first-contact messages for: [Lead IDs].
For each: check the permission record first (04-contact-and-consent.md). If there's no permitted channel, mark it "Visit in person" and skip.
Use 1–2 real audit observations. Offer the free 5-minute check. Include the opt-out line.
Put drafts in Outreach (Approved = N) and create one Approvals row per draft.
```

## H3 · Saad → Founder: approval request

```
APPROVAL — [Approval ID] — [Lead ID] [Business name]
Channel: [email / contact form / in person] · Permission: [status + evidence]
Audit score: [x/100] · Top gaps: [1, 2]
Draft:
---
[message]
---
Reply: ✅ send · ✏️ [changes] · ❌ skip
```

## H4 · Saad → Delivery coordinator: deal won / proposal

```
PROPOSAL REQUEST — [Lead ID] [Business name]
Package: [LB-GF / LB-GC / LB-SC / LB-CHK / LB-MC] · Price: [from 01-offer.md only, incl. the LB-GF launch price if eligible]
Customer contact: [name, channel, opted-in Y/N]
What they asked for: [their words]
Audit: [Audit ID + evidence link]
Special requests (need founder): [none / list]
→ Delivery: create the proposal with templates/proposal.md via Claude, then Approvals row.
```

## H5 · Delivery coordinator → Claude: production

```
PRODUCTION — [Project ID] — [Package]
Customer: [Customer ID] — [Business name AR / EN]
Category: [ ] · District: [ ] · Maps link: [ ]
Template (websites only): [cafe-restaurant / professional-services / retail-shop]

INTAKE DATA (only use these facts):
- Phone: [ ] · WhatsApp: [ ]
- Hours: [Sun–Sat] · Ramadan: [ ] · Eid: [ ]
- Services / menu with prices: [ ]
- About the business (owner's words): [ ]
- Brand colours / logo file: [ ]
- Photo filenames: [ ]
- Instagram / other links: [ ]
- Reviews needing reply drafts (paste text, no reviewer names needed): [ ]

Produce: [list from bots/claude-production.md sections A/B]
Return in the standard output format.
```

## H6 · Delivery coordinator → QC

```
QA REQUEST — [Deliverable IDs] for [Project ID]
Package: [ ] · Intake: [Drive link] · Drafts: [Drive link / preview URL]
Run templates/qa-checklist.md. Return PASS/FAIL per deliverable with numbered fixes.
```

## H7 · QC FAIL → Claude: fix request

```
FIX — [Deliverable ID] — QA failed
Fix ONLY these items, change nothing else:
1. [ ]
2. [ ]
Return the full corrected deliverable.
```

## H8 · Delivery coordinator → Founder: go-live approval

```
GO-LIVE — [Approval ID] — [Project ID] [Business name]
QA: PASS on [date] · Customer approved: [date + evidence]
Payment: [Confirmed by founder on date]
Changes going live: [list]
Before screenshots: [link]
Reply: ✅ go live · ✏️ changes · ⏸ hold
```

## H9 · Hadi → Claude: monthly report (Stay Current)

```
MONTHLY REPORT — [Customer ID] — [Month YYYY-MM]
Data (only use this):
- Health check results: [ ]
- Updates made: [ ] (of max 2)
- Review replies drafted / approved: [ ] (of max 10)
- New reviews this month: [count, avg rating]
- GBP performance numbers from the owner's dashboard, if provided: [ ] or "not provided"
Fill templates/monthly-report.md in Arabic. One page.
```
