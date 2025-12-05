#!/usr/bin/env python3
"""Erstellt Lesson.ipynb fuer Tag 19."""

from pathlib import Path
import sys

import nbformat as nbf


def create_lesson():
    nb = nbf.v4.new_notebook()

    cells = [
        nbf.v4.new_markdown_cell(
            """# 🎄 Tag 19 - DOM-Magie im Zaubererturm

Felix, du betrittst die Ruine des alten Zaubererturms und findest den legendaeren Elementarstab in drei Teilen. Der Waechter erklaert dir, dass dieser Stab wie ein JavaScript-Zauberstab funktioniert: Mit klaren Gedanken (also DOM-Befehlen) kannst du Elemente erschaffen, veraendern oder wieder verschwinden lassen. Heute reparierst du den Stab, indem du lernst, wie DOM-Manipulation funktioniert und wie Events deine Zauber ausloesen."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎯 Lerneinheit: DOM wie einen Elementarstab steuern

Du entdeckst drei grosse Kuenste:

- **DOM verstehen:** Das Document Object Model ist ein lebender HTML-Baum, den du lesen und veraendern kannst.
- **Events als Ausloeser:** Buttons, Klicks und andere Events starten deine Zaubersprueche.
- **Elemente erschaffen:** Mit `createElement`, `appendChild` und `textContent` entstehen neue Bloecke aus dem Nichts.

Alles siehst du direkt in `Tag_19/Loesung/index.html` und `Tag_19/Loesung/script.js`.
"""
        ),
        nbf.v4.new_markdown_cell(
            """### 🏗️ Die wichtigsten DOM-Magie-Bausteine

**`document.querySelector()`** - Dein Suchzauber 🔍

```javascript
const creationField = document.querySelector("#creationField");
const spellButtons = document.querySelector("#spellButtons");
```

> Wie in Minecraft, wenn du gezielt einen Block auswaehlst. Mit Query-Selektoren findest du exakt das Element im DOM, das du veraendern willst.

**`addEventListener()`** - Der Ausloeser fuer deine Rituale 🧠

```javascript
spellButtons.addEventListener("click", (event) => {
  const button = event.target.closest("[data-spell]");
  if (!button) return;
  castSpell(button.dataset.spell);
});
```

> Du koppelst einen Button an eine Funktion, genau wie du einen Redstone-Schalter an eine Schaltung anschliesst.
"""
        ),
        nbf.v4.new_markdown_cell(
            """### 🌐 Weitere starke Tricks

**Event-Delegation** - Ein einziger Listener reicht:

```javascript
spellLog.addEventListener("click", (event) => {
  if (!event.target.classList.contains("spell-log__entry")) return;
  // ...
});
```

So musst du nicht fuer jeden Log-Eintrag ein eigenes Event registrieren.

**Sichere Inhalte mit `textContent`:** Damit du keine fremden Scripts ausloest, setzt du reinen Text, statt HTML einzufuegen.
"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎨 Dein WOW-Ziel heute

✅ **Elemente beschwoeren:** Buttons erzeugen neue Karten im Bereich `#creationField`.

✅ **Elemente stylen:** Der Funkenregen-Zauber versieht Karten mit einer Glow-Animation.

✅ **Elemente entfernen:** Du kannst das letzte Element oder gleich alle Projektionen loeschen.

✅ **Magisches Logbuch:** Jedes Ereignis landet im `#spellLog` und laesst sich anklicken.

**Ergebnis:** Eine Steuerkonsole, mit der du DOM-Elemente genauso flexibel kontrollierst wie Bloecke in einer Minecraft-Welt!"""
        ),
        nbf.v4.new_markdown_cell("""# 🧪 Verstehen"""),
        nbf.v4.new_markdown_cell(
            """## 🔍 DOM-Struktur verstehen

Stell dir vor, deine HTML-Datei ist ein riesiger Baum: jeder `div` ist ein Ast, jedes `button`-Element ein Blatt. Mit DOM-Methoden kannst du:

1. **Elemente finden** (`querySelector`, `getElementById`).
2. **Kinder hinzufuegen** (`appendChild`).
3. **Eigenschaften setzen** (`classList`, `style`).

```javascript
const cardTemplate = document.getElementById("spellCard");
const fragment = cardTemplate.content.cloneNode(true);
creationField.appendChild(fragment);
```

Du vervielfaeltigst eine Vorlage wie beim Kopieren eines Minecraft-Bauplans.
"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎨 Events - so zuendest du deine Zauber

Events sind Signale. Ein Klick liefert dir ein `event`-Objekt mit Infos darueber, welcher Button gedrueckt wurde.

```javascript
spellButtons.addEventListener("click", (event) => {
  const button = event.target.closest("[data-spell]");
  if (!button) return;
  castSpell(button.dataset.spell);
});
```

`closest()` funktioniert wie ein Kompass: Er sucht vom angeklickten Element nach oben den Button mit `data-spell`. So musst du nicht jede Schaltflaeche einzeln behandeln.
"""
        ),
        nbf.v4.new_markdown_cell(
            """## ⚡ Elemente erschaffen und stylen

Neue Elemente machst du mit `document.createElement` oder - wie in der Loesung - mit einem `<template>`.

```javascript
function addLogEntry(message) {
  const entry = document.createElement("button");
  entry.className = "spell-log__entry";
  entry.textContent = message;
  spellLog.prepend(entry);
}
```

Hier nutzt du `textContent`, damit keine unerwarteten HTML-Befehle eingeschleust werden. Der Eintrag landet ganz oben im Log, weil `prepend` ihn an den Anfang setzt.
"""
        ),
        nbf.v4.new_markdown_cell(
            """# 🧪 Ausprobieren

Fuehre die naechste Zelle aus, um eine Mini-Version der Zauberkonsole direkt im Notebook zu testen."""
        ),
        nbf.v4.new_code_cell(
            """from IPython.core.display import HTML
HTML(\"\"\"
<!DOCTYPE html>
<html>
  <head>
    <style>
      body { font-family: \"Space Grotesk\", sans-serif; background:#020617; color:#e2e8f0; }
      .demo-panel { max-width: 640px; margin: 0 auto; padding: 24px; border-radius: 18px; background: rgba(15,23,42,0.9); border:1px solid rgba(45,212,191,0.3); }
      .demo-buttons { display:flex; gap:12px; flex-wrap:wrap; margin-bottom:16px; }
      .demo-buttons button { flex:1 1 140px; border-radius:12px; border:1px solid rgba(45,212,191,0.4); background:rgba(15,118,110,0.35); color:#a5f3fc; padding:10px; cursor:pointer; }
      .demo-field { min-height:140px; border-radius:16px; border:1px dashed rgba(148,163,184,0.4); padding:12px; display:grid; gap:8px; }
      .demo-card { padding:10px 12px; border-radius:12px; border:1px solid rgba(45,212,191,0.6); background:rgba(8,47,73,0.8); font-size:14px; }
    </style>
    <script>
      function addBlock(type) {
        const field = document.getElementById(\"demoField\");
        const card = document.createElement(\"div\");
        card.className = \"demo-card\";
        card.textContent = type + \" erschaffen\";
        field.prepend(card);
      }
      function clearBlocks() {
        document.getElementById(\"demoField\").innerHTML = \"\";
      }
    </script>
  </head>
  <body>
    <section class=\"demo-panel\">
      <div class=\"demo-buttons\">
        <button onclick=\"addBlock('Wald')\">🌲 Wald</button>
        <button onclick=\"addBlock('Quelle')\">💧 Quelle</button>
        <button onclick=\"clearBlocks()\">🧼 Alles loeschen</button>
      </div>
      <div id=\"demoField\" class=\"demo-field\"></div>
    </section>
  </body>
</html>
\"\"\")
"""
        ),
        nbf.v4.new_markdown_cell(
            """# 🚀 Deine Aufgabe: Der Stab will wieder funkeln"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎯 Mission: 3 magische TODOs loesen

Im Ordner `Tag_19/Aufgabe/` wartet eine fast fertige Version deiner Konsole. Ergaenze drei fehlende Teile, damit sie identisch mit `Tag_19/Loesung/` wirkt."""
        ),
        nbf.v4.new_markdown_cell(
            """### 📝 **TODO 1: HTML - Funkenregen-Schaltflaeche ergaenzen**
**Datei:** `Aufgabe/index.html` (bei den Buttons um Zeile 34)

Fuege den Button hinzu, der die Funkenregen-Stilfunktion startet:

```html
<!-- TODO 1: Fuege hier den Funkenregen-Button mit data-spell="funken" hinzu -->
```

Du brauchst denselben Aufbau wie bei den anderen Buttons (Klasse `spell-button`, Emoji, `data-spell="funken"`). Ohne ihn kann Felix den Styling-Zauber nicht ausloesen.
"""
        ),
        nbf.v4.new_markdown_cell(
            """### 🎨 **TODO 2: CSS - Glow-Animation aktivieren**
**Datei:** `Aufgabe/style.css` (unterhalb der `.spell-card--spark` Regel)

Aktiviere wieder die Klasse `.spell-card.is-charged` inklusive `@keyframes charge`, damit der Funkenregen sichtbar pulsiert. Die Loesung zeigt dir:

```css
.spell-card.is-charged {
  outline: 2px dashed rgba(250, 204, 21, 0.8);
  animation: charge 1.3s ease infinite;
  animation-delay: var(--spark, 0s);
}
```

Baue zusaetzlich die passende `@keyframes charge` Animation wieder ein.
"""
        ),
        nbf.v4.new_markdown_cell(
            """### ⚡ **TODO 3: JavaScript - Speziallogik fuer Funkenregen**
**Datei:** `Aufgabe/script.js` (in der Funktion `castSpell`)

Der Kommentar markiert die fehlende Logik. Du sollst pruefen, ob `name === "funken"` ist, dann alle vorhandenen `.spell-card` Elemente durchgehen, ihnen die Klasse `is-charged` umschalten, die CSS-Variable `--spark` setzen und einen Log-Eintrag hinzufuegen.

```javascript
if (name === "funken") {
  document.querySelectorAll(".spell-card").forEach((card, index) => {
    card.style.setProperty("--spark", `${index * 0.2}s`);
    card.classList.toggle("is-charged");
  });
  addLogEntry("⚡ Funkenregen toggled alle Karten");
  return;
}
```

So wird aus einem einfachen Button ein Styling-Zauber, genau wie in der Loesung.
"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🏆 Erfolgskontrolle

Nach allen TODOs solltest du sehen:

✅ Vier Buttons inklusive Funkenregen.

✅ Karten bekommen bei Funkenregen eine animierte Umrandung.

✅ Das Logbuch zeigt Meldungen fuer Erstellen, Loeschen und Glow-Schalter an.

✅ `creationField` leuchtet, sobald mindestens eine Karte existiert.
"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🌐 Testen deiner Loesung

**Starte die Aufgabe:**

http://192.168.0.20:8000/2025_Adventskalender/Tag_19/Aufgabe/

**Vergleiche mit der Loesung:**

http://192.168.0.20:8000/2025_Adventskalender/Tag_19/Loesung/

Oeffne beide Seiten im Browser. Achte darauf, dass du wirklich ueber den lokalen Server gehst, damit Skripte und Pfade funktionieren.
"""
        ),
        nbf.v4.new_markdown_cell(
            """# 🌟 Weitere Ideen

- Lass die Karten abhaengig vom Zauber unterschiedliche Sounds abspielen.
- Speichere das Logbuch spaeter im `localStorage`, damit es beim Reload bleibt.
- Ergaenze Slider, mit denen du ganze Waelder statt nur eines Eintrags beschwoeren kannst.
- Experimentiere mit Anime.js oder GSAP, um Karten schweben zu lassen.
"""
        ),
    ]

    nb.cells.extend(cells)

    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as exc:
        print(f"❌ Validierungsfehler: {exc}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    output_path = Path.cwd() / filename
    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            nbf.write(nb, handle)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as exc:  # pylint: disable=broad-except
        print(f"❌ Fehler beim Speichern: {exc}")
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
