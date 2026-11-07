"""Builds the three LocalBoost service brochures (A4, 2 pages each, Arabic).

Usage:  python3 localboost/brochures/build.py <qr.svg> <out-dir>
Then:   node localboost/brochures/render.js <out-dir>     (HTML -> PDF)

All prices, inclusions and policies come from localboost/01-offer.md (CEO-locked).
Nothing here may promise rankings, customer numbers or revenue.
"""
import sys, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parents[1]          # localboost/
ASSETS = ROOT / "site" / "assets"
SITE_URL = "crashbook2014.github.io/newme-"

qr_svg = pathlib.Path(sys.argv[1]).read_text()
out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
F = (ASSETS / "fonts").as_uri()
LOGO = (ASSETS / "logo.png").as_uri()

CSS = f"""
@font-face{{font-family:Plex;font-weight:400;src:url({F}/ibm-plex-sans-arabic-arabic-400-normal.woff2)}}
@font-face{{font-family:Plex;font-weight:600;src:url({F}/ibm-plex-sans-arabic-arabic-600-normal.woff2)}}
@font-face{{font-family:Plex;font-weight:700;src:url({F}/ibm-plex-sans-arabic-arabic-700-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:400;src:url({F}/inter-latin-400-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:600;src:url({F}/inter-latin-600-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:700;src:url({F}/inter-latin-700-normal.woff2)}}
@page{{size:A4;margin:0}}
:root{{--navy:#022754;--orange:#EA5C0A;--amber:#F6880F;--yellow:#FFD332;--mist:#F2F2F2;--ink:#0A1F3D;--soft:#55657c;--line:#dde3ec;--ok:#16794a}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:Plex,Inter,sans-serif;color:var(--ink);font-size:10.4pt;line-height:1.65}}
.lat{{font-family:Inter,Plex,sans-serif;direction:ltr;unicode-bidi:isolate}}
.page{{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;display:flex;flex-direction:column}}
.page:last-child{{page-break-after:auto}}
.pad{{padding:0 14mm}}
h2{{font-size:14.5pt;color:var(--navy);font-weight:700;margin-bottom:3mm;display:flex;align-items:center;gap:2.5mm}}
h2 .n{{font:700 9pt Inter;color:#fff;background:var(--orange);border-radius:50%;width:6.2mm;height:6.2mm;display:grid;place-items:center;flex:none}}
.top{{display:flex;justify-content:space-between;align-items:center;padding:7mm 14mm 5mm}}
.top img{{height:10mm}}
.top .tag{{font-weight:600;color:var(--navy);font-size:9.5pt}}
/* hero */
.hero{{background:radial-gradient(ellipse at 15% 120%,rgba(234,92,10,.45),rgba(2,39,84,0) 55%),linear-gradient(160deg,#03306a,var(--navy) 55%,#011a3b);color:#fff;padding:9mm 14mm 10mm;position:relative}}
.hero .eyebrow{{font:700 8.5pt Inter;letter-spacing:.22em;color:var(--yellow);text-transform:uppercase}}
.hero h1{{font-size:30pt;line-height:1.15;margin:2mm 0 1mm}}
.hero .en{{font:600 11pt Inter;color:#b9c7dc}}
.hero .promise{{font-size:12.5pt;margin-top:4mm;max-width:118mm;color:#e6ecf5}}
.price{{position:absolute;left:14mm;bottom:10mm;background:#fff;color:var(--navy);border-radius:5mm;padding:4mm 6mm;text-align:center;min-width:46mm;box-shadow:0 3mm 8mm rgba(0,0,0,.25)}}
.price b{{display:block;font:700 23pt Inter;line-height:1.1}}
.price small{{font-size:8.5pt;color:var(--soft);display:block}}
.price .launch{{margin-top:1.5mm;font-size:7.6pt;color:var(--orange);font-weight:700;line-height:1.35}}
/* blocks */
.sec{{margin-top:6mm}}
.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:3.5mm}}
.card{{border:.3mm solid var(--line);border-radius:3.5mm;padding:3.5mm 4mm;background:#fff}}
.card b{{display:block;color:var(--navy);font-size:10.6pt;margin-bottom:.8mm}}
.card p{{font-size:9.2pt;color:var(--soft);line-height:1.55}}
.ticks{{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:1.6mm 6mm}}
.ticks li{{position:relative;padding-inline-start:6mm;font-size:9.8pt}}
.ticks li::before{{content:"";position:absolute;inset-inline-start:0;top:1.6mm;width:3.6mm;height:3.6mm;border-radius:50%;background:var(--orange)}}
.ticks li::after{{content:"";position:absolute;inset-inline-start:1.05mm;top:2.35mm;width:1.5mm;height:.9mm;border-left:.45mm solid #fff;border-bottom:.45mm solid #fff;transform:rotate(-45deg)}}
.ticks.one{{grid-template-columns:1fr}}
.ticks.no li::before{{background:#c9d1dd}}
.ticks.no li::after{{content:"×";border:0;transform:none;top:1.15mm;inset-inline-start:.95mm;width:auto;height:auto;color:#fff;font:700 8pt Inter}}
.band{{background:var(--mist);border-radius:4mm;padding:5mm 6mm}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:5mm}}
/* steps */
.steps{{list-style:none;counter-reset:s;display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}}
.steps li{{counter-increment:s;background:#fff;border:.3mm solid var(--line);border-radius:3.5mm;padding:3.2mm 3.6mm;position:relative}}
.steps li::before{{content:counter(s);font:700 9pt Inter;color:#fff;background:var(--navy);width:6mm;height:6mm;border-radius:50%;display:grid;place-items:center;margin-bottom:1.5mm}}
.steps b{{display:block;color:var(--navy);font-size:10.2pt;line-height:1.4}}
.steps p{{font-size:8.9pt;color:var(--soft);line-height:1.5;margin-top:.6mm}}
.steps .who{{display:inline-block;margin-top:1.3mm;font-size:7.6pt;font-weight:700;border-radius:99px;padding:.2mm 2.4mm;background:#fff1e7;color:var(--orange)}}
.steps .who.you{{background:#e8eef8;color:var(--navy)}}
.honest{{border-inline-start:1.4mm solid var(--orange);background:#fff8f2;border-radius:3mm;padding:4mm 5mm}}
.honest ul{{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:1mm 6mm;font-size:9.3pt}}
.honest li::before{{content:"• ";color:var(--orange);font-weight:700}}
.example{{border:.4mm dashed #b6c1d1;border-radius:3.5mm;padding:3.5mm 4.5mm;font-size:9pt;background:#fff}}
.example .flag{{display:inline-block;background:var(--navy);color:#fff;font-size:7.6pt;font-weight:700;border-radius:2mm;padding:.3mm 2.2mm;margin-bottom:1.5mm}}
.example table{{width:100%;border-collapse:collapse}}
.example td{{padding:.9mm 0;border-bottom:.25mm solid var(--mist)}}
.example td:last-child{{text-align:left;color:var(--soft)}}
/* footer CTA */
.cta{{margin-top:auto;background:var(--navy);color:#fff;padding:7mm 14mm;display:flex;align-items:center;gap:7mm}}
.cta .qr{{background:#fff;padding:2.2mm;border-radius:2.5mm;width:30mm;height:30mm;flex:none}}
.cta .qr svg{{width:100%;height:100%;display:block}}
.cta h3{{font-size:15pt;line-height:1.3}}
.cta p{{color:#c9d5e6;font-size:9.6pt;margin-top:1mm}}
.cta .url{{font:600 9.6pt Inter;color:var(--yellow);margin-top:1.6mm;display:block;direction:ltr;unicode-bidi:isolate;text-align:right}}
.legal{{background:#011430;color:#8fa1bb;font-size:7.6pt;padding:2.6mm 14mm;display:flex;justify-content:space-between}}
.foot1{{margin-top:auto;padding:4mm 14mm;display:flex;justify-content:space-between;align-items:center;border-top:.3mm solid var(--line);font-size:8.6pt;color:var(--soft)}}
.foot1 b{{color:var(--navy)}}
.next{{display:flex;gap:3mm;margin-top:3mm}}
.next div{{flex:1;border:.3mm solid var(--line);border-radius:3mm;padding:2.8mm 3.6mm;font-size:8.9pt}}
.next b{{color:var(--navy)}}
"""

