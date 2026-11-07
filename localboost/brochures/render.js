// Renders every *.html in <dir> to an A4 PDF next to it.  Usage: node render.js <dir>
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]);
  const b = await chromium.launch();
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html'))) {
    const p = await b.newPage();
    await p.goto('file://' + path.join(dir, f), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    // fail loudly if any page's content overflows its A4 sheet
    const over = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg, i) => {
      const last = [...pg.children].pop(); return last.getBoundingClientRect().bottom - pg.getBoundingClientRect().bottom > 0.5 ? i + 1 : 0; }).filter(Boolean));
    const fonts = await p.evaluate(() => [...new Set([...document.fonts].filter(x => x.status === 'loaded').map(x => x.family))]);
    await p.pdf({ path: path.join(dir, f.replace('.html', '.pdf')), preferCSSPageSize: true, printBackground: true });
    console.log(f, 'fonts:', fonts.join('/'), over.length ? 'OVERFLOW on page ' + over : 'fits');
    await p.close();
  }
  await b.close();
})();
