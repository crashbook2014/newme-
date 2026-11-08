"""Builds the LocalBoost Delivery Playbook (founder-facing, English + Arabic templates).

Usage:  python3 localboost/playbook/build.py <out-dir>
        node localboost/playbook/render.js <out-dir>
Facts come from localboost/01-offer.md, 00-operating-rules.md, templates/ and 03-handoffs.md.
"""
import sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "site" / "assets"
F = (A / "fonts").as_uri()
LOGO = (A / "logo.png").as_uri()
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)

CSS = f"""
@font-face{{font-family:Plex;font-weight:400;src:url({F}/ibm-plex-sans-arabic-arabic-400-normal.woff2)}}
@font-face{{font-family:Plex;font-weight:700;src:url({F}/ibm-plex-sans-arabic-arabic-700-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:400;src:url({F}/inter-latin-400-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:600;src:url({F}/inter-latin-600-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:700;src:url({F}/inter-latin-700-normal.woff2)}}
@page{{size:A4;margin:16mm 15mm 18mm}}
@page:first{{margin:0}}
:root{{--navy:#022754;--orange:#EA5C0A;--yellow:#FFD332;--mist:#F2F2F2;--ink:#0A1F3D;--soft:#55657c;--line:#dde3ec;--ok:#16794a;--bad:#a33}}
*{{box-sizing:border-box}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{margin:0;font-family:Inter,Plex,sans-serif;color:var(--ink);font-size:9.6pt;line-height:1.55}}
[dir=rtl],.ar{{font-family:Plex,Inter,sans-serif}}
h1,h2,h3,h4{{color:var(--navy);line-height:1.25;margin:0}}
h2{{font-size:19pt;margin-bottom:2mm}}
h3{{font-size:12.5pt;margin:6mm 0 2mm;display:flex;align-items:center;gap:2.5mm;break-after:avoid}}
h3 .k{{font:700 9pt Inter;color:#fff;background:var(--orange);border-radius:1.6mm;padding:.4mm 2mm;flex:none}}
h4{{font-size:10.4pt;margin:3.5mm 0 1.2mm;break-after:avoid}}
p{{margin:0 0 2mm}}
ul,ol{{margin:0 0 2mm;padding-inline-start:5mm}}
li{{margin-bottom:.8mm}}
.part{{break-before:page}}
.part-head{{background:var(--navy);color:#fff;border-radius:3mm;padding:6mm 7mm;margin-bottom:5mm}}
.part-head .n{{font:700 8.5pt Inter;letter-spacing:.2em;color:var(--yellow);text-transform:uppercase}}
.part-head h2{{color:#fff;margin:1mm 0}}
.part-head p{{color:#c9d5e6;margin:0;font-size:10pt}}
.box{{border:.3mm solid var(--line);border-radius:2.5mm;padding:3.5mm 4.5mm;margin:2.5mm 0;break-inside:avoid}}
.box.warn{{border-color:#f3c6a6;background:#fff7f0}}
.box.ok{{border-color:#bfe0cc;background:#f2faf5}}
.box.navy{{background:#eef3fa;border-color:#cfdbec}}
.box h4{{margin-top:0}}
.chk{{list-style:none;padding:0}}
.chk li{{position:relative;padding-left:6mm;margin-bottom:1.1mm}}
.chk li::before{{content:"";position:absolute;left:0;top:.9mm;width:3.3mm;height:3.3mm;border:.4mm solid var(--navy);border-radius:.8mm;background:#fff}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:4mm}}
table{{width:100%;border-collapse:collapse;margin:2mm 0 3mm;font-size:9pt;break-inside:auto}}
th{{background:var(--navy);color:#fff;text-align:left;padding:1.6mm 2.4mm;font-weight:600}}
td{{border-bottom:.25mm solid var(--line);padding:1.6mm 2.4mm;vertical-align:top}}
tr{{break-inside:avoid}}
.who{{display:inline-block;font:700 7.4pt Inter;border-radius:99px;padding:.2mm 2.2mm;margin-left:1.5mm;vertical-align:1px}}
.you{{background:var(--orange);color:#fff}} .bot{{background:#e5ecf6;color:var(--navy)}} .cli{{background:#e9f7ef;color:var(--ok)}}
.step{{border-left:1mm solid var(--orange);padding:1mm 0 1mm 4mm;margin:3mm 0;break-inside:avoid}}
.step .t{{font-weight:700;color:var(--navy);font-size:10.4pt}}
.msg{{direction:rtl;font-family:Plex,sans-serif;background:var(--mist);border-radius:2.5mm;padding:3mm 4mm;margin:1.5mm 0 2.5mm;white-space:pre-line;font-size:9.6pt;line-height:1.7;break-inside:avoid}}
.msg .lbl{{display:block;direction:ltr;text-align:left;font:700 7.6pt Inter;color:var(--soft);letter-spacing:.06em;text-transform:uppercase;margin-bottom:1mm}}
.small{{font-size:8.6pt;color:var(--soft)}}
code{{font:600 8.6pt Inter;background:#eef1f5;border-radius:1mm;padding:0 1.2mm}}
/* cover */
.cover{{height:297mm;display:flex;flex-direction:column;background:linear-gradient(160deg,#03306a,var(--navy) 55%,#011a3b);color:#fff;position:relative;overflow:hidden}}
.cover::after{{content:"";position:absolute;left:-30mm;bottom:-40mm;width:170mm;height:170mm;border-radius:50%;background:radial-gradient(circle,rgba(234,92,10,.5),rgba(234,92,10,0) 65%)}}
.cover .logo{{background:#fff;border-radius:3mm;padding:3mm 5mm;margin:18mm 18mm 0;align-self:flex-start}}
.cover .logo img{{height:11mm;display:block}}
.cover .mid{{margin:auto 18mm 0;position:relative;z-index:1}}
.cover .eyebrow{{font:700 9pt Inter;letter-spacing:.25em;color:var(--yellow)}}
.cover h1{{color:#fff;font-size:36pt;line-height:1.1;margin:4mm 0}}
.cover .sub{{font-size:13pt;color:#d4deec;max-width:150mm}}
.cover .meta{{margin:16mm 18mm 18mm;position:relative;z-index:1;display:flex;gap:10mm;font-size:9.5pt;color:#c9d5e6}}
.cover .meta b{{color:#fff;display:block}}
.toc{{list-style:none;padding:0;columns:1}}
.toc li{{display:flex;justify-content:space-between;border-bottom:.25mm dotted #b8c3d3;padding:1.6mm 0;font-size:10.4pt}}
.toc li span:first-child b{{color:var(--orange);margin-right:2.5mm}}
.legend span{{margin-right:4mm}}
.compact{{font-size:9pt;line-height:1.42}}
.compact .chk li{{margin-bottom:.35mm}}
.compact h3{{margin:3.2mm 0 1.2mm}}
.compact td{{padding:1.1mm 2.2mm}}
.compact ul li{{margin-bottom:.4mm}}
.compact .box{{padding:2.6mm 4mm;margin:1.8mm 0}}
"""

