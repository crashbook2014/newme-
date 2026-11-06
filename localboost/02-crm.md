# LocalBoost CRM — Google Sheet Structure

One Google Sheet named **`LocalBoost CRM`**. Import each CSV in `crm/` as a tab with the same name. Share it **only** with the founder's Google account and the account the bots use.

## IDs

| Record | Format | Example | Rule |
|---|---|---|---|
| Lead | `LB-L-0001` | LB-L-0007 | One per business location. Before creating one, check Leads for the same Maps link or phone (no duplicates). |
| Customer | `LB-C-001` | LB-C-002 | Created only when a lead is **Won**. Has a `Lead ID` column linking back. |
| Project | `LB-P-001` | LB-P-003 | One per package purchase. Linked to a Customer ID. |
| Deliverable | `LB-D-0001` | LB-D-0012 | One per file or link handed over |

## Tabs

| Tab | One row per | Owner bot |
|---|---|---|
| `Leads` | business discovered | Saad |
| `Audits` | audit performed | Saad |
| `Outreach` | contact attempt or reply | Saad |
| `Customers` | paying customer | Delivery coordinator |
| `Projects` | package purchased | Delivery coordinator |
| `Deliverables` | file or link | Delivery coordinator / QC |
| `Recurring` | Stay Current subscription | Hadi |
| `Finance` | money in or out | **Founder only** (bots may draft rows with Status = Unverified) |
| `Log` | every status change and important action | All bots |
| `Approvals` | anything waiting on the founder | All bots create rows; founder decides |

## Statuses (use exactly these words)

**Lead status (Leads tab)**

`Discovered → Audited → Qualified → Contact permitted → Contacted → Interested → Proposal sent → Won` · or `Lost (reason)` · or `Do not contact`

- **Qualified** = audit score ≤ 60, fits a package, and is in the target area and category
- **Contact permitted** = a lawful first-contact channel is recorded (see `04-contact-and-consent.md`)
- **Do not contact** = they opted out. Permanent; no bot ever reverses it.

**Project status (Projects tab)**

`Payment pending → Onboarding → Production → QA → Customer review → Approved → Delivered` · or `On hold (reason)` · or `Cancelled`

- Work starts only when Finance shows payment **Confirmed by founder**
- **Delivered** needs a handover record in Deliverables

**Recurring status (Recurring tab)**

`Active → Monthly review → Report sent → Renewal due → Renewed` · or `Cancelled`

**Permission (Outreach tab)**

`None` · `B2B first contact OK (channel)` · `Opted-in (evidence)` · `Opted-out`

**Approvals (Approvals tab)**

`Waiting → Approved` · `Rejected` · `Changes requested`

## Update rules

1. Never guess a status. Change it only when there is evidence, and write the evidence in the `Log` tab: `Timestamp | Bot | Record ID | Old status | New status | Reason / evidence link`.
2. Every row needs `Next action` and `Next action owner` filled in. An empty next action means the lead or project is stuck, and Hadi flags it.
3. Dates use `YYYY-MM-DD`, times are Riyadh time, and amounts are plain numbers in SAR.
4. Keep only business contact data. No personal ID numbers, no customer passwords, and no data unrelated to the job.
5. Never delete rows. Mark them `Lost` or `Cancelled` instead.
