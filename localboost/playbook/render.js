// Renders the playbook HTML to PDF with page numbers.  Usage: node render.js <dir>
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(dir, 'localboost-delivery-playbook.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const fonts = await p.evaluate(() => [...new Set([...document.fonts].filter(x => x.status === 'loaded').map(x => x.family))]);
  await p.pdf({
    path: path.join(dir, 'localboost-delivery-playbook.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-size:7px;color:#7a879b;padding:0 15mm;display:flex;justify-content:space-between;font-family:Arial"><span>LocalBoost · Delivery Playbook · internal</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
  });
  console.log('fonts:', fonts.join('/'));
  await b.close();
})();
