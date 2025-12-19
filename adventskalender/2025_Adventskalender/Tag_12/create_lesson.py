#!/usr/bin/env python3
"""Erzeugt Lesson.ipynb für Tag 12."""

import sys
from pathlib import Path

import nbformat as nbf


def build_cells():
    """Erstellt alle Notebook-Zellen für Tag 12."""

    story = nbf.v4.new_markdown_cell(
        """# 🎄 Tag 12 · Der zerstörte Frosttempel

Felix, die Frost-Priesterin führt dich durch zerborstene Glasplatten. "Diese Wände bestanden aus hauchdünnem Eisglas mit Glow", erklärt sie. Du erkennst sofort: Das ist Glasmorphismus – halbtransparente Paneele, sanfter Blur, Glow und Licht, das wie Nordlichter tanzt. Heute reparierst du den Tempel digital, damit alle Besucher*innen wieder in der schimmernden Halle lernen können."""
    )

    learning = nbf.v4.new_markdown_cell(
        """## 🎯 Lern-Checkpoint

- **Glasmorphismus verstehen**: `backdrop-filter`, Transparenzen und Layer, damit Elemente wie Glas wirken.
- **Schatten-Strategien**: Unterschied zwischen `box-shadow` (Paneel) und `drop-shadow` (SVG/Icon).
- **Custom Properties in Aktion**: `--panel-hue` oder `--frost-blur` bündeln Designwerte und lassen sich per JS live ändern.
- **Fallbacks & Barrierefreiheit**: `@supports`-Block in `style.css` erklärt Besucher*innen ohne Filter, was passiert."""
    )

    essentials = nbf.v4.new_markdown_cell(
        """### 🏗️ Die wichtigsten Bausteine aus `Tag_12/Loesung/`

**`<section class=\"control-panel glass-panel\">`** – steuert Blur, Glow und Farben (siehe `index.html` Zeile ~27):
```html
<label for=\"blurRange\" class=\"control\">
  <span>Frostlevel (Blur)</span>
  <input id=\"blurRange\" type=\"range\" min=\"5\" max=\"40\" value=\"26\" />
</label>
```
So ähnlich wie ein Redstone-Poti: Ein Dreh (Schieberegler) ändert alle Paneele gleichzeitig.

**`.glass-panel`** – Herzstück des Glasmorphismus (`style.css` Zeile ~44):
```css
.glass-panel {
  background: rgba(5, 15, 28, var(--glass-alpha));
  border: 1px solid rgba(255, 255, 255, var(--border-alpha));
  backdrop-filter: blur(var(--frost-blur)) saturate(140%) contrast(115%);
}
```
Diese Kombination legt halbtransparente Eisflächen mit klarer Outline an.

**`updateBlur()`** – JavaScript-Kontrolle (`script.js` Zeile ~38):
```javascript
const updateBlur = (value) => {
  root.style.setProperty("--frost-blur", `${value}px`);
  blurValue.textContent = `Frost-Level: ${value}px Blur`;
};
```
Wie ein Minecraft-Schieber für Partikel: Ein Wert steuert gleich mehrere Anzeige-Elemente."""
    )

    more_concepts = nbf.v4.new_markdown_cell(
        """### 🌐 Weitere wichtige Konzepte

- **Transparenz-Hierarchie** (`Tag_12/Loesung/index.html` · Abschnitt "Transparenz-Hierarchie"): Drei Layer mit 10/35/70 % Opazität vermitteln Tiefe.
- **Fallback-Strategie** (`style.css` Zeile ~174): `@supports not (backdrop-filter: ...)` informiert Besucher*innen, falls ihr Browser die Eis-Effekte nicht kennt.
- **Theme-System** (`script.js` Zeile ~15): `themes.aurora`, `themes.moonstone`, `themes.ember` speichern Farbwerte und Glow-Intensitäten.
- **Diagnostik-Anzeigen**: `#transparencyBar` nutzt lineare Gradients als Fortschrittsbalken und reagiert direkt auf das Slider-Ereignis."""
    )

    wow_goal = nbf.v4.new_markdown_cell(
        """## 🎨 Dein WOW-Ziel heute

✅ **Kontrollzentrale** – Slider, Glow-Toggle und Farbknöpfe fühlen sich wie ein echtes Tempel-HUD an.

✅ **Schimmernde Glas-Paneele** – Jede Karte reagiert auf Custom Properties, sodass Themes sofort wechseln.

✅ **Shadow-Labor** – Du siehst live, warum `box-shadow` Flächen und `drop-shadow` nur transparente Icons betrifft.

✅ **Transparenz-Treppe** – Unterschiedliche Deckkräfte erzeugen Tiefe wie gestapelte Eisschichten.

**Endergebnis:** Ein frostiges UI, das Felix klar zeigt, wie moderne Glas-Effekte im Web gebaut werden. 🎮✨"""
    )

    understand_header = nbf.v4.new_markdown_cell("""# 🧪 Verstehen""")

    concept_one = nbf.v4.new_markdown_cell(
        """## 🔍 Glasmorphismus = gestapelte Eisplatten

Genau wie du in Minecraft mehrere Glasblöcke übereinander legst, braucht Glasmorphismus mehrere Layer:

```css
.glass-panel::before {
  background: linear-gradient(135deg, hsla(var(--panel-hue), 90%, 70%, 0.4), transparent);
  opacity: var(--glow-strength);
}
```

- **`rgba()` Hintergrund** sorgt für leichte Tönung.
- **`backdrop-filter`** verwischt alles dahinter → wirkt wie echtes Glas.
- **Pseudo-Element** liefert einen Lichtstreifen, damit der Block lebendig aussieht."""
    )

    concept_two = nbf.v4.new_markdown_cell(
        """## 🎨 Schatten & Blur-Ketten kombinieren

Box-Shadow und Drop-Shadow sind wie zwei verschiedene Zauberstäbe:

```css
.shadow-card--box .panel-demo {
  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.45);
}

.shadow-card--drop svg {
  filter: drop-shadow(0 15px 35px rgba(93, 241, 255, 0.45));
}
```

- `box-shadow` schiebt die ganze Fläche nach vorne, perfekt für Karten.
- `drop-shadow` folgt nur der Form des SVGs – ideal für Glyphen, damit es scheint, als schwebten sie wirklich über dem Eis."""
    )

    concept_three = nbf.v4.new_markdown_cell(
        """## ⚡ Custom Properties + Controller

`script.js` behandelt Custom Properties wie Inventar-Slots, die du auf einen Schlag austauschst:

```javascript
const applyTheme = (themeKey) => {
  const data = themes[themeKey];
  root.style.setProperty("--panel-hue", data.hue);
  root.style.setProperty("--accent-1", data.accents[0]);
};
```

Alle Paneele lesen später einfach `var(--panel-hue)` – dadurch wechseln Farben sofort, ohne dass du 20 Klassen anfassen musst."""
    )

    try_intro = nbf.v4.new_markdown_cell(
        """# 🧪 Ausprobieren

Starte den Mini-Controller unten und beobachte, wie Blur und Glow zusammenarbeiten."""
    )

    demo_code = nbf.v4.new_code_cell(
        """from IPython.core.display import HTML
HTML(\"\"\"
<style>
  .mini-lab {\n    font-family: 'Space Grotesk', system-ui;\n    background: linear-gradient(160deg, #041225, #071d32);\n    border-radius: 1.5rem;\n    padding: 1.5rem;\n    color: #f7fbff;\n    border: 1px solid rgba(255, 255, 255, 0.2);\n    max-width: 580px;\n  }\n  .mini-glass {\n    background: rgba(255, 255, 255, 0.12);\n    border: 1px solid rgba(255, 255, 255, 0.35);\n    border-radius: 1.2rem;\n    padding: 1.25rem;\n    backdrop-filter: blur(var(--demo-blur, 18px)) saturate(150%);\n    -webkit-backdrop-filter: blur(var(--demo-blur, 18px)) saturate(150%);\n    box-shadow: 0 18px 40px rgba(5, 17, 30, 0.55);\n    transition: backdrop-filter 0.2s ease;\n  }\n  .mini-meta {\n    display: flex;\n    gap: 0.75rem;\n    align-items: center;\n    margin-top: 1rem;\n  }\n  .mini-meta span {\n    font-family: 'Orbitron', sans-serif;\n  }\n  .mini-meta input {\n    flex: 1;\n  }\n</style>
<div class=\"mini-lab\">
  <div class=\"mini-glass\" id=\"mini-glass\">
    <strong>Frost-Diagnose</strong>
    <p>Mehr Blur = milchigeres Glas, weniger Blur = transparentes HUD.</p>
  </div>
  <div class=\"mini-meta\">
    <span id=\"mini-readout\">18px Blur</span>
    <input type=\"range\" id=\"mini-slider\" min=\"8\" max=\"40\" value=\"18\" />
  </div>
</div>
<script>
  const miniSlider = document.getElementById('mini-slider');\n  const miniGlass = document.getElementById('mini-glass');\n  const miniReadout = document.getElementById('mini-readout');\n  miniSlider.addEventListener('input', (event) => {\n    const value = `${event.target.value}px`;\n    miniGlass.style.setProperty('--demo-blur', value);\n    miniReadout.textContent = `${value} Blur`;\n  });
</script>
\"\"\")
"""
    )

    task_intro = nbf.v4.new_markdown_cell(
        """# 🚀 Deine Aufgabe: Glas-Paneele polieren

Im Verzeichnis `Tag_12/Aufgabe/` wartet die fast fertige Rekonstruktion. Drei gezielte TODOs starten Glow, Themes und Controller."""
    )

    mission = nbf.v4.new_markdown_cell(
        """## 🎯 Mission: 3 magische TODOs lösen

Nutze `Tag_12/Loesung/` als Referenz, damit du genau siehst, wie die fertigen Paneele aussehen und reagieren sollen."""
    )

    todo_html = nbf.v4.new_markdown_cell(
        """### 📝 TODO 1: HTML – Theme-Buttons platzieren
**Datei:** `Tag_12/Aufgabe/index.html` (Abschnitt Frost-Controller)

Der Kommentar erinnert dich daran, die drei Farbknöpfe einzufügen:
```html
<div class=\"theme-buttons\">
  <button data-theme=\"aurora\" class=\"is-active\">Aurora</button>
  <button data-theme=\"moonstone\">Mondstein</button>
  <button data-theme=\"ember\">Polar-Glut</button>
</div>
```
Ohne sie kann Felix keine Palette wählen – der Tempel bleibt farblos."""
    )

    todo_css = nbf.v4.new_markdown_cell(
        """### 🎨 TODO 2: CSS – Backdrop-Filter aktivieren
**Datei:** `Tag_12/Aufgabe/style.css` (`.glass-panel` Regel)

Der Kommentar wartet darauf, dass du Folgendes ergänzt:
```css
backdrop-filter: blur(var(--frost-blur)) saturate(140%) contrast(115%);
-webkit-backdrop-filter: blur(var(--frost-blur)) saturate(140%) contrast(115%);
```
Erst damit wirkt das Paneel wie durchsichtiges Eis und nicht wie eine matte Fläche."""
    )

    todo_js = nbf.v4.new_markdown_cell(
        """### ⚡ TODO 3: JavaScript – `updateBlur` füllen
**Datei:** `Tag_12/Aufgabe/script.js`

Im Kommentar steht genau, was fehlt:
```javascript
root.style.setProperty("--frost-blur", `${rounded}px`);
blurValue.textContent = `Frost-Level: ${rounded}px Blur`;
transparencyBar.style.width = `${percent}%`;
```
Außerdem soll `contrastBadge` zwischen den drei Texten wechseln. Danach reagiert der komplette HUD wieder auf deine Eingaben."""
    )

    success = nbf.v4.new_markdown_cell(
        """## 🏆 Erfolgskontrolle

Nach allen TODOs solltest du sehen:

- Slider verändert Blur UND Textanzeige.
- Theme-Buttons wechseln Farben + Glow sofort.
- Paneele wirken tatsächlich wie Eisglas statt wie matte Karten.
- Das Shadow-Labor zeigt klar den Unterschied der beiden Schattenarten."""
    )

    testing = nbf.v4.new_markdown_cell(
        """## 🌐 Testen

1. Aufgabe öffnen: `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_12/Aufgabe/`
2. Lösung vergleichen: `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_12/Loesung/`
3. Prüfe Slider, Glow-Taste, Theme-Buttons und die Transparenz-Balken.
4. Stelle sicher, dass auch mit `prefers-reduced-motion` alles ruhig bleibt – das haben wir bereits vorbereitet."""
    )

    ideas = nbf.v4.new_markdown_cell(
        """# 🌟 Weitere Ideen

- Lass den Glow automatisch pulsieren, indem du `setInterval` auf `--glow-strength` anwendest.
- Verbinde die frostigen Werte mit einem Audio-Feedback (z.B. Klingeln beim Theme-Wechsel).
- Ergänze weitere Layer mit `drop-shadow` für Schneeflocken, um Tiefenwirkung zu steigern.
- Nutze Tailwind-Utilities (z.B. `backdrop-blur-xl`) direkt auf neuen Elementen, um noch schneller Layouts zu testen."""
    )

    return [
        story,
        learning,
        essentials,
        more_concepts,
        wow_goal,
        understand_header,
        concept_one,
        concept_two,
        concept_three,
        try_intro,
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
    """Notebook erzeugen und validieren."""

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
    """Speichert das Notebook im Tag-Verzeichnis."""

    base_dir = Path(__file__).resolve().parent
    output_path = base_dir / filename
    with open(output_path, "w", encoding="utf-8") as handle:
        nbf.write(nb, handle)
    print(f"✅ Lesson erfolgreich erstellt: {output_path}")
    return output_path


def main():
    """Script Entry."""

    print("🎄 Erstelle Lesson.ipynb...")
    print("=" * 60)
    notebook = create_lesson()
    output_path = save_notebook(notebook)
    print("=" * 60)
    print("🎉 Fertig! Lesson wurde erstellt.")
    print(f"📁 Pfad: {output_path}")


if __name__ == "__main__":
    main()