def chk(items): return '<ul class="chk">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def ul(items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def who(*w):
    m = {"you": ("you", "YOU"), "bot": ("bot", "BOTS"), "cli": ("cli", "CLIENT")}
    return "".join(f'<span class="who {m[x][0]}">{m[x][1]}</span>' for x in w)
def step(code, title, w, body): return f'<div class="step"><div class="t">{code} · {title} {w}</div>{body}</div>'
def msg(label, text): return f'<div class="msg"><span class="lbl">{label}</span>{text.strip()}</div>'
def part(n, title, sub, body): return f'<section class="part"><div class="part-head"><div class="n">{n}</div><h2>{title}</h2><p>{sub}</p></div>{body}</section>'

# ---------------------------------------------------------------- cover + contents
cover = f"""<section class="cover"><div class="logo"><img src="{LOGO}" alt="LocalBoost"></div>
<div class="mid"><div class="eyebrow">INTERNAL · FOUNDER ONLY</div><h1>Delivery Playbook</h1>
<p class="sub">How to deliver every LocalBoost package from A to Z: what you do, what the bots do, and exactly what you must review before anything reaches a client.</p></div>
<div class="meta"><div><b>For</b>Abdulelah (founder)</div><div><b>Packages</b>Get Found · Get Chosen · Stay Current</div><div><b>Version</b>8 Nov 2026</div></div></section>"""

toc = part("Contents", "What's inside", "Read Part 0 once. Then use the part for the package you're delivering as a step-by-step checklist.",
  '<ul class="toc">'
  + "".join(f'<li><span><b>{a}</b>{b}</span><span>{c}</span></li>' for a, b, c in [
      ("0", "Before any delivery: rules, start gate, roles, tools", "All packages"),
      ("1", "Get Found · خلّهم يلقونك · 900 SAR", "A → K"),
      ("2", "Get Chosen · خلّهم يختارونك · 2,200 SAR", "A → L"),
      ("3", "Stay Current · خلّك محدّث · 299 SAR / month", "Monthly cycle"),
      ("3B", "Shop Check · زيارة التقييم · 3,300 SAR (one visit)", "S·A → S·H"),
      ("3C", "Monthly Care · المتابعة الشهرية · 1,700 SAR / month", "Monthly cycle"),
      ("4", "Final review: the “before you press Deliver” gate", "All packages"),
      ("5", "Message templates (Arabic, ready to send)", "Copy & paste"),
      ("6", "When things go wrong", "Fixes & escalation")])
  + "</ul>"
  + '<div class="box navy"><h4>How to read the step labels</h4><p class="legend">'
  + who("you") + " only you can do it (approval, payment, publishing, client calls)   "
  + who("bot") + " Grok team or Claude prepares it   "
  + who("cli") + " the shop owner must do it</p>"
  + '<p class="small">Targets in this playbook are working targets, not promises to clients. Never promise a client a date that isn\'t written in their proposal.</p></div>')

