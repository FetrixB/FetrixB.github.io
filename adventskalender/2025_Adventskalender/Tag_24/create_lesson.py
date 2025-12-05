#!/usr/bin/env python3
"""
Erstellt die Lesson.ipynb für Tag 24 – Deployment & Intro-Screen.
"""

import nbformat as nbf
import sys
from pathlib import Path


def create_lesson():
    nb = nbf.v4.new_notebook()

    cell1 = nbf.v4.new_markdown_cell("""# 📚 Tag 24 – Portal-Launch im Minecraft-Weihnachtsreich

Der Bürgermeister, die Eishexe und sogar der lächelnde Schneemann stehen im Halbkreis vor dem Portal. Alle warten nur auf dich! Heute wird das komplette Minecraft-Weihnachtsreich öffentlich gemacht und du bringst es mit einem cineastischen Intro-Screen auf GitHub Pages online. Das ist das Finale – nach 23 Tagen Training bist du jetzt derjenige, der den Hebel umlegt.
""")
    nb.cells.append(cell1)

    cell2 = nbf.v4.new_markdown_cell("""## 🎯 Deployment & Accessibility – Deine Bühne für die Welt

Damit Besucher vom ersten Pixel an staunen, brauchst du drei Dinge:

1. **GitHub Pages Deployment** – damit jeder weltweit die Seite sehen kann.
2. **Accessibility** – Screenreader, Tastaturnavigation und hoher Kontrast müssen passen, damit niemand ausgeschlossen wird.
3. **Intro-Screen mit GSAP** – die große Eröffnung fühlt sich wie eine Minecraft-Cutscene an.

Genau das passiert in `Tag_24/Loesung/`. Schau dir den fertigen Ablauf an und übertrage ihn Schritt für Schritt in deine eigene Umsetzung.
""")
    nb.cells.append(cell2)

    cell3 = nbf.v4.new_markdown_cell("""### 🏗️ Die wichtigsten Launch-Bausteine

**`GitHub Pages Checkliste`** 📜

```html
<!-- aus Loesung/index.html -->
<div class="glass-panel">
  <h3 class="text-lg font-semibold">GitHub Pages Checkliste</h3>
  <ul class="mt-4 space-y-2 text-sm">
    <li>✔ Settings → Pages → Branch `main`</li>
    <li>✔ URL merken und sharen</li>
    <li>✔ HTTPS aktivieren</li>
  </ul>
</div>
```

Das Panel ist wie ein To-do-Buch im Minecraft-Inventar: Wenn jedes Kästchen angehakt ist, weiß der Bürgermeister, dass das Portal sicher geöffnet werden kann.

**`ARIA Intro-Dialog`** 📝

```html
<div id="intro-overlay" role="dialog" aria-modal="true" aria-labelledby="intro-title">
  <button id="launch-btn" class="launch-button">Intro-Screen zünden</button>
</div>
```

Der Intro-Screen funktioniert wie eine Schutzbarriere: Niemand sieht die Seite, bevor du das "Intro-Screen zünden"-Relais betätigst. Durch `role="dialog"` und `aria-modal="true"` wissen Screenreader exakt, wo sich der Fokus befindet.
""")
    nb.cells.append(cell3)

    cell4 = nbf.v4.new_markdown_cell("""### 🌐 Weitere wichtige Konzepte

**AOS Scroll-Magie** (Story-Kapitel tauchen nacheinander auf):

```html
<div class="aos-demo" data-aos="zoom-out">Star Zoom</div>
```

`data-aos="zoom-out"` sorgt dafür, dass Elemente beim Scrollen wie Partikel vom Nether-Portal herausfliegen.

**Interaktive Accessibility Toggles** (High Contrast, Schrift Boost, Ruhemodus):

```html
<button class="toggle-btn" data-toggle-class="text-boost" aria-pressed="false">
  Schrift Boost
</button>
```

Jeder Button fügt auf dem `<body>` eine Klasse hinzu. Dadurch kannst du live testen, wie Menschen mit Sehschwäche oder Motion-Sickness die Seite erleben.
""")
    nb.cells.append(cell4)

    cell5 = nbf.v4.new_markdown_cell("""## 🎨 Dein praktisches WOW-Ziel heute:

✅ **Cineastischer Intro-Screen** – GSAP blendet Portal, Statistiken und Text ein wie ein Trailer.

✅ **GitHub Pages Deployment** – die Seite läuft auf einer echten URL mit HTTPS.

✅ **Accessibility Deck** – High-Contrast-Modus, Fokus-Markierungen und Live-Region.

✅ **Mission Control Checkliste** – Checkboxen aktualisieren Fortschrittsbalken und Timeline.

**Das Ergebnis:** Besucher fühlen sich wie in deinem Minecraft-Reich und können es sofort selbst erkunden. 🎮✨
""")
    nb.cells.append(cell5)

    cell6 = nbf.v4.new_markdown_cell("""# 🧪 Verstehen

Bevor du irgendetwas änderst, lies dir jede Sektion auf der Lösung gründlich durch. Frage dich: *Warum ist dieses Element wichtig? Was würde passieren, wenn es fehlt?* Danach bist du bereit, das Finale selbst zu steuern.
""")
    nb.cells.append(cell6)

    cell7 = nbf.v4.new_markdown_cell("""## 🔍 GitHub Pages Workflow verstehen

GitHub Pages läuft wie ein Minecart-System: Repository ➜ Branch ➜ öffentlicher Tunnel.

```text
1. `git status` prüfen
2. `git add Tag_24/...`
3. `git commit -m "Launch Tag 24"`
4. `git push`
5. Repository → Settings → Pages → Branch `main`
```

Sobald du den Branch gespeichert hast, baut GitHub alles nach und stellt es unter einer URL zur Verfügung. Achte darauf, dass `Tag_24/` im Repository liegt, damit der Server alles findet.
""")
    nb.cells.append(cell7)

    cell8 = nbf.v4.new_markdown_cell("""## 🎨 Intro-Screen & Accessibility

Der Intro-Screen schützt die Seite, bis du bereit bist, ihn zu öffnen.

```html
<div id="intro-overlay" class="intro-screen" role="dialog" aria-modal="true">
  <h1 id="intro-title">Ready für das Portal-Feuerwerk?</h1>
  <button id="launch-btn" class="launch-button">Intro-Screen zünden</button>
</div>
```

- `role="dialog"` + `aria-modal="true"` sperren den Rest der Seite.
- Der Button bekommt ein klares `aria-label`, damit auch Screenreader verstehen, was passiert.
- Escape schließt das Overlay sofort, wie ein Notausgang im Portalraum.
""")
    nb.cells.append(cell8)

    cell9 = nbf.v4.new_markdown_cell("""## ⚡ JavaScript Mission Control

Mit JavaScript verbindest du Checkboxen, Progress-Bar und Timeline.

```javascript
const updateProgress = () => {
  const checked = Array.from(stepBoxes).filter((box) => box.checked).length;
  const percent = Math.round((checked / stepBoxes.length) * 100);
  progressFill.style.width = `${percent}%`;
  progressBar.setAttribute('aria-valuenow', String(percent));
  if (srStatus) {
    srStatus.textContent = `Checkliste steht bei ${percent} Prozent.`;
  }
};
```

Die Funktion funktioniert wie ein Redstone-Comparator: Sie misst, wie viele Checkboxen aktiv sind und aktualisiert alle Anzeigen in Echtzeit.
""")
    nb.cells.append(cell9)

    cell10 = nbf.v4.new_markdown_cell("""# 🧪 Ausprobieren

Starte die folgende Demo. Sie simuliert einen Mini-Launch mit Progress-Bar und Accessibility-Toggles. Spiele damit herum und beobachte, wie die Live-Region reagiert.
""")
    nb.cells.append(cell10)

    cell11 = nbf.v4.new_code_cell('''from IPython.core.display import HTML
HTML("""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <style>
      body {font-family: 'Space Grotesk', sans-serif; background:#030712; color:#f8fafc; padding:20px;}
      .panel {border-radius:22px; border:1px solid rgba(255,255,255,0.15); padding:24px; max-width:540px; margin:auto; background:rgba(13,38,49,0.8);}
      .progress {height:12px; border-radius:999px; background:rgba(255,255,255,0.15); overflow:hidden; margin-top:16px;}
      .progress span {display:block; height:100%; width:0; background:linear-gradient(90deg,#3dd68c,#7ee8fa); transition:width 0.4s ease;}
      button {margin-top:12px; margin-right:8px; border:none; border-radius:999px; padding:10px 16px; font-weight:600; cursor:pointer;}
      button[data-contrast='true'] {background:#3dd68c; color:#032224;}
      .contrast body, .contrast .panel {background:#fef3c7; color:#082f49;}
      .sr {position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0,0,0,0);}
    </style>
  </head>
  <body>
    <div class="panel">
      <p>Mini-Mission Control</p>
      <label><input type="checkbox" class="js-step" /> Pages aktivieren</label><br />
      <label><input type="checkbox" class="js-step" /> HTTPS & Domain</label><br />
      <label><input type="checkbox" class="js-step" /> Accessibility prüfen</label>
      <div class="progress"><span id="demo-bar"></span></div>
      <p id="demo-label">0% erledigt</p>
      <button id="contrast-btn" data-contrast="false">High Contrast</button>
      <p id="demo-live" class="sr" aria-live="polite"></p>
    </div>
    <script>
      const steps = Array.from(document.querySelectorAll('.js-step'));
      const bar = document.getElementById('demo-bar');
      const label = document.getElementById('demo-label');
      const live = document.getElementById('demo-live');
      const btn = document.getElementById('contrast-btn');
      const update = () => {
        const percent = Math.round((steps.filter(step => step.checked).length / steps.length) * 100);
        bar.style.width = percent + '%';
        label.textContent = percent + '% erledigt';
        live.textContent = 'Launch-Status bei ' + percent + ' Prozent';
      };
      steps.forEach(step => step.addEventListener('change', update));
      update();
      btn.addEventListener('click', () => {
        const isActive = btn.getAttribute('data-contrast') === 'true';
        document.body.style.background = isActive ? '#030712' : '#fef3c7';
        document.body.style.color = isActive ? '#f8fafc' : '#082f49';
        btn.setAttribute('data-contrast', String(!isActive));
        btn.textContent = isActive ? 'High Contrast' : 'Standard';
        live.textContent = isActive ? 'High Contrast deaktiviert' : 'High Contrast aktiviert';
      });
    </script>
  </body>
</html>
""")
''')

    nb.cells.append(cell11)

    cell12 = nbf.v4.new_markdown_cell(
        """# 🚀 Deine Aufgabe: Seite deployen & den Intro-Screen perfektionieren"""
    )
    nb.cells.append(cell12)

    cell13 = nbf.v4.new_markdown_cell("""## 🎯 Mission: 3 magische TODOs lösen

Im Ordner `Tag_24/Aufgabe/` ist alles vorbereitet. Drei gezielte TODOs fehlen, damit Mission Control so mächtig wird wie in der Lösung.
""")
    nb.cells.append(cell13)

    cell14 = nbf.v4.new_markdown_cell("""### 📝 **TODO 1: HTML – High-Contrast-Schalter wieder einsetzen**
**Datei:** `Tag_24/Aufgabe/index.html` (Bereich Accessibility Deck, Zeile ~176)

**Was zu tun ist:**
```html
<!-- TODO 1: Baue hier den High-Contrast-Button ein -->
```

**Lösungshinweis:** Kopiere aus der Lösung den Button mit `data-toggle-class="contrast-mode"` und `data-label="High Contrast"`. Dadurch kann Felix live prüfen, wie stark der Kontrast sein muss. Vergiss nicht `aria-pressed="false"`, damit Screenreader wissen, ob der Modus aktiv ist.
""")
    nb.cells.append(cell14)

    cell15 = nbf.v4.new_markdown_cell("""### 🎨 **TODO 2: CSS – High-Contrast-Stile ergänzen**
**Datei:** `Tag_24/Aufgabe/style.css` (Bereich um Zeile ~410)

**Was zu tun ist:**
```css
/* TODO 2: Ergänze hier den High-Contrast-Look */
```

**Lösungshinweis:** Erstelle wieder die Selektoren `.contrast-mode` und `.contrast-mode .mission-card`. Nutze satte Farben (`#01040c`, `#fef08a`), damit das Accessibility Deck sichtbar zeigt, wie kontrastreiche Oberflächen aussehen. Ohne diese Styles sieht der Button zwar nett aus, aber er verändert nichts.
""")
    nb.cells.append(cell15)

    cell16 = nbf.v4.new_markdown_cell("""### ⚡ **TODO 3: JavaScript – Timeline-Status zurückbringen**
**Datei:** `Tag_24/Aufgabe/script.js` (Funktion `updateProgress`, Zeile ~32)

**Was zu tun ist:**
```javascript
// TODO 3: Aktiviere hier wieder das Umschalten der Timeline-Klasse
```

**Lösungshinweis:** Verwende dieselbe Zeile wie in der Lösung:
```javascript
target.classList.toggle('active', box.checked);
```
So sehen Mitspieler sofort, welcher Deployment-Schritt erledigt ist. Ohne diese Zeile bleibt die Timeline grau.
""")
    nb.cells.append(cell16)

    cell17 = nbf.v4.new_markdown_cell("""## 🏆 Erfolgskontrolle

✅ Die Launch-Bar steigt, wenn du Checkboxen aktivierst.

✅ Die Timeline färbt erledigte Schritte grün.

✅ High-Contrast-Button verändert wirklich die Farben.

✅ Der Intro-Screen verschwindet sauber (Dialog, Escape, GSAP).
""")
    nb.cells.append(cell17)

    cell18 = nbf.v4.new_markdown_cell("""## 🌐 Testen deiner Lösung

**Browser-Vorschau Aufgabe:**

http://192.168.0.20:8000/2025_Adventskalender/Tag_24/Aufgabe/

**Vergleich mit Musterlösung:**

http://192.168.0.20:8000/2025_Adventskalender/Tag_24/Loesung/

Denk daran: Auf dem Server funktionieren auch alle CDNs (Tailwind Play CDN, GSAP, AOS), genau so wie es die Dokumentation beschreibt.
""")
    nb.cells.append(cell18)

    cell19 = nbf.v4.new_markdown_cell("""# Weitere Ideen""")
    nb.cells.append(cell19)

    cell20 = nbf.v4.new_markdown_cell("""- Baue ein zusätzliches Deployment-Panel mit Logs von GitHub Actions.
- Erstelle Screenshots und packe sie als Social Preview (`og:image`).
- Ergänze einen "Launch Countdown" mit `setInterval` und Audioeffekten.
- Nutze Three.js (aus Woche 4) für ein rotierendes Portal im Hintergrund.
""")
    nb.cells.append(cell20)

    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as error:
        print(f"❌ Validierungsfehler: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    output_path = Path.cwd() / filename

    try:
        with open(output_path, "w", encoding="utf-8") as file_handler:
            nbf.write(nb, file_handler)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as error:
        print(f"❌ Fehler beim Speichern: {error}")
        sys.exit(1)


def main():
    print("🎄 Erstelle Lesson.ipynb...")
    print("=" * 60)
    nb = create_lesson()
    output_path = save_notebook(nb)
    print("=" * 60)
    print("🎉 Fertig! Lesson wurde erstellt.")
    print(f"📁 Pfad: {output_path}")


if __name__ == "__main__":
    main()
