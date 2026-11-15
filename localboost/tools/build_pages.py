#!/usr/bin/env python3
"""Builds the LocalBoost service pages and tips pages (Arabic + English).

Run from the repo root:  python3 localboost/tools/build_pages.py
Writes into localboost/site/. Edit the text in PAGES below, then re-run.
Rules: only the five prices, no guarantees, examples labelled, no districts.
"""
import json, os

SITE = os.path.join(os.path.dirname(__file__), '..', 'site')
BASE = 'https://localboostsa.store/'
WA = {
 'ar': 'https://wa.me/966557891433?text=%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85%20%D8%B9%D9%84%D9%8A%D9%83%D9%85%D8%8C%20%D8%A3%D8%A8%D9%8A%20%D8%A7%D9%84%D9%81%D8%AD%D8%B5%20%D8%A7%D9%84%D9%85%D8%AC%D8%A7%D9%86%D9%8A%20%D9%84%D9%85%D8%AD%D9%84%D9%8A%20%D8%B9%D9%84%D9%89%20%D8%A7%D9%84%D8%AE%D8%B1%D9%8A%D8%B7%D8%A9',
 'en': 'https://wa.me/966557891433?text=Hello%2C%20I%27d%20like%20the%20free%20Maps%20check%20for%20my%20shop.',
}
UI = {
 'ar': dict(home='الرئيسية', packages='الباقات', orbit='تجربة المحل', tips='نصائح', lang='English', langcode='en',
            cta='اطلب فحص الخريطة', skip='تخطَّ إلى المحتوى', policies='السياسات والاسترجاع',
            tag='سهل يلقونك. واضح. وجاهز لزبائنك.', indep='خدمة مستقلة، ما نتبع قوقل ولا Meta.',
            ctah='نبدأ بفحص مجاني ٥ دقايق', ctap='نشوف ملفك ونقولك وش ناقص بالضبط، بدون أي التزام.',
            ctab='راسلنا على واتساب', related='صفحات لها علاقة', svc='خدماتنا', price_once='مرة وحدة', per_month='/ شهرياً'),
 'en': dict(home='Home', packages='Packages', orbit='Shop experience', tips='Tips', lang='العربية', langcode='ar',
            cta='Request a Maps check', skip='Skip to content', policies='Policies & refunds',
            tag='Findable. Clear. Ready for customers.', indep='Independent service, not affiliated with Google or Meta.',
            ctah='Start with a free 5-minute check', ctap="We look at your profile and tell you exactly what's missing. No commitment.",
            ctab='Message us on WhatsApp', related='Related pages', svc='Our services', price_once='one-time', per_month='/ month'),
}
SERVICES = ['get-found', 'get-chosen', 'shop-check', 'monthly-care']
TIPS = ['maps-photos', 'ramadan-hours', 'review-replies']

