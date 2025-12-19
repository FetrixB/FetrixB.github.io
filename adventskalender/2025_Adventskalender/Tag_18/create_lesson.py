#!/usr/bin/env python3
"""Erstellt das Lesson.ipynb für Tag 18 – Arrays & Loops im Eiszapfen-Vorhang."""

import nbformat as nbf
import sys
from pathlib import Path


def create_lesson():
    nb = nbf.v4.new_notebook()

    cells = []

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 📚 Tag 18 – Der singende Eiszapfen-Vorhang
Felix, die Festhalle wurde von einem Blizzard zu einer riesigen Orgel aus Eiszapfen gefroren. Jeder Kristall hat eine Länge, ein Leuchten und einen Ton. Deine Mission: Du organisierst diese Kristalle mit Arrays und Loops so geschickt, dass der Wind eine ganze Melodie daraus spielen kann!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎯 Kristall-Symphonie – Arrays + Loops
Stell dir ein Array wie eine schicke Truhe vor, in die du Eiszapfen nach Nummern einsortierst. Mit Loops wie `for` oder `for...of` läufst du an dieser Truhe entlang, ohne dabei einen Kristall zu vergessen. Genau so erzeugt `Tag_18/Loesung/index.html` die animierte Wand: Du erzeugst Daten, sortierst sie, filterst sie und lässt Buttons deine magischen Aktionen auslösen."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🏗️ Die wichtigsten JavaScript-Bausteine

**`const baseIcicles = [...]`** 📜

```javascript
const baseIcicles = [
  { id: "Polar Echo", length: 220, chill: 8, shimmer: "#67e8f9" },
  { id: "Snow Lyra", length: 170, chill: 6, shimmer: "#bae6fd" },
  // ... weitere Zapfen
];
```

So speichert `Loesung/script.js` jede Zahl und Farbe wie einzelne Minecraft-Blöcke. Jeder Eintrag ist ein Objekt – du kannst also mehrere Informationen pro Kristall kombinieren.

**`for (let index = 0; index < activeData.length; index++) { ... }`** 🔁

```javascript
for (let index = 0; index < activeData.length; index++) {
  const icicleInfo = activeData[index];
  // erstellt DOM-Elemente und setzt Höhe + Farbe
}
```

Damit malst du jeden Zapfen in der richtigen Reihenfolge an die Wand. Es fühlt sich an wie ein Redstone-Repeater, der jeden Takt genau einmal spielt."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🌐 Weitere wichtige Konzepte

**`createSparkleGrid()`** (verschachtelte Schleife für Atmosphäre):

```javascript
for (let row = 0; row < 8; row++) {
  for (let col = 0; col < 16; col++) {
    // platziert Lichtpunkte mit Animation
  }
}
```

Du erzeugst damit 128 glitzernde Partikel. Zwei Schleifen ineinander = Koordinaten in Minecraft, wenn du Zeile für Zeile ein Pixel-Bild baust."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎨 Dein praktisches WOW-Ziel heute
✅ **Interaktives Kristall-Board** – Die Bühne in `Loesung/index.html` skaliert wie eine lebendige Partitur.

✅ **Bedienfeld mit Buttons** – `Loesung/script.js` nutzt `push`, `pop`, `sort`, `filter` und Fisher-Yates-Shuffle.

✅ **Loop-Narrator-Panel** – Zeigt dir in Echtzeit, welcher Loop gerade zaubert.

✅ **Datenanalyse-Karten** – Durchschnitt, Höchstwert und Filterstatus geben dir sofort Feedback.

