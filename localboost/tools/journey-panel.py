# Generator for the animated "journey" panel already inserted in localboost/site (kept for reference/edits).
# It refuses to run twice (asserts id="journey" is absent).
"""Inserts the animated 'journey' panel (sign -> launch -> pass the alien -> moon) into both home pages."""
import sys
SITE = sys.argv[1]

def owner(arms_up=False):
    # Saudi shop owner: white thobe, red-and-white checked shemagh, black agal, short beard
    if arms_up:   # riding: one hand holds the rocket, the other waves
        arms = ('<path d="M-8 6 Q-14 12 -12 20" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
                '<path d="M-8 6 Q-14 12 -12 20" fill="none" stroke="#022754" stroke-width="1.2" stroke-linecap="round" opacity=".5"/>'
                '<g class="jwave"><path d="M8 5 Q15 -2 16 -11" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
                '<circle cx="16.5" cy="-13" r="2.8" fill="#E9B98B" stroke="#022754" stroke-width="1"/></g>')
    else:         # standing: pen hand toward the contract
        arms = ('<path d="M-8 6 Q-12 14 -10 20" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
                '<path d="M8 6 Q14 12 19 14" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
                '<circle cx="20" cy="14.5" r="2.6" fill="#E9B98B" stroke="#022754" stroke-width="1"/>'
                '<path d="M21 13 l6 -6" stroke="#022754" stroke-width="1.6" stroke-linecap="round"/>')
    return (f'{arms}'
            '<path d="M-10 3 Q0 -1 10 3 L12 32 Q0 35 -12 32 Z" fill="#fff" stroke="#022754" stroke-width="1.5"/>'
            '<path d="M0 4 V16" stroke="#022754" stroke-width=".8" opacity=".5"/>'
            '<path d="M-10 -9 Q0 -24 10 -9 L13 9 Q7 4 5 -2 L-5 -2 Q-7 4 -13 9 Z" fill="url(#shm)" stroke="#022754" stroke-width="1.3"/>'
            '<circle cx="0" cy="-5" r="6.2" fill="#E9B98B" stroke="#022754" stroke-width="1.2"/>'
            '<path d="M-5.6 -2.5 Q0 6 5.6 -2.5 Q3 3 0 3.2 Q-3 3 -5.6 -2.5Z" fill="#3a2a20"/>'
            '<circle cx="-2.2" cy="-6" r=".9" fill="#022754"/><circle cx="2.2" cy="-6" r=".9" fill="#022754"/>'
            '<path d="M-1.8 -2.6 Q0 -1.2 1.8 -2.6" fill="none" stroke="#fff" stroke-width=".9" stroke-linecap="round"/>'
            '<ellipse cx="0" cy="-13.5" rx="8.6" ry="2.6" fill="none" stroke="#141414" stroke-width="2.2"/>')

def stars():
    pts = [(40,30,1.2),(90,70,0.9),(150,25,1.4),(210,60,1),(260,20,1.1),(300,95,0.8),(350,40,1.3),(410,70,0.9),(450,18,1),
           (610,150,1.1),(580,230,0.9),(30,140,1),(120,120,0.8),(470,120,1),(250,140,0.9),(620,40,1.2),(395,15,0.8),(180,100,1)]
    return "".join(f'<circle class="tw" style="animation-delay:{(i*0.37)%3:.2f}s" cx="{x}" cy="{y}" r="{r}" fill="#fff"/>' for i,(x,y,r) in enumerate(pts))

