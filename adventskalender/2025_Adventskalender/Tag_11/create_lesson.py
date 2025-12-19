#!/usr/bin/env python3
"""Erstellt Lesson.ipynb für Tag 11."""

import sys
from pathlib import Path

import nbformat as nbf


def build_cells():
    """Return the complete list of notebook cells for Tag 11."""

    story = nbf.v4.new_markdown_cell(
        """# 🎄 Tag 11 · Portalwald auf mehreren Ebenen

Felix, du betrittst den magischen Wald, den der Wächter in mehrere Dimensionen aufgeteilt hat. Die vorderen Bäume reagieren blitzschnell auf deinen Scroll, die mittleren schwingen gemütlich und der Hintergrund bleibt fast ruhig – genau wie verschiedene Ebenen in Minecraft, wenn du sie mit Redstone-Signalen verbindest. Deine Aufgabe: Du steuerst diesen Portalwald mit CSS-Positionierung, Z-Index und Parallax-Animationen so, dass Besucher*innen eine echte Tiefenreise erleben."""
    )

    learning = nbf.v4.new_markdown_cell(
        """## 🎯 Lern-Checkpoint

- **CSS Positioning & Z-Index**: Du stapelst Himmel, Berge, Wald und Pfad sauber übereinander.
- **Parallax-Scrolling**: Du gibst jeder Ebene eine eigene Geschwindigkeit und einen Transform-Ursprung.
- **Performance-Denken**: Transform3D + requestAnimationFrame halten alles bei 60fps geschmeidig.
- **Library-Einsatz**: `simpleParallax.js` bewegt zusätzliche Bildportale für noch mehr Tiefe."""
    )

    essentials = nbf.v4.new_markdown_cell(
        """### 🏗️ Die wichtigsten Bausteine aus `Tag_11/Loesung/`

**`<div class=\"layer\" data-depth>`** – in `index.html` stapeln sich Ebenen wie Minecraft-Blöcke:
```html
<div class=\"layer layer--midtrees\" data-depth=\"0.7\"></div>
```
Analog zu Chunks mit unterschiedlichen Höhen sorgt `data-depth` dafür, dass JavaScript weiß, wie schnell eine Ebene scrollen darf.

**`transform-origin` + `z-index`** – in `style.css` legst du fest, welche Ebene vorne liegt:
```css
.layer--mountains {
  z-index: -20;
  transform-origin: center;
}
```
Wie beim Stapeln deiner Inventarfächer muss jede Ebene wissen, wo ihr Drehpunkt ist.

**Scroll-Controller** – in `script.js` wertet `requestAnimationFrame` die Scrollposition aus:
```javascript
const translateY = (relativeScroll * depth * speedFactor) / 400;
layer.style.transform = `translate3d(0, ${translateY * -1}px, ${zShift}px)`;
```
So bleibt die Animation ruckelfrei, weil du die Berechnung nur dann startest, wenn der Browser bereit ist."""
    )

    more_concepts = nbf.v4.new_markdown_cell(
        """### 🌐 Weitere wichtige Konzepte

- **Transform3D & Perspective**: Das Parallax-Fenster (`.parallax-stage`) besitzt `perspective: 1200px`, damit kleine Bewegungen nach echter Tiefe aussehen.
- **CSS-Variablen**: `var(--tree-density)` macht es super-einfach, die Dichte der Baum-Muster live zu verändern.
- **simpleParallax.js**: Über das CDN `https://cdn.jsdelivr.net/npm/simple-parallax-js@5.6.2/dist/simpleParallax.min.js` bekommen die drei Galerie-Bilder denselben Tiefeneffekt wie deine Layer.
- **Zustands-HUD**: Der Scroll-Sensor zeigt, wie weit Besucher*innen sind – das hilft später enorm beim Debuggen."""
    )

    wow_goal = nbf.v4.new_markdown_cell(
        """## 🎨 Dein WOW-Ziel heute

✅ **Vielschichtiger Himmel** – Sterne, Aurora und Berge bewegen sich unterschiedlich schnell.

✅ **Reaktiver Wald** – Vordergrund, Mittelwald und Hintergrund reagieren je nach `data-depth`.

✅ **HUD mit Feedback** – der Scroll-Sensor und die Layer-Liste zeigen live die Reise an.

✅ **Dimension-Schalter** – ein Button ändert Farben und Ursprünge wie ein Portal zwischen zwei Biomen.

**Ergebnis:** Ein Portalwald, der beim Scrollen in Tiefe abtaucht und zeigt, warum CSS-Positionierung + JavaScript-Animationen zusammengehören. 🎮✨"""
    )

    understand_header = nbf.v4.new_markdown_cell("""# 🧪 Verstehen""")

    positioning = nbf.v4.new_markdown_cell(
        """## 🔍 Positionierung & Layer-Stack

Stell dir jede Ebene wie ein eigenes Minecraft-Plot vor. Mit `position: absolute` und `inset: 0` klebst du sie exakt übereinander. Der `z-index` bestimmt, welche Ebene vorne liegt – negative Werte verstecken etwas im Hintergrund, hohe Werte holen es nach vorn.

```css
.layer {
  position: absolute;
  inset: 0;
  transform-origin: center;
  will-change: transform;
}
```

`transform-origin` ist hier wie der Kompass des Baums: wenn er am Fuß sitzt, wirkt eine Drehung ganz anders, als wenn er oben sitzt."""
    )

    transforms = nbf.v4.new_markdown_cell(
        """## 🎨 Transform3D + Perspektive = Tiefe

`perspective: 1200px` auf der Bühne sagt dem Browser, wie weit entfernt der Beobachter steht. Jede Ebene bekommt anschließend `translate3d`-Werte. Kleine Bewegungen fühlen sich dadurch wie echte Tiefe an.

```css
.parallax-stage {
  perspective: 1200px;
  background: radial-gradient(circle at 50% 20%, rgba(104, 255, 208, 0.1), transparent);
}
```

Das ist wie beim Beobachten eines Minecraft-Gebirges: je höher die Berggipfel, desto langsamer wirken sie, wenn du dich bewegst."""
    )

    controller = nbf.v4.new_markdown_cell(
        """## ⚡ JavaScript-Controller

`script.js` sammelt Scrollwerte, vergleicht sie mit `data-depth` und zieht jede Ebene nach. `requestAnimationFrame` sorgt dafür, dass der Browser die Arbeit dann erledigt, wenn der letzte Frame fertig ist – kein Ruckeln, kein Stress für die GPU.

```javascript
const highlightLayers = (progress) => {
  const threshold = Number(badge.dataset.layerBadge || 0);
  // wenn progress >= threshold → Klasse `is-active`
};
```

So weiß der HUD sofort, welche Ebene gerade dran ist – wie ein Fortschrittsbalken beim Craften."""
    )

    try_header = nbf.v4.new_markdown_cell(
        """# 🧪 Ausprobieren

Führe die nächste Zelle aus und bewege den Regler – du simulierst den Scroll im Miniatur-Wald."""
    )

    demo_code = nbf.v4.new_code_cell(
        """from IPython.core.display import HTML
HTML(\"\"\"
<style>
  .demo-shell {\n    background: #041024;\n    color: #dff6ff;\n    padding: 1.5rem;\n    border-radius: 1.5rem;\n    border: 1px solid rgba(255, 255, 255, 0.1);\n    font-family: 'Space Grotesk', system-ui;\n  }\n  .demo-stage {\n    position: relative;\n    height: 180px;\n    margin-bottom: 1rem;\n    border-radius: 1rem;\n    overflow: hidden;\n    border: 1px solid rgba(255, 255, 255, 0.15);\n    perspective: 800px;\n    background: linear-gradient(180deg, #040d21 0%, #07162c 100%);\n  }\n  .demo-layer {\n    position: absolute;\n    inset: 0;\n    will-change: transform;\n  }\n  .demo-layer--sky {\n    background: linear-gradient(180deg, #03102c 0%, #050d1c 100%);\n  }\n  .demo-layer--mountain::before {\n    content: '';\n    position: absolute;\n    inset: 0;\n    background: linear-gradient(120deg, #16305c, #112238);\n    clip-path: polygon(0% 100%, 15% 55%, 35% 85%, 55% 45%, 85% 80%, 100% 100%, 0 100%);\n  }\n  .demo-layer--trees::before {\n    content: '';\n    position: absolute;\n    inset: 0;\n    background-image: repeating-linear-gradient(-75deg, rgba(46, 162, 154, 0.7) 0%, rgba(46, 162, 154, 0.7) 8%, transparent 8%, transparent 16%);\n    opacity: 0.8;\n  }\n  .demo-label {\n    display: flex;\n    align-items: center;\n    gap: 0.75rem;\n    font-size: 0.9rem;\n  }\n  .demo-label span {\n    font-family: 'Orbitron', sans-serif;\n    letter-spacing: 0.1em;\n  }\n</style>
<div class=\"demo-shell\">\n  <div class=\"demo-stage\">\n    <div class=\"demo-layer demo-layer--sky\" data-depth=\"0.1\"></div>\n    <div class=\"demo-layer demo-layer--mountain\" data-depth=\"0.4\"></div>\n    <div class=\"demo-layer demo-layer--trees\" data-depth=\"0.9\"></div>\n  </div>\n  <label class=\"demo-label\" for=\"demo-slider\">\n    <span>Scroll</span>\n    <input id=\"demo-slider\" type=\"range\" min=\"0\" max=\"100\" value=\"0\" />\n  </label>\n</div>
<script>
  const slider = document.getElementById('demo-slider');\n  const demoLayers = document.querySelectorAll('.demo-layer');\n  slider.addEventListener('input', (event) => {\n    const value = Number(event.target.value);\n    demoLayers.forEach((layer) => {\n      const depth = Number(layer.dataset.depth);\n      const offset = (value * depth) / 5;\n      layer.style.transform = `translate3d(0, ${offset * -1}px, ${depth * -80}px)`;\n    });\n  });
</script>
\"\"\")
"""
    )

    task_intro = nbf.v4.new_markdown_cell(
        """# 🚀 Deine Aufgabe: Portalwald finalisieren

Im Verzeichnis `Tag_11/Aufgabe/` wartet eine fast fertige Version. Drei TODOs schalten die wichtigsten Tiefen-Elemente frei."""
    )

    mission = nbf.v4.new_markdown_cell(
        """## 🎯 Mission: 3 magische TODOs lösen

Schau dir immer zuerst `Tag_11/Loesung/` an, damit du genau weißt, wie die fertige Szene aussehen soll."""
    )

    todo_html = nbf.v4.new_markdown_cell(
        """### 📝 TODO 1: HTML – Mittelwald einfügen
**Datei:** `Tag_11/Aufgabe/index.html` (Zeile ~70)

Füge den fehlenden Layer wieder ein:
```html
<!-- TODO 1: ... -->
<div class=\"layer layer--midtrees\" data-depth=\"0.7\"></div>
```
Ohne diesen Layer springt der Besucher vom Hintergrund direkt in den Vordergrund – wie ein Portal ohne Zwischenraum."""
    )

    todo_css = nbf.v4.new_markdown_cell(
        """### 🎨 TODO 2: CSS – Baummuster zurückbringen
**Datei:** `Tag_11/Aufgabe/style.css` (Zeile ~200)

Der Kommentar erinnert dich daran, das komplette Regelwerk wieder aufzubauen:
```css
.layer--midtrees::before {
  background-image: repeating-linear-gradient(...);
  background-size: calc(120px - var(--tree-density) * 3px) 220px;
}
```
Nutze `var(--tree-density)`, damit der Slider später wirklich spürbar wird."""
    )

    todo_js = nbf.v4.new_markdown_cell(
        """### ⚡ TODO 3: JavaScript – Layer-HUD aktivieren
**Datei:** `Tag_11/Aufgabe/script.js` (Zeile ~44)

Im Kommentar siehst du bereits den Plan: Lies jede `data-layer-badge`, vergleiche sie mit `progress` und setze `classList.add('is-active')` oder entferne sie.

```javascript
if (progress >= threshold) {
  badge.classList.add('is-active');
} else {
  badge.classList.remove('is-active');
}
```
Dann zeigt die Liste genau, welche Ebene gerade reagiert.
"""
    )

    success = nbf.v4.new_markdown_cell(
        """## 🏆 Erfolgskontrolle

Wenn alle TODOs erledigt sind, solltest du sehen:

- Ein sanfter Übergang vom Hintergrund zum Vordergrund.
- Grün leuchtende Einträge in der Layer-Liste, sobald du scrollst.
- Der Baumdichte-Slider verändert sichtbar die Muster.
- Die Dimensionstaste schaltet die Farben ohne ruckeln um."""
    )

    testing = nbf.v4.new_markdown_cell(
        """## 🌐 Teste deine Version

1. Aufgabe öffnen: `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_11/Aufgabe/`
2. Lösung vergleichen: `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_11/Loesung/`
3. Prüfe Scroll, Slider, Button und Parallax-Galerie.
4. Wenn alles passt, committen und den nächsten Tag genießen!

⚠️ Wichtig: Öffne die Dateien immer über den Server, sonst funktionieren die Pfade und Fonts nicht korrekt."""
    )

    ideas = nbf.v4.new_markdown_cell(
        """# 🌟 Weitere Ideen

- Gib jeder Ebene eigene Geräusche, z.B. Eulen vorne und Wind hinten.
- Experimentiere mit Blur-Filtern, um Tiefe noch stärker zu zeigen.
- Lass den Slider automatisch oszillieren, damit sich der Wald selbst bewegt.
- Koppel den Dimension-Schalter an farbige Tailwind-Utilities, um schneller neue Themen zu testen."""
    )

    return [
        story,
        learning,
        essentials,
        more_concepts,
        wow_goal,
        understand_header,
        positioning,
        transforms,
        controller,
        try_header,
        demo_code,
        task_intro,
        mission,
        todo_html,
        todo_css,
        todo_js,
        success,
        testing,
        ideas,
    ]


def create_lesson():
    """Create the notebook object with all required cells."""

    nb = nbf.v4.new_notebook()
    nb.cells = build_cells()

    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as error:  # pragma: no cover
        print(f"❌ Validierungsfehler: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    """Persist the notebook in the current directory."""

    output_path = Path.cwd() / filename
    with open(output_path, "w", encoding="utf-8") as file_handle:
        nbf.write(nb, file_handle)
    print(f"✅ Lesson erfolgreich erstellt: {output_path}")
    return output_path


def main():
    """Script entrypoint."""

    print("🎄 Erstelle Lesson.ipynb...")
    print("=" * 60)
    notebook = create_lesson()
    output_path = save_notebook(notebook)
    print("=" * 60)
    print("🎉 Fertig! Lesson wurde erstellt.")
    print(f"📁 Pfad: {output_path}")


if __name__ == "__main__":
    main()