**Das Ergebnis:** Ein bewegter, dynamischer Eiszapfen-Vorhang, der direkt auf deine Array-Aktionen reagiert. 🎮✨"""
        )
    )

    cells.append(nbf.v4.new_markdown_cell("# 🧪 Verstehen"))

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🔍 Arrays als Inventar
Arrays helfen dir, alles ordentlich zu sammeln. In `Loesung/script.js` findest du `const baseIcicles = [...]`. Jeder Eintrag speichert Name, Länge, Kältestufe und Farbe. So kannst du später gezielt nach langen oder kurzen Zapfen suchen. Denk an deine Minecraft-Kisten: Du legst nicht jeden Smaragd einzeln auf den Boden, sondern in Slots mit Nummern – genau das machen die Indizes eines Arrays."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎨 Loops als Windmaschine
Der `for`-Loop läuft Index für Index durch das Array und baut DOM-Elemente. Ein `for...of` Loop addiert z. B. alle Längen zusammen (`updateStats()`), damit du weißt, wie stark der Vorhang gefüllt ist. Durch diese Automatisierung musst du nie jeden Zapfen einzeln anfassen – einmal programmieren, beliebig oft wiederholen!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## ⚡ Array-Methoden wie Zaubersprüche
- `push()` fügt neue Kristalle hinten an (siehe `addCluster()`)
- `pop()` entfernt den letzten Eintrag, falls ein Zapfen schmilzt
- `sort()` ordnet alles nach Länge, damit der Klang steigt oder fällt
- `filter()` zeigt nur bestimmte Zapfen (Button „extra lange anzeigen")

Jede Methode verändert das Array sofort – so fühlt es sich an, als würdest du Redstone-Schalter umlegen."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🧪 Ausprobieren
Spiel mit dem Mini-Demo unten: Füge Zapfen hinzu, sortiere sie oder filtere die langen Exemplare. Achte darauf, wie sich Text und Grafik gleichzeitig verändern – genau das passiert auch in deiner Hauptaufgabe."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            '''from IPython.core.display import HTML

display(HTML("""
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {font-family: 'Orbitron', sans-serif; background:#020617; color:#f8fafc;}
      .demo-card {border:1px solid rgba(255,255,255,0.15); border-radius:18px; padding:20px; background:rgba(15,23,42,0.8);}
      .demo-stage {display:flex; align-items:flex-end; gap:12px; min-height:120px; margin:18px 0;}
      .demo-icicle {width:28px; border-radius:12px 12px 4px 4px; background:linear-gradient(180deg,#bae6fd,#38bdf8); transition:0.3s; position:relative;}
      .demo-icicle span {position:absolute; bottom:-22px; left:50%; transform:translateX(-50%); font-size:10px; color:#a5f3fc;}
      .demo-actions {display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px;}
      button {background:#0ea5e9; border:none; border-radius:999px; color:#020617; font-weight:700; padding:10px; cursor:pointer;}
      button:hover {background:#38bdf8;}
      .demo-log {font-size:12px; color:#cbd5f5; min-height:32px;}
    </style>
  </head>
  <body>
    <div class="demo-card">
      <p id="demoStatus">Array: [120, 190, 150, 210]</p>
      <div class="demo-stage" id="demoStage"></div>
      <div class="demo-actions">
        <button id="pushDemo">push()</button>
        <button id="sortDemo">sort()</button>
        <button id="filterDemo">filter()</button>
      </div>
      <div class="demo-log" id="demoLog">Aktionen erscheinen hier...</div>
    </div>
    <script>
      const stage = document.getElementById("demoStage");
      const statusLine = document.getElementById("demoStatus");
      const demoLog = document.getElementById("demoLog");
      let lengths = [120, 190, 150, 210];

      function paintStage(data = lengths) {
        stage.innerHTML = data.map((value) => `<div class="demo-icicle" style="height:${value / 2}px"><span>${value}</span></div>`).join("");
        statusLine.textContent = `Array: [${lengths.join(", ")}]`;
      }

      document.getElementById("pushDemo").addEventListener("click", () => {
        const newLength = Math.floor(Math.random() * 90) + 120;
        lengths.push(newLength);
        paintStage();
        demoLog.textContent = `push() hat ${newLength} cm angehängt.`;
      });

      document.getElementById("sortDemo").addEventListener("click", () => {
        lengths.sort((a, b) => a - b);
        paintStage();
        demoLog.textContent = "sort() ordnet von klein nach groß.";
      });

      document.getElementById("filterDemo").addEventListener("click", () => {
        const filtered = lengths.filter((value) => value >= 180);
        paintStage(filtered);
        demoLog.textContent = `filter() zeigt nur Zapfen >= 180 cm (${filtered.length} Stück).`;
      });

      paintStage();
    </script>
  </body>
</html>
"""))
'''
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            "# 🚀 Deine Aufgabe: Lücken im Kristall-Labor schließen!"
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎯 Mission: 3 magische TODOs lösen
Im Ordner `Tag_18/Aufgabe/` wartet eine fast fertige Version. Drei Lücken bremsen den Zauber. Wenn du sie füllst, verhält sich alles genau wie die Musterlösung in `Tag_18/Loesung/`."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 📝 **TODO 1: HTML – Der Loop-Narrator fehlt**
**Datei:** `Aufgabe/index.html` (~Zeile 70)

Du siehst dort den Kommentar:
```html
<!-- TODO 1: Baue hier einen zweiten Artikel ... -->
```
Füge an dieser Stelle einen zweiten `<article>` mit Überschrift "Loop-Narrator" ein. Darin brauchst du den Textabsatz und ein `<div class="loop-console" id="loopNarration">`. Erst dann kann das Skript seine Log-Meldungen anzeigen."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🎨 **TODO 2: CSS – Glitzer-Effekt aktivieren**
**Datei:** `Aufgabe/style.css` (~Zeile 80)

Dort ist der Kommentar
```css
/* TODO 2: ... ::after-Element ... */
```
Ersetze ihn durch die `::after`-Regel und die Hover-Version. Nutze einen radialen Verlauf und erhöhe die `opacity` beim Hover. Damit glänzen die Zapfen wieder, wenn Felix mit der Maus darüber fährt."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### ⚡ **TODO 3: JavaScript – Filter-Button programmieren**
**Datei:** `Aufgabe/script.js` (~Zeile 170)

Die Funktion `toggleFilter()` enthält nur einen Kommentar. Du musst:
1. `filterLongOnly` umschalten (`true` ↔︎ `false`).
2. Den Button-Text (`filterToggle.textContent`) passend setzen.
3. Eine Log-Zeile mit `logLoop(...)` schreiben.
4. `renderAll()` aufrufen, damit das UI reagiert.

Schau dir die fertige Version in `Loesung/script.js` an, wenn du einen Tipp brauchst."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🏆 Erfolgskontrolle
✅ Die Log-Konsole zeigt wieder Nachrichten an.

✅ Beim Hover glitzern die Zapfen und fühlen sich "icy" an.

✅ Der Filter-Button zeigt nur noch Zapfen ≥ 180 cm, inklusive Status-Text.

✅ Deine Seite sieht wie `Tag_18/Loesung/` aus und reagiert gleich schnell."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🌐 Testen deiner Lösung
**Aufgabe öffnen:** `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_18/Aufgabe/`

**Mit Lösung vergleichen:** `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_18/Loesung/`

Starte außerdem `node --check Tag_18/Aufgabe/script.js`, damit du sicher bist, dass keine Tippfehler im JavaScript stecken."""
        )
    )

    cells.append(nbf.v4.new_markdown_cell("# Weitere Ideen"))

    cells.append(
        nbf.v4.new_markdown_cell(
            """- Lass besonders lange Zapfen pulsieren, indem du Klassen aus Tailwind ergänzt.
- Experimentiere mit zusätzlichen Array-Methoden wie `map()` für Farbstufen.
- Lass die Buttons Sounds abspielen, wenn du sortierst oder filterst.
- Baue eine kleine "Playlist" für verschiedene Blizzard-Patterns mit gespeicherten Arrays."""
        )
    )

    nb.cells = cells

    try:
        nbf.validate(nb)
    except nbf.ValidationError as err:
        print(f"❌ Validierungsfehler: {err}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
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
    nb = create_lesson()
    save_notebook(nb)
    print("🎉 Fertig! Lesson wurde erstellt.")


if __name__ == "__main__":
    main()