def svg(lang):
    ar = lang == 'ar'
    bubble = 'وش ذا؟!' if ar else 'WHAT?!'
    flag = 'محلك' if ar else 'Your shop'
    shop = 'محلك' if ar else 'Your shop'
    label = ('رسمة متحركة: صاحب محل يوقّع مع LocalBoost، يركب الصاروخ ويعدّي فضائي متفاجئ، ويوصل للقمر والنجوم تلمع حوله.' if ar else
             'Animation: a shop owner signs with LocalBoost, rides the rocket past a surprised alien, and lands on the moon as the stars sparkle.')
    return f'''<svg class="jsvg" viewBox="0 0 640 320" role="img" aria-label="{label}" direction="ltr">
  <defs>
    <linearGradient id="jsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#010d1f"/><stop offset=".7" stop-color="#022754"/><stop offset="1" stop-color="#03306a"/></linearGradient>
    <radialGradient id="jsun" cx=".5" cy="1" r=".6"><stop offset="0" stop-color="#FFD332" stop-opacity=".9"/><stop offset=".25" stop-color="#F6880F" stop-opacity=".75"/><stop offset=".5" stop-color="#EA5C0A" stop-opacity=".35"/><stop offset="1" stop-color="#EA5C0A" stop-opacity="0"/></radialGradient>
    <radialGradient id="jmoon" cx=".35" cy=".32" r=".75"><stop offset="0" stop-color="#fffaf0"/><stop offset=".45" stop-color="#ffe9b8"/><stop offset=".8" stop-color="#f7c46f"/><stop offset="1" stop-color="#e7a248"/></radialGradient>
    <pattern id="shm" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="4" fill="#fff"/><path d="M0 0h2v2H0zM2 2h2v2H2z" fill="#d7262e" opacity=".9"/></pattern>
    <radialGradient id="jglow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFD332" stop-opacity=".45"/><stop offset="1" stop-color="#FFD332" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="640" height="320" fill="url(#jsky)"/>
  <ellipse cx="320" cy="330" rx="440" ry="110" fill="url(#jsun)"/>
  {stars()}

  <!-- the moon, with the dashed orbit ring -->
  <g transform="translate(540 118)">
    <circle r="92" fill="url(#jglow)" class="jglow"/>
    <circle r="46" fill="url(#jmoon)"/>
    <circle cx="-12" cy="10" r="8" fill="#c78634" opacity=".25"/><circle cx="16" cy="-14" r="5" fill="#c78634" opacity=".25"/><circle cx="14" cy="18" r="3.5" fill="#c78634" opacity=".22"/>
    <ellipse rx="76" ry="22" fill="none" stroke="#FFD332" stroke-width="2" stroke-dasharray="6 6" transform="rotate(-18)" opacity=".85"/>
    <!-- flag planted on arrival -->
    <g class="jflag"><path d="M26 -38 L26 -72" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/><path d="M26 -72 L76 -65 L26 -56 Z" fill="#EA5C0A"/>
      <text x="46" y="-61.5" font-size="8.5" font-weight="700" fill="#fff" text-anchor="middle" font-family="Readex Pro, IBM Plex Sans Arabic, sans-serif" direction="{'rtl' if ar else 'ltr'}">{flag}</text></g>
    <!-- sparkles -->
    <g class="jspark" fill="#FFD332">
      <path d="M-70 -50 l3 -9 3 9 9 3 -9 3 -3 9 -3 -9 -9 -3 z"/><path d="M62 -40 l2 -7 2 7 7 2 -7 2 -2 7 -2 -7 -7 -2 z"/>
      <path d="M-58 44 l2 -6 2 6 6 2 -6 2 -2 6 -2 -6 -6 -2 z"/><path d="M70 46 l2.5 -8 2.5 8 8 2.5 -8 2.5 -2.5 8 -2.5 -8 -8 -2.5 z"/>
    </g>
  </g>

  <!-- start: the little shop and the contract -->
  <g transform="translate(40 228)">
    <rect x="0" y="16" width="70" height="46" rx="4" fill="#fff"/>
    <path d="M-4 16 L74 16 L68 2 L2 2 Z" fill="#EA5C0A"/>
    <path d="M12 2 L10 16 M26 2 L25 16 M40 2 L40 16 M54 2 L55 16" stroke="#fff" stroke-width="5" opacity=".9"/>
    <rect x="22" y="34" width="26" height="28" rx="2" fill="#022754"/>
    <text x="35" y="28.5" font-size="8" font-weight="700" fill="#022754" text-anchor="middle" font-family="Readex Pro, IBM Plex Sans Arabic, sans-serif" direction="{'rtl' if ar else 'ltr'}">{shop}</text>
  </g>
  <g class="jowner" transform="translate(128 254) scale(1.25)">{owner()}</g>
  <g transform="translate(150 266)">
    <rect x="0" y="0" width="30" height="22" rx="2" fill="#fff" stroke="#022754" stroke-width="1.2" transform="rotate(-8)"/>
    <path class="jsign" d="M5 15 q4 -9 7 0 t7 -2 t6 1" fill="none" stroke="#EA5C0A" stroke-width="1.8" stroke-linecap="round" transform="rotate(-8)"/>
  </g>

  <!-- the alien in its saucer, with its coffee -->
  <g class="jalien" transform="translate(372 150)">
    <g class="jbob">
      <ellipse cx="0" cy="12" rx="34" ry="9" fill="#c9d3e1" stroke="#022754" stroke-width="1.4"/>
      <circle cx="-18" cy="13" r="2" fill="#FFD332"/><circle cx="0" cy="15" r="2" fill="#FFD332"/><circle cx="18" cy="13" r="2" fill="#FFD332"/>
      <path d="M-16 8 Q0 -26 16 8 Z" fill="#dfe8f5" opacity=".55" stroke="#022754" stroke-width="1"/>
      <g class="jhead">
        <path d="M-3 -12 L-7 -22 M3 -12 L7 -22" stroke="#022754" stroke-width="1.4"/><circle cx="-7" cy="-23" r="2.2" fill="#FFD332"/><circle cx="7" cy="-23" r="2.2" fill="#FFD332"/>
        <ellipse cx="0" cy="-3" rx="11" ry="10" fill="#a6e05c" stroke="#022754" stroke-width="1.4"/>
        <g class="jeyes"><circle cx="-4.5" cy="-5" r="3.4" fill="#fff" stroke="#022754" stroke-width="1"/><circle cx="4.5" cy="-5" r="3.4" fill="#fff" stroke="#022754" stroke-width="1"/>
          <circle cx="-3.6" cy="-5" r="1.6" fill="#022754"/><circle cx="5.4" cy="-5" r="1.6" fill="#022754"/></g>
        <path class="jsmile" d="M-3 2 Q0 4.5 3 2" fill="none" stroke="#022754" stroke-width="1.2" stroke-linecap="round"/>
        <ellipse class="jgasp" cx="0" cy="3" rx="2.4" ry="3" fill="#022754"/>
      </g>
      <g class="jcup"><path d="M13 1 h10 q-1 7 -5 7 q-4 0 -5 -7 z" fill="#fff" stroke="#022754" stroke-width="1"/><path d="M13.6 3 h8.8" stroke="#EA5C0A" stroke-width="1.3"/>
        <path class="jsteam" d="M17 -3 q-2 -3 0 -6 M20 -3 q2 -3 0 -6" fill="none" stroke="#fff" stroke-width="1" opacity=".7"/></g>
    </g>
    <g class="jbubble"><rect x="-58" y="-62" width="62" height="24" rx="10" fill="#fff"/><path d="M-20 -39 l6 9 l2 -10 z" fill="#fff"/>
      <text x="-27" y="-45.5" font-size="12" direction="{'rtl' if ar else 'ltr'}" font-weight="700" fill="#EA5C0A" text-anchor="middle" font-family="Readex Pro, IBM Plex Sans Arabic, sans-serif">{bubble}</text></g>
  </g>

  <!-- the ship: the real LocalBoost rocket + the owner riding it -->
  <g class="jship">
    <g class="jspeed"><path d="M-46 22 h-34 M-40 32 h-24 M-52 12 h-22" stroke="#FFD332" stroke-width="2.4" stroke-linecap="round" opacity=".8"/></g>
    <image href="{ 'assets/favicon.png' if ar else '../assets/favicon.png' }" x="-34" y="-34" width="68" height="68"/>
    <g class="jrider" transform="translate(-10 -30) scale(.88)">{owner(arms_up=True)}</g>
  </g>
</svg>'''