# ---------------------------------------------------------------- PART 0
p0 = part("Part 0", "Before any delivery", "These rules and the start gate apply to every package. If one item fails, you don't start.",
  "<h3><span class='k'>0.1</span>The eight non-negotiable rules</h3>"
  + "<table><tr><th>#</th><th>Rule</th><th>Why it matters</th></tr>" + "".join(f"<tr><td>{i}</td><td><b>{a}</b></td><td>{b}</td></tr>" for i, (a, b) in enumerate([
      ("No work before payment is confirmed in your bank app.", "A screenshot from the client is not payment. Only you mark Finance → “Confirmed by founder”."),
      ("Nothing goes live without written client approval.", "Save the approval (WhatsApp/email screenshot) in 04-evidence. No approval = no publish."),
      ("Client owns every account. You are a Manager, never an Owner.", "Never ask for or store passwords or 2FA codes. Domains are registered in the client's name."),
      ("Only use facts the client gave you.", "Hours, prices, services, phone: from the intake only. Unknown = ask, never guess."),
      ("No guarantees, no fake reviews, no keyword-stuffed names.", "Breaking Google's rules can get the client's profile suspended. That ends the relationship."),
      ("One scope, in writing.", "Anything not in the proposal is a new decision: price it or decline it. No silent freebies."),
      ("Log it or it didn't happen.", "Every status change goes in the CRM Log tab with a reason. Evidence goes in Drive."),
      ("Customers' privacy and the shop's money data are off limits.", "Photos inside a shop only with the owner's written permission, never customers' faces. Never ask for accounting, sales or bank data. Every money example says «مثال حسابي، مو وعد»."),
  ], 1)) + "</table>"
  + "<h3><span class='k'>0.2</span>The start gate: tick all before Day 1</h3>"
  + chk(["Proposal sent and accepted in writing (“موافق”) and saved",
         "Payment received and <b>confirmed by you</b> in the bank app; Finance row = Confirmed by founder",
         "Customer ID (<code>LB-C-…</code>) and Project ID (<code>LB-P-…</code>) created; Project status = <b>Onboarding</b>",
         "Drive folder created: <code>LocalBoost/Customers/LB-C-…/</code> with <code>01-intake · 02-drafts · 03-final · 04-evidence</code>",
         "Onboarding form sent; all required fields received (name, Maps link, phone, WhatsApp, hours, services, photos, consent tick)",
         "Google Business Profile <b>Manager</b> access granted to the LocalBoost email",
         "BEFORE screenshots taken (see 1·C) and saved in 04-evidence",
         "Target date written in the Projects tab, matching the proposal"])
  + "<h3><span class='k'>0.3</span>Who does what</h3>"
  + "<table><tr><th>Role</th><th>Does</th><th>Never does</th></tr>"
  + "<tr><td><b>You</b></td><td>Approve proposals & messages, confirm payments, final review, publish/apply changes (or approve them), talk to the client when it matters</td><td>Skip the review gate because you're busy</td></tr>"
  + "<tr><td><b>Delivery coordinator</b> (Grok)</td><td>Creates records, sends approved messages, chases intake, files evidence, updates statuses</td><td>Promises dates, applies changes without both approvals</td></tr>"
  + "<tr><td><b>Claude</b> (production)</td><td>Writes descriptions, services, reply drafts, QR card text, websites, proposals, reports from the intake</td><td>Invents facts; contacts clients; publishes</td></tr>"
  + "<tr><td><b>Quality controller</b> (Grok)</td><td>Runs the QA checklist and returns PASS / FAIL with numbered fixes</td><td>Fixes work itself</td></tr>"
  + "<tr><td><b>Hadi</b> (Grok)</td><td>Daily brief, capacity (max 2 active projects), renewals, weekly scorecard</td><td>Counts unconfirmed money</td></tr></table>"
  + "<h3><span class='k'>0.4</span>Tools you need ready</h3>"
  + '<div class="two"><div>' + ul([
      "<b>LocalBoost Google account</b> (business email). This is the account clients add as Manager.",
      "<b>Phone with Google Maps</b>, for checking what customers really see and taking screenshots.",
      "<b>business.google.com</b>, or Google Search/Maps → “Edit profile”, signed in as LocalBoost."])
  + "</div><div>" + ul([
      "<b>Google Drive + the LocalBoost CRM sheet</b>.",
      "<b>Claude</b>, the LocalBoost Production project, with the <code>H5 PRODUCTION</code> handoff.",
      "<b>A QR generator</b> (any free one) and a simple design tool for the QR card.",
      "For Get Chosen: <b>a domain registrar</b> and <b>hosting</b> (GitHub Pages or another static host works)."])
  + "</div></div>"
  + '<div class="box warn"><h4>Google changes its menus often</h4><p>Button names in this playbook (“Edit profile”, “Special hours”, “Ask for reviews”) can move or be renamed. If you can\'t find one, search the setting name in Google Business Profile Help. Don\'t improvise around a missing setting.</p></div>')

