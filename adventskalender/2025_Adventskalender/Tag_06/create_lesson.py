#!/usr/bin/env python3
"""Erstellt die Lesson.ipynb für Tag 06."""

from pathlib import Path
import sys
import nbformat as nbf

ROOT = Path(__file__).parent


def create_lesson():
    """Baue das Notebook gemäß Adventskalender-Template."""

    nb = nbf.v4.new_notebook()
    cells = []

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🎄 Tag 06 – Das lebendige Buch der Webmagie\n\nTief in der verschneiten Bibliothek von Frostquill findest du das staubige Manuskript *\"Die Geheimnisse der Webmagie – Band I\"*.\nDer Bibliothekar bittet dich, das Buch digital zu erwecken: Jede Seite nutzt strukturierten Text, gezielt platzierte Bilder\nund Turn.js, damit die Seiten beim Umblättern flüstern wie echte Pergamente."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 📚 Was du heute lernst\n\n- **Strukturierte Artikel**: Mit `<article>`, Zwischenüberschriften, `p`, `blockquote`, `em` und `strong` erzählst du Geschichten wie Kapitel.\n- **Bilder im Textfluss**: `<figure>` + `<figcaption>` bündeln Medien, während `float` und `object-fit` elegante Layouts zaubern.\n- **Turn.js Interaktion**: Du bindest die Library via CDN ein, erzeugst Page-Turn-Effekte und pflegst einen Fallback ohne JavaScript.\n- **Progressive Enhancement**: Auch ohne Skripte bleibt dein Artikel lesbar – das Buch verhält sich freundlich zu allen Spielern."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🏗️ Artikel, Text und Storytelling\n\n**`<article>` als Kapitelcontainer**\n\n```html\n<article class=\"page page-card\">\n  <h2>Kapitel 1 · Ordnung wie im Inventar</h2>\n  <p><strong>Artikel strukturieren:</strong> ...</p>\n  <blockquote>\n    &ldquo;Ohne Zwischenüberschriften blättert niemand freiwillig weiter.&rdquo;\n  </blockquote>\n</article>\n```\n\n- Quelle: `Loesung/index.html` ab Zeile 95\n- Minecraft-Analogie: `<article>` ist wie eine beschriftete Shulker-Box – alles zum Thema ist sauber einsortiert."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🌐 Bilder und Beschreibungen im Textfluss\n\n**`<figure>` + CSS-Float**\n\n```css\n.page-card figure {\n  float: right;\n  width: clamp(180px, 45%, 320px);\n  border-radius: 1rem;\n  overflow: hidden;\n}\n\n.page-card figure img {\n  object-fit: cover;\n}\n```\n\n- Quelle: `Loesung/style.css` Zeilen 97–119\n- Der float-Effekt lässt das Bild rechts schweben wie ein Item-Frame, während der Text links weitererzählt."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎨 Dein praktisches WOW-Ziel heute\n\n✅ **Realistisches Buchlayout** – Turn.js macht Seiten, die wirklich umblättern.\n\n✅ **Schwebendes Kapitelbild** – `<figure>` mit Caption erklärt das Motiv.\n\n✅ **Fortschrittsanzeige** – JavaScript liest die aktuelle Seite und aktualisiert Label + Glow-Balken.\n\n✅ **Fallback-Artikel** – Wenn JS aus ist, bleibt `#static-article` sichtbar und lesbar.\n\n**Ergebnis:** Eine magische Buchseite unter `Tag_06/Loesung/`, die aussieht wie eine verzauberte Minecraft-Geschichte und sogar ohne Skripte funktioniert."""
        )
    )

    cells.append(nbf.v4.new_markdown_cell("# 🧪 Verstehen"))

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🔍 Strukturierte Artikel verankern\n\n- In `Loesung/index.html` nutzt jedes Kapitel `<article class=\"page page-card\">`.\n- Die Hierarchie `h2` → `p` → `blockquote` sorgt für klare Abschnitte.\n- Mit `<strong>` betonst du Regeln, `<em>` hebt Stichworte hervor.\n\n```html\n<p>\n  <strong>Artikel strukturieren:</strong> ...\n  Mit <code>&lt;h2&gt;</code> bis <code>&lt;h4&gt;</code> entstehen klare Hierarchien.\n</p>\n```\n\n➡️ Überlege dir vor dem Coden, welche Abschnitte du wirklich brauchst, damit Leser nicht die Orientierung verlieren."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎨 Bilder strategisch einsetzen\n\n- Die Lösung packt das Buchfoto in `<figure>` und bringt mit `<figcaption>` sofort Kontext.\n- CSS `float: right` lässt den Text drumherum fließen.\n- `object-fit: cover` verhindert verzerrte Bilder.\n\n```html\n<figure>\n  <img src=\"...\" alt=\"Magisches Buch...\" />\n  <figcaption>Magnetisiere Leser mit sprechenden Bildunterschriften...</figcaption>\n</figure>\n```\n\n➡️ Accessibility: Das `alt`-Attribut beschreibt das Bild auch für Screenreader."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## ⚡ Turn.js + Progressive Enhancement\n\n- `Loesung/script.js` initialisiert Turn.js nur, wenn `window.jQuery.fn.turn` existiert.\n- Die Funktion `updateProgress(page, total)` aktualisiert Label, Balkenbreite und den drehenden Sigil.\n- Fallback: `enableFallback()` blendet `#static-article` ein, falls Turn.js fehlt.\n\n```javascript\nconst $book = window.jQuery('#book');\n$book.turn({\n  width,\n  height,\n  when: {\n    turning: (event, page) => updateProgress(page, $book.turn('pages'))\n  }\n});\n```\n\n➡️ So stellst du sicher, dass niemand ausgesperrt wird – ob mit oder ohne JavaScript."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🧪 Ausprobieren\nSchau dir an, wie Artikelstruktur, Figure und Fortschrittsanzeige zusammen spielen. Du kannst Buttons anklicken und sehen, wie sich Text und Layout verändern."""
        )
    )

    demo_code = """from IPython.core.display import HTML\nHTML_CODE = \"\"\"\n<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset=\"utf-8\" />\n    <style>\n      body {\n        font-family: 'Space Grotesk', sans-serif;\n        background: #0f172a;\n        color: #f8fafc;\n        padding: 24px;\n      }\n      .demo-book {\n        max-width: 540px;\n        margin: 0 auto;\n        background: rgba(15, 23, 42, 0.85);\n        border-radius: 24px;\n        border: 1px solid rgba(255, 255, 255, 0.2);\n        padding: 24px;\n      }\n      .demo-book figure {\n        float: right;\n        width: 45%;\n        margin-left: 16px;\n      }\n      .demo-book figure img {\n        width: 100%;\n        border-radius: 16px;\n        object-fit: cover;\n        box-shadow: 0 10px 25px rgba(14, 165, 233, 0.2);\n      }\n      .meter {\n        margin-top: 24px;\n        height: 10px;\n        border-radius: 999px;\n        background: rgba(255, 255, 255, 0.15);\n        overflow: hidden;\n      }\n      .meter span {\n        display: block;\n        height: 100%;\n        width: 25%;\n        background: linear-gradient(120deg, #f6d860, #22d3ee);\n        transition: width 0.3s ease;\n      }\n      .controls {\n        display: flex;\n        gap: 12px;\n        margin-top: 16px;\n      }\n      button {\n        flex: 1;\n        border: none;\n        border-radius: 999px;\n        padding: 10px;\n        font-weight: 600;\n        cursor: pointer;\n      }\n    </style>\n  </head>\n  <body>\n    <section class=\"demo-book\">\n      <article id=\"demoArticle\">\n        <h2>Demo-Kapitel</h2>\n        <figure id=\"demoFigure\">\n          <img src=\"https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=500&q=80\" alt=\"Glühendes Buch\" />\n          <figcaption>Figure + Caption erzählen, was das Bild bedeutet.</figcaption>\n        </figure>\n        <p>Dieses Mini-Kapitel nutzt <strong>&lt;article&gt;</strong>, ein schwebendes Bild und einen Fortschrittsbalken.</p>\n        <blockquote>Struktur + Style + Interaktion = Webmagie.</blockquote>\n      </article>\n      <div class=\"meter\"><span id=\"demoMeter\"></span></div>\n      <div class=\"controls\">\n        <button id=\"prevBtn\">← vorher</button>\n        <button id=\"nextBtn\">weiter →</button>\n      </div>\n    </section>\n    <script>\n      const meter = document.getElementById('demoMeter');\n      const figure = document.getElementById('demoFigure');\n      const pages = ['Deckblatt', 'Kapitel', 'Epilog'];\n      let index = 1;\n      function updateDemo() {\n        const percent = (index / (pages.length - 1)) * 100;\n        meter.style.width = percent + '%';\n        figure.style.float = index === 1 ? 'right' : 'none';\n      }\n      document.getElementById('prevBtn').addEventListener('click', () => {\n        index = Math.max(0, index - 1);\n        updateDemo();\n      });\n      document.getElementById('nextBtn').addEventListener('click', () => {\n        index = Math.min(pages.length - 1, index + 1);\n        updateDemo();\n      });\n      updateDemo();\n    </script>\n  </body>\n</html>\n\"\"\"\nHTML(HTML_CODE)\n"""

    cells.append(nbf.v4.new_code_cell(demo_code))

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🚀 Deine Aufgabe: Interaktives Buch fertigstellen\nDu hast im Ordner `Tag_06/Aufgabe/` bereits ein fast fertiges Buch. Ergänze exakt drei Stellen, damit Bild, Styles und Fortschritt wieder so glänzen wie in der Lösung."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎯 Mission: 3 magische TODOs lösen\n1. HTML – füge die Figure inklusive Caption ein.\n2. CSS – gib der Figure wieder Float + Stylings.\n3. JS – implementiere die Fortschrittslogik für Turn.js."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 📝 **TODO 1: HTML – Illustrierte Seite ergänzen**\n**Datei:** `Aufgabe/index.html` (Zeile ~112)\n\n```html\n<!-- TODO 1: Füge hier eine <figure> mit Bild + <figcaption> ein ... -->\n```\n\n- Baue `<figure>` wie in der Lösung: Bild mit `alt`-Text + sprechender Caption.\n- Tipp: Nutze dasselbe Unsplash-Bild oder ein eigenes Motiv aus der Minecraft-Welt."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🎨 **TODO 2: CSS – Figure schweben lassen**\n**Datei:** `Aufgabe/style.css` (Zeile ~97)\n\n```css\n/* TODO 2: Gestalte die <figure> so, dass sie rechts schwebt ... */\n```\n\n- Stelle `float: right`, Breite (`clamp(...)`) und `object-fit: cover` wieder her.\n- Vergiss die Caption nicht: Hintergrund, Padding und gut lesbare Schriftfarbe."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### ⚡ **TODO 3: JavaScript – Fortschritt synchronisieren**\n**Datei:** `Aufgabe/script.js` (Zeile ~60)\n\n```javascript\n// TODO 3: Nutze formatStage(page, total), berechne die Prozentbreite ...\nprogressLabel.textContent = 'TODO: Fortschritt berechnen';\nprogressFill.style.width = '20%';\n```\n\n- Ersetze den Platzhalter durch die echte Logik aus der Lösung.\n- Nutze `formatStage(page, total)` für den Text, berechne `progress` (0–1) und rufe `updateSigil(progress)` auf.\n- Optional: Wechsle die Status-Tipps wieder mit `tips`/`tipIndex` durch."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🏆 Erfolgskontrolle\n- Beim Klicken dreht Turn.js jede Seite und der Fortschrittsbalken läuft mit.\n- Seite 2 enthält wieder das Bild samt Caption und float-Effekt.\n- Die Sigil-Kugel pulsiert stärker, wenn du weiterblätterst.\n- `#static-article` bleibt nur sichtbar, wenn Turn.js wirklich fehlt."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🌐 Testen deiner Lösung\n- Aufgabe öffnen: `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_06/Aufgabe/`\n- Lösung vergleichen: `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_06/Loesung/`\n- Browser-DevTools nutzen, um `float`/`object-fit` zu prüfen.\n- Falls Turn.js-Fehler auftauchen, Screenshot & Konsole checken."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🌟 Erfolg & Möglichkeiten\nDu beherrschst jetzt strukturierte Artikel, semantische Bildtrenner und ein komplettes Page-Turn-Erlebnis.\nAls Nächstes kannst du weitere Kapitel hinzufügen, Audio-Lesungen einbetten oder das Buch als Quest-Log für\ndeine Minecraft-Welt einsetzen. Lass die Bibliothek wachsen!"""
        )
    )

    nb.cells = cells

    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as error:
        print(f"❌ Validierungsfehler: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    """Speichert das Notebook am Tag-Verzeichnis."""

    output_path = ROOT / filename
    try:
        with output_path.open("w", encoding="utf-8") as handle:
            nbf.write(nb, handle)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except OSError as error:
        print(f"❌ Fehler beim Speichern: {error}")
        sys.exit(1)


def main():
    """Entry point."""

    print("🎄 Erstelle Lesson.ipynb...")
    print("=" * 60)
    nb = create_lesson()
    output_path = save_notebook(nb)
    print("=" * 60)
    print("🎉 Fertig! Lesson wurde erstellt.")
    print(f"📁 Pfad: {output_path}")


if __name__ == "__main__":
    main()
