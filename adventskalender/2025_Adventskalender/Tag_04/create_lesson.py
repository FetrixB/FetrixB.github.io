#!/usr/bin/env python3
"""Erstellt die Lesson.ipynb für Tag 04 – Interaktive Dorfkarte."""

import nbformat as nbf
import sys
from pathlib import Path


def create_lesson():
    """Baut das Notebook mit Story, Theorie, Demo und Aufgaben auf."""

    nb = nbf.v4.new_notebook()

    # 1) Titel & Story
    nb.cells.append(
        nbf.v4.new_markdown_cell(
            """# 🎄 Tag 04 – Teleporter-Karte fürs Weihnachtsdorf

Felix, der Schneesturm hat nicht nur Zäune, sondern auch alle Wegweiser fortgeweht. Händler verirren sich auf dem Weg zum Portal und niemand findet mehr die Schatzkiste. Der Dorf-Kartograph vertraut auf dich: In `Loesung/index.html` wartet bereits eine magische Karte, deren Links sich wie Minecraft-Teleporter anfühlen. Dein Job ist es, zu verstehen, wie Ankerlinks, Bildkarten und Tooltips zusammenarbeiten, damit jede Besucherin sicher landet."""
        )
    )

    # 2) Lern-Kapitel
    nb.cells.append(
        nbf.v4.new_markdown_cell(
            """## 📚 Lernkapitel: Interne Links + Bildkarten = Rettungsplan

### 1. Interne Teleporter mit `<a href="#ziel">`
- Die Navigationsleiste in `Loesung/index.html` zeigt vier Links (`Portal`, `Schneemarkt`, `Schmiede`, `Bibliothek`).
- Jeder Link verweist auf einen Abschnitt mit passender `id`, z.B. `<section id="portal">`.
- `scroll-behavior: smooth;` im `style.css` sorgt dafür, dass der Sprung wie eine Gleiterfahrt wirkt.

```html
<nav class="anchor-nav" aria-label="Interne Wegpunkte">
  <a href="#portal" class="anchor-link">Portal</a>
  ...
</nav>
<section id="portal" class="location-card">...</section>
```

### 2. Bildkarten mit `<map>` und `<area>`
- Das Dorfbild (`map-figure`) nutzt `usemap="#dorfMap"` und beschreibt Hotspots über `<area>`.
- Koordinaten (`coords="220,210,60"`) legen fest, wo ein Kreis, Rechteck oder Polygon aktiv ist.
- Jeder Bereich hat sowohl ein `href` als auch ein `data-location`, damit das Skript weiß, welcher Abschnitt aktiv ist.

```html
<img src="..." usemap="#dorfMap">
<map name="dorfMap">
  <area shape="circle" coords="220,210,60" href="#portal" data-location="portal">
</map>
```

### 3. Sichtbare Hotspots & Tooltips
- Zusätzlich zu den unsichtbaren `<area>`-Flächen liegen absolut positionierte Buttons auf der Karte. Sie bekommen `data-tooltip`-Texte, die per CSS angezeigt werden.
- Das Info-Panel rechts zeigt immer den aktuell ausgewählten Ort – gesteuert durch JavaScript in `Loesung/script.js`.
- Diese Kombination erfüllt den WOW-Wunsch: sofortiges Feedback, hübsche Tooltips und klare Orientierung."""
        )
    )

    # 3) Verstehen & Ausprobieren – Markdown Teil
    nb.cells.append(
        nbf.v4.new_markdown_cell(
            """## 🧠 Verstehen & Ausprobieren: So greifen die Mechanismen ineinander

### Klickbereiche wie Wegpunkte setzen
`coords` geben die Pixel-Positionen innerhalb des Bildes an. Du kannst sie mit jedem Bildeditor oder über DevTools auslesen. Kreise benötigen drei Werte (`x, y, radius`), Rechtecke vier (`x1, y1, x2, y2`).

```html
<area shape="rect" coords="520,110,640,190" href="#schmiede" title="Zur Schmiede" data-location="schmiede">
```

### Tooltip-Magie in CSS
Die Lösung speichert den Tooltip-Text direkt im Element und liest ihn mit `attr(data-tooltip)` aus. Gleichzeitig sorgt eine `pulse`-Animation dafür, dass die Buttons wirken wie schimmernde Baken.

```css
.map-hotspot::after {
  content: attr(data-tooltip);
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(94, 234, 212, 0.6);
  opacity: 0;
  transition: opacity 0.2s ease;
}
.map-hotspot:hover::after { opacity: 1; }
```

### Info-Panel + Smooth Scrolling in JS
`setActiveLocation` sammelt alle Views: Tooltip-Badge, Text und aktive Klassen. Sobald `scrollToSection=True`, wird der Zielabschnitt mit `scrollIntoView` angesteuert und kurz mit `focus-glow` markiert – genau wie ein aufleuchtender Pfad in Minecraft.

```javascript
const setActiveLocation = (locationId, scrollToSection = false) => {
  infoTitle.textContent = locations[locationId].title;
  navLinks.forEach((link) => link.classList.toggle('active', link.dataset.locationLink === locationId));
  if (scrollToSection) {
    const target = document.getElementById(locationId);
    target.scrollIntoView({ behavior: 'smooth' });
    target.classList.add('focus-glow');
  }
};
```

Im nächsten Schritt probierst du eine Mini-Version davon aus."""
        )
    )

    # 3b) Interaktive Demo – Code Cell
    demo_html = """from IPython.core.display import HTML

HTML(\"\"\"
<!DOCTYPE html>
<html lang=\\"de\\">
<head>
  <meta charset=\\"UTF-8\\" />
  <style>
    body { font-family: 'Nunito', system-ui; background:#020617; color:#e2e8f0; margin:0; padding:32px; }
    .demo-shell { max-width: 760px; margin: 0 auto; background: rgba(15,23,42,0.85); border-radius: 24px; padding: 24px; border:1px solid rgba(94,234,212,0.4); box-shadow:0 20px 40px rgba(2,6,23,0.7); }
    .demo-map { position: relative; border-radius: 18px; overflow: hidden; }
    .demo-map img { width:100%; display:block; }
    .demo-hotspot { position:absolute; width:40px; height:40px; border-radius:999px; border:2px solid rgba(255,255,255,0.8); background:rgba(15,118,110,0.6); transform:translate(-50%,-50%); cursor:pointer; animation:pulse 2s infinite; }
    .demo-hotspot.is-active { background:rgba(250,204,21,0.7); border-color:#facc15; }
    .demo-info { margin-top: 18px; padding: 16px; border-radius: 16px; background: rgba(2,6,23,0.8); border:1px solid rgba(148,163,184,0.3); min-height: 120px; }
    .demo-info h4 { margin:0 0 8px 0; font-family:'Orbitron', sans-serif; letter-spacing:0.1em; }
    .demo-buttons { display:flex; gap:12px; margin-top:12px; flex-wrap:wrap; }
    .demo-buttons button { flex:1 1 140px; border:none; padding:10px 14px; border-radius:999px; background:rgba(16,185,129,0.2); color:#a7f3d0; letter-spacing:0.15em; text-transform:uppercase; cursor:pointer; }
    .demo-buttons button.is-active { background:linear-gradient(125deg,#14b8a6,#22d3ee); color:#020617; }
    @keyframes pulse { 0% { box-shadow:0 0 0 0 rgba(16,185,129,0.4); } 70% { box-shadow:0 0 0 14px rgba(16,185,129,0); } 100% { box-shadow:0 0 0 0 rgba(16,185,129,0); } }
  </style>
</head>
<body>
  <div class=\\"demo-shell\\">
    <p>Teste ein Mini-Map-System: Klicke auf Kreise oder Buttons.</p>
    <div class=\\"demo-map\\">
      <img src=\\"https://images.unsplash.com/photo-1482192597420-4817fdd7e8b0?auto=format&fit=crop&w=800&q=60\\" alt=\\"Winterliches Dorf\\" usemap=\\"#demoMap\\" />
      <map name=\\"demoMap\\">
        <area shape=\\"circle\\" coords=\\"220,150,50\\" href=\\"#\\" data-location=\\"portal\\" alt=\\"Portal\\" />
        <area shape=\\"circle\\" coords=\\"520,190,45\\" href=\\"#\\" data-location=\\"markt\\" alt=\\"Markt\\" />
        <area shape=\\"rect\\" coords=\\"120,240,230,330\\" href=\\"#\\" data-location=\\"bibliothek\\" alt=\\"Bibliothek\\" />
      </map>
      <button class=\\"demo-hotspot\\" data-location=\\"portal\\" style=\\"top:42%; left:32%;\\"></button>
      <button class=\\"demo-hotspot\\" data-location=\\"markt\\" style=\\"top:55%; left:65%;\\"></button>
      <button class=\\"demo-hotspot\\" data-location=\\"bibliothek\\" style=\\"top:78%; left:28%;\\"></button>
    </div>
    <div class=\\"demo-info\\" id=\\"demoInfo\\">
      <h4 id=\\"demoTitle\\">Portal</h4>
      <p id=\\"demoDesc\\">Teleportiere Spieler direkt zum Story-Start: Setze `id` am Abschnitt und verlinke ihn mit einem internen Anchor.</p>
    </div>
    <div class=\\"demo-buttons\\">
      <button data-location=\\"portal\\" class=\\"is-active\\">Portal</button>
      <button data-location=\\"markt\\">Markt</button>
      <button data-location=\\"bibliothek\\">Bibliothek</button>
    </div>
  </div>
  <script>
    const demoData = {
      portal: { title: 'Portal zur Schneewelt', desc: 'Hier beginnt die Reise. Mit href=\"#portal\" landet jeder genau hier.' },
      markt: { title: 'Schneemarkt', desc: 'Zeig Tooltips, damit Reisende wissen, dass dort Händler warten.' },
      bibliothek: { title: 'Kristall-Bibliothek', desc: 'Ein ruhiger Abschnitt voller UX-Tipps und Layout-Ideen.' }
    };
    const buttons = document.querySelectorAll('.demo-buttons button');
    const hotspots = document.querySelectorAll('.demo-hotspot');
    const areas = document.querySelectorAll('area[data-location]');
    const title = document.getElementById('demoTitle');
    const desc = document.getElementById('demoDesc');

    const updateDemo = (location) => {
      const data = demoData[location];
      if (!data) return;
      title.textContent = data.title;
      desc.textContent = data.desc;
      buttons.forEach((btn) => btn.classList.toggle('is-active', btn.dataset.location === location));
      hotspots.forEach((dot) => dot.classList.toggle('is-active', dot.dataset.location === location));
    };

    [...buttons, ...hotspots].forEach((interactive) => {
      interactive.addEventListener('click', () => updateDemo(interactive.dataset.location));
      interactive.addEventListener('mouseenter', () => updateDemo(interactive.dataset.location));
    });

    areas.forEach((area) => {
      area.addEventListener('mouseenter', () => updateDemo(area.dataset.location));
      area.addEventListener('focus', () => updateDemo(area.dataset.location));
    });
  </script>
</body>
</html>
\"\"\")
"""

    nb.cells.append(nbf.v4.new_code_cell(demo_html))

    # 4) Aufgabe mit TODOs
    nb.cells.append(
        nbf.v4.new_markdown_cell(
            """# 🚀 Deine Aufgabe: Karte vervollständigen
Im Ordner `Tag_04/Aufgabe/` wartet die abgespeckte Karte. Drei gezielte TODOs machen sie identisch zur Lösung.

### 📝 TODO 1 – HTML-Hotspot ergänzen
- **Datei:** `Aufgabe/index.html` (Map-Bereich, ca. Zeile 55)
- **Aufgabe:** Der Bibliotheksbereich fehlt in der `<map>`. Füge ein `area` mit `shape="rect"`, passenden `coords` (über dem rot leuchtenden Gebäude) und `href="#bibliothek"` ein. Vergiss `data-location="bibliothek"` nicht.

### 🎨 TODO 2 – Tooltip-Styling bauen
- **Datei:** `Aufgabe/style.css` (Hotspot-Abschnitt, unmittelbar nach `.map-hotspot`)
- **Aufgabe:** Schreibe die CSS-Regeln für `.map-hotspot::after` wieder hinein: `content: attr(data-tooltip)`, dunkler Hintergrund, Schrift, Padding, Border und Transition. Ergänze außerdem die Hover-/Focus-Regeln, damit sich die Blase einblendet.

### ⚡ TODO 3 – Smooth Scroll aktivieren
- **Datei:** `Aufgabe/script.js` (`setActiveLocation` Funktion, ca. Zeile 60)
- **Aufgabe:** Vervollständige den `if (scrollToSection)`-Block. Wenn Nutzer klicken, soll `document.getElementById(locationId).scrollIntoView({ behavior: 'smooth' })` ausgelöst werden. Danach kurz `focus-glow` hinzufügen und per `setTimeout` wieder entfernen.

💡 Prüfe nach jedem Schritt, ob die Karte weiterhin reagiert. Schon mit zwei TODOs merkst du, wie schnell sich UX verbessert!"""
        )
    )

    # 5) Erfolg & Möglichkeiten
    nb.cells.append(
        nbf.v4.new_markdown_cell(
            """## 🌟 Erfolg & Möglichkeiten
Wenn alle TODOs sitzen, fühlt sich die Karte wieder wie ein echtes Navigationssystem an:

- Die Hotspots teleportieren Besucher zu `#portal`, `#markt`, `#schmiede` und `#bibliothek`.
- Tooltips erscheinen sowohl über Buttons als auch über den `title`-Text der `<area>`-Tags.
- `setActiveLocation` scrollt sanft und hebt Abschnitte durch `focus-glow` hervor.
- Teste zuerst die Aufgabe-Version (`http://192.168.0.20:8000/2025_Adventskalender/Tag_04/Aufgabe/`) und vergleiche danach mit der Lösung.
- Technische Checks: `node --check Tag_04/Loesung/script.js`, `node --check Tag_04/Aufgabe/script.js`, `stylelint Tag_04/Loesung/style.css`.

🎁 Bonus-Ideen: Ergänze weitere Wegpunkte (z.B. `#geschenke`), baue responsive Layout-Switches oder lass das Info-Panel Bilder anzeigen. Deine Karte kann wachsen wie ein echtes Minecraft-Dorf!"""
        )
    )

    # Notebook validieren
    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as err:
        print(f"❌ Validierungsfehler: {err}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    """Speichert das Notebook direkt im Tag_04 Verzeichnis."""

    output_path = Path(__file__).resolve().parent / filename

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            nbf.write(nb, f)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as err:
        print(f"❌ Fehler beim Speichern: {err}")
        sys.exit(1)


def main():
    print("🎄 Erstelle Lesson.ipynb...")
    print("=" * 60)
    notebook = create_lesson()
    output_path = save_notebook(notebook)
    print("=" * 60)
    print("🎉 Fertig! Lesson wurde erstellt.")
    print(f"📁 Pfad: {output_path}")


if __name__ == "__main__":
    main()