# ---------------------------------------------------------------- PART 1  Get Found
p1 = part("Part 1", "Get Found · خلّهم يلقونك", "900 SAR one-time (launch 750 for the first 1–2 clients). A complete, accurate, easy-to-contact Google Maps profile.",
  '<div class="box navy"><h4>What the client receives</h4>' + ul([
      "Correct primary and secondary categories, and an accurate pin",
      "Hours for every day, plus Ramadan and Eid special hours (when provided)",
      "Services/menu with clear descriptions (and prices if the client wants them shown)",
      "A clear Saudi-Arabic business description (≤ 750 characters)",
      "Photos ordered: logo, cover, exterior, interior, work, team",
      "Call button (phone) and WhatsApp contact",
      "Review link + printable QR card",
      "Review-reply drafts (posted only after approval)",
      "Before/after screenshots and a short walkthrough"])
  + '<p class="small"><b>Working target:</b> about 3–5 working days from complete intake, depending on how fast the client replies. Google can take extra days to show some edits.</p></div>'
  + step("1·A", "Kickoff", who("you", "bot"),
         "<p>Delivery coordinator sends the kickoff message (template 5·1) <b>after you approve it</b>, plus the onboarding form link and manager-invite steps.</p>")
  + step("1·B", "Intake + Manager access", who("cli", "bot"),
         ul(["Client fills in the onboarding form and adds the LocalBoost email as <b>Manager</b> (not Owner).",
             "Coordinator chases missing items once every 2 working days, max 3 reminders, then escalates to you.",
             "<b>Check verification:</b> if the profile is unclaimed or unverified, the <b>owner</b> must claim/verify it (Google may ask for a video or other method). Pause the project and explain. Don't verify on their behalf without them present."]))
  + step("1·C", "Audit + BEFORE screenshots", who("bot", "you"),
         "<p>On a phone, signed out (or in incognito), search the shop the way a customer would and capture:</p>"
         + ul(["The search/Maps result card", "Overview tab (hours, phone, buttons)", "About/description", "Photos tab", "Reviews tab (count, rating, replies)", "The pin location on the map"])
         + "<p>Save them as <code>04-evidence/before-01.png …</code> and note every gap in the Audits tab.</p>")
  + step("1·D", "Production", who("bot"),
         "<p>Coordinator sends Claude the <code>H5 PRODUCTION</code> handoff with the intake data only. Claude returns:</p>"
         + ul(["Description in Arabic (≤ 750 chars; no links, phone numbers, prices, promotions or superlatives)",
               "Category recommendation (primary + up to a few relevant secondary ones) with reasons",
               "Services list with short descriptions", "Hours table + Ramadan/Eid special-hours plan",
               "Photo checklist (what's missing)", "QR card text, e.g. «رأيك يهمنا — امسح الكود وقيّم تجربتك»",
               "Reply drafts for real existing reviews", "A list: “MISSING — needs customer input”"]))
  + step("1·E", "QC review", who("bot"),
         "<p>The Quality controller runs <code>templates/qa-checklist.md</code>. Any FAIL goes back to Claude with the <code>H7 FIX</code> prompt (fix only the listed items). Repeat until PASS.</p>")
  + step("1·F", "Your review", who("you"), "<p>Run the Get Found checklist in <b>Part 4</b> on the drafts. You're the last line of defence.</p>")
  + step("1·G", "Client approval", who("cli", "you"),
         "<p>Send <b>one</b> clear summary of every change (template 5·3). Wait for a written “موافق”. Save it in 04-evidence and record the date in Projects. Status → <b>Approved</b>.</p>")
  + step("1·H", "Apply the changes in Google Business Profile", who("you"),
         "<p>Signed in as LocalBoost (Manager) → open the profile → <b>Edit profile</b>. Work top to bottom:</p>"
         + "<table><tr><th>Section</th><th>What to do</th><th>Watch out</th></tr>"
         + "<tr><td>Business name</td><td>Exactly the real-world name on the sign</td><td>Never add keywords or locations (“best barber Narjis”). This can get the profile suspended.</td></tr>"
         + "<tr><td>Category</td><td>Set the primary category; add only truly relevant secondary ones</td><td>Primary category matters most; don't add unrelated ones</td></tr>"
         + "<tr><td>Description</td><td>Paste the approved Arabic text</td><td>≤ 750 chars; no URLs or phone numbers</td></tr>"
         + "<tr><td>Location</td><td>Check the pin; move it to the real entrance if needed</td><td>Address edits may trigger re-verification</td></tr>"
         + "<tr><td>Contact</td><td>Phone number; website if any; WhatsApp if the editor offers a chat/WhatsApp option</td><td>If there's no WhatsApp option, make sure the listed phone is the WhatsApp number and say so in the handover</td></tr>"
         + "<tr><td>Hours</td><td>Regular hours for all 7 days, then <b>Special hours</b> for Ramadan/Eid dates</td><td>Special hours are per date: enter the real dates</td></tr>"
         + "<tr><td>Services / Menu</td><td>Add each service with its description (price only if approved)</td><td>Match the intake exactly</td></tr>"
         + "<tr><td>Photos</td><td>Upload logo, cover, exterior with sign, interior, work, team</td><td>Real, owner-approved photos only; no stock images, no heavy text overlays</td></tr>"
         + "<tr><td>Reviews</td><td>Post <b>only approved</b> reply drafts</td><td>Never reveal private customer details in a reply</td></tr></table>"
         + "<p><b>Review link:</b> use the profile's “Ask for reviews” / “Get more reviews” option to copy the review link → make a QR code from it → put it on the card (logo + «رأيك يهمنا» + QR). Test it on your phone: it must open the review box for <b>this</b> business.</p>"
         + '<p class="small">Some edits show “under review” or take a few days to appear. Note that in the Log and re-check in step 1·I.</p>')
  + step("1·I", "After-check (24–72 hours later)", who("you", "bot"),
         "<p>Search again on a phone, the same way as in 1·C. Confirm every edit is live, take AFTER screenshots from the same angles (<code>after-01.png …</code>), and call the listed number to confirm it rings. If Google rejected or changed something, see Part 6.</p>")
  + step("1·J", "Handover", who("you", "bot"),
         ul(["Send the handover message (template 5·4) with: the QR card (PDF + PNG), before/after images, and a 3-point walkthrough (how to reply to a review, how to change hours, how to add a photo).",
             "Remind them: everything is in their name; they can remove the LocalBoost manager at any time.",
             "Offer Stay Current <b>once</b>. No pressure follow-ups."]))
  + step("1·K", "Close", who("bot"),
         ul(["Projects → <b>Delivered</b> with the date; Deliverables rows filled in (links, QA = Pass, approval date).",
             "Day 7: one feedback message (template 5·5).",
             "If they bought Stay Current: Hadi creates the Recurring row (Part 3)."])))