def section(lang):
    ar = lang == 'ar'
    t = (dict(j1='من التوقيع…', j2='لين القمر.', j3='رحلة قصيرة: توقّع معنا، تنطلق، تعدّي الكل… وتوصل والنجوم تلمع حولك.',
              s=['توقّع', 'تنطلق', 'تعدّي الكل', 'توصل وتلمع'], note='رسمة للمتعة، مو وعد. النتيجة الحقيقية تبدأ بالفحص المجاني.') if ar else
         dict(j1='From the signature…', j2='to the moon.', j3='A short trip: sign with us, take off, pass everyone… and land with the stars shining around you.',
              s=['Sign', 'Take off', 'Pass everyone', 'Land and shine'], note='Just for fun, not a promise. The real results start with the free check.'))
    nums = ['١', '٢', '٣', '٤'] if ar else ['1', '2', '3', '4']
    steps = "".join(f'<li class="js{i+1}"><b>{nums[i]}</b><span data-i="js{i+1}">{t["s"][i]}</span></li>' for i in range(4))
    return f'''
<!-- 3b · Journey (animated, just for fun) -->
<section class="block journey" id="journey" aria-labelledby="h2j">
  <div class="wrap">
    <div class="center"><h2 id="h2j"><span data-i="j1">{t['j1']}</span> <span data-i="j2">{t['j2']}</span></h2><p data-i="j3">{t['j3']}</p></div>
    <div class="jcard">
      {svg(lang)}
      <ol class="jsteps">{steps}</ol>
    </div>
    <p class="note" data-i="j8">{t['note']}</p>
  </div>
</section>
'''

