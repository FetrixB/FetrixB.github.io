#!/usr/bin/env python3
"""
Erstellt die Lesson.ipynb für Tag 05 mit Story, Theorie und Aufgaben.
"""

import nbformat as nbf
import sys
from pathlib import Path


def create_lesson():
    """Erstellt ein vollständig ausgefülltes Notebook für Tag 05."""

    nb = nbf.v4.new_notebook()

    cell1 = nbf.v4.new_markdown_cell(
        """# 🎄 Tag 05 – Schneemanns digitales Fundament

Der Blizzard hat die Holzhütte des weisen Schneemanns zerlegt. In deiner Werkstatt baust du ihm nun eine sichere HTML-Hütte mit warmem CSS-Licht und cleveren Buttons, damit er wieder alle Dorfbewohner beraten kann."""
    )
    nb.cells.append(cell1)

    cell2 = nbf.v4.new_markdown_cell(
        """## 🎯 Deine Mission für heute
- Verwende semantische Elemente wie Header, Main und Footer als stabiles Fundament.
- Plane Layout-Container, die Inhalte zusammenhalten wie Mauern aus Schneeblöcken.
- Gestalte Buttons mit klaren States, sodass jede Interaktion wie ein magischer Hebel wirkt.
- Nutze die Dateien in `Loesung/` als Referenz und `Aufgabe/` als Spielplatz."""
    )
    nb.cells.append(cell2)

    cell3 = nbf.v4.new_markdown_cell(
        """### 🏗️ Die wichtigsten HTML-Fundamente
**`<header>`** – Dachbalken der Seite

- Enthält Logo, Navigation und Introtext.
- In `Loesung/index.html` bekommst du einen Orbitron-Titel plus eine Navi-Liste.

```html
<header class=\"content-shell frost-card\">
  <nav aria-label=\"Seiten-Navigation\">
    <ul>
      <li><a href=\"#blaupause\">Blueprints</a></li>
      ...
    </ul>
  </nav>
</header>
```

**`<main>`** – Warmer Hauptraum mit mehreren `section`-Blöcken

**`<footer>`** – Feuerstelle für Kontaktinfos."""
    )
    nb.cells.append(cell3)

    cell4 = nbf.v4.new_markdown_cell(
        """### 🌐 Layout-Container & Flexbox-Orga
Container halten alles auf Breite und bringen Ordnung:

```css
.content-shell {
  width: min(1200px, 92vw);
  margin-inline: auto;
  padding: clamp(1.5rem, 1.5vw, 2.5rem);
}

.blueprint-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
}
```

Damit fühlen sich die Sektionen wie Räume in einem Minecraft-Haus an."""
    )
    nb.cells.append(cell4)

    cell5 = nbf.v4.new_markdown_cell(
        """## ✨ Dein praktisches WOW-Ziel
- ✅ Hero-Sektion mit Status-Badge und Button `Schneesturm stoppen`.
- ✅ Blueprint-Karten plus Timeline, die jeden Bau-Schritt visualisiert.
- ✅ Button-Labor mit `aria-pressed`, damit States zugänglich sind.
- ✅ Footer-Feuerstelle mit Accessibility-Hinweis.

**Das Ergebnis:** Eine frostige, aber stabile Mini-Seite, die per Klick Feedback gibt."""
    )
    nb.cells.append(cell5)

    cell6 = nbf.v4.new_markdown_cell("""# 🧪 Verstehen""")
    nb.cells.append(cell6)

    cell7 = nbf.v4.new_markdown_cell(
        """## 🔍 Semantische Schichten verstehen
Jede Ebene deiner Seite erfüllt eine Aufgabe. In `Loesung/index.html` findest du dieses Grundgerüst:

```html
<header class=\"frost-card\">...</header>
<main>
  <section class=\"hero\">...</section>
  <section class=\"blueprint\">...</section>
  <section class=\"button-lab\">...</section>
</main>
<footer class=\"content-shell footer\">...</footer>
```

Das hilft Screenreadern genau zu verstehen, was Header, Inhalte und Footer sind."""
    )
    nb.cells.append(cell7)

    cell8 = nbf.v4.new_markdown_cell(
        """## 🎨 Container = gleichmäßige Räume
Mit `content-shell`, `frost-card` und `frost-panel` bestimmst du Breite, Hintergrund und Schatten.

```css
.frost-card {
  backdrop-filter: blur(18px);
  border-bottom: 1px solid var(--border-glow);
}

.frost-panel ul {
  list-style: none;
  margin: 1rem 0 0;
  padding: 0;
}
```

Flexbox im Header und Grid in der Blueprint-Sektion halten die Elemente flexibel wie modulare Blöcke."""
    )
    nb.cells.append(cell8)

    cell9 = nbf.v4.new_markdown_cell(
        """## ⚡ Buttons mit Persönlichkeit
Die Buttons im Labor verbinden CSS und JavaScript:

```javascript
const blueprintMessages = { foundation: { title: "Header-Dach" } };

button.addEventListener("click", () => {
  button.setAttribute("aria-pressed", "true");
  updateOutput(button.dataset.blueprint);
});
```

Mit `aria-pressed` verstehen Screenreader den aktuellen Button-State, `dataset` liefert Infos für das Ausgabefeld."""
    )
    nb.cells.append(cell9)

    cell10 = nbf.v4.new_markdown_cell(
        """# 🧪 Ausprobieren
Starte dieses Mini-Labor: Klick auf die Buttons und beobachte, wie HTML, CSS und JS zusammenspielen."""
    )
    nb.cells.append(cell10)

    cell11 = nbf.v4.new_code_cell(
        '''from IPython.core.display import HTML

demo_html = """
<!DOCTYPE html>
<html lang=\"de\">
<head>
  <style>
    body { font-family: 'Inter', sans-serif; background:#020617; color:#f8fbff; }
    .demo-shell { max-width: 620px; margin: 0 auto; padding: 24px; border-radius: 24px; background: rgba(255,255,255,0.04); border:1px solid rgba(91,250,222,0.4); }
    .demo-buttons { display:flex; gap:12px; flex-wrap:wrap; }
    .demo-button { flex:1 1 160px; border:none; border-radius:999px; padding:12px 18px; font-weight:700; text-transform:uppercase; color:#020617; background:linear-gradient(135deg,#5bfade,#7bdff2); box-shadow:0 6px 0 rgba(11,61,99,0.9); cursor:pointer; transition:transform .2s, box-shadow .2s; }
    .demo-button.is-active { background:linear-gradient(135deg,#8b5cf6,#5bfade); color:#fff; }
    .demo-button:active { transform:translateY(3px); box-shadow:0 3px 0 rgba(11,61,99,0.9); }
    .demo-output { margin-top:20px; padding:16px; border-radius:16px; background:rgba(2,6,23,0.8); border:1px solid rgba(91,250,222,0.4); min-height:120px; }
    .demo-output h4 { margin:0 0 8px; font-family:'Orbitron',sans-serif; }
    .demo-output code { background:rgba(0,0,0,0.4); padding:3px 6px; border-radius:6px; display:inline-block; }
  </style>
</head>
<body>
  <div class=\"demo-shell\">
    <p>Blueprint-Auswahl:</p>
    <div class=\"demo-buttons\">
      <button class=\"demo-button is-active\" data-blueprint=\"header\">Header</button>
      <button class=\"demo-button\" data-blueprint=\"main\">Main</button>
      <button class=\"demo-button\" data-blueprint=\"footer\">Footer</button>
    </div>
    <div class=\"demo-output\">
      <h4>Header-Dach aktiv</h4>
      <p>Navigation, Logo und Story-Intro wohnen hier.</p>
      <code>&lt;header&gt;...&lt;/header&gt;</code>
    </div>
  </div>
  <script>
    const demoData = {
      header: { title: 'Header-Dach aktiv', text: 'Navigation, Logo und Story-Intro wohnen hier.', code: '<header>...</header>' },
      main: { title: 'Main-Fluss aktiv', text: 'Hero, Blueprints und Button-Labor sitzen im Main.', code: '<main>...</main>' },
      footer: { title: 'Footer-Signal', text: 'Kontakt + Accessibility-Hinweis geben Wärme.', code: '<footer>...</footer>' }
    };
    const buttons = document.querySelectorAll('.demo-button');
    const output = document.querySelector('.demo-output');
    const title = output.querySelector('h4');
    const text = output.querySelector('p');
    const code = output.querySelector('code');
    buttons.forEach((btn) => {
      btn.addEventListener('click', () => {
        buttons.forEach((button) => button.classList.remove('is-active'));
        btn.classList.add('is-active');
        const info = demoData[btn.dataset.blueprint];
        title.textContent = info.title;
        text.textContent = info.text;
        code.textContent = info.code;
      });
    });
  </script>
</body>
</html>
"""

display(HTML(demo_html))
'''
    )
    nb.cells.append(cell11)

    cell12 = nbf.v4.new_markdown_cell(
        """# 🚀 Deine Aufgabe: Frost-Timeline vollenden"""
    )
    nb.cells.append(cell12)

    cell13 = nbf.v4.new_markdown_cell(
        """## 🎯 Mission: 3 magische TODOs lösen
Im Ordner `Aufgabe/` wartet eine fast fertige Version. Ergänze drei Stellen, damit sie mit `Loesung/` mithalten kann."""
    )
    nb.cells.append(cell13)

    cell14 = nbf.v4.new_markdown_cell(
        """### 📝 **TODO 1: HTML – Timeline ergänzen**
**Datei:** `Aufgabe/index.html` (Zeile ~100)

Füge die drei Schritte ein, die in der Lösung nach dem Blueprint-Grid stehen.

```html
<!-- TODO 1: ... -->
<div class=\"timeline\">
  <div class=\"timeline-step\">...</div>
  ...
</div>
```

So visualisierst du Fundament → Layout → Buttons."""
    )
    nb.cells.append(cell14)

    cell15 = nbf.v4.new_markdown_cell(
        """### 🎨 **TODO 2: CSS – 3D-Frost-Effekt aktivieren**
**Datei:** `Aufgabe/style.css` (Zeile ~130)

Im Kommentar steht, dass der Verlauf + Schatten fehlt. Nutze das Beispiel aus `Loesung/style.css`, damit der Button wieder leuchtet und auf Hover/Active reagiert."""
    )
    nb.cells.append(cell15)

    cell16 = nbf.v4.new_markdown_cell(
        """### ⚡ **TODO 3: JavaScript – Blueprint aktualisieren**
**Datei:** `Aufgabe/script.js` (Zeile ~25)

Schreibe in `updateOutput` die drei Zeilen, die Titel, Beschreibung und Code setzen und löse den kurzen Flash-Effekt aus. Ohne diesen Schritt bleiben die Texte statisch."""
    )
    nb.cells.append(cell16)

    cell17 = nbf.v4.new_markdown_cell(
        """## 🏆 Erfolgskontrolle
- Timeline zeigt nacheinander `Fertig!` wenn du den Schneesturm-Button klickst.
- Buttons im Labor wechseln Farbe + Text.
- Status-Badge taucht nach dem Klick sichtbar auf.
- Header/Main/Footer wirken wie warme Räume mit gleichen Abständen."""
    )
    nb.cells.append(cell17)

    cell18 = nbf.v4.new_markdown_cell(
        """## 🌐 Testen deiner Lösung
- Aufgabe testen: https://web.tb-cloudlab.org/2025_Adventskalender/Tag_05/Aufgabe/
- Musterlösung vergleichen: https://web.tb-cloudlab.org/2025_Adventskalender/Tag_05/Loesung/

Nutze unbedingt diese Server-URLs, damit Tailwind-CDN und Pfade stimmen."""
    )
    nb.cells.append(cell18)

    cell19 = nbf.v4.new_markdown_cell("""# 🌟 Erfolg & Möglichkeiten""")
    nb.cells.append(cell19)

    cell20 = nbf.v4.new_markdown_cell(
        """- Schiebe weitere Story-Sektionen in neue `section`-Blöcke.
- Tausche die Timeline-Phrasen gegen eigene Bauabschnitte.
- Spiele mit `aria-pressed` oder `aria-live`, um Accessibility weiter auszubauen.
- Erstelle eigene Frost-Buttons, die Anime.css-Klassen nutzen.
"""
    )
    nb.cells.append(cell20)

    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as error:
        print(f"❌ Validierungsfehler: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    """Speichert das Notebook im aktuellen Verzeichnis."""

    output_path = Path.cwd() / filename

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            nbf.write(nb, file)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as error:  # pylint: disable=broad-except
        print(f"❌ Fehler beim Speichern: {error}")
        sys.exit(1)


def main():
    """CLI-Einstiegspunkt."""

    print("🎄 Erstelle Lesson.ipynb...")
    print("=" * 60)
    nb = create_lesson()
    output_path = save_notebook(nb)
    print("=" * 60)
    print("🎉 Fertig! Lesson wurde erstellt.")
    print(f"📁 Pfad: {output_path}")


if __name__ == "__main__":
    main()
