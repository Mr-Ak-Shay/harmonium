# 🎵 harmonium

A web-based harmonium that works on **any computer** — use your mouse or trackpad as the bellows. No installs, no special hardware. Just open and play.

> Forked from [gajraj-m/iharmonium](https://github.com/gajraj-m/iharmonium) — original used a MacBook lid angle sensor. This version works on **every computer** using mouse/trackpad movement.

---

## ▶️ How to Play

### Step 1 — Start the backend
```bash
pip install websockets
python harmonium.py
```

### Step 2 — Open the HTML
```bash
open harmonium.html
```

### Step 3 — Play!
1. **Click** anywhere on the page to activate audio
2. **Hold a key** to select a note
3. **Move your mouse UP** to pump the bellows and make sound

---

## 🎹 Key Mapping

```
White Keys:        Black Keys:
A = C              W = C#
S = D              E = D#
D = E              T = F#
F = F              Y = G#
G = G              U = A#
H = A
J = B
K = C (octave)
```

---

## 🔧 How It Works

- **Keys** — Press keyboard keys to select notes
- **Bellows** — Move your mouse toward the top of the screen to pump air
- **Air Decay** — Air slowly leaks out just like a real harmonium
- **WebSocket** — Python backend bridges mouse position to the HTML interface
- **Sound** — Web Audio API generates harmonium-like tones

---

## 💻 Requirements

- Python 3.7+
- `websockets` library (`pip install websockets`)
- Any modern browser (Chrome, Safari, Firefox)
- Any computer with a mouse or trackpad — **Mac, Windows, Linux all work**

---

## 🎶 Tips

- Move mouse **slowly upward** for smooth sustained notes
- **Flick up fast** for a loud attack that fades out
- Hold **A + D + G** together for a C major chord
- Hold **A + D + G + J** for a full rich chord with octave

---

## 🙌 Credits

Original concept and code by [gajraj-m](https://github.com/gajraj-m).  
Trackpad/mouse bellows adaptation by [Mr-Ak-Shay](https://github.com/Mr-Ak-Shay).