for lang, f in [('ar', 'index.html'), ('en', 'en/index.html')]:
    s = open(f'{SITE}/{f}', encoding='utf-8').read()
    assert 'id="journey"' not in s, 'already inserted'
    anchor = '\n<!-- 4 · Packages -->'
    assert s.count(anchor) == 1, f
    s = s.replace(anchor, section(lang) + anchor)
    open(f'{SITE}/{f}', 'w', encoding='utf-8').write(s)

css = r'''

/* ===== v2026-11-09 · Journey panel (sign → launch → pass the alien → moon) · 12s loop ===== */
.journey{padding-block:72px}
.jcard{max-width:860px;margin:0 auto;border-radius:24px;overflow:hidden;background:#010d1f;box-shadow:0 24px 60px rgba(2,39,84,.22)}
.jsvg{display:block;width:100%;height:auto}
.jsvg *{transform-box:fill-box}
.jsteps{list-style:none;margin:0;padding:12px 14px 16px;display:grid;grid-template-columns:repeat(4,1fr);gap:8px;background:#022754}
.jsteps li{display:flex;align-items:center;justify-content:center;gap:8px;padding:8px 6px;border-radius:999px;color:#9fb0c7;font-weight:600;font-size:14px;background:rgba(255,255,255,.05);transition:none}
.jsteps b{width:24px;height:24px;border-radius:50%;display:grid;place-items:center;background:rgba(255,255,255,.12);color:#fff;font-size:12px;flex:none}
/* final (static) state = what reduced-motion users see */
.jsteps .js4{background:rgba(234,92,10,.18);color:#fff}.jsteps .js4 b{background:#EA5C0A}
.jship{transform:translate(522px,62px)}
.jowner{opacity:0}.jsign{stroke-dasharray:60;stroke-dashoffset:0}
.jgasp,.jbubble{opacity:0}
.jflag,.jspark{opacity:1}
.jspeed{opacity:0}
@media (prefers-reduced-motion:no-preference){
  .jship{animation:jship 12s ease-in-out infinite}
  .jowner{animation:jowner 12s linear infinite}
  .jrider{animation:jrider 12s linear infinite}
  .jsign{animation:jsign 12s ease-out infinite}
  .jspeed{animation:jspeed 12s linear infinite}
  .jbob{animation:jbob 2.4s ease-in-out infinite}
  .jwave{animation:jwave .9s ease-in-out infinite;transform-origin:left bottom}
  .jalien{animation:jalienspin 12s ease-in-out infinite;transform-origin:center}
  .jeyes{animation:jeyes 12s ease-in-out infinite;transform-origin:center}
  .jsmile{animation:jsmile 12s linear infinite}
  .jgasp{animation:jgasp 12s linear infinite}
  .jcup{animation:jcup 12s ease-in infinite;transform-origin:center}
  .jsteam{animation:jsteam 1.6s ease-in-out infinite}
  .jbubble{animation:jbubble 12s ease-out infinite;transform-origin:center bottom}
  .jflag{animation:jflag 12s ease-out infinite;transform-origin:left bottom}
  .jspark{animation:jspark 12s ease-out infinite;transform-origin:center}
  .jglow{animation:jglow 12s ease-in-out infinite;transform-origin:center}
  .tw{animation:tw 3s ease-in-out infinite}
  .jsteps li{animation:jstepoff 12s linear infinite}
  .jsteps .js1{animation-name:js1}.jsteps .js2{animation-name:js2}.jsteps .js3{animation-name:js3}.jsteps .js4{animation-name:js4}
}
@keyframes jship{
  0%,13%{transform:translate(168px,262px) rotate(0)}
  12.5%{transform:translate(168px,260px) rotate(-3deg)}
  28%{transform:translate(260px,205px)}
  42%{transform:translate(372px,148px)}
  56%{transform:translate(462px,96px)}
  66%,92%{transform:translate(522px,62px)}
  97%{transform:translate(522px,62px);opacity:1}
  99%{opacity:0}100%{transform:translate(168px,262px);opacity:0}
}
@keyframes jowner{0%,11%{opacity:1}12.5%,98%{opacity:0}100%{opacity:1}}
@keyframes jrider{0%,11%{opacity:0}12.5%,97%{opacity:1}99%,100%{opacity:0}}
@keyframes jsign{0%,2%{stroke-dashoffset:60}10%,96%{stroke-dashoffset:0}100%{stroke-dashoffset:60}}
@keyframes jspeed{0%,13%{opacity:0}16%,60%{opacity:1}66%,100%{opacity:0}}
@keyframes jwave{0%,100%{transform:rotate(0)}50%{transform:rotate(-18deg)}}
@keyframes jbob{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
@keyframes jalienspin{0%,40%{transform:translate(372px,150px) rotate(0)}45%{transform:translate(372px,150px) rotate(-26deg)}52%{transform:translate(372px,150px) rotate(14deg)}58%,100%{transform:translate(372px,150px) rotate(0)}}
@keyframes jeyes{0%,40%{transform:scale(1)}44%,62%{transform:scale(1.45)}70%,100%{transform:scale(1)}}
@keyframes jsmile{0%,40%{opacity:1}41%,66%{opacity:0}70%,100%{opacity:1}}
@keyframes jgasp{0%,40%{opacity:0}41%,66%{opacity:1}70%,100%{opacity:0}}
@keyframes jcup{0%,41%{transform:translate(0,0) rotate(0);opacity:1}55%{transform:translate(26px,-38px) rotate(220deg);opacity:1}64%{transform:translate(40px,-10px) rotate(400deg);opacity:0}96%{opacity:0;transform:translate(0,0)}100%{opacity:1}}
@keyframes jsteam{0%,100%{opacity:.2}50%{opacity:.8}}
@keyframes jbubble{0%,43%{opacity:0;transform:scale(.4)}47%{opacity:1;transform:scale(1.08)}50%,64%{opacity:1;transform:scale(1)}68%,100%{opacity:0;transform:scale(.8)}}
@keyframes jflag{0%,68%{opacity:0;transform:scale(0)}73%{opacity:1;transform:scale(1.15)}76%,96%{opacity:1;transform:scale(1)}99%,100%{opacity:0}}
@keyframes jspark{0%,70%{opacity:0;transform:scale(.3) rotate(0)}76%{opacity:1;transform:scale(1.15) rotate(20deg)}84%{transform:scale(.9) rotate(35deg)}92%{opacity:1;transform:scale(1.05) rotate(45deg)}99%,100%{opacity:0}}
@keyframes jglow{0%,66%{opacity:.5;transform:scale(1)}76%,94%{opacity:1;transform:scale(1.25)}100%{opacity:.5;transform:scale(1)}}
@keyframes tw{0%,100%{opacity:.35}50%{opacity:1}}
@keyframes js1{0%,13%{background:rgba(234,92,10,.18);color:#fff}14%,100%{background:rgba(255,255,255,.05);color:#9fb0c7}}
@keyframes js2{0%,13%{background:rgba(255,255,255,.05);color:#9fb0c7}14%,40%{background:rgba(234,92,10,.18);color:#fff}41%,100%{background:rgba(255,255,255,.05);color:#9fb0c7}}
@keyframes js3{0%,40%{background:rgba(255,255,255,.05);color:#9fb0c7}41%,64%{background:rgba(234,92,10,.18);color:#fff}65%,100%{background:rgba(255,255,255,.05);color:#9fb0c7}}
@keyframes js4{0%,64%{background:rgba(255,255,255,.05);color:#9fb0c7}65%,100%{background:rgba(234,92,10,.18);color:#fff}}
@media (max-width:860px){.journey{padding-block:56px}.jsteps{grid-template-columns:1fr 1fr}.jsteps li{font-size:13px}}
'''
open(f'{SITE}/assets/css/home.css', 'a', encoding='utf-8').write(css)
print('inserted')
