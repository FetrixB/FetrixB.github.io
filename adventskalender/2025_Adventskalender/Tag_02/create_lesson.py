#!/usr/bin/env python3
"""
Erstellt die Lesson.ipynb für Tag 02.
"""

import nbformat as nbf
import sys
from pathlib import Path


STORY_TITLE = "# 🎄 Tag 02 – Portalenergie im Dorfkern"
STORY_TEXT = (
    "Die Elfen haben das riesige Portal auf dem Dorfplatz verloren: Ohne Block-"
    "und Inline-Magie kann niemand mehr zwischen den Dimensionen reisen. "
    "Du sollst die Struktur neu sortieren, die Glow-Animationen anwerfen und "
    "lernst dabei, wie `<div>` und `<span>` zusammenarbeiten."
)


def create_lesson():
    """Erstellt ein inhaltlich gefülltes Notebook entsprechend agenten_kontext."""

    nb = nbf.v4.new_notebook()
    cells = [
        nbf.v4.new_markdown_cell(f"{STORY_TITLE}\n\n{STORY_TEXT}"),
        nbf.v4.new_markdown_cell(
            "## 🎯 Block- & Inline-Magie – Portalstruktur meistern\n\n"
            '- Baue stabile Abschnitte mit Block-Elementen (z.B. `<div id="portalFrame">`).\n'
            '- Lass Kristalle als Inline-Elemente (`<span class="portal-crystal">◈</span>`) nebeneinander schweben.\n'
            "- Nutze IDs für Unikate, Klassen für wiederholte Kristalle.\n"
            "- Verbinde Tailwind-Utilities, eigene CSS-Regeln und Animate.css für Glow und Puls."
        ),
        nbf.v4.new_markdown_cell(
            "### 🏗️ Die wichtigsten HTML-Elemente:\n\n"
            '**`<div id="portalFrame">`** 📜\n\n'
            "Der Rahmen ist ein Block-Element, das den gesamten Bereich beansprucht – genau wie ein Obsidian-Ring in Minecraft.\n\n"
            "```html\n"
            '<div id="portalFrame" class="portal-frame">\n'
            '  <div id="portalEnergy" class="portal-energy">\n'
            '    <span class="portal-crystal">◈</span>\n'
            "  </div>\n"
            "</div>\n"
            "```\n\n"
            '**`<span class="portal-crystal">`** 📝\n\n'
            "Inline-Elemente bleiben so breit wie ihr Inhalt. Dadurch tanzen die Kristalle Seite an Seite, ohne sich gegenseitig wegzuschubsen."
        ),
        nbf.v4.new_markdown_cell(
            "### 🌐 CSS-Glow, IDs & Animate.css\n\n"
            "**Glow-Style (`box-shadow`)**: Mehrere Schattenlayer lassen das Portal wie Nether-Lava flackern.\n\n"
            "```css\n"
            "#portalFrame {\n"
            "  box-shadow: inset 0 0 25px rgba(247, 113, 236, 0.35);\n"
            "}\n"
            "```\n\n"
            "**Animate.css Klassen**: `animate__pulse` hält die Energie in Bewegung, ohne dass wir eigenen Keyframe-Code schreiben müssen."
        ),
        nbf.v4.new_markdown_cell(
            "## 🎨 Dein praktisches WOW-Ziel heute:\n\n"
            "✅ **Glow-Rahmen** – das Portal strahlt wie echtes Obsidian-Licht.\n\n"
            "✅ **Kristallwolken** – Inline-Elemente bilden bewegliche Reihen.\n\n"
            "✅ **Statusanzeige** – JavaScript reagiert auf Klicks und Hover.\n\n"
            "✅ **Portal-Button** – aktiviert zusätzliche Sparkles und Animationen.\n\n"
            "**Das Ergebnis:** Eine pulsierende Seite (`Loesung/index.html`), die den Unterschied zwischen Block- und Inline-Elementen sichtbar macht."
        ),
        nbf.v4.new_markdown_cell("# 🧪 Verstehen"),
        nbf.v4.new_markdown_cell(
            "## 🔍 Block-Elemente = Obsidian-Rahmen\n\n"
            "Stell dir `<div>` wie einen vollständigen Block vor: Er beginnt in einer neuen Zeile und spannt sich über die gesamte Breite.\n"
            "So können wir den Rahmen mit einer ID ausstatten und später im CSS ganz gezielt stylen.\n\n"
            "```html\n"
            '<div id="portalFrame" class="portal-frame">\n'
            "  <!-- Hier wohnen alle Inline-Kristalle -->\n"
            "</div>\n"
            "```\n"
            "Wenn du mehrere Abschnitte brauchst, erstellst du einfach weitere Block-Elemente – wie neue Plattformen in Minecraft."
        ),
        nbf.v4.new_markdown_cell(
            "## 🎨 Inline-Kristalle & Klassen\n\n"
            "Kristalle sind `<span>`-Elemente. Sie bleiben inline, also direkt neben ihren Nachbarn.\n"
            "Mit der Klasse `.portal-crystal` gibst du allen Kristallen in einem Schritt dieselbe Farbe, Größe und denselben Glow.\n\n"
            "```css\n"
            ".portal-crystal {\n"
            "  display: inline-block;\n"
            "  padding: 0.35rem 0.85rem;\n"
            "  box-shadow: 0 0 15px rgba(176, 115, 255, 0.5);\n"
            "}\n"
            "```\n"
            "IDs (`#portalFrame`) vs. Klassen (`.portal-crystal`): IDs verwendest du einmal, Klassen beliebig oft."
        ),
        nbf.v4.new_markdown_cell(
            "## ⚡ JavaScript steuert den Glow\n\n"
            "In `Loesung/script.js` reagiert ein Klick auf den Button `#portalButton` und toggelt eine CSS-Klasse.\n"
            "Parallel erzeugt `createSparkle()` kleine Partikel, sobald das Portal aktiv ist.\n\n"
            "```javascript\n"
            "function togglePortal() {\n"
            "  portalActive = !portalActive;\n"
            '  portalEnergy.classList.toggle("portal-energy-active", portalActive);\n'
            "}\n"
            "```\n"
            "So siehst du perfekt, wie HTML-Struktur, CSS-Klassen und JavaScript zusammenspielen."
        ),
        nbf.v4.new_markdown_cell(
            "# 🧪 Ausprobieren\n\n"
            "Starte die Demo, klicke auf Kristalle und beobachte, wie Block- und Inline-Elemente miteinander funktionieren."
        ),
        nbf.v4.new_code_cell(
            "from IPython.core.display import HTML\n"
            'display(HTML("""\n'
            "<!DOCTYPE html>\n"
            "<html>\n"
            "  <head>\n"
            "    <style>\n"
            "      body {\n"
            "        font-family: 'Space Grotesk', sans-serif;\n"
            "        background: #090515;\n"
            "        color: #f5f4ff;\n"
            "        padding: 20px;\n"
            "      }\n"
            "      .demo-frame {\n"
            "        border: 5px solid rgba(139, 92, 246, 0.9);\n"
            "        border-radius: 18px;\n"
            "        padding: 18px;\n"
            "        background: linear-gradient(145deg, rgba(118, 0, 255, 0.6), rgba(255, 0, 142, 0.5));\n"
            "        box-shadow: 0 0 20px rgba(143, 101, 255, 0.6);\n"
            "        position: relative;\n"
            "        overflow: hidden;\n"
            "      }\n"
            "      .demo-crystals span {\n"
            "        display: inline-block;\n"
            "        margin: 0 6px 6px 0;\n"
            "        padding: 6px 12px;\n"
            "        border-radius: 12px;\n"
            "        background: rgba(255,255,255,0.08);\n"
            "        box-shadow: 0 0 10px rgba(255, 255, 255, 0.35);\n"
            "        cursor: pointer;\n"
            "        transition: transform 0.3s ease;\n"
            "      }\n"
            "      .demo-crystals span:hover {\n"
            "        transform: translateY(-4px) scale(1.05);\n"
            "      }\n"
            "      .demo-status {\n"
            "        margin-top: 12px;\n"
            "        font-size: 0.95rem;\n"
            "        color: #b0ffea;\n"
            "      }\n"
            "      .demo-frame.active {\n"
            "        border-color: #ffe394;\n"
            "        box-shadow: 0 0 20px rgba(255, 227, 148, 0.7);\n"
            "      }\n"
            "      button {\n"
            "        margin-top: 12px;\n"
            "        padding: 8px 18px;\n"
            "        border-radius: 999px;\n"
            "        border: none;\n"
            "        background: linear-gradient(120deg, #8b5cf6, #f472b6);\n"
            "        color: #fff;\n"
            "        font-weight: 600;\n"
            "        cursor: pointer;\n"
            "      }\n"
            "    </style>\n"
            "  </head>\n"
            "  <body>\n"
            '    <div id="demoFrame" class="demo-frame">\n'
            '      <div class="demo-crystals">\n'
            '        <span data-message="Kristall A sendet Funken">◈</span>\n'
            '        <span data-message="Kristall B summt">◈</span>\n'
            '        <span data-message="Kristall C lädt Energie">◈</span>\n'
            "      </div>\n"
            '      <p id="demoStatus" class="demo-status">Tippe auf einen Kristall.</p>\n'
            "    </div>\n"
            '    <button onclick="window.toggleDemoPortal()">Portal starten</button>\n'
            "    <script>\n"
            "      const demoFrame = document.getElementById('demoFrame');\n"
            "      const demoStatus = document.getElementById('demoStatus');\n"
            "      let demoActive = false;\n"
            "      window.toggleDemoPortal = function() {\n"
            "        demoActive = !demoActive;\n"
            "        demoFrame.classList.toggle('active', demoActive);\n"
            "        demoStatus.textContent = demoActive ? 'Portal pulsiert!' : 'Portal ruht...';\n"
            "      };\n"
            "      document.querySelectorAll('.demo-crystals span').forEach((span) => {\n"
            "        span.addEventListener('mouseenter', () => {\n"
            "          demoStatus.textContent = span.dataset.message;\n"
            "        });\n"
            "      });\n"
            "    </script>\n"
            "  </body>\n"
            "</html>\n"
            '"""))'
        ),
        nbf.v4.new_markdown_cell("# 🚀 Deine Aufgabe: Portal-Training meistern"),
        nbf.v4.new_markdown_cell(
            "## 🎯 Mission: 3 magische TODOs lösen\n\n"
            "Im Ordner `Aufgabe/` liegt deine fast fertige Seite. Ergänze die TODOs und vergleiche sie anschließend mit `Loesung/`."
        ),
        nbf.v4.new_markdown_cell(
            "### 📝 **TODO 1: HTML – Zweite Kristallreihe ergänzen**\n"
            "**Datei:** `Aufgabe/index.html` (Bereich rund um Zeile 37)\n\n"
            "**Was zu tun ist:**\n"
            "```html\n"
            "<!-- TODO 1 ... -->\n"
            "```\n"
            'Nutze vier neue `<span class="portal-crystal">◈</span>` Elemente mit eigenen `data-message` Texten. So erkennst du direkt, dass Inline-Elemente nebeneinander stehen können.\n\n'
            "**Tipp:** Schau dir in `Loesung/index.html` an, wie die zweite `.crystal-row` aufgebaut ist."
        ),
        nbf.v4.new_markdown_cell(
            "### 🎨 **TODO 2: CSS – Aktivierten Glow stylen**\n"
            "**Datei:** `Aufgabe/style.css` (Abschnitt `.portal-energy-active`)\n\n"
            "**Was zu tun ist:**\n"
            "```css\n"
            ".portal-energy-active {\n"
            "  /* TODO 2: ... */\n"
            "}\n"
            "```\n"
            "Fülle die Regel mit einem helleren `box-shadow` und einem auffälligen Verlauf. Dadurch sieht Felix sofort, wann das Portal aktiv ist.\n\n"
            "**Tipp:** Werte aus der Lösung übernehmen, dann Schritt für Schritt anpassen."
        ),
        nbf.v4.new_markdown_cell(
            "### ⚡ **TODO 3: JavaScript – Status per Hover aktualisieren**\n"
            "**Datei:** `Aufgabe/script.js` (unter `crystal.addEventListener('mouseenter', ...)`)\n\n"
            "**Was zu tun ist:**\n"
            "```javascript\n"
            "// TODO 3: updateStatus(message) aufrufen\n"
            "```\n"
            "Sobald ein Kristall berührt wird, soll `updateStatus(message)` laufen. So zeigt die Statusanzeige die passende Nachricht aus `data-message` an.\n\n"
            "**Kontrolle:** In `Loesung/script.js` findest du die fertige Variante."
        ),
        nbf.v4.new_markdown_cell(
            "## 🏆 Erfolgskontrolle\n\n"
            "✅ Zwei Kristallreihen schweben nebeneinander.\n\n"
            "✅ Der Glow verändert sich sichtbar beim Aktivieren.\n\n"
            "✅ Hover auf einem Kristall schreibt eine neue Statusmeldung.\n\n"
            "✅ Der Start-Button toggelt Portal und Sparkles ohne Fehler."
        ),
        nbf.v4.new_markdown_cell(
            "## 🌐 Testen deiner Lösung\n\n"
            "1. Öffne `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_02/Aufgabe/` in deinem Browser.\n"
            "2. Klicke auf den Button, beobachte den Glow und bewege den Mauszeiger über die Kristalle.\n"
            "3. Vergleiche anschließend mit `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_02/Loesung/`.\n"
            "4. Wenn alles identisch aussieht, bist du bereit für Tag 03!"
        ),
        nbf.v4.new_markdown_cell("# 🌟 Erfolg & Möglichkeiten"),
        nbf.v4.new_markdown_cell(
            "- Variiere Farben oder Schatten, um unterschiedliche Dimensionen darzustellen.\n"
            "- Lass Kristalle verschwinden oder erscheinen, sobald du sie anklickst.\n"
            "- Kombiniere mehrere Block-Container zu einem ganzen Portal-Layout.\n"
            "- Schreibe eigene Keyframes für noch verrücktere Glow-Effekte."
        ),
    ]

    nb.cells = cells

    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as exc:
        print(f"❌ Validierungsfehler: {exc}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    """Speichert das Notebook im aktuellen Verzeichnis."""

    output_path = Path(__file__).parent / filename

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            nbf.write(nb, file)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as exc:
        print(f"❌ Fehler beim Speichern: {exc}")
        sys.exit(1)


def main():
    """CLI-Einstiegspunkt."""

    print("🎄 Erstelle Lesson.ipynb...")
    nb = create_lesson()
    output_path = save_notebook(nb)
    print("🎉 Fertig! Lesson wurde erstellt.")
    print(f"📁 Pfad: {output_path}")


if __name__ == "__main__":
    main()
