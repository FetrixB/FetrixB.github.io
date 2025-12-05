#!/usr/bin/env python3
"""Erstellt Lesson.ipynb für Tag 09 mit Story, Theorie, Demos und Aufgaben."""

import nbformat as nbf
import sys
from pathlib import Path


def create_lesson():
    """Baut das Notebook entsprechend der Vorgaben aus agenten_kontext.md."""

    nb = nbf.v4.new_notebook()

    story_cell = nbf.v4.new_markdown_cell(
        """# 🎄 Tag 09 – Banner-Schmiede im Weihnachtsdorf

Felix, heute führt dich der Decorations-Elf in die geheime Banner-Werkstatt. Überall stapeln sich leere Karten, doch sie sehen so trist aus wie ungefüllte Item-Frames. Die Elfen brauchen deine Web-Magie, damit jedes Banner seine eigene Geschichte erzählt und doch perfekt ins Dorf passt. Deine Mission: Baue ein wiederverwendbares Kartensystem, das wie ein Set aus Minecraft-Blöcken funktioniert – gleich aufgebaut, aber mit individuellen Farben, Icons und Effekten."""
    )

    learning_cell = nbf.v4.new_markdown_cell(
        """## 📘 Dein Lernpfad heute

### 🧱 Komponenten wie Baupläne denken
Stell dir vor, du legst erst einzelne Blöcke (Farben, Abstände, Icons) bereit, dann kombinierst du sie zu Molekülen (Badge + Titel + Button) und schließlich zu Organismen (fertige Karten). In `Tag_09/Loesung/index.html` erkennst du diese Layer: Der Abschnitt mit `class="design-pill"` erklärt Atome, Moleküle und Organismen direkt im Layout.

### 🌼 DaisyUI als Designsystem nutzen
DaisyUI liefert dir fertige Komponenten, z. B. `card`, `badge`, `btn`. Kombiniert mit Tailwind-Utilities machst du daraus ein persönliches Theme. Im Header der Lösung findest du Buttons mit `data-theme-choice="winter|forest|candy|ember"`, die wie ein Texture-Pack-Umschalter funktionieren. Über `Tag_09/Loesung/script.js` setzt du dann `document.documentElement.setAttribute('data-theme', theme)` und lässt die ganze Seite in einem anderen Licht erscheinen.

### 🪄 Card-Layouts mit Hover-Magie veredeln
In `Tag_09/Loesung/style.css` steckt der Effekt `card-floating:hover { transform: translateY(calc(var(--float-range) * -1)) scale(1.01); }`. Diese eine Regel sorgt dafür, dass jede Karte beim Hover schwebt wie ein Item, das frisch gedroppt wurde. Zusammen mit dem Slider (`#floatRange`) kannst du die Höhe der Schwebe sogar live steuern – perfekt, um zu verstehen, wie Komponenten dynamisch reagieren."""
    )

    understand_cell = nbf.v4.new_markdown_cell(
        """## 🧠 Verstehen & Ausprobieren

### 1. Wie setzt die Lösung Karten zusammen?
In `Tag_09/Loesung/script.js` erzeugt `createCardTemplate()` jede Karte aus den Banner-Daten:
```html
<article class="card ..." data-id="aurora-loom">
  <figure class="relative h-40">
    <div class="absolute inset-0" style="background:linear-gradient(135deg,#7dd3fc,#c4b5fd);"></div>
    <span class="badge badge-primary">frostig</span>
  </figure>
  <div class="card-body">
    <h3 class="card-title">Aurora Loom</h3>
    <button class="btn btn-primary btn-sm">Zum Dorf schicken</button>
  </div>
</article>
```
*Minecraft-Vergleich*: Du kopierst immer denselben Bauplan, füllst aber andere Banner-Daten ein – wie eine Schmiede, die jedes Mal ein anderes Erzen-Inlay verwendet.

### 2. Filter und Layout-Toggle als Redstone-Schalter
Die Funktion `setFilter()` stellt ein, welche Stimmung aktiv ist, und `layoutToggle` (HTML-Button in der Kontrolle) wechselt zwischen Raster und Liste. Zusammen wirken sie wie ein Redstone-Panel: ein Klick ändert globale Variablen (`currentFilter`, `listMode`), danach ruft `renderCards()` sofort das passende Layout auf.

### 3. Hover-Stärke per Slider justieren
Über `initFloatControl()` greifst du auf eine CSS-Variable zu: `document.documentElement.style.setProperty('--float-range', value + 'px')`. Das fühlt sich an wie der Helligkeitsregler in Minecraft – der Slider schickt neue Werte durch das ganze Stylesheet, und die Karten reagieren sofort. Probiere gleich unten mit den Mini-Karten, wie sich unterschiedliche Werte anfühlen!"""
    )

    demo_code = nbf.v4.new_code_cell(
        '''from IPython.core.display import HTML

HTML("""
<style>
  .demo-wrap {
    font-family: 'Nunito', sans-serif;
    background: linear-gradient(135deg, #111826, #1f0c27);
    color: #f8fafc;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0 30px 80px rgba(8, 12, 38, 0.6);
  }
  .demo-controls {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 18px;
  }
  .demo-controls button,
  .demo-controls label {
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    background: rgba(255, 255, 255, 0.05);
    padding: 8px 14px;
    color: inherit;
    font-size: 0.9rem;
    cursor: pointer;
    transition: background 0.2s ease;
  }
  .demo-controls button.active {
    background: rgba(255, 255, 255, 0.2);
  }
  .demo-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
  }
  .demo-card {
    border-radius: 18px;
    padding: 18px;
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    transform-origin: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .demo-card:hover {
    transform: translateY(var(--demo-float, -12px)) scale(1.02);
    box-shadow: 0 25px 50px rgba(8, 12, 38, 0.7);
  }
  .demo-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    border-radius: 999px;
    padding: 4px 10px;
  }
  .demo-range {
    width: 160px;
  }
</style>
<div class=\"demo-wrap\">
  <div class=\"demo-controls\">
    <button data-mood=\"alle\" class=\"active\">Alle Stimmungen</button>
    <button data-mood=\"festlich\">Festlich</button>
    <button data-mood=\"mystisch\">Mystisch</button>
    <button data-mood=\"frostig\">Frostig</button>
    <label>Hover: <input type=\"range\" min=\"4\" max=\"20\" value=\"12\" class=\"demo-range\" /></label>
  </div>
  <div class=\"demo-cards\" id=\"demoCards\"></div>
</div>
<script>
  const demoCards = document.getElementById('demoCards');
  const demoButtons = document.querySelectorAll('[data-mood]');
  const demoRange = document.querySelector('.demo-range');
  const demoData = [
    { title: 'Aurora Loom', mood: 'frostig', gradient: 'linear-gradient(135deg,#7dd3fc,#c4b5fd)', badge: 'Frosttal', icon: '❄️' },
    { title: 'Ember Crest', mood: 'festlich', gradient: 'linear-gradient(135deg,#fb7185,#f97316)', badge: 'Kaminhalle', icon: '🔥' },
    { title: 'Prism Drift', mood: 'mystisch', gradient: 'linear-gradient(135deg,#a855f7,#ec4899,#f97316)', badge: 'Polarhafen', icon: '💠' }
  ];

  function renderDemo(filter = 'alle') {
    const cards = filter === 'alle' ? demoData : demoData.filter(card => card.mood === filter);
    demoCards.innerHTML = cards.map(card => `
      <article class=\"demo-card\">
        <div style=\"background:${card.gradient};border-radius:14px;padding:14px;color:white;margin-bottom:14px;display:flex;justify-content:space-between;align-items:center;\">
          <span class=\"demo-badge\" style=\"background:rgba(255,255,255,0.15);\">${card.badge}</span>
          <span>${card.icon}</span>
        </div>
        <h4 style=\"font-family:'Orbitron',sans-serif;margin-bottom:6px;\">${card.title}</h4>
        <p style=\"font-size:0.85rem;color:#cbd5f5;\">Mood: ${card.mood}</p>
      </article>
    `).join('');
  }

  demoButtons.forEach(button => {
    button.addEventListener('click', () => {
      demoButtons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');
      renderDemo(button.dataset.mood);
    });
  });

  demoRange.addEventListener('input', event => {
    document.documentElement.style.setProperty('--demo-float', `${-event.target.value}px`);
  });

  renderDemo();
</script>
""")
'''
    )

    mission_cell = nbf.v4.new_markdown_cell(
        """# 🚀 Deine Aufgabe: Banner-Kontrollpult perfektionieren

In `Tag_09/Aufgabe/` ist schon alles zu 80 % aufgebaut. Jetzt fehlen nur noch drei Zauberzüge:

### 📝 TODO 1 – Theme-Schalter einbauen (HTML)
**Datei:** `Tag_09/Aufgabe/index.html` (ca. Zeile 48)

Füge in den Header wieder eine `btn-group` mit vier Buttons ein. Jeder Button braucht `data-theme-choice="winter|forest|candy|ember"` und ein Emoji, damit `initThemeButtons()` überhaupt ein Ziel hat. Stell dir das wie Item-Slots vor: Ohne Slot kann das Script keine Skins anwenden.

### 🎨 TODO 2 – Hover-Schwebe aktivieren (CSS)
**Datei:** `Tag_09/Aufgabe/style.css` (Abschnitt `.card-floating:hover`)

Im Moment ist der Block leer. Trage dort `transform: translateY(calc(var(--float-range) * -1)) scale(1.01);` und einen stärkeren Schatten ein (`box-shadow: 0 30px 70px rgba(15, 23, 42, 0.45);`). Damit erfüllst du das WOW-Ziel "Banner schweben sanft beim Hover".

### ⚡ TODO 3 – Theme-Logik anschließen (JavaScript)
**Datei:** `Tag_09/Aufgabe/script.js` (Funktion `initThemeButtons()`)

Schreibe dort die Event-Listener: Lies das `data-theme-choice` aus, setze `document.documentElement.setAttribute('data-theme', themeMap[choice])` und markiere den aktiven Button mit `btn-active`. Vergleiche mit `Tag_09/Loesung/script.js`, um zu sehen, wie sauber die Lösung aussieht.

👉 Test-URL Aufgabe: `http://192.168.0.20:8000/2025_Adventskalender/Tag_09/Aufgabe/`

👉 Referenz-URL Lösung: `http://192.168.0.20:8000/2025_Adventskalender/Tag_09/Loesung/`"""
    )

    success_code = nbf.v4.new_code_cell(
        '''from IPython.core.display import HTML

HTML("""
<style>
  .success-panel {font-family:'Nunito',sans-serif;background:linear-gradient(135deg,#0f172a,#312e81);color:#f8fafc;padding:24px;border-radius:18px;box-shadow:0 25px 70px rgba(8,10,30,0.6);}
  .success-panel h3 {font-family:'Orbitron',sans-serif;margin-top:0;}
  .step-list {display:grid;gap:16px;margin:0;padding:0;list-style:none;}
  .step {background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:14px;padding:14px;display:flex;justify-content:space-between;align-items:center;}
  .step span:first-child {font-weight:600;}
</style>
<div class=\"success-panel\">
  <h3>✅ Schnell-Check, ob alles passt</h3>
  <ul class=\"step-list\">
    <li class=\"step\"><span>Theme-Schalter sichtbar?</span><span>➡️ `Aufgabe/index.html` Header</span></li>
    <li class=\"step\"><span>Hover wirkt wie Schwebe?</span><span>✅ Prüfe `Aufgabe/style.css`</span></li>
    <li class=\"step\"><span>Buttons ändern das Theme?</span><span>⚡ Konsole von `Aufgabe/script.js` beobachten</span></li>
  </ul>
</div>
""")
'''
    )

    possibilities_cell = nbf.v4.new_markdown_cell(
        """## 🌟 Erfolg & Möglichkeiten

Du hast jetzt ein echtes Mini-Designsystem gebaut: Karten ziehen ihre Daten aus `script.js`, DaisyUI liefert konsistente Styles und kleine Regler verändern das Verhalten live. Das bedeutet:

- Du kannst weitere Banner hinzufügen, indem du nur das Daten-Array in `Tag_09/Loesung/script.js` erweiterst – die Komponente wächst automatisch mit.
- Du könntest neue Themen (z. B. "crystal") ergänzen, indem du einen weiteren Button + Mapping hinzufügst.
- Experimentiere damit, Cards als eigene HTML-Komponente in zukünftigen Projekten zu verwenden – baue zum Beispiel Quest-Boards oder Shop-Listings.

Nächster Schritt? Beobachte beim Programmieren immer, welche Teile du wiederverwenden kannst. Genau so entstehen später echte UI-Bibliotheken!"""
    )

    nb.cells.extend(
        [
            story_cell,
            learning_cell,
            understand_cell,
            demo_code,
            mission_cell,
            success_code,
            possibilities_cell,
        ]
    )

    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except (
        nbf.ValidationError
    ) as error:  # pragma: no cover - Validation must halt execution
        print(f"❌ Validierungsfehler: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    """Speichert das Notebook im aktuellen Verzeichnis."""

    script_dir = Path(__file__).resolve().parent
    output_path = script_dir / filename

    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            nbf.write(nb, handle)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as exc:  # pragma: no cover - Fatal IO error should stop execution
        print(f"❌ Fehler beim Speichern: {exc}")
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