# ---------------------------------------------------------------- PART 2  Get Chosen
p2 = part("Part 2", "Get Chosen · خلّهم يختارونك", "2,200 SAR one-time + domain/hosting at cost. Everything in Get Found, plus a simple mobile-first website in the client's name.",
  '<div class="box navy"><h4>What the client receives</h4>' + ul([
      "Everything in Part 1 (do all of steps 1·A → 1·K)",
      "A mobile-first website, Arabic by default (bilingual only if agreed in the proposal)",
      "Up to about 4 sections: Home, About, Services, Menu/Prices",
      "WhatsApp click-to-chat, call button and embedded map",
      "Their own domain and hosting, registered in <b>their</b> name, at cost",
      "The website link added to their Google Business Profile"])
  + '<p class="small"><b>Working target:</b> the timeline is written in the proposal. Work in parallel: the Maps profile track (Part 1) and the website track below.</p></div>'
  + step("2·A", "Lock the scope in writing", who("you"),
         ul(["Sections (max ~4), languages, the template (café/restaurant · professional services/clinic · retail shop), domain name.",
             "Write the exclusions in the proposal: no online ordering, bookings, payments, blog, or ongoing content edits (those go in Stay Current)."]))
  + step("2·B", "Domain + hosting, in the client's name", who("cli", "you"),
         ul(["The client registers the domain with their own email as owner, or you register it <b>for</b> them with their approval and payment at cost, with the receipt saved.",
             "Hosting: a free static host (e.g. GitHub Pages) usually works for these sites. Create it under an account the <b>client</b> controls, or document how it will be transferred to them.",
             "Record every cost in the Finance tab as Unverified until you confirm it."]))
  + step("2·C", "Website content", who("cli", "bot"),
         ul(["From the intake: logo, colours, about text in their words, services/menu with prices, real photos, preferred domain.",
             "Missing photos? Ask. Stock photos only with the client's explicit approval."]))
  + step("2·D", "Build", who("bot"),
         "<p>Claude builds the site from the matching template with the <code>H5</code> handoff (section B of the production instructions): a single fast HTML file, <code>dir=\"rtl\"</code>, a <code>wa.me/966…</code> button with a prefilled Arabic message, a <code>tel:</code> button, an embedded map from their Maps link, meta title/description, and LocalBusiness data using intake facts only. Compress images (under ~300 KB each).</p>")
  + step("2·E", "Preview link", who("bot", "you"),
         "<p>Publish to a preview address first (not the real domain). Keep the preview link private to the client.</p>")
  + step("2·F", "QC + your review", who("bot", "you"),
         "<p>QC runs the website section of the QA checklist. Then you run the Get Chosen checklist in Part 4, <b>on a real phone</b>.</p>")
  + step("2·G", "Client review round", who("cli", "you"),
         ul(["Send the preview link + a short list of what to check (template 5·3).",
             "Collect changes in one message; apply what's within the written scope; anything outside it → price it or decline it (your decision).",
             "Get a written “موافق” on the final preview. Save it."]))
  + step("2·H", "Launch", who("you"),
         ul(["Connect the domain to the hosting (the host shows the DNS records to add at the registrar).",
             "Wait for HTTPS (the padlock) to be active. Test both <code>domain.com</code> and <code>www.domain.com</code>.",
             "Add the website link to the client's Google Business Profile (Contact → Website).",
             "Optional, but good: help the owner add the site to Google Search Console with <b>their</b> Google account."]))
  + step("2·I", "Post-launch test (same day)", who("you"),
         chk(["Open the real domain on iPhone and Android (or two different phones)",
              "Tap WhatsApp → opens a chat with the right number and the prefilled message",
              "Tap Call → dials the right number", "Map shows the right place",
              "All pages/sections load; no placeholder text anywhere",
              "Run Google PageSpeed Insights (mobile) and fix anything red"]))
  + step("2·J", "Handover", who("you", "bot"),
         ul(["Registrar and hosting logins: the client sets or keeps their own passwords. You never store them.",
             "Send the handover message (template 5·4) with the live link, the QR card, before/after images, and how to request changes.",
             "Explain renewals: the domain renews yearly, and they pay the registrar directly."]))
  + step("2·K", "Close", who("bot"), "<p>As in 1·K: Delivered, Deliverables rows, Day-7 feedback, offer Stay Current once.</p>")
  + step("2·L", "Keep a copy", who("bot"),
         "<p>Save the final site files in <code>03-final/</code> so you can restore or update them under Stay Current.</p>"))

# ---------------------------------------------------------------- PART 3  Stay Current
p3 = part("Part 3", "Stay Current · خلّك محدّث", "299 SAR / month. Add-on only, after Get Found or Get Chosen. One health check, up to 2 updates, up to 10 reply drafts and a one-page report every month.",
  '<div class="compact"><div class="box warn"><h4>Before the first month</h4>' + chk([
      "Client has a delivered Get Found or Get Chosen project (never sell it on its own)",
      "Monthly payment confirmed by you before the month's work starts",
      "LocalBoost still has Manager access",
      "Recurring row created: fee, start date, billing day, counters reset to 0"]) + "</div>"
  + "<h3><span class='k'>3.1</span>The monthly cycle</h3>"
  + "<table><tr><th>When</th><th>What</th><th>Who</th></tr>"
  + "<tr><td><b>Billing day</b></td><td>Confirm payment in the bank → Recurring = <b>Active</b>. No payment = pause; no work.</td><td>" + who("you") + "</td></tr>"
  + "<tr><td><b>Days 1–3</b></td><td><b>Health check</b> (list below). Anything wrong → tell the client and propose the fix <b>before</b> touching it.</td><td>" + who("bot", "you") + "</td></tr>"
  + "<tr><td><b>Ongoing</b></td><td><b>Update requests</b> (max 2 a month): hours, services, prices, photos, factual corrections. Draft → client OK → apply → log the counter.</td><td>" + who("cli", "you") + "</td></tr>"
  + "<tr><td><b>Weekly</b></td><td><b>New reviews</b> → Claude drafts replies (max 10 a month) → client approves → you post.</td><td>" + who("bot", "cli", "you") + "</td></tr>"
  + "<tr><td><b>Before seasons</b></td><td>Ask early for Ramadan/Eid/holiday hours (counts as an update) so special hours go in <b>before</b> the date.</td><td>" + who("bot") + "</td></tr>"
  + "<tr><td><b>Days 25–28</b></td><td><b>Monthly report</b>: Claude fills <code>templates/monthly-report.md</code> (H9 handoff) → you review → send.</td><td>" + who("bot", "you") + "</td></tr>"
  + "<tr><td><b>5 days before billing</b></td><td>Renewal reminder (template 5·7), after your approval.</td><td>" + who("bot", "you") + "</td></tr></table>"
  + '<div class="two"><div><h4>Health-check list</h4>' + chk([
      "Profile still verified and showing normally",
      "Name, category, hours, phone, website unchanged (Google or users can suggest edits; check for any)",
      "Upcoming holidays have special hours",
      "New photos from others: anything inappropriate → report it",
      "New reviews since last month", "If Get Chosen: site loads, HTTPS works, WhatsApp/call/map work, domain not near expiry"])
  + '</div><div><h4>Limits: how to handle them</h4>' + ul([
      "3rd update or 11th reply in a month → tell the client kindly; it waits for next month, or you quote it as extra (your decision).",
      "Bigger requests (new pages, redesign, ads, social media) → outside Stay Current. Quote separately or decline.",
      "Numbers in the report come <b>only</b> from the owner's dashboard. If not provided → «غير متوفر». Never estimate.",
      "Cancellation: they can stop before the next month starts. Close the Recurring row; remove manager access if they ask."])
  + "</div></div>" + "</div>")

