# QA Checklist

Mark ✔ or ✘ for each item. Any ✘ is a FAIL. Record the result in the Deliverables tab.

## All deliverables
- [ ] Every fact matches the intake: name, phone, WhatsApp, hours, address, prices, services
- [ ] No facts that aren't in the intake
- [ ] No forbidden claims: rankings, "الأفضل", "#1", guarantees, fake reviews or stats, Google/Meta affiliation
- [ ] Arabic spelling and grammar are correct, the tone is natural, and mixed Arabic/English text displays correctly
- [ ] No other customer's data appears anywhere
- [ ] The scope matches the package in Projects

## Google Business Profile pack
- [ ] Description ≤ 750 characters, no URLs, no promos, no keyword stuffing
- [ ] Category recommendation matches what the business actually does
- [ ] Hours cover all 7 days; Ramadan/Eid plan included if the intake gave them
- [ ] Review reply drafts are polite, specific, and reveal no private details
- [ ] QR card links to the correct review URL for this profile (test by scanning)

## Website
- [ ] Opens on mobile (390px) with no horizontal scroll and readable text
- [ ] `dir="rtl"` and `lang="ar"` set; layout is right-to-left
- [ ] WhatsApp button → `wa.me/966…` with the correct number and a prefilled message (test by tapping)
- [ ] Call button → `tel:` with the correct number
- [ ] Map embed shows the correct location
- [ ] All links open the right destination (Instagram etc.)
- [ ] Images load, are the customer's own, and are reasonably compressed (< 300 KB each)
- [ ] Meta title and description filled in; JSON-LD contains intake facts only
- [ ] No placeholder text left (`[...]`, lorem ipsum, "TODO")
- [ ] Footer shows the business name, not LocalBoost branding (unless the founder approved a small credit)

## Outreach draft
- [ ] A permission record exists for this channel
- [ ] Sender identified ("عبدالإله من LocalBoost")
- [ ] Observations match the audit evidence
- [ ] Opt-out line included
- [ ] Price, if mentioned, matches `01-offer.md`
