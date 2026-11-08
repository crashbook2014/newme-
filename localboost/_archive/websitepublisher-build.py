# Builds WebsitePublisher versions of localboost/site pages (CDN asset URLs, /en/index.html links, Optimizer tags).
# Usage: python3 localboost/tools/websitepublisher-build.py localboost/site <output-dir>
# Project 27483 -> https://project27483.websitepublisher.ai ; assets at https://cdn.websitepublisher.ai/custom/wid27483/
import re, sys, posixpath
def load(site, f):
    # site pages use relative paths; turn them back into root-relative ones for WebsitePublisher
    h=open(f'{site}/{f}',encoding='utf-8').read()
    d=posixpath.dirname('/'+f)
    def fix(m):
        url=m.group(2)
        if re.match(r'^(https?:|#|data:|mailto:|tel:)',url): return m.group(0)
        path,_,frag=url.partition('#')
        a=posixpath.normpath(posixpath.join(d,path)) if path else '/'+f
        if path.endswith('/') or path in ('.','./','..'): a=a.rstrip('/')+'/'
        return m.group(1)+a+('#'+frag if frag else '')+'"'
    return re.sub(r'((?:href|src)=")([^"]*)"',fix,h).replace('https://crashbook2014.github.io/newme-','https://localboost-zeto.netlify.app')
SITE, OUT = sys.argv[1], sys.argv[2]
CDN='https://cdn.websitepublisher.ai/custom/wid27483'
NEW='https://project27483.websitepublisher.ai'
OLD='https://localboost-zeto.netlify.app'
OPT_HEAD='<!-- Optimizer - Canonical -->\n<!-- Optimizer - Custom Meta -->\n<!-- Optimizer - Open Graph -->\n<!-- Optimizer - Header Javascripts -->\n</head>'
def common(h):
    h=h.replace(OLD+'/assets/og-image.png',CDN+'/img/og-image.png').replace(OLD+'/assets/logo-large.png',CDN+'/img/logo-large.png')
    h=h.replace(OLD+'/en/"',NEW+'/en/index.html"').replace(OLD+'/',NEW+'/')
    h=h.replace('/assets/css/home.css',CDN+'/css/home.css').replace('/assets/js/home.js',CDN+'/js/home.js')
    h=h.replace('/assets/logo.png',CDN+'/img/logo.png').replace('/assets/favicon.png',CDN+'/img/favicon.png').replace('/assets/fonts/',CDN+'/fonts/')
    h=re.sub(r'href="/en/(#[a-z]*)?"',lambda m:'href="/en/index.html'+(m.group(1) or '')+'"',h)
    h=re.sub(r'<link rel="canonical"[^>]*>\n','',h); h=re.sub(r'<meta property="og:url"[^>]*>\n','',h)
    h=h.replace('</head>',OPT_HEAD,1).replace('</body>','<!-- Optimizer - Footer Javascripts -->\n</body>',1)
    assert '/assets/' not in h and 'netlify' not in h, [l for l in h.splitlines() if '/assets/' in l or 'netlify' in l][:3]
    return h
for src,dst in [('index.html','index.html'),('en/index.html','en-index.html')]:
    open(f'{OUT}/{dst}','w').write(common(load(SITE,src)))

# policies pages rebuilt with the home header/footer
home={'ar':load(SITE,'index.html'),'en':load(SITE,'en/index.html')}
DOCCSS='''<style>
.doc{max-width:780px;margin:0 auto;padding-block:64px}
.doc h1{font-size:clamp(32px,4vw,44px);color:var(--navy);margin-bottom:12px}
.doc h2{font-size:22px;color:var(--navy);margin:32px 0 8px}
.doc ul{padding-inline-start:1.2em;margin:0}.doc li{margin-bottom:6px}
.ph{display:inline-block;border:2px dashed var(--amber);background:#FFF6E5;color:#7A3A00;border-radius:8px;padding:0 .5em;font-weight:600}
</style>
'''
for lang,src,dst,title,desc in [('ar','policies.html','policies.html','السياسات | LocalBoost','سياسات LocalBoost: الفحص المجاني، العرض والدفع، الإلغاء والاسترجاع، رسوم الطرف الثالث، وملكية الحسابات.'),
                                 ('en','en/policies.html','en-policies.html','Policies | LocalBoost','LocalBoost policies: free audit, proposals and payment, cancellations and refunds, third-party fees, and account ownership.')]:
    p=load(SITE,src); h=home[lang]
    main=p[p.index('<main'):p.index('</main>')+7]
    main=main.replace('<main id="main" class="section">','<main id="main">').replace('<div class="wrap doc">','<div class="wrap doc">',1)
    header=h[h.index('<header>'):h.index('</header>')+9]
    footer=h[h.index('<footer>'):h.index('</footer>')+9]
    # header: nav links point back to the home page sections
    homeurl='/' if lang=='ar' else '/en/index.html'
    header=re.sub(r'href="#([a-z]+)"',lambda m:f'href="{homeurl}#{m.group(1)}"',header)
    other='/en/policies.html' if lang=='ar' else '/policies.html'
    header=re.sub(r'<a class="lang" href="[^"]*"',f'<a class="lang" href="{other}"',header)
    footer=re.sub(r'(<a href=")[^"]*(" hreflang="[a-z]+" lang="[a-z]+" data-i="langf">)',lambda m:m.group(1)+other+m.group(2),footer)
    head=h[:h.index('<body>')]
    head=re.sub(r'<title>[^<]*</title>',f'<title>{title}</title>',head)
    head=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',head)
    head=re.sub(r'<meta property="og:(title|description)" content="[^"]*">\n','',head)
    head=re.sub(r'<link rel="alternate" hreflang="(ar|en|x-default)" href="[^"]*">\n','',head)
    head=re.sub(r'<link rel="preload"[^>]*>\n','',head)
    head=re.sub(r'<script type="application/ld\+json">.*?</script>\n','',head,flags=re.S)
    head=head.replace('</head>',f'<link rel="alternate" hreflang="ar" href="{OLD}/policies.html">\n<link rel="alternate" hreflang="en" href="{OLD}/en/policies.html">\n'+DOCCSS+'</head>')
    page=head+'<body>\n<a class="skip" href="#main">'+('تخطَّ إلى المحتوى' if lang=='ar' else 'Skip to content')+'</a>\n'+header+'\n'+main+'\n'+footer+'\n</body>\n</html>\n'
    open(f'{OUT}/{dst}','w').write(common(page))
print('built')