# ---------------------------------------------------------------- PART 4  Final review
p4 = part("Part 4", "Final review: before you press Deliver", "Print these pages. Nothing is handed over until every box for that package is ticked. Any unticked box → fix it, then start the list again.",
  '<div class="compact"><h3><span class="k">ALL</span>Every package</h3>' + chk([
      "Payment confirmed by you (Finance tab), and the client's written approval saved in 04-evidence",
      "Every fact matches the intake exactly: name, phone, WhatsApp, hours, address, prices, services",
      "No fact that isn't in the intake; nothing invented",
      "No forbidden claims: “#1”, «الأفضل», guarantees, made-up reviews or numbers, Google/Meta affiliation",
      "Arabic: correct spelling, natural tone, displays right-to-left properly",
      "No other client's data anywhere (names, photos, numbers)",
      "Scope = exactly what's in the proposal; nothing missing, no unpaid extras",
      "QC returned PASS, recorded in the Deliverables tab"])
  + '<h3><span class="k">GF</span>Get Found: Google Business Profile</h3>' + chk([
      "Business name = the real sign, with no keywords",
      "Primary category correct; secondary categories relevant",
      "Pin on the real entrance (checked on the map)",
      "Hours correct for all 7 days; special hours on the right dates",
      "Phone tested by calling; WhatsApp contact tested",
      "Description ≤ 750 chars, Arabic, no URL/phone/price/promo/superlatives",
      "Services match the intake (prices only if approved)",
      "Photos: real, owner-approved, sharp, in the agreed order",
      "Review link opens <b>this</b> business's review box; the QR scans on two phones",
      "Only approved replies were posted",
      "BEFORE and AFTER screenshots saved from the same angles"])
  + '<h3><span class="k">GC</span>Get Chosen: website (plus everything above)</h3>' + chk([
      "Opens on a real phone: no sideways scrolling, text readable, buttons easy to tap",
      "Right-to-left layout correct; English parts (if any) read correctly",
      "WhatsApp button → right number + prefilled message; Call button → right number",
      "Map embed shows the right place; all links go to the right destinations",
      "Images load, are the client's own, and are compressed",
      "Page title and description filled in; business data uses intake facts only",
      "No placeholder text ([…], lorem ipsum, TODO) anywhere",
      "Live on the real domain with HTTPS; www and non-www both work",
      "Website link added to the Google Business Profile",
      "Domain and hosting registered to the client; costs recorded at cost with receipts"])
  + '<h3><span class="k">SC</span>Stay Current: monthly report</h3>' + chk([
      "Updates used ≤ 2 and replies ≤ 10, matching the Recurring counters",
      "Every posted reply and update had client approval",
      "Numbers come from the owner's dashboard, or say «غير متوفر»",
      "One page, Arabic, with one practical suggestion for next month",
      "Next billing date and amount correct"])
  + '<h3><span class="k">SX</span>Shop Check / Monthly Care report</h3>' + chk([
      "Score adds up to 100 by the rubric; every deduction has a photo or a clear note",
      "No customers' faces; staff appear only with the owner's permission",
      "No staff member named in a negative finding",
      "Every money example says «مثال حسابي، مو وعد», shows a gain bigger than the fee, and uses no real sales data",
      "No accounting, sales or bank data requested or used",
      "Top 5 fixes are practical and ordered, each with why and how",
      "Prices match offer sheet v2026-11-08 exactly: 3,300 (one visit) and 1,700/month",
      "Monthly: comparison with last month is correct; the fixes-held list matches the previous report"]) + "</div>")

