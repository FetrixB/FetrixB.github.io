#!/usr/bin/env python3
"""Erstellt die Lesson.ipynb für Tag 20."""

import sys
from pathlib import Path

import nbformat as nbf


def create_lesson():
    nb = nbf.v4.new_notebook()

    cells = [
        nbf.v4.new_markdown_cell(
            """# 📚 Tag 20 – Die Crafting-Station erwacht wieder zum Leben

Hey Felix! Heute rettest du die kaputte Crafting-Station der Meister-Handwerkerin. Wir bauen eine richtige **Drag & Drop UI**, bei der alle Elemente live mit `createElement` entstehen. Zusammen mit cleveren `data-*`-Attributen fühlt sich alles wie eine echte Minecraft-Workbench an."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎯 createElement + Drag & Drop = magische Werkbank

Die Elfen können nur weiterbauen, wenn die UI wieder selbst neue Slots, Karten und Rezepte erzeugt. Du lernst heute:

- wie `createElement` + `setAttribute` ganze UI-Bereiche erzeugen (`Loesung/script.js`)
- wie `data-` Attribute geheime Infos transportieren
- wie Drag-&-Drop-Events und State-Management zusammenarbeiten

**Story:** Die Crafting-Station steht im kalten Schneesturm. Ohne dynamische Slots könnten keine Rezepte mehr getestet werden. Du stellst wieder Ordnung her!"""
        ),
        nbf.v4.new_markdown_cell(
            """### 🏗️ Die wichtigsten Interface-Bausteine

**`createElement` für Inventar-Karten** 🧱

```javascript
const card = document.createElement('button');
card.className = `inventory-card text-left bg-gradient-to-br ${item.accent}`;
card.setAttribute('draggable', 'true');
card.dataset.itemId = item.id;
card.dataset.itemName = item.name;
```

Genau so baut `Loesung/script.js` jede Item-Karte. Statt HTML-Blöcke vorzuschreiben, craftet JavaScript selbst.

**Daten im Slot speichern** 🎒

```javascript
slot.dataset.itemId = item.id;
slot.dataset.itemName = item.name;
slot.dataset.filled = 'true';
slot.textContent = item.emoji;
```

Data-Attribute sind wie Notizzettel. Die Slots wissen, welches Item auf ihnen liegt und ob sie befüllt sind – perfekt für spätere Checks."""
        ),
        nbf.v4.new_markdown_cell(
            """### 🌐 Weitere wichtige Konzepte

**State-Objekt** (wer liegt wo?):

```javascript
const craftingState = {
  slots: { 'slot-1': null, 'slot-2': null, 'slot-3': null, 'slot-4': null },
  history: [],
};
```

**Rezepte prüfen:**

```javascript
const key = Object.values(craftingState.slots)
  .filter(Boolean)
  .sort()
  .join('|');
```

So erkennt die Station, ob `['scissors', 'paper']` das Geschenkpapier ergibt. Sortieren macht die Reihenfolge egal – wie beim Crafting-Grid in Minecraft."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎨 Dein praktisches WOW-Ziel heute

✅ **Drag & Drop Inventar** – Karten werden komplett per `createElement` aufgebaut.

✅ **Crafting-Gitter mit vier Slots** – inklusive Energie-Balken und Reset-Button.

✅ **Rezept-Buch** – zeigt alle Kombinationen mit Emojis und Tipps.

✅ **Live-Ergebnis** – sobald eine gültige Mischung erkannt wird, erscheint sie mit Beschreibung und Bonus-Hinweis.

**Das Ergebnis:** Eine Minecraft-ähnliche Crafting-Konsole, erreichbar unter `Tag_20/Loesung/`!"""
        ),
        nbf.v4.new_markdown_cell("""# 🧪 Verstehen"""),
        nbf.v4.new_markdown_cell(
            """## 🔍 createElement + setAttribute verstehen

Stell dir vor, du platzierst einen Block in Minecraft. `createElement` macht genau das – nur für HTML.

```javascript
const slot = document.createElement('button');
slot.className = 'crafting-slot text-white text-4xl flex items-center justify-center';
slot.setAttribute('data-slot-id', slotId);
slot.setAttribute('data-slot-label', label);
slot.setAttribute('aria-label', `Crafting Slot ${label}`);
```

Jeder Slot bekommt sofort alle Infos, die er später braucht. Dadurch kannst du ihn Drag & Drop-fähig machen, ohne irgendwo im HTML nachzupflegen."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎨 Data-Attribute = geheime Redstone-Kabel

Wenn du in `Loesung/index.html` schaust, siehst du überall Attribute wie `data-grid-panel` oder `data-result-card`. Diese Marker helfen dem Skript, die passenden Stellen zu finden. Noch wichtiger: Slots speichern eigene Infos über `dataset`:

```javascript
if (slot.hasAttribute('data-item-id')) {
  logEvent(`Slot ${slot.getAttribute('data-slot-label')} wurde überschrieben.`);
}
slot.dataset.itemId = item.id;
```

Das ist wie ein Namensschild auf einer Kiste. Ohne `dataset` wüsste das Script nie, welches Item gerade liegt."""
        ),
        nbf.v4.new_markdown_cell(
            """## ⚡ Drag & Drop Events koordinieren

Eine Drag-&-Drop-Reise besteht aus mehreren Events:

```javascript
slot.addEventListener('dragover', (event) => {
  event.preventDefault();
  slot.classList.add('ring-2', 'ring-emerald-300/60');
});

slot.addEventListener('drop', (event) => {
  event.preventDefault();
  const itemId = event.dataTransfer.getData('text/plain');
  placeItemInSlot(slot, itemId);
});
```

`event.preventDefault()` erlaubt das Ablegen, `dataTransfer` liefert den Item-Code. Danach übernimmt `placeItemInSlot()` und aktualisiert State, UI und Log."""
        ),
        nbf.v4.new_markdown_cell(
            """# 🧪 Ausprobieren

Starte die Demo unten. Ziehe Emojis auf das Feld und sieh, wie sich Daten ändern. Probier auch `Reset` aus – genau so arbeitet deine große Version im `Tag_20` Ordner."""
        ),
        nbf.v4.new_code_cell(
            '''from IPython.core.display import HTML
HTML("""
<style>
  .demo-wrap { font-family: 'Nunito', sans-serif; background: #030712; color: white; padding: 24px; border-radius: 18px; border: 1px solid rgba(255,255,255,0.1); }
  .demo-inventory { display: flex; gap: 12px; margin-bottom: 18px; }
  .demo-card { flex: 1; padding: 14px; border-radius: 16px; text-align: center; cursor: grab; border: 1px solid rgba(255,255,255,0.2); }
  .demo-grid { display: grid; grid-template-columns: repeat(2, 110px); gap: 12px; justify-content: center; margin-bottom: 12px; }
  .demo-slot { height: 110px; border-radius: 16px; border: 1px dashed rgba(255,255,255,0.4); display: flex; align-items: center; justify-content: center; font-size: 2rem; }
  .demo-slot[data-filled="true"] { border-style: solid; border-color: #00ffb2; background: rgba(0,255,178,0.08); }
  .demo-energy { width: 220px; height: 8px; border-radius: 999px; background: rgba(255,255,255,0.08); margin: 0 auto 16px; }
  .demo-energy-bar { height: 100%; width: 0%; border-radius: 999px; background: linear-gradient(90deg, #00ffb2, #ff4d6d); transition: width 300ms ease; }
</style>
<div class="demo-wrap">
  <p><strong>Mini Crafting-Station:</strong> Ziehe Emojis in das Grid und beobachte den Energiebalken.</p>
  <div class="demo-energy"><div class="demo-energy-bar" data-demo-energy></div></div>
  <div class="demo-inventory">
    <button class="demo-card" draggable="true" data-item="scissors">✂️<br/>Laser-Schere</button>
    <button class="demo-card" draggable="true" data-item="paper">📜<br/>Polar-Papier</button>
  </div>
  <div class="demo-grid">
    <div class="demo-slot" data-slot></div>
    <div class="demo-slot" data-slot></div>
    <div class="demo-slot" data-slot></div>
    <div class="demo-slot" data-slot></div>
  </div>
  <button id="demo-reset">Reset</button>
</div>
<script>
  const demoSlots = document.querySelectorAll('[data-slot]');
  const demoCards = document.querySelectorAll('.demo-card');
  const energy = document.querySelector('[data-demo-energy]');
  demoCards.forEach(card => {
    card.addEventListener('dragstart', event => {
      event.dataTransfer.setData('text/plain', card.dataset.item);
    });
  });
  demoSlots.forEach(slot => {
    slot.addEventListener('dragover', event => event.preventDefault());
    slot.addEventListener('drop', event => {
      event.preventDefault();
      const id = event.dataTransfer.getData('text/plain');
      slot.dataset.item = id;
      slot.dataset.filled = 'true';
      slot.textContent = id === 'scissors' ? '✂️' : '📜';
      updateEnergy();
    });
  });
  document.getElementById('demo-reset').addEventListener('click', () => {
    demoSlots.forEach(slot => {
      slot.textContent = '';
      slot.removeAttribute('data-item');
      slot.dataset.filled = 'false';
    });
    updateEnergy();
  });
  function updateEnergy() {
    const filled = [...demoSlots].filter(slot => slot.dataset.filled === 'true').length;
    energy.style.width = `${(filled / demoSlots.length) * 100}%`;
  }
</script>
""")
'''
        ),
        nbf.v4.new_markdown_cell(
            """# 🚀 Deine Aufgabe: Crafting-Station perfektionieren"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎯 Mission: 3 magische TODOs lösen

Im Ordner `Tag_20/Aufgabe/` wartet eine fast fertige Version. Drei Bausteine fehlen noch – du ergänzt sie Schritt für Schritt und prüfst alles direkt im Browser (`http://192.168.0.20:8000/2025_Adventskalender/Tag_20/Aufgabe/`)."""
        ),
        nbf.v4.new_markdown_cell(
            """### 📝 **TODO 1: HTML – Reset-Button ergänzen**
**Datei:** `Aufgabe/index.html` (Bereich Inventar-Header)

**Was zu tun ist:**
```html
<!-- TODO 1: Baue hier den Reset-Button mit data-reset-grid wieder ein, damit Felix alle Slots mit einem Klick leeren kann. -->
```

**Lösung:** Füge wieder einen Button mit der Klasse `btn-secondary`, dem Text `🔄 Slots räumen` und dem Attribut `data-reset-grid` hinzu. Nur dann findet `resetButton?.addEventListener(...)` den Knopf.

**Minecraft-Vergleich:** Ohne diesen Button stapeln sich Items wie lose Items auf dem Boden – du brauchst das Räum-Kommando!"""
        ),
        nbf.v4.new_markdown_cell(
            """### 🎨 **TODO 2: CSS – Energie-Balken wieder sichtbar machen**
**Datei:** `Aufgabe/style.css` (am Ende)

**Was zu tun ist:**
```css
/* TODO 2: Style hier wieder die .energy-bar ... */
```

**Lösung:** Schreib den Stil aus der Lösung hinein: linearer Farbverlauf (`var(--emerald)` ➜ `var(--nether)`), `width: 0%`, `border-radius: 999px`, `transition: width 300ms var(--transition)`. Nur so zeigt der Balken, wie viele Slots belegt sind.

**Analogie:** Der Balken ist wie deine Erfahrungsleiste. Ohne Farbe weißt du nie, wie viele Slots schon glühen!"""
        ),
        nbf.v4.new_markdown_cell(
            """### ⚡ **TODO 3: JavaScript – Rezept-Check programmieren**
**Datei:** `Aufgabe/script.js` (`evaluateRecipe` Funktion)

**Was zu tun ist:**
```javascript
  const key = filledItems
    .slice()
    .sort()
    .join('|');

  // TODO 3: Vergleiche hier den sortierten key mit den Rezepten und aktualisiere Ergebnis + Logs.
  updateResultCard();
```

**Lösung:** Implementiere wieder die Logik aus `Loesung/script.js`: suche mit `recipeBook.find(...)` nach einem Rezept, das den gleichen sortierten Schlüssel hat. Bei Treffern `updateResultCard(match, true)` und `logEvent(...)` ausführen, sonst eine Fehlermeldung zeigen. Vergiss nicht, fehlgeschlagene Kombinationen mit einem Hinweis abzudecken.

**Warum wichtig?** Ohne diese Funktion erkennt die Station kein Rezept – genau wie eine Crafting-Table ohne Rezeptbuch."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🏆 Erfolgskontrolle

Nach allen TODOs solltest du sehen:

✅ Reset-Button leert sofort die Slots.

✅ Der Energie-Balken leuchtet in Grün ➜ Pink, wenn du Items platzierst.

✅ Jede gültige Kombination (Schere+Papier, Kerze+Halter, Glocke+Redstone) zeigt sofort ein Rezept mit Beschreibung und Log-Nachricht.

✅ Die Status-Konsole listet alle Aktionen mit Uhrzeit."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🌐 Testen deiner Lösung

1. **Aufgabe öffnen:** `http://192.168.0.20:8000/2025_Adventskalender/Tag_20/Aufgabe/`
2. **Vergleich:** `http://192.168.0.20:8000/2025_Adventskalender/Tag_20/Loesung/`
3. Klicke durch alle Rezepte, aktiviere den Reset-Button und prüfe, ob der Balken reagiert.
4. Erst wenn alles identisch aussieht, bist du ready für Tag 21!"""
        ),
        nbf.v4.new_markdown_cell("""# ✨ Weitere Ideen"""),
        nbf.v4.new_markdown_cell(
            """- Baue einen dritten Inventarslot für automatische Ergebnisse.
- Lass das Ergebnis-Panel pulsieren, sobald ein Rezept fertig ist.
- Ergänze Audio-Sounds (z. B. Glocke) bei Erfolgen.
- Erstelle zusätzliche Rezepte – das Script kann beliebig viele!"""
        ),
    ]

    nb.cells = cells

    try:
        nbf.validate(nb)
    except nbf.ValidationError as exc:  # pragma: no cover
        print(f"❌ Validierungsfehler: {exc}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    script_dir = Path(__file__).resolve().parent
    output_path = script_dir / filename
    with open(output_path, "w", encoding="utf-8") as file:
        nbf.write(nb, file)
    print(f"✅ Lesson erfolgreich erstellt: {output_path}")
    return output_path


def main():
    print("🎄 Erstelle Lesson.ipynb...")
    notebook = create_lesson()
    save_notebook(notebook)


if __name__ == "__main__":
    main()