def ul(items, cls="ticks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def steps(items):
    out = '<ol class="steps">'
    for title, desc, who in items:
        cls = "who you" if who == "أنت" else "who"
        out += f'<li><b>{title}</b><p>{desc}</p><span class="{cls}">{who}</span></li>'
    return out + "</ol>"

COMMON_HONEST = [
    "ما نضمن ترتيب في قوقل ولا عدد زباين أو مبيعات",
    "ما نسوي تقييمات وهمية أبداً",
    "كل الحسابات باسمك وملكك، ونضاف كمدير بس",
    "ما نطلب كلمة مرور ولا رمز تحقق",
    "ما ينزل أي تعديل إلا بعد موافقتك",
    "مستقلين، ما نتبع قوقل ولا Meta",
]
PAYMENT = ("السعر وجدول الدفع مكتوبين في العرض قبل ما نبدأ. تلغي قبل البدء = ترجع فلوسك كاملة. "
           "بعد البدء = نرجع قيمة الجزء اللي ما تسلّم. رسوم الطرف الثالث (دومين، استضافة، Meta) ما ترجع. بدون ضريبة قيمة مضافة.")

def page(body_p1, body_p2, title):
    top = (f'<div class="top"><img src="{LOGO}" alt="LocalBoost"><span class="tag">سهل يلقونك. واضح. وجاهز لزبائنك.</span></div>')
    cta = (f'<div class="cta"><div class="qr">{qr_svg}</div><div><h3>اطلب فحص الخريطة المجاني</h3>'
           f'<p>امسح الكود: نشوف ملف محلك على خرائط قوقل ونقولك وش ينقصه بالضبط. ٥ دقايق، بدون أي التزام.</p>'
           f'<span class="url">{SITE_URL}</span></div></div>'
           f'<div class="legal"><span>LocalBoost · خدمة مستقلة في شمال الرياض: العارض · النرجس · الياسمين · طريق الملك سلمان</span>'
           f'<span>غير تابعين لقوقل أو Meta</span></div>')
    foot1 = '<div class="foot1"><span><b>LocalBoost</b> · العارض · النرجس · الياسمين · طريق الملك سلمان</span><span>قلب الصفحة ←</span></div>'
    return (f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f'<style>{CSS}</style></head><body>'
            f'<section class="page">{top}{body_p1}{foot1}</section>'
            f'<section class="page"><div style="height:8mm"></div>{body_p2}{cta}</section></body></html>')

def hero(eyebrow, name, en, promise, price, unit, launch=""):
    l = f'<div class="launch">{launch}</div>' if launch else ""
    return (f'<div class="hero"><div class="eyebrow">{eyebrow}</div><h1>{name}</h1><div class="en">{en}</div>'
            f'<p class="promise">{promise}</p><div class="price"><b class="lat">{price}</b><small>{unit}</small>{l}</div></div>')

def why(cards):
    return '<div class="cards">' + "".join(f'<div class="card"><b>{t}</b><p>{d}</p></div>' for t, d in cards) + "</div>"

# ------------------------------------------------------------------ 1. Get Found
gf_p1 = (hero("Package 1 · Get Found", "خلّهم يلقونك", "Get Found",
              "نجهّز ملف محلك على خرائط قوقل ونخليه كامل وواضح وسهل يتواصلون معك منه، عشان زبون الحي يلقاك قبل غيرك.",
              "900 SAR", "مرة وحدة", "سعر الإطلاق 750 لأول عميلين<br>نأكد لك توفره في الفحص")
         + '<div class="pad">'
         + '<div class="sec"><h2>لمين هذي الباقة؟</h2>'
         + why([("محلك ما يطلع زين", "التصنيف غلط أو الدبوس مو دقيق، فالزبون يلقى غيرك قبلك."),
                ("المعلومات ناقصة", "ساعات بدون رمضان والعيد، خدمات مو مكتوبة، وصور قليلة أو قديمة."),
                ("صعب يتواصلون معك", "ما فيه زر واتساب ولا رقم واضح، والتقييمات بدون رد.")])
         + '</div><div class="sec"><h2>وش تشمل الباقة</h2>'
         + ul(["ملف قوقل للأنشطة التجارية كامل: التصنيف الصحيح والدبوس",
               "ساعات العمل لكل يوم، ومعها رمضان والعيد إذا أرسلتها",
               "قائمة الخدمات أو المنيو بوصف واضح",
               "وصف للمحل بالعربي السعودي، واضح ومختصر",
               "ترتيب الصور: الواجهة، الداخل، الشغل، الفريق",
               "زر واتساب وزر اتصال على الملف",
               "رابط تقييم مباشر وكرت QR جاهز للطباعة",
               "مسودات ردود على التقييمات، ما تنزل إلا بموافقتك",
               "صور قبل وبعد للتعديلات",
               "شرح بسيط عند التسليم، وكل شي باسمك"])
         + '</div><div class="sec band"><h2>النتيجة اللي تستلمها</h2>'
         + '<p>ملف على الخريطة كامل ودقيق ومرتب، فيه كل اللي يحتاجه الزبون عشان يقرر ويتواصل معك: وين أنت، متى فاتح، وش تقدّم، وكيف يكلمك. '
           'ومعه كرت QR تحطه عند الكاشير عشان زبائنك الحقيقيين يقيّمونك بسهولة.</p></div>'
         + f'<div class="sec band"><h2>الدفع والإلغاء</h2><p style="font-size:9.4pt">{PAYMENT}</p></div>'
         + '<div class="next"><div><b>تبي موقع كمان؟</b><br>«خلّهم يختارونك»: كل هذا + موقع جوال بسيط، <span class="lat">2,200 SAR</span>.</div>'
           '<div><b>تبي متابعة شهرية؟</b><br>«خلّك محدّث» بعد التسليم، <span class="lat">299 SAR</span> شهرياً.</div></div></div>')
gf_p2 = ('<div class="pad"><div class="sec" style="margin-top:0"><h2>كيف نشتغل، من البداية للنهاية</h2>'
         + steps([("فحص مجاني ٥ دقايق", "ترسل رابط محلك على الخريطة، ونرد عليك بوش ينقصه بالضبط.", "إحنا"),
                  ("عرض مكتوب", "الباقة والسعر والمدة وجدول الدفع، واضحة قبل أي شغل.", "إحنا"),
                  ("تضيفنا كمدير", "من جوالك، بدون كلمة مرور. ونرسل لك الطريقة خطوة بخطوة.", "أنت"),
                  ("ترسل المعلومات والصور", "عبر نموذج بسيط: الساعات، الخدمات، الصور.", "أنت"),
                  ("نجهّز وأنت تراجع", "نرسل لك كل التعديلات والنصوص قبل النشر.", "إحنا"),
                  ("توافق، ننشر، ونسلّم", "ننشر بعد موافقتك، ونسلّمك كرت QR وصور قبل وبعد.", "إحنا")])
         + '<p style="font-size:9pt;color:var(--soft);margin-top:2.5mm">المدة: عادةً أيام قليلة، وتعتمد على سرعة إرسال الصور والمعلومات. تعديلات قوقل أحياناً تاخذ وقت لين تظهر.</p></div>'
         + '<div class="sec cols"><div><h2>وش نحتاج منك</h2>'
         + ul(["رابط محلك على خرائط قوقل", "إضافتنا كمدير على الملف (بدون كلمة مرور)", "ساعات العمل، ورمضان والعيد إن وجدت",
               "قائمة الخدمات أو المنيو والأسعار", "٥ إلى ١٠ صور: واجهة، داخل، شغل، فريق", "موافقتك على النصوص قبل النشر"], "ticks one")
         + '</div><div><h2>وش ما تشمل</h2>'
         + ul(["موقع إلكتروني (موجود في «خلّهم يختارونك»)", "إعلانات مدفوعة أو إدارة حسابات التواصل", "تصوير احترافي",
               "متابعة شهرية بعد التسليم (موجودة في «خلّك محدّث»)"], "ticks one no")
         + '</div></div>'
         + '<div class="sec honest"><h2>للأمانة</h2>' + ul(COMMON_HONEST, "") + '</div>'
         + '</div>')

# ------------------------------------------------------------------ 2. Get Chosen
gc_p1 = (hero("Package 2 · Get Chosen", "خلّهم يختارونك", "Get Chosen",
              "كل شغل «خلّهم يلقونك» + موقع بسيط للجوال باسمك، عشان الزبون يشوف محلك وخدماتك وأسعارك ويتواصل معك بضغطة.",
              "2,200 SAR", "مرة وحدة · الدومين والاستضافة بالتكلفة")
         + '<div class="pad">'
         + '<div class="sec"><h2>لمين هذي الباقة؟</h2>'
         + why([("تبي مكان واحد لكل شي", "رابط واحد تحطه في انستقرام والواتساب والكروت، فيه كل معلوماتك."),
                ("عندك منيو أو أسعار", "تبي الزبون يشوف الخدمات والأسعار قبل ما يسأل نفس السؤال كل مرة."),
                ("تبي شكل احترافي", "صفحة مرتبة بالعربي على الجوال تعطي انطباع أول قوي.")])
         + '</div><div class="sec"><h2>وش تشمل الباقة</h2>'
         + '<p style="font-weight:700;color:var(--navy);margin-bottom:2mm">١) كل شي في «خلّهم يلقونك»</p>'
         + ul(["ملف قوقل كامل: التصنيف، الدبوس، الخدمات", "الساعات ومعها رمضان والعيد", "وصف عربي واضح وترتيب الصور",
               "زر واتساب واتصال + كرت QR للتقييمات"])
         + '<p style="font-weight:700;color:var(--navy);margin:3.5mm 0 2mm">٢) موقع بسيط للجوال</p>'
         + ul(["حتى ٤ أقسام تقريباً: الرئيسية، من نحن، الخدمات، المنيو/الأسعار", "مصمم للجوال أولاً، وبالعربي أساساً",
               "ثنائي اللغة (عربي/إنجليزي) إذا اتفقنا عليه", "زر واتساب واتصال وخريطة الموقع داخل الصفحة",
               "صورك الحقيقية وشعارك وألوانك", "الدومين والاستضافة باسمك وبسعر التكلفة"])
         + '</div>'
         + f'<div class="sec band"><h2>الدفع والإلغاء</h2><p style="font-size:9.4pt">{PAYMENT}</p></div>'
         + '<div class="next"><div><b>تبي بس ملف الخريطة؟</b><br>«خلّهم يلقونك»، <span class="lat">900 SAR</span>.</div>'
           '<div><b>تبي متابعة شهرية؟</b><br>«خلّك محدّث» بعد التسليم، <span class="lat">299 SAR</span> شهرياً.</div></div></div>')
gc_p2 = ('<div class="pad"><div class="sec" style="margin-top:0"><h2>كيف نشتغل، من البداية للنهاية</h2>'
         + steps([("فحص مجاني ٥ دقايق", "نشوف ملفك على الخريطة ونفهم وش تحتاج.", "إحنا"),
                  ("عرض مكتوب", "الأقسام والسعر والمدة وجدول الدفع، قبل أي شغل.", "إحنا"),
                  ("المعلومات والدومين", "ترسل الشعار والصور والأسعار، وتختار اسم الدومين.", "أنت"),
                  ("نجهّز الملف والموقع", "نكمّل ملف قوقل ونبني الموقع على رابط معاينة.", "إحنا"),
                  ("تراجع وتعدّل", "تشوف الموقع من جوالك وترسل ملاحظاتك ضمن النطاق المكتوب.", "أنت"),
                  ("نطلق ونسلّم", "بعد موافقتك ننشر، ونسلّمك كل الحسابات باسمك مع شرح.", "إحنا")])
         + '<p style="font-size:9pt;color:var(--soft);margin-top:2.5mm">المدة: تعتمد على سرعة إرسال المعلومات والصور، ونكتبها لك في العرض. شراء الدومين والاستضافة يكون بموافقتك وباسمك.</p></div>'
         + '<div class="sec cols"><div><h2>وش نحتاج منك</h2>'
         + ul(["كل متطلبات «خلّهم يلقونك»", "الشعار والألوان (إن وجدت)", "المنيو أو قائمة الخدمات والأسعار",
               "نبذة عن المحل بكلامك", "صور المحل وشغلك", "اسم الدومين المفضل"], "ticks one")
         + '</div><div><h2>وش ما تشمل</h2>'
         + ul(["طلبات أو حجوزات أو دفع إلكتروني", "مدونة أو صفحات كثيرة", "صور جاهزة (ستوك) بدل صورك، إلا بموافقة",
               "تحديث المحتوى بعد التسليم (موجود في «خلّك محدّث»)"], "ticks one no")
         + '</div></div>'
         + '<div class="sec honest"><h2>للأمانة</h2>' + ul(COMMON_HONEST, "") + '</div>'
         + '</div>')

# ------------------------------------------------------------------ 3. Stay Current
sc_p1 = (hero("Add-on · Stay Current", "خلّك محدّث", "Stay Current",
              "متابعة شهرية لملفك على الخريطة بعد التسليم: نتأكد إنه سليم ومحدّث، ونجهّز ردود التقييمات، ونرسل لك تقرير واضح.",
              "299 SAR", "شهرياً · إضافة بعد باقة فقط")
         + '<div class="pad">'
         + '<div class="sec"><h2>لمين هذي الخدمة؟</h2>'
         + why([("ما عندك وقت", "تبي ملفك يبقى صحيح بدون ما تتابعه بنفسك كل شهر."),
                ("التقييمات تتراكم", "تبي ترد على زبائنك باحترام، بس ما تلقى وقت تكتب."),
                ("المعلومات تتغير", "ساعات رمضان، خدمة جديدة، صور جديدة… تبيها تنزل صح.")])
         + '</div><div class="sec"><h2>وش تشمل كل شهر</h2>'
         + ul(["فحص شهري لصحة الملف على الخريطة", "حتى تحديثين للمعلومات (ساعات، خدمات، صور)",
               "حتى ١٠ مسودات ردود على التقييمات، لموافقتك", "تقرير صفحة وحدة بالعربي آخر الشهر",
               "تنبيهك لو لاحظنا شي غلط في الملف", "كل التعديلات بعد موافقتك فقط"])
         + '<p style="margin-top:3mm;padding:2.5mm 4mm;background:#e8eef8;border-radius:2.5mm;font-size:9.4pt">'
           '<b style="color:var(--navy)">مهم:</b> «خلّك محدّث» إضافة، ما تنباع لحالها. تكون بعد «خلّهم يلقونك» أو «خلّهم يختارونك».</p></div>'
         + '<div class="sec"><h2>مثال على التقرير الشهري</h2><div class="example"><span class="flag">مثال توضيحي، مو عميل حقيقي</span>'
           '<table><tr><td>حالة الملف</td><td>سليم، بدون ملاحظات</td></tr>'
           '<tr><td>التحديثات</td><td>١ من ٢: إضافة ساعات رمضان</td></tr>'
           '<tr><td>ردود التقييمات</td><td>٤ مسودات، اعتمدت ٤</td></tr>'
           '<tr><td>أرقام قوقل</td><td>من لوحة تحكمك، أو «غير متوفر»</td></tr>'
           '<tr><td>اقتراح الشهر الجاي</td><td>إضافة صور المنيو الجديد</td></tr></table></div></div>'
         + '<div class="next"><div><b>ما عندك باقة؟</b><br>ابدأ بـ «خلّهم يلقونك»، <span class="lat">900 SAR</span>.</div>'
           '<div><b>تبي موقع كمان؟</b><br>«خلّهم يختارونك»، <span class="lat">2,200 SAR</span>.</div></div></div>')
sc_p2 = ('<div class="pad"><div class="sec" style="margin-top:0"><h2>كيف يمشي الشهر، من البداية للنهاية</h2>'
         + steps([("بداية الشهر: الفحص", "نراجع الملف: الساعات، الصور، الأزرار، المعلومات.", "إحنا"),
                  ("تنبيه إذا فيه شي", "لو لقينا شي غلط أو ناقص، نرسل لك قبل أي تعديل.", "إحنا"),
                  ("ترسل التحديثات", "ساعات جديدة، خدمة، صور… حتى تحديثين بالشهر.", "أنت"),
                  ("ردود التقييمات", "نجهّز حتى ١٠ مسودات وترسل لك للموافقة.", "إحنا"),
                  ("توافق وننشر", "ما ينزل شي على ملفك إلا بعد موافقتك.", "أنت"),
                  ("آخر الشهر: التقرير", "صفحة وحدة: وش سوينا، ووش نقترح للشهر الجاي.", "إحنا")])
         + '</div><div class="sec cols"><div><h2>وش يعتبر «تحديث»</h2>'
         + ul(["تغيير ساعات العمل أو ساعات المواسم", "إضافة أو تعديل خدمة أو سعر", "إضافة صور جديدة أو ترتيبها",
               "تصحيح معلومة (رقم، رابط، وصف)"], "ticks one")
         + '</div><div><h2>وش ما تشمل</h2>'
         + ul(["إعلانات مدفوعة أو إدارة حسابات التواصل", "صفحات أو أقسام جديدة في الموقع", "تصوير احترافي",
               "أكثر من تحديثين أو ١٠ ردود بالشهر"], "ticks one no")
         + '</div></div>'
         + '<div class="sec honest"><h2>للأمانة</h2>' + ul(COMMON_HONEST, "") + '</div>'
         + '<div class="sec band"><h2>الاشتراك والإيقاف</h2><p style="font-size:9.4pt">'
           '<span class="lat">299 SAR</span> شهرياً، بدون ضريبة قيمة مضافة. تقدر توقف الاشتراك قبل بداية الشهر الجاي. '
           'الأرقام في التقرير من لوحة تحكمك في قوقل فقط. ما نقدّر ولا نخترع أرقام.</p></div>'
         + '</div>')

for slug, p1, p2, title in [("01-get-found", gf_p1, gf_p2, "LocalBoost — خلّهم يلقونك"),
                            ("02-get-chosen", gc_p1, gc_p2, "LocalBoost — خلّهم يختارونك"),
                            ("03-stay-current", sc_p1, sc_p2, "LocalBoost — خلّك محدّث")]:
    (out / f"{slug}.html").write_text(page(p1, p2, title), encoding="utf-8")
print("built", sorted(p.name for p in out.glob("*.html")))