# ---------------------------------------------------------------- PART 5  Templates
p5 = part("Part 5", "Message templates", "Arabic, ready to send after you approve. Replace the [brackets]. Sign every message <bdi dir=\"rtl\">«عبدالإله من LocalBoost»</bdi>.",
  msg("5·1 Kickoff (after payment confirmed)", """
السلام عليكم [الاسم]،
وصلت الدفعة، شكراً لك 🌟 نبدأ الحين على [اسم الباقة] لـ [اسم المحل].
الخطوة الجاية بسيطة:
١. عبّ نموذج المعلومات: [رابط النموذج]
٢. أضف إيميلنا كمدير على ملف قوقل (الطريقة بالخطوات تحت)
أول ما توصلنا المعلومات نجهّز الشغل ونرسله لك تراجعه قبل أي نشر."""))
p5 += msg("5·2 Manager invite steps", """
عشان نشتغل على ملفك بدون ما تعطينا أي كلمة مرور:
١. افتح ملف محلك في قوقل ماب (أو business.google.com)
٢. الإعدادات ← الأشخاص والوصول ← إضافة
٣. اكتب: [إيميل LocalBoost] واختر «مدير» (مو مالك)
تقدر تشيلنا متى ما بغيت، والملف يبقى باسمك ١٠٠٪.""")
p5 += msg("5·3 Review request (before anything goes live)", """
هلا [الاسم]، جهّزنا التعديلات لـ [اسم المحل]:
• التصنيف: [..]
• الساعات + رمضان/العيد: [..]
• الوصف: [النص]
• الخدمات: [..]
• الصور: [عدد] صورة بالترتيب المرفق
• للموقع: رابط المعاينة [الرابط]، جرّبه من جوالك
إذا كل شي تمام رد بـ «موافق»، وإذا فيه تعديل اكتبه لي في رسالة وحدة.""")
p5 += msg("5·4 Handover", """
السلام عليكم [الاسم]،
خلصنا شغل [اسم المحل] 🎉
اللي تم: [بند ١] · [بند ٢] · [بند ٣]
المرفقات: كرت التقييم QR (اطبعه وحطه عند الكاشير) · صور قبل وبعد · رابط الموقع (لباقة الموقع)
تذكير: كل شي باسمك وملكك، وتعديلات قوقل أحياناً تاخذ أيام لين تظهر.
وإذا تبي نتابع الملف كل شهر، عندنا «خلّك محدّث» بـ 299 ريال شهرياً. وإذا لا، يعطيك العافية وأي وقت تحتاجنا موجودين.""")
p5 += msg("5·5 Day-7 feedback (once)", """
هلا [الاسم]، مر أسبوع على التسليم. كل شي تمام؟ إذا فيه ملاحظة أو شي تبي يتعدل قل لي.""")
p5 += msg("5·6 Reply drafts for approval (Stay Current)", """
هلا [الاسم]، وصلت [عدد] تقييمات جديدة هالأسبوع. جهّزنا الردود:
١. [التقييم باختصار] ← الرد: [..]
٢. ..
رد بـ «موافق» وننشرها، أو عدّل اللي تبي.""")
p5 += msg("5·8 Shop Check booking", """
هلا [الاسم]، تم تأكيد زيارة التقييم لـ [اسم المحل] 🔭
الزيارة بتكون خلال [الفترة]، وفريقك ما يدري عن الموعد عشان نشوف التجربة طبيعية.
نحتاج منك موافقة مكتوبة على التصوير داخل المحل (بدون وجوه الزباين). رد بـ «موافق».""")
p5 += msg("5·9 Report ready + results session", """
هلا [الاسم]، تقرير زيارة التقييم جاهز ✅
درجة المحل: [x] من 100، ومعها أهم 5 تعديلات.
متى يناسبك نجلس [30–45 دقيقة] نشرح النتائج؟""")
p5 += msg("5·10 Monthly Care offer (once)", """
إذا حاب نتابع معك كل شهر ونتأكد إن التعديلات ثابتة: «المتابعة الشهرية» بـ 1,700 ريال شهرياً.
زيارة سرّية كل شهر، ونتأكد إن التعديلات ثابتة، وجلسة قصيرة مع الفريق، وتقرير شهري.""")
p5 += msg("5·11 Monthly Care report", """
هلا [الاسم]، تقرير المتابعة لشهر [..] جاهز:
• الدرجة: [x] من 100 (الشهر الماضي [y])
• التعديلات الثابتة: [..]
• نشتغل عليها الشهر الجاي: [..]
وموعد جلسة الفريق الجاية: [..]""")
p5 += msg("5·7 Renewal reminder", """
هلا [الاسم]، تذكير بسيط: اشتراك «خلّك محدّث» لـ [اسم المحل] يتجدد بتاريخ [..] بمبلغ 299 ريال.
إذا تبي توقفه، قل لي قبل التاريخ وما فيه أي مشكلة.""")

# ---------------------------------------------------------------- PART 6  Problems
p6 = part("Part 6", "When things go wrong", "Fast answers to the problems you'll actually meet. When in doubt: pause, tell the client honestly, decide yourself. Bots escalate, they don't improvise.",
  "<div class='compact'><table><tr><th>Problem</th><th>What to do</th></tr>" + "".join(f"<tr><td><b>{a}</b></td><td>{b}</td></tr>" for a, b in [
      ("Owner can't find how to add a Manager", "Send template 5·2 again with screenshots; offer a 5-minute call or a visit. Never ask for their password instead."),
      ("Profile isn't claimed or verified", "Only the owner can verify. Pause the project, explain why, and resume after verification. The target date moves; tell them in writing."),
      ("Profile is suspended", "Stop. Don't create a new listing. The owner files Google's reinstatement request with real proof of the business. Escalate to you."),
      ("Edit stuck “under review” or rejected", "Wait 2–3 days. Check the edit follows Google's rules (real name, real address, no keywords). Resubmit once, then tell the client honestly."),
      ("Duplicate listings for the same shop", "Note it in the audit. The owner can request removal/merge through Google support. Don't delete anything yourself."),
      ("Client asks for guaranteed ranking or fake reviews", "Politely refuse (FAQ wording in 01-offer.md). It's both a promise you can't keep and against Google's rules."),
      ("Client wants a discount or extra scope", "Bots never agree. You decide: price it, swap it for something in scope, or decline."),
      ("A wave of negative or fake reviews", "Don't argue publicly. Draft calm replies for approval, and the owner reports policy-violating reviews through Google. Never post counter-reviews."),
      ("Client unhappy after delivery", "Listen and compare with the written scope. Fix anything that's in scope quickly; for the rest, explain kindly. Refunds follow the policy: you decide."),
      ("Payment not received", "No work starts or continues. One polite reminder, then pause. Never mark it paid from a screenshot."),
      ("Owner refuses photo permission (Shop Check)", "Do the visit with written notes only, and tell the owner the report will have fewer images. Never photograph secretly."),
      ("Staff recognised you during the visit", "Note it; don't score the affected items. Repeat the visit another day (your decision on cost)."),
      ("Owner wants names and blame in the report", "Keep the written report about the shop. Discuss individuals privately with the owner only."),
      ("Owner offers to show sales numbers", "Politely decline: it's out of scope. Use only what a customer can see."),
      ("Client stops replying mid-project", "Max 3 reminders, 2 working days apart. Then Project → On hold (client unresponsive), and one final message saying you're ready when they are."),
  ]) + "</table>"
  + '<div class="box ok"><h4>The one-line test before anything goes out</h4><p>“Is it <b>true</b>, <b>approved</b>, <b>paid for</b>, <b>in scope</b>, and <b>logged</b>?” If any answer is no, it doesn\'t go out.</p></div>' + '</div>')