# ---------- content ----------
P = {}
P['get-found'] = {
 'code': 'LB-GF · STAGE 1', 'price': ('900', 'once'),
 'ar': dict(title='خلّهم يلقونك: ملف قوقل ماب كامل لمحلك في الرياض', h1='خلّهم يلقونك',
   desc='نكمّل ملف محلك على خرائط قوقل: التصنيف، الموقع، الساعات مع رمضان والعيد، الوصف، الصور، أزرار واتساب والاتصال، وكرت QR للتقييمات. ٩٠٠ ريال مرة وحدة.',
   lead='الزبون يدوّر على الخريطة قبل ما يتحرك. نخلّي ملف محلك كامل وصحيح وواضح، عشان اللي يلقاك يعرف وش عندك ومتى تفتح وكيف يوصلك.',
   body='''<div class="facts"><div><small>المدة</small><b>٥ أيام عمل</b></div><div><small>التعديلات</small><b>جولتين خلال ٧ أيام</b></div><div><small>الدفع</small><b>نص بالبداية ونص بالتسليم</b></div></div>
<h2>وش يشمل</h2>
<ul><li>التصنيف الصحيح والدبوس في مكانه، والخدمات أو المنيو</li><li>ساعات الأسبوع كاملة، مع ساعات رمضان والعيد</li><li>وصف عربي واضح، وترتيب الصور بحيث أول اللي يشوفه الزبون هو الأحسن</li><li>أزرار واتساب والاتصال والاتجاهات</li><li>كرت QR يسهّل على زباينك الحقيقيين يقيّمونك</li><li>مسودات ردود على التقييمات، ما تنزل إلا بموافقتك</li></ul>
<p>سعر الإطلاق <b>٧٥٠ ريال</b> لأول عميلين، ونأكد لك توفره في الفحص.</p>
<h2>وش نحتاج منك</h2>
<ul><li>تضيفنا كمدير على ملفك من جوالك، ونرسل لك الطريقة خطوة بخطوة. ما نطلب أي كلمة مرور.</li><li>صور المحل، أو إذنك نصوّره.</li><li>معلومات المحل: الساعات، الخدمات، الأسعار إذا تبي تظهر.</li></ul>
<h2>بعد التسليم</h2>
<p>تقدر تضيف «خلّك محدّث» بـ<b>٢٩٩ ريال شهرياً</b>: فحص شهري للملف، تحديثين، ١٠ مسودات ردود على التقييمات، وتقرير صفحة وحدة.</p>
<div class="honest"><b>للأمانة:</b> ما نضمن ترتيب في قوقل ولا عدد زباين. اللي نلتزم فيه إن ملفك يكون كامل وصحيح وواضح، والحساب يبقى باسمك.</div>''',
   related=[('get-chosen', 'تبي موقع بسيط بعد؟', 'خلّهم يختارونك: الملف + موقع جوال'), ('tips/maps-photos', 'نصيحة', 'أول ٣ صور = واجهة محلك الجديدة'), ('tips/ramadan-hours', 'نصيحة', 'جهّز ساعات رمضان والعيد')]),
 'en': dict(title='Get Found: a complete Google Maps profile for your Riyadh shop', h1='Get Found',
   desc='We complete your Google Maps profile: category, pin, hours incl. Ramadan and Eid, description, photos, WhatsApp and call buttons, and a review QR card. SAR 900 one-time.',
   lead='Customers check the map before they leave home. We make your profile complete, correct and clear, so whoever finds you knows what you offer, when you open and how to reach you.',
   body='''<div class="facts"><div><small>Delivery</small><b>5 working days</b></div><div><small>Edits</small><b>2 rounds within 7 days</b></div><div><small>Payment</small><b>50% at start, 50% on delivery</b></div></div>
<h2>What's included</h2>
<ul><li>The right category, the pin in the right place, and your services or menu</li><li>Full weekly hours, plus Ramadan and Eid hours</li><li>A clear Arabic description, and photos ordered so customers see the best first</li><li>WhatsApp, call and directions buttons</li><li>A QR card that makes it easy for real customers to review you</li><li>Review-reply drafts, published only with your approval</li></ul>
<p>Launch price <b>SAR 750</b> for the first 2 clients; we confirm availability during the check.</p>
<h2>What we need from you</h2>
<ul><li>Add us as a manager on your profile from your phone; we send you the steps. We never ask for a password.</li><li>Photos of the shop, or permission to take them.</li><li>Your details: hours, services, and prices if you want them shown.</li></ul>
<h2>After delivery</h2>
<p>You can add Stay Current for <b>SAR 299/month</b>: a monthly profile check, 2 updates, 10 review-reply drafts and a one-page report.</p>
<div class="honest"><b>To be honest:</b> we don't guarantee rankings or customer numbers. We commit to a complete, correct, clear profile, and the account stays in your name.</div>''',
   related=[('get-chosen', 'Want a simple website too?', 'Get Chosen: profile + mobile site'), ('tips/maps-photos', 'Tip', 'Your first 3 photos are your new storefront'), ('tips/ramadan-hours', 'Tip', 'Get your Ramadan and Eid hours ready')]),
}
P['get-chosen'] = {
 'code': 'LB-GC · STAGE 1', 'price': ('2,200', 'once'),
 'ar': dict(title='خلّهم يختارونك: ملف قوقل ماب + موقع جوال بسيط لمحلك', h1='خلّهم يختارونك',
   desc='كل اللي في «خلّهم يلقونك» مع موقع جوال بسيط باسمك: الرئيسية، عنّا، الخدمات أو المنيو بالأسعار، الخريطة وواتساب. ٢٬٢٠٠ ريال مرة وحدة.',
   lead='بعد ما يلقاك الزبون، يبي يتأكد قبل ما يختارك. موقع بسيط وسريع على الجوال يعرض خدماتك وأسعارك ويوصله لك بضغطة.',
   body='''<div class="facts"><div><small>المدة</small><b>١٠ أيام عمل</b></div><div><small>التعديلات</small><b>جولتين قبل الإطلاق + ١٤ يوم إصلاح أخطاء</b></div><div><small>الدومين والاستضافة</small><b>بالتكلفة وباسمك</b></div></div>
<h2>وش يشمل</h2>
<ul><li>كل اللي في <a href="../get-found/">باقة خلّهم يلقونك</a></li><li>موقع جوال بسيط: الرئيسية، عنّا، الخدمات أو المنيو بالأسعار، الخريطة</li><li>أزرار واتساب والاتصال والخريطة</li><li>عربي، وثنائي اللغة إذا اتفقنا</li></ul>
<h2>وش نحتاج منك</h2>
<ul><li>نفس اللي نحتاجه لملف الخريطة، مع قائمة الخدمات أو المنيو والأسعار</li><li>شعار المحل إذا موجود</li><li>تختار الدومين، ونسجّله باسمك</li></ul>
<div class="honest"><b>للأمانة:</b> الموقع ما يضمن مبيعات. يخلّي الزبون يلقى معلومات صحيحة وواضحة، وكل شي يبقى ملكك.</div>''',
   related=[('get-found', 'تبي الملف بس؟', 'خلّهم يلقونك: ملف قوقل ماب كامل'), ('shop-check', 'بعد ما يجونك', 'زيارة التقييم: تجربة الزبون داخل المحل'), ('tips/review-replies', 'نصيحة', 'ردّك على التقييم يقراه الزبون الجاي')]),
 'en': dict(title='Get Chosen: Google Maps profile + a simple mobile website', h1='Get Chosen',
   desc='Everything in Get Found plus a simple mobile website in your name: Home, About, Services or Menu with prices, map and WhatsApp. SAR 2,200 one-time.',
   lead="Once customers find you, they want to be sure before choosing you. A simple, fast mobile site shows your services and prices and reaches you in one tap.",
   body='''<div class="facts"><div><small>Delivery</small><b>10 working days</b></div><div><small>Edits</small><b>2 rounds before launch + 14 days of bug fixes</b></div><div><small>Domain and hosting</small><b>At cost, in your name</b></div></div>
<h2>What's included</h2>
<ul><li>Everything in the <a href="../get-found/">Get Found package</a></li><li>A simple mobile site: Home, About, Services or Menu with prices, map</li><li>WhatsApp, call and map buttons</li><li>Arabic, bilingual if agreed</li></ul>
<h2>What we need from you</h2>
<ul><li>The same as the Maps profile, plus your services or menu and prices</li><li>Your logo, if you have one</li><li>You choose the domain; we register it in your name</li></ul>
<div class="honest"><b>To be honest:</b> a website doesn't guarantee sales. It gives customers correct, clear information, and everything stays yours.</div>''',
   related=[('get-found', 'Just the profile?', 'Get Found: a complete Google Maps profile'), ('shop-check', 'Once they walk in', 'Shop Check: the in-shop customer experience'), ('tips/review-replies', 'Tip', 'Your review reply is read by the next customer')]),
}
P['shop-check'] = {
 'code': 'LB-CHK · STAGE 2', 'price': ('3,300', 'once'),
 'ar': dict(title='زيارة التقييم: تشخيص كامل لتجربة الزبون في محلك', h1='زيارة التقييم',
   desc='تشخيص كامل لتجربة الزبون: دراسة التقييمات، زيارة كزبون سرّي، درجة من ١٠٠، تقرير بالصور، أهم ٥ تعديلات و٣ تحسينات سريعة، وجلسة نتائج ٤٥ دقيقة. ٣٬٣٠٠ ريال.',
   lead='ملفك يجيب الزبون لباب المحل، وبعدها تبدأ التجربة. نشوف محلك بعين زبونك، ونقولك بالضبط وش يشوف، ووين تضيع فلوس وهي قدامك.',
   body='''<div class="facts"><div><small>التقرير</small><b>خلال ٥ أيام عمل بعد الزيارة</b></div><div><small>بعد التقرير</small><b>جلسة ٤٥ دقيقة + ١٤ يوم أسئلة</b></div><div><small>الدفع</small><b>نص بالبداية ونص بالتسليم</b></div></div>
<h2>وش يشمل</h2>
<ul><li>دراسة تقييماتك على قوقل: وش يتكرر، ووش يمدحون، ووش يزعّلهم</li><li>زيارة كزبون عادي بدون ما يدري الفريق</li><li>درجة من ١٠٠ على ٥ محاور: الاستقبال ٢٠ · الانتظار والخدمة ٢٠ · النظافة ٢٠ · المظهر ٢٥ · الفلوس اللي تضيع ١٥</li><li>تقرير بالصور</li><li>أهم ٥ تعديلات حسب الأولوية، و٣ تحسينات سريعة مجاناً</li><li>جلسة ٤٥ دقيقة نشرح فيها النتائج، و١٤ يوم تسألنا فيها اللي تبي</li></ul>
<p>الدرجة ما تتغير بالطلب. نصحح الأخطاء في المعلومات بس، جولة وحدة.</p>
<h2>الفلوس اللي تضيع</h2>
<div class="example"><span class="label">مثال حسابي، مو وعد</span><p style="margin:0">إضافة صغيرة بـ١٠ ريال × ١٠ زباين باليوم × ٣٠ يوم = ٣٬٠٠٠ ريال بالشهر. مثلاً مشروب أو خدمة إضافية يقترحها الفريق بالشكل الصح.</p></div>
<h2>خارج النطاق</h2>
<p>ما نطلب حسابات أو مبيعات أو بيانات بنك، ولا نتدخل في عقود الموردين، ولا نوعد بأرباح. ما نصوّر وجوه الزباين، وصور الفريق بموافقتك المكتوبة بس.</p>''',
   related=[('monthly-care', 'بعد الزيارة', 'المتابعة الشهرية: نتأكد إن التعديلات ثابتة'), ('tips/review-replies', 'نصيحة', 'ردّك على التقييم يقراه الزبون الجاي'), ('get-found', 'محلك ما يطلع في الخريطة؟', 'خلّهم يلقونك: ابدأ من هنا')]),
 'en': dict(title='Shop Check: a full diagnosis of your customer experience', h1='Shop Check',
   desc='A full customer-experience diagnosis: review study, secret-shopper visit, score out of 100, photo report, top 5 fixes + 3 quick wins, and a 45-minute results session. SAR 3,300.',
   lead="Your profile brings customers to the door; then the experience starts. We see your shop through your customer's eyes and tell you exactly what they see, and where money slips away in plain sight.",
   body='''<div class="facts"><div><small>Report</small><b>Within 5 working days of the visit</b></div><div><small>After the report</small><b>45-min session + 14 days of questions</b></div><div><small>Payment</small><b>50% at start, 50% on delivery</b></div></div>
<h2>What's included</h2>
<ul><li>A study of your Google reviews: what repeats, what customers praise, what upsets them</li><li>A visit as a normal customer, without your team knowing</li><li>A score out of 100 on 5 areas: Welcome 20 · Wait & service 20 · Cleanliness 20 · Appearance 25 · Money leaks 15</li><li>A photo report</li><li>The top 5 fixes by priority, plus 3 free quick wins</li><li>A 45-minute results session, and 14 days to ask us anything</li></ul>
<p>The score never changes on request. We correct factual errors only, in one round.</p>
<h2>Money leaks</h2>
<div class="example"><span class="label">A worked example, not a promise</span><p style="margin:0">A 10-riyal add-on × 10 customers a day × 30 days = SAR 3,000 a month. For example a drink or extra service your team suggests the right way.</p></div>
<h2>Out of scope</h2>
<p>We never ask for accounts, sales or bank data, don't touch supplier contracts, and don't promise profit. No customer faces in photos; staff only with your written permission.</p>''',
   related=[('monthly-care', 'After the visit', 'Monthly Care: make sure the fixes hold'), ('tips/review-replies', 'Tip', 'Your review reply is read by the next customer'), ('get-found', 'Not on the map yet?', 'Get Found: start here')]),
}
P['monthly-care'] = {
 'code': 'LB-MC · STAGE 2', 'price': ('1,700', 'month'),
 'ar': dict(title='المتابعة الشهرية: زيارة كل شهر عشان النتائج تثبت', h1='المتابعة الشهرية',
   desc='زيارة سرّية كل شهر مع مقارنة بالشهر اللي قبله، متابعة التعديلات، ٤ قوائم للفريق، جلسة قصيرة، وتقرير شهري. ١٬٧٠٠ ريال شهرياً.',
   lead='التعديلات تنسى إذا محد يتابعها. نرجع كل شهر كزبون، ونقارن بالشهر اللي قبله، ونتأكد إن اللي اتفقنا عليه صار عادة.',
   body='''<div class="facts"><div><small>الدفع</small><b>مقدّم بداية كل شهر</b></div><div><small>الإيقاف</small><b>بإشعار قبل ١٥ يوم</b></div><div><small>التعديل</small><b>القوائم تتحدث كل شهر + تغيير تركيز واحد</b></div></div>
<h2>وش يشمل</h2>
<ul><li>زيارة سرّية كل شهر، ومقارنة بالشهر اللي قبله</li><li>نتأكد إن التعديلات ثابتة</li><li>٤ قوائم للفريق تتحدث كل شهر: الفتح، الإغلاق، النظافة، الاستقبال</li><li>جلسة قصيرة مع الفريق</li><li>تقرير شهري</li></ul>
<div class="example"><span class="label">مثال حسابي، مو وعد</span><p style="margin:0">إضافة بـ١٠ ريال × ١٠ زباين باليوم × ٣٠ يوم = ٣٬٠٠٠ ريال بالشهر، مقابل ١٬٧٠٠ ريال رسوم المتابعة.</p></div>
<p>أفضل بداية لها بعد <a href="../shop-check/">زيارة التقييم</a>، عشان يكون عندنا درجة نقارن عليها.</p>
<div class="honest"><b>للأمانة:</b> ما نوعد بأرباح، وما نطلب حسابات أو مبيعات. نشتغل على اللي يشوفه الزبون بس.</div>''',
   related=[('shop-check', 'ابدأ من هنا', 'زيارة التقييم: التشخيص الكامل'), ('get-found', 'ملف الخريطة', 'خلّهم يلقونك'), ('tips/review-replies', 'نصيحة', 'كيف ترد على التقييمات')]),
 'en': dict(title='Monthly Care: a visit every month so results hold', h1='Monthly Care',
   desc='A secret-shopper visit every month compared with the last, fix follow-up, 4 staff checklists, a short staff session and a monthly report. SAR 1,700/month.',
   lead="Fixes fade when nobody follows up. We come back as a customer every month, compare with last month, and make sure what we agreed becomes a habit.",
   body='''<div class="facts"><div><small>Payment</small><b>In advance, each month</b></div><div><small>Stopping</small><b>15 days' notice</b></div><div><small>Changes</small><b>Checklists updated monthly + 1 change of focus</b></div></div>
<h2>What's included</h2>
<ul><li>A secret-shopper visit every month, compared with the month before</li><li>A check that the fixes held</li><li>4 staff checklists updated monthly: opening, closing, cleaning, welcome</li><li>A short session with your team</li><li>A monthly report</li></ul>
<div class="example"><span class="label">A worked example, not a promise</span><p style="margin:0">A 10-riyal add-on × 10 customers a day × 30 days = SAR 3,000 a month, against the SAR 1,700 fee.</p></div>
<p>It works best after a <a href="../shop-check/">Shop Check</a>, so we have a score to compare against.</p>
<div class="honest"><b>To be honest:</b> we don't promise profit and never ask for accounts or sales. We work only on what customers can see.</div>''',
   related=[('shop-check', 'Start here', 'Shop Check: the full diagnosis'), ('get-found', 'Maps profile', 'Get Found'), ('tips/review-replies', 'Tip', 'How to reply to reviews')]),
}
P['tips'] = {
 'code': 'TIPS · LOCALBOOST', 'price': None,
 'ar': dict(title='نصائح لأصحاب المحلات: ملف قوقل ماب وتجربة الزبون', h1='نصائح تقدر تطبقها اليوم',
   desc='نصائح عملية لأصحاب المحلات في الرياض: صور ملف قوقل ماب، ساعات رمضان والعيد، والرد على التقييمات. تطبقها بنفسك ومجاناً.',
   lead='أشياء صغيرة يشوفها الزبون قبل ما يدخل محلك. كل نصيحة تقدر تطبقها بنفسك، ومجاناً.',
   body='''<ul class="hub-links related">
<li><a href="maps-photos/"><b>أول ٣ صور = واجهة محلك الجديدة</b><span>وش تصوّر، ومن وين، ووش تتجنب</span></a></li>
<li><a href="ramadan-hours/"><b>جهّز ساعات رمضان والعيد</b><span>الساعات الغلط تخسرك الزبون مرتين</span></a></li>
<li><a href="review-replies/"><b>ردّك على التقييم يقراه الزبون الجاي</b><span>صيغة رد من ٣ خطوات، مع مثال</span></a></li>
</ul>''', related=[('get-found', 'تبينا نسويها عنك؟', 'خلّهم يلقونك: ملف قوقل ماب كامل'), ('shop-check', 'داخل المحل', 'زيارة التقييم')]),
 'en': dict(title='Tips for shop owners: Google Maps profile and customer experience', h1='Tips you can use today',
   desc='Practical tips for shop owners in Riyadh: Google Maps photos, Ramadan and Eid hours, and replying to reviews. Free to apply yourself.',
   lead='Small things customers see before they walk in. You can apply every tip yourself, for free.',
   body='''<ul class="hub-links related">
<li><a href="maps-photos/"><b>Your first 3 photos are your new storefront</b><span>What to shoot, from where, and what to avoid</span></a></li>
<li><a href="ramadan-hours/"><b>Get your Ramadan and Eid hours ready</b><span>Wrong hours lose you the customer twice</span></a></li>
<li><a href="review-replies/"><b>Your review reply is read by the next customer</b><span>A 3-step reply formula, with an example</span></a></li>
</ul>''', related=[('get-found', 'Want us to do it for you?', 'Get Found: a complete Google Maps profile'), ('shop-check', 'Inside the shop', 'Shop Check')]),
}
P['tips/maps-photos'] = {
 'code': 'TIP · LB-GF', 'price': None,
 'ar': dict(title='صور ملف قوقل ماب: أول ٣ صور هي واجهة محلك', h1='أول ٣ صور = واجهة محلك الجديدة',
   desc='الزبون غالباً ما يفتح كل الصور في ملفك على قوقل ماب. هذي الصور اللي تحطها أول، ووش تتجنب، ومتى تحدّثها.',
   lead='الزبون غالباً ما يفتح كل الألبوم. أول اللي يشوفه هو اللي يحكم عليه، حتى لو محلك أحلى من الصور.',
   body='''<h2>سوّها اليوم</h2>
<ol><li><b>الواجهة في النهار،</b> من الرصيف المقابل، واللوحة مقروءة.</li><li><b>الداخل وهو مرتّب ومضاء،</b> قبل وقت الزحمة.</li><li><b>أشهر منتج أو خدمة عندك،</b> قريب وواضح.</li></ol>
<h2>تجنّب</h2>
<ul><li>الصور المظلمة أو الليلية الضبابية</li><li>وجوه الزباين بدون إذن</li><li>الشعار بدل صورة حقيقية للمحل</li></ul>
<h2>نصيحة زيادة</h2>
<p>حدّث صورك كل شهر. الصورة القديمة تقول للزبون: «هالمحل محد يتابعه».</p>''',
   related=[('get-found', 'تبينا نرتبها عنك؟', 'خلّهم يلقونك: ملف قوقل ماب كامل'), ('tips/ramadan-hours', 'النصيحة الجاية', 'جهّز ساعات رمضان والعيد')]),
 'en': dict(title='Google Maps photos: your first 3 photos are your storefront', h1='Your first 3 photos are your new storefront',
   desc="Customers rarely open every photo on your Google Maps profile. Which photos to put first, what to avoid, and when to update them.",
   lead="Customers rarely open the whole album. The first photos they see are what they judge you on, even if your shop looks better in person.",
   body='''<h2>Do it today</h2>
<ol><li><b>The storefront in daylight,</b> from across the street, with the sign readable.</li><li><b>The inside, tidy and well lit,</b> before the rush.</li><li><b>Your best-known product or service,</b> close up and clear.</li></ol>
<h2>Avoid</h2>
<ul><li>Dark or blurry night photos</li><li>Customers' faces without permission</li><li>Your logo instead of a real photo of the shop</li></ul>
<h2>One more tip</h2>
<p>Update your photos every month. Old photos tell customers: "nobody looks after this shop".</p>''',
   related=[('get-found', 'Want us to sort it out?', 'Get Found: a complete Google Maps profile'), ('tips/ramadan-hours', 'Next tip', 'Get your Ramadan and Eid hours ready')]),
}
P['tips/ramadan-hours'] = {
 'code': 'TIP · LB-GF', 'price': None,
 'ar': dict(title='ساعات رمضان والعيد في قوقل ماب: جهّزها قبلها بأسبوع', h1='ساعات غلط = زبون تخسره مرتين',
   desc='كيف تجهّز ساعات رمضان والعيد واليوم الوطني في ملف محلك على قوقل ماب قبل ما تبدأ، وكيف تعدّلها إذا سكّرت فجأة.',
   lead='مرة لما يوصل ويلقاه مسكّر، ومرة لما يكتب تقييم عن المشوار اللي راح عليه.',
   body='''<h2>سوّها اليوم</h2>
<ol><li><b>راجع ساعات الأسبوع</b> يوم يوم، خصوصاً الجمعة.</li><li><b>أضف «ساعات خاصة»</b> لرمضان والعيد واليوم الوطني، قبلها بأسبوع.</li><li><b>سكّرت فجأة؟</b> عدّلها من جوالك في دقيقة، قبل ما يتحرك الزبون.</li></ol>
<h2>تجنّب</h2>
<ul><li>«مفتوح ٢٤ ساعة» وأنت مو كذا</li><li>ساعات مختلفة بين قوقل واللوحة والانستقرام</li></ul>
<h2>اختبار سريع</h2>
<p>اسأل صديق يدوّر محلك الحين ويقولك وش مكتوب. إذا تفاجأت، زبونك بيتفاجأ قبلك.</p>''',
   related=[('get-found', 'نجهّزها عنك؟', 'خلّهم يلقونك: الساعات مع رمضان والعيد'), ('tips/review-replies', 'النصيحة الجاية', 'ردّك على التقييم يقراه الزبون الجاي')]),
 'en': dict(title='Ramadan and Eid hours on Google Maps: set them a week before', h1='Wrong hours lose you the customer twice',
   desc='How to set Ramadan, Eid and National Day hours on your Google Maps profile before they start, and how to fix them fast if you close unexpectedly.',
   lead='Once when they arrive and find you closed, and again when they write a review about the wasted trip.',
   body='''<h2>Do it today</h2>
<ol><li><b>Check your weekly hours</b> day by day, especially Friday.</li><li><b>Add "special hours"</b> for Ramadan, Eid and National Day, a week before.</li><li><b>Closed unexpectedly?</b> Update it from your phone in a minute, before customers set off.</li></ol>
<h2>Avoid</h2>
<ul><li>"Open 24 hours" when you aren't</li><li>Different hours on Google, your sign and Instagram</li></ul>
<h2>Quick test</h2>
<p>Ask a friend to search for your shop right now and read you what it says. If you're surprised, your customers will be too.</p>''',
   related=[('get-found', 'Want us to set them up?', 'Get Found: hours incl. Ramadan and Eid'), ('tips/review-replies', 'Next tip', 'Your review reply is read by the next customer')]),
}
P['tips/review-replies'] = {
 'code': 'TIP · LB-GF', 'price': None,
 'ar': dict(title='الرد على تقييمات قوقل ماب: صيغة من ٣ خطوات', h1='ردّك على التقييم يقراه الزبون الجاي',
   desc='كيف ترد على تقييمات محلك في قوقل ماب بصيغة من ٣ خطوات، مع مثال، ووش تتجنب.',
   lead='صاحب التقييم قال كلمته. ردّك يوصل للي لسى يقارن بينك وبين غيرك.',
   body='''<h2>الصيغة</h2>
<ol><li><b>اشكره</b> وسمِّ الخدمة اللي أخذها.</li><li><b>وضّح أو اعتذر،</b> وقل وش غيّرت.</li><li><b>ادعه يرجع،</b> بدون مبالغة.</li></ol>
<div class="example"><span class="label">مثال توضيحي</span><p style="margin:0">«شكراً على ملاحظتك عن الانتظار يوم الخميس. أضفنا موظف وقت الذروة، ونتشرف بزيارتك الجاية.»</p></div>
<h2>تجنّب</h2>
<ul><li>الجدال مع صاحب التقييم</li><li>نفس الرد للكل</li><li>خصم أو هدية مقابل تقييم</li></ul>''',
   related=[('get-found', 'نجهّز لك ردود جاهزة؟', 'خلّهم يلقونك: مسودات ردود لموافقتك'), ('shop-check', 'التقييمات تتكرر؟', 'زيارة التقييم: نشوف السبب داخل المحل')]),
 'en': dict(title='Replying to Google Maps reviews: a 3-step formula', h1='Your review reply is read by the next customer',
   desc='How to reply to your shop\'s Google Maps reviews with a 3-step formula, an example, and what to avoid.',
   lead="The reviewer has had their say. Your reply reaches the people still comparing you with someone else.",
   body='''<h2>The formula</h2>
<ol><li><b>Thank them</b> and name the service they had.</li><li><b>Explain or apologise,</b> and say what you changed.</li><li><b>Invite them back,</b> without overdoing it.</li></ol>
<div class="example"><span class="label">Illustrative example</span><p style="margin:0">"Thank you for your note about the wait on Thursday. We've added a team member at peak time, and we'd be glad to see you again."</p></div>
<h2>Avoid</h2>
<ul><li>Arguing with the reviewer</li><li>The same reply for everyone</li><li>Discounts or gifts in exchange for reviews</li></ul>''',
   related=[('get-found', 'Want reply drafts ready?', 'Get Found: review-reply drafts for your approval'), ('shop-check', 'Same complaint again?', 'Shop Check: find the cause inside the shop')]),
}

