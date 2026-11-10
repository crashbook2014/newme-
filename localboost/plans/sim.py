import random, statistics as st, json
random.seed(7)
DAYS=15; N=20000
def run(plan):
    deals=[]  # (close_day, type)
    warm_rate=random.betavariate(4,22)          # your data: 3 warm / 24
    to_call=random.uniform(.25,.55)
    close=random.uniform(.10,.35)
    # existing 3 warm leads
    for _ in range(3):
        if random.random()<to_call and random.random()<close: deals.append(random.randint(2,6))
    for d in range(DAYS):
        for _ in range(plan['wa'][d]):
            if random.random()<warm_rate and random.random()<to_call and random.random()<close:
                deals.append(d+random.randint(3,7))
    for d in plan['walk_days']:
        for _ in range(5):
            if random.random()<random.uniform(.15,.30) and random.random()<close*1.2:
                deals.append(d+random.randint(2,5))
    if plan['network']:
        for _ in range(20):
            if random.random()<random.uniform(.20,.35) and random.random()<min(.9,close*1.5):
                deals.append(random.randint(2,10))
    deals=sorted(x for x in deals if x<DAYS)
    hours=0; signed=0; cash=0; n750=0; out=[]
    sc_share=plan['sc']
    for day in deals:
        r=random.random()
        if r<sc_share: t,price,h,deliv='SC',3300,11,7
        elif r<sc_share+.15: t,price,h,deliv='GC',2200,14,10
        else:
            t,h,deliv='GF',6,5
            price=750 if n750<2 else 900
            if price==750: n750+=1
        if hours+h>plan['cap']: continue   # no capacity left
        hours+=h; signed+=price; cash+=price/2
        if day+deliv<DAYS: cash+=price/2
        out.append(t)
    return signed,cash,len(out),out.count('SC')
plans={
 'WhatsApp only (Saad 20/day)':dict(wa=[20]*DAYS,walk_days=[],network=False,sc=.15,cap=60),
 'Recommended mix (WA + walk-ins + network, Shop Check focus)':dict(wa=[17]*DAYS,walk_days=[3,4,8,9],network=True,sc=.35,cap=60),
 'Recommended mix, more founder hours (80h)':dict(wa=[17]*DAYS,walk_days=[3,4,8,9,13,14],network=True,sc=.35,cap=80),
}
res={}
for k,p in plans.items():
    R=[run(p) for _ in range(N)]
    s=sorted(r[0] for r in R); c=sorted(r[1] for r in R); n=[r[2] for r in R]
    q=lambda a,x:a[int(x*len(a))]
    res[k]=dict(p10=q(s,.1),p50=q(s,.5),p90=q(s,.9),cash50=q(c,.5),
      hit_signed=sum(x>=10000 for x in s)/N, hit_cash=sum(x>=10000 for x in c)/N,
      hit_6500=sum(x>=6500 for x in c)/N, deals50=st.median(n), zero=sum(x==0 for x in s)/N,
      hist=[sum(1 for x in s if lo<=x<lo+2000)/N for lo in range(0,20000,2000)])
    print(k, {a:(round(b,2) if isinstance(b,float) else b) for a,b in res[k].items() if a!='hist'})
json.dump(res,open('sim.json','w'))