# ---------------------------------------------------------------- PART 3B / 3C  Shop Experience (Stage 2 · Orbit)
p3b = part("Part 3B · Stage 2 · Orbit", "Shop Check · زيارة التقييم", "3,300 SAR, one visit (LB-CHK). Secret-shopper visit, shop appearance, visible money leaks, photo report, score out of 100, top 5 fixes by priority, results session.",
  '<div class="box navy"><h4>What the client receives</h4>' + ul([
      "One secret-shopper visit at a normal busy time (the owner knows, the staff don't)",
      "Shop appearance: storefront, sign, display, menu/prices, staff look",
      "Visible money leaks (no add-on offered, unclear prices, long waits, missing items)",
      "A photo report with a score out of 100 (rubric: <code>templates/shop-check-report.md</code>)",
      "Top 5 fixes, ordered by impact and effort",
      "A results session with the owner"])
  + '<p class="small"><b>Scope:</b> no accounting, no sales or bank data, no supplier contracts, no profit promises. <b>Pitch it to</b> shops that already show well on Maps but have weak service or appearance.</p></div>'
  + step("S·A", "Agreement + permissions", who("you", "cli"),
         ul(["Written scope and price (offer sheet v2026-11-07). Payment confirmed by you before the visit.",
             "<b>Written permission to take photos inside the shop.</b> No permission → visit with notes only.",
             "Agree a visit window with the owner. The staff must not know the day.",
             "<code>[FOUNDER DECISION]</code> who pays for any purchase made during the visit."]))
  + step("S·B", "Prepare", who("bot"),
         ul(["Print the scoring sheet from <code>templates/shop-check-report.md</code>.",
             "Plan the customer journey: approach → enter → ask/order → wait → pay → leave.",
             "Pick a normal busy time, not opening minute or closing minute."]))
  + step("S·C", "The visit (20–40 minutes)", who("you"),
         ul(["Behave like a normal customer. Don't reveal who you are.",
             "Note: greeting (yes/no, how long), cleanliness, display, price clarity, wait time, whether an add-on was offered, how you were thanked.",
             "Photos, discreetly: storefront, sign, display, menu, shelves. <b>Never customers' faces.</b> Staff only if the owner allowed it.",
             "Write your full notes within 30 minutes of leaving, while it's fresh."]))
  + step("S·D", "Report draft", who("bot"),
         ul(["Claude drafts the report from your notes and photos using the template: score per category, each finding with a photo or note, money leaks, and the top 5 fixes (problem → why it matters → the fix → effort).",
             "Any money example says «مثال حسابي، مو وعد», shows a gain bigger than the fee, and never uses the shop's real sales data."]))
  + step("S·E", "QC + your review", who("bot", "you"), "<p>QC checks the report; you run the <b>SX</b> checklist in Part 4.</p>")
  + step("S·F", "Results session (30–45 min)", who("you", "cli"),
         ul(["Owner only (or whoever the owner chooses). Start with what works.",
             "Walk through the score and the top 5 fixes. Agree which 1–2 to start with this week.",
             "The report is about the shop, never about blaming a named staff member."]))
  + step("S·G", "Offer Monthly Care", who("you"),
         "<p>Offer Monthly Care (LB-MC, 1,700/month) once, with no pressure: a monthly visit compared with this one, a check that the fixes held, simple checklists, a short staff session and a monthly report.</p>")
  + step("S·H", "Close", who("bot"),
         ul(["Project → Delivered; report PDF in 03-final; consents saved.",
             "Day 7: one check-in (how are the first fixes going?)."])))

p3c = part("Part 3C · Stage 2 · Orbit", "Monthly Care · المتابعة الشهرية", "1,700 SAR / month (LB-MC). One secret-shopper visit, a fix check, checklists, a staff session and a report every month.",
  '<div class="compact"><div class="box warn"><h4>Before the first month</h4>' + chk([
      "A baseline score exists: the Shop Check, or the first month's visit",
      "Monthly payment confirmed by you before the month's work starts",
      "Cancellation terms recorded. <code>[FOUNDER DECISION]</code> Monthly Care cancellation terms",
      "Photo permission still valid; Recurring row created",
      "Capacity: every client = 1 visit + 1 session + 1 report a month. <code>[FOUNDER DECISION]</code> the maximum number of Monthly Care clients"]) + "</div>"
  + "<h3><span class='k'>3C.1</span>The monthly cycle</h3>"
  + "<table><tr><th>When</th><th>What</th><th>Who</th></tr>"
  + "<tr><td><b>Billing day</b></td><td>Confirm payment. No payment = pause, no visit.</td><td>" + who("you") + "</td></tr>"
  + "<tr><td><b>Month 1, week 1</b></td><td>Deliver the four simple checklists (opening, closing, cleaning, welcome) as a printable PDF.</td><td>" + who("bot", "you") + "</td></tr>"
  + "<tr><td><b>Visit</b></td><td>Secret-shopper visit on a <b>different day and time</b> each month. Same rubric, same journey.</td><td>" + who("you") + "</td></tr>"
  + "<tr><td><b>Within 3 days</b></td><td>Report: score vs last month, which fixes held or slipped, up to 3 new priorities, photos.</td><td>" + who("bot", "you") + "</td></tr>"
  + "<tr><td><b>Staff session</b></td><td>15–20 minutes, positive and practical, built on the checklists. Praise in public, coach in private; no blaming.</td><td>" + who("you", "cli") + "</td></tr>"
  + "<tr><td><b>5 days before billing</b></td><td>Renewal reminder (template 5·7 wording, adapted), after your approval.</td><td>" + who("bot", "you") + "</td></tr></table>"
  + '<div class="box ok"><h4>What “good” looks like</h4><p>The score is compared honestly month to month, even if it drops. Never inflate a score to keep a client.</p></div></div>')

page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>LocalBoost Delivery Playbook</title><style>{CSS}</style></head><body>'
        + cover + toc + p0 + p1 + p2 + p3 + p3b + p3c + p4 + (p5.replace('</section>', '', 1) + '</section>') + p6 + "</body></html>")
(out / "localboost-delivery-playbook.html").write_text(page, encoding="utf-8")
print("built")
