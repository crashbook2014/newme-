// LocalBoost — rocket follows the path as the launch section scrolls. Page works without it.
(function(){
  // Launch: rocket follows the path as the section scrolls
  const sec=document.getElementById('launch'), path=document.getElementById('path'),
        rocket=document.getElementById('rocket'), rot=document.getElementById('rocketRot'),
        steps=[...document.querySelectorAll('.steps .step')], L=path.getTotalLength();
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function place(p){
    const a=path.getPointAtLength(L*p), b=path.getPointAtLength(Math.min(L,L*p+2));
    const ang=Math.atan2(b.y-a.y,b.x-a.x)*180/Math.PI+90;
    rocket.setAttribute('transform',`translate(${a.x} ${a.y})`); rot.setAttribute('transform',`rotate(${ang})`);
    steps.forEach(s=>s.classList.toggle('on',p>=+s.dataset.at-.08));
  }
  function track(){
    if(reduce){place(1);return}
    const r=sec.getBoundingClientRect(), span=Math.max(1,r.height-innerHeight);
    let p=Math.min(1,Math.max(0,(-r.top+innerHeight*.35)/span));
    if(innerWidth<=860){ p=Math.min(1,Math.max(0,(innerHeight-r.top)/(innerHeight+r.height*.6))); }
    place(p);
  }
  addEventListener('scroll',()=>requestAnimationFrame(track),{passive:true}); addEventListener('resize',track); track();
})();