# ---------- template ----------
def rel(n): return '../' * n

def render(slug, lang):
    d = P[slug]; c = d[lang]; u = UI[lang]
    depth = slug.count('/') + 1             # folders below the language root
    up = rel(depth + (1 if lang == 'en' else 0))   # to site root
    lroot = rel(depth)                        # to this language's root
    other = (rel(depth) + 'en/' if lang == 'ar' else rel(depth + 1)) + slug + '/'
    url = BASE + ('en/' if lang == 'en' else '') + slug + '/'
    alt_ar = BASE + slug + '/'; alt_en = BASE + 'en/' + slug + '/'
    dirattr = 'lang="ar" dir="rtl"' if lang == 'ar' else 'lang="en" dir="ltr"'
    def href(s): return lroot + s + '/'
    crumbs = [(u['home'], lroot)]
    if slug.startswith('tips/'): crumbs.append((u['tips'], href('tips')))
    elif slug in SERVICES: crumbs.append((u['svc'], lroot + ('#orbit' if slug in ('shop-check', 'monthly-care') else '#packages')))
    crumb_html = ' › '.join(f'<a href="{h}">{t}</a>' for t, h in crumbs) + ' › ' + c['h1']
    price = ''
    if d['price']:
        amt, kind = d['price']
        price = f'<div class="price-ticket">SAR {amt} <small>{u["price_once"] if kind=="once" else u["per_month"]}</small></div>'
    rel_html = ''.join(f'<a href="{href(s)}"><span>{k}</span><b>{t}</b></a>' for s, k, t in c['related'])
    ld = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + ('en/' if lang == 'en' else '') + p}
        for i, (n, p) in enumerate([(u['home'], '')] + ([(u['tips'], 'tips/')] if slug.startswith('tips/') else []) + [(c['h1'], slug + '/')])]}]
    if d['price']:
        ld.append({"@context": "https://schema.org", "@type": "Service", "name": c['h1'], "description": c['desc'],
                   "provider": {"@type": "ProfessionalService", "name": "LocalBoost", "url": BASE, "telephone": "+966557891433"},
                   "areaServed": {"@type": "City", "name": "Riyadh"},
                   "offers": {"@type": "Offer", "price": d['price'][0].replace(',', ''), "priceCurrency": "SAR"}})
    ld_html = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    footer_links = ''.join(f'<li><a href="{href(s)}">{P[s][lang]["h1"]}</a></li>' for s in SERVICES)
    return f'''<!doctype html>
<html {dirattr}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{c['title']} | LocalBoost</title>
<meta name="description" content="{c['desc']}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="ar" href="{alt_ar}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="x-default" href="{alt_ar}">
<meta property="og:type" content="website">
<meta property="og:title" content="{c['title']}">
<meta property="og:description" content="{c['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/og-image.png?v=20261109">
<meta name="theme-color" content="#022754">
<link rel="icon" type="image/png" href="{up}assets/favicon.png">
<link rel="stylesheet" href="{up}assets/css/style.css">
<link rel="stylesheet" href="{up}assets/css/page.css">
{ld_html}
</head>
<body>
<a class="skip" href="#main">{u['skip']}</a>
<header class="header">
  <div class="wrap header__in">
    <a class="logo" href="{lroot}" aria-label="LocalBoost"><img src="{up}assets/logo.png" alt="LocalBoost" width="173" height="38"></a>
    <nav class="page-nav" aria-label="{u['home']}">
      <a class="pn-link" href="{lroot}#packages">{u['packages']}</a>
      <a class="pn-link" href="{lroot}#orbit">{u['orbit']}</a>
      <a class="pn-link" href="{href('tips')}">{u['tips']}</a>
      <a class="lang" href="{other}" hreflang="{u['langcode']}" lang="{u['langcode']}">{u['lang']}</a>
      <a class="btn btn--primary btn--small" href="{WA[lang]}" target="_blank" rel="noopener">{u['cta']}</a>
    </nav>
  </div>
</header>
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs">{crumb_html}</p>
    <span class="code-tag">{d['code']}</span>
    <h1>{c['h1']}</h1>
    <p>{c['lead']}</p>
    {price}
  </div>
</section>
<section class="section" style="padding-top:clamp(32px,5vw,56px)">
  <div class="wrap doc">
{c['body']}
    <div class="cta-box"><h2>{u['ctah']}</h2><p>{u['ctap']}</p><a class="btn btn--primary" href="{WA[lang]}" target="_blank" rel="noopener">{u['ctab']}</a></div>
    <h2>{u['related']}</h2>
    <div class="related">{rel_html}</div>
  </div>
</section>
</main>
<footer class="footer">
  <div class="wrap footer__in">
    <span class="flogo"><img src="{up}assets/logo.png" alt="LocalBoost" width="128" height="28" loading="lazy"></span>
    <p class="footer__tag">{u['tag']}</p>
    <ul><li><a href="{lroot}">{u['home']}</a></li>{footer_links}<li><a href="{href('tips')}">{u['tips']}</a></li><li><a href="{lroot}policies.html">{u['policies']}</a></li><li><a href="{other}" hreflang="{u['langcode']}" lang="{u['langcode']}">{u['lang']}</a></li></ul>
    <p style="margin:0;flex-basis:100%">© 2026 LocalBoost · {u['indep']}</p>
  </div>
</footer>
</body>
</html>
'''

def main():
    slugs = SERVICES + ['tips'] + ['tips/' + t for t in TIPS]
    for s in slugs:
        for lang in ('ar', 'en'):
            out = os.path.join(SITE, ('en' if lang == 'en' else ''), s, 'index.html')
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, 'w', encoding='utf-8').write(render(s, lang))
    urls = ['', 'en/', 'policies.html', 'en/policies.html'] + [p for s in slugs for p in (s + '/', 'en/' + s + '/')]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         ''.join(f'  <url><loc>{BASE}{u}</loc></url>\n' for u in urls) + '</urlset>\n'
    open(os.path.join(SITE, 'sitemap.xml'), 'w').write(sm)
    print(len(slugs) * 2, 'pages,', len(urls), 'sitemap URLs')

if __name__ == '__main__':
    main()
