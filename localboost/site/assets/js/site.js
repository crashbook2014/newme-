// LocalBoost — mobile menu + package picker. The page works without this script.
(function () {
  var btn = document.querySelector('.menu-btn');
  var links = document.getElementById('nav-links');
  if (btn && links) {
    btn.addEventListener('click', function () {
      var open = links.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { links.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  var picker = document.getElementById('picker');
  if (!picker) return;
  var out = document.getElementById('picker-out');
  var msgs = JSON.parse(picker.getAttribute('data-msgs'));
  function update() {
    var site = picker.querySelector('input[name="site"]:checked');
    var monthly = picker.querySelector('input[name="monthly"]').checked;
    if (!site) { out.textContent = msgs.pick; return; }
    var text = site.value === 'yes' ? msgs.chosen : msgs.found;
    if (monthly) text += ' ' + msgs.current;
    out.textContent = text;
  }
  picker.addEventListener('change', update);
  update();
})();
