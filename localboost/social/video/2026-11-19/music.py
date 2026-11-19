#!/usr/bin/env python3
"""Synthesises the 60 s soundtrack for the LocalBoost ad: warm pad, oud-like plucks,
light darbuka and sound effects timed to ad.html. Writes audio.wav next to this file."""
import numpy as np, wave, os
SR = 44100; DUR = 60.0; N = int(SR * DUR)
out = np.zeros(N)
rng = np.random.default_rng(7)
def t_(d): return np.arange(int(SR * d)) / SR
def add(sig, at, gain=1.0):
    i = int(at * SR); j = min(N, i + len(sig))
    if j > i: out[i:j] += sig[:j - i] * gain
def hz(m): return 440.0 * 2 ** ((m - 69) / 12)
def lowpass(x, a):
    y = np.empty_like(x); acc = 0.0
    for i, v in enumerate(x): acc += a * (v - acc); y[i] = acc
    return y

# ---- pad (chords every 4 s) ----
dark = [[50, 53, 57], [46, 50, 53], [48, 52, 55], [45, 49, 52]]      # Dm Bb C A
bright = [[53, 57, 60], [48, 52, 55], [50, 53, 57], [46, 50, 53]]    # F C Dm Bb
for k in range(15):
    start = k * 4.0
    chord = (dark if start < 30 else bright)[k % 4]
    if start >= 54: chord = [50, 53, 57, 62]
    d = 4.6; tt = t_(d)
    env = np.minimum(1, tt / 0.8) * np.minimum(1, (d - tt) / 0.8)
    s = np.zeros(len(tt))
    for m in chord:
        f = hz(m)
        for det in (-0.12, 0.12):
            s += np.sin(2 * np.pi * f * (1 + det / 100) * tt) * 0.5 + 0.18 * np.sin(2 * np.pi * 2 * f * tt)
    s += 0.6 * np.sin(2 * np.pi * hz(chord[0] - 12) * tt)            # bass
    add(s * env, start, 0.045 if start < 6 else 0.05)

# ---- oud-like plucks (Karplus-Strong), D hijaz motif ----
def pluck(f, d=1.2):
    n = int(SR * d); p = int(SR / f)
    buf = rng.uniform(-1, 1, p); y = np.empty(n)
    for i in range(n):
        y[i] = buf[i % p]; buf[i % p] = 0.5 * (buf[i % p] + buf[(i + 1) % p]) * 0.994
    return y * np.exp(-t_(d)[:n] * 2.2)
motif = [(62, 0), (63, .45), (66, .9), (67, 1.35), (69, 1.8), (67, 2.6), (66, 3.0), (62, 3.6)]
for base in (0.6, 46.4, 50.4):
    for m, dt in motif: add(pluck(hz(m)), base + dt, 0.22)
for m, dt in [(69, 0), (67, .4), (69, .8), (74, 1.3)]:
    add(pluck(hz(m)), 30.2 + dt, 0.24)

# ---- darbuka (maqsum-like, 100 bpm) ----
def doum():
    tt = t_(0.35); return np.sin(2 * np.pi * (90 * np.exp(-tt * 6) + 60) * tt) * np.exp(-tt * 9)
def tak():
    tt = t_(0.08); n = rng.uniform(-1, 1, len(tt)); n = n - lowpass(n, 0.3)
    return n * np.exp(-tt * 60) + 0.4 * np.sin(2 * np.pi * 700 * tt) * np.exp(-tt * 50)
beat = 60 / 100 / 2
pattern = ['D', 'T', '', 'T', 'D', '', 'T', '']
t0 = 6.0
while t0 < 54:
    for i, h in enumerate(pattern):
        at = t0 + i * beat
        if at >= 54: break
        g = 0.18 if at < 20 else 0.28 if at < 30 else 0.34
        if 38 <= at < 46: g = 0.26
        if h == 'D': add(doum(), at, g * 1.4)
        elif h == 'T': add(tak(), at, g * 0.55)
    t0 += 8 * beat

# ---- sound effects ----
def whoosh(d, up=True):
    tt = t_(d); n = rng.uniform(-1, 1, len(tt))
    a = (0.02 + 0.25 * (tt / d if up else 1 - tt / d))
    y = np.zeros_like(n); acc = 0.0
    for i in range(len(n)): acc += a[i] * (n[i] - acc); y[i] = acc
    return y * np.sin(np.pi * tt / d) ** 2 * 3
def bell(f, d=1.4):
    tt = t_(d); return (np.sin(2 * np.pi * f * tt) + 0.5 * np.sin(2 * np.pi * f * 2.76 * tt) + 0.25 * np.sin(2 * np.pi * f * 5.4 * tt)) * np.exp(-tt * 4)
def thump():
    tt = t_(0.4); return np.sin(2 * np.pi * (70 * np.exp(-tt * 8) + 40) * tt) * np.exp(-tt * 10)
def click():
    tt = t_(0.05); return rng.uniform(-1, 1, len(tt)) * np.exp(-tt * 120)
add(whoosh(3.6), 0.4, 0.5); add(whoosh(1.8), 20.0, 0.5); add(thump(), 21.6, 0.7)
add(click(), 23.0, 0.5); add(click(), 23.07, 0.4)
for at in (22.8, 24.4, 26.0, 27.4, 27.65, 27.9): add(bell(1568, .5), at, 0.12)
add(thump(), 28.35, 0.5)
add(bell(1319), 30.2, 0.25); add(bell(1976), 30.35, 0.15)
add(whoosh(2.0, False), 31.0, 0.4)
add(bell(1760, 1.6), 35.4, 0.2); add(bell(2217, 1.6), 35.55, 0.16)
for k, f in enumerate([2093, 2349, 2637, 3136, 3520]): add(bell(f, .4), 41.5 + k * .06, 0.07)
for k, at in enumerate((43.2, 44.0, 44.8)): add(bell(1319 * (1 + k * .12), .8), at, 0.16)
for k in range(18): add(bell(rng.choice([1319, 1568, 1760, 1976]), .6), 46.4 + k * 0.36 + rng.uniform(0, .1), 0.05)
add(whoosh(2.4), 53.4, 0.35)
for m in (62, 66, 69, 74): add(pluck(hz(m), 2.5), 54.6, 0.2)

# ---- master ----
fade = np.ones(N); fi = int(.5 * SR); fo = int(1.8 * SR)
fade[:fi] = np.linspace(0, 1, fi); fade[-fo:] = np.linspace(1, 0, fo)
out *= fade
out /= np.max(np.abs(out)) / 0.89
st = np.stack([out, out], axis=1)
# light stereo width: delay the right channel a little
st[:, 1] = np.concatenate([np.zeros(220), out[:-220]])
pcm = (st * 32767).astype(np.int16)
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio.wav')
with wave.open(p, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('wrote', p)
