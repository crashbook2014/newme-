// Renders a playbook HTML to PDF with page numbers.
// Usage: node render.js <dir> [basename]   (default basename: localboost-delivery-playbook)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]);
  const name = process.argv[3] || 'localboost-delivery-playbook';
  const ar = name.endsWith('-ar');
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(dir, name + '.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const fonts = await p.evaluate(() => [...new Set([...document.fonts].filter(x => x.status === 'loaded').map(x => x.family))]);
  const label = ar ? 'LocalBoost · دليل التسليم · داخلي' : 'LocalBoost · Delivery Playbook · internal';
  await p.pdf({
    path: path.join(dir, name + '.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: `<div dir="${ar ? 'rtl' : 'ltr'}" style="width:100%;font-size:7px;color:#7a879b;padding:0 15mm;display:flex;justify-content:space-between;font-family:Arial"><span>${label}</span><span dir="ltr"><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
  });
  console.log(name, 'fonts:', fonts.join('/'));
  await b.close();
})();
