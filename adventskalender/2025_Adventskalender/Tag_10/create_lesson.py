#!/usr/bin/env python3
"""Erstellt Lesson.ipynb für Tag 10"""

import nbformat as nbf
import sys
from pathlib import Path


def create_lesson():
    """Erstellt ein individuelles Notebook für Tag 10"""

    nb = nbf.v4.new_notebook()

    interactive_demo = '''from IPython.core.display import HTML
HTML("""
<!DOCTYPE html>
<html>
  <head>
    <style>
      * { box-sizing: border-box; }
      body {
        font-family: 'Poppins', sans-serif;
        margin: 0;
        padding: 1.5rem;
        background: #040a1c;
        color: #f3fbff;
      }
      .demo-shell {
        max-width: 720px;
        margin: 0 auto;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(158,248,255,0.3);
        border-radius: 18px;
        padding: 1.2rem;
        box-shadow: 0 15px 40px rgba(0,0,0,0.4);
      }
      .demo-flex {
        display: grid;
        gap: 1rem;
      }
      @media (min-width: 700px) {
        .demo-flex {
          grid-template-columns: 1fr 1fr;
        }
      }
      label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
      }
      input, select {
        width: 100%;
        padding: 0.7rem 0.9rem;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.12);
        background: rgba(255,255,255,0.08);
        color: #fff;
      }
      button {
        border: none;
        border-radius: 10px;
        padding: 0.7rem 1rem;
        background: #ff5c8d;
        color: #fff;
        cursor: pointer;
        font-weight: 600;
      }
      .preview {
        border-radius: 16px;
        padding: 1rem;
        background: linear-gradient(135deg, rgba(158,248,255,0.2), rgba(255,92,141,0.2));
        min-height: 160px;
      }
      .orders {
        list-style: none;
        margin: 1rem 0 0;
        padding: 0;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
      }
      .orders li {
        border-radius: 12px;
        padding: 0.8rem;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
      }
    </style>
  </head>
  <body>
    <div class="demo-shell">
      <h3>Mini-Werkbank</h3>
      <div class="demo-flex">
        <form id="demo-form">
          <label for="demo-kid">Kind</label>
          <input id="demo-kid" name="kid" placeholder="Name" required />
          <label for="demo-wish">Wunsch</label>
          <input id="demo-wish" name="wish" placeholder="Gadget" required />
          <label for="demo-priority">Priorität</label>
          <select id="demo-priority" name="priority">
            <option>Standard</option>
            <option>Express</option>
            <option>Notfall</option>
          </select>
          <button type="submit">Wunsch speichern</button>
        </form>
        <div class="preview" id="demo-preview">
          <strong>Noch kein Wunsch</strong>
          <p>Die Vorschau reagiert sofort auf deine Eingaben.</p>
        </div>
      </div>
      <ul class="orders" id="demo-orders"></ul>
    </div>
    <script>
      const form = document.getElementById('demo-form');
      const preview = document.getElementById('demo-preview');
      const list = document.getElementById('demo-orders');
      const orders = [];

      form.addEventListener('input', () => {
        const kid = form.kid.value || 'Noch kein Wunsch';
        const wish = form.wish.value || 'Schreibe etwas hinein';
        preview.innerHTML = `<strong>${kid}</strong><p>${wish}</p><small>Priorität: ${form.priority.value}</small>`;
      });

      form.addEventListener('submit', (event) => {
        event.preventDefault();
        const entry = {
          kid: form.kid.value,
          wish: form.wish.value,
          priority: form.priority.value
        };
        orders.unshift(entry);
        list.innerHTML = orders.map((order) => `<li>${order.kid} → ${order.wish} (${order.priority})</li>`).join('');
        form.reset();
        preview.innerHTML = '<strong>Noch kein Wunsch</strong><p>Die Vorschau reagiert sofort auf deine Eingaben.</p>';
      });
    </script>
  </body>
</html>
""")
'''

    cells = [
        nbf.v4.new_markdown_cell(
            """# 🎄 Tag 10 · Die Elfenwerkbank lebt wieder!

Felix, die Elfenwerkbank ist heute dein Einsatzort. Die alten Holzhebel haben aufgegeben und die
Maschinen warten auf eine moderne Benutzeroberfläche. Nur wenn du strukturierte Formulare,
sympathische Statusanzeigen und eine clevere Navigation baust, können die Geschenk-Bänder wieder
rollen!"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎯 Das lernst du heute

- **Formulare gestalten wie Redstone-Schaltungen:** passende `label`/`input` Kombinationen,
  unterschiedliche Input-Types und sinnvolle Platzhalter
- **Panel-Systeme denken:** Inhalte logisch gruppieren, Navigation per Buttons steuern und Panels bei
  Bedarf ein- oder ausblenden
- **Dashboard-UX planen:** visuelle Statusmeldungen, Validierungsfeedback und Fortschritt so zeigen,
  dass Elfen sofort verstehen, was zu tun ist"""
        ),
        nbf.v4.new_markdown_cell(
            """### 🏗️ Formular-Bauteile wie Redstone-Kabel
In `Loesung/index.html` siehst du, wie jedes Feld sein Label wie ein Redstone-Schaltplan bekommt:

```html
<label for=\"kidName\">Kind / Empfänger</label>
<input id=\"kidName\" name=\"kidName\" type=\"text\" required placeholder=\"Name des Kindes\" />
```

- `for` und `id` verbinden Label und Feld – so kann jeder Elf per Klick das richtige Feld aktivieren
- `placeholder` erklärt, welche Daten erwartet werden
- `required` sorgt dafür, dass dein Skript später weiß, wann ein Feld leer ist"""
        ),
        nbf.v4.new_markdown_cell(
            """### 🌐 Panel-Systeme mit Navigation verknüpfen
Der obere Bereich in `Loesung/index.html` nutzt Buttons mit `data-panel-target`, um gezielt Sektionen
anzuzeigen:

```html
<button class=\"nav-pill\" data-panel-target=\"inventory\">🧰 Ressourcen</button>
<section class=\"panel hidden\" data-panel=\"inventory\">...</section>
```

Wenn du später per JavaScript die passende Sektion ent-hidest, fühlt sich die Oberfläche wie ein
Mini-Dashboard an – genau so, wie der Werkstattleiter es braucht."""
        ),
        nbf.v4.new_markdown_cell(
            """### ⚡ Status-Feedback für jede Eingabe
`Loesung/style.css` arbeitet mit Datenattributen, um Fehler sofort sichtbar zu machen:

```css
.elf-field[data-state='error'] input {
  border-color: rgba(255, 92, 141, 0.7);
}
```

Im Zusammenspiel mit `Loesung/script.js` zeigt dein Formular so an, ob ein Feld noch fehlt oder schon
bereit für die Maschinen ist."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎨 Dein praktisches WOW-Ziel heute:

✅ **Festliche Navigation** – Buttons, die Panels wie Werkbank-Schubladen öffnen

✅ **Live-Vorschau** – sofort sehen, was eine Eingabe bewirkt

✅ **Status-Karten & Toasts** – Elfen erkennen auf einen Blick, ob alles grün ist

✅ **Kapazitäts-Panel** – Slider & Meter zeigen, wie voll die Maschinen schon sind"""
        ),
        nbf.v4.new_markdown_cell("""# 🧪 Verstehen"""),
        nbf.v4.new_markdown_cell(
            """## 🔍 Feldgruppen & Validierung verstehen
In `Loesung/script.js` weist `markFieldState()` jedem `.elf-field` ein Datenattribut zu. Dadurch kann
das CSS auf `data-state=\"error\"` reagieren. Stell dir das wie Warnlampen in der Werkstatt vor: Sobald
ein Feld leer ist, glüht der Rahmen rot. Wenn alles stimmt, wird es mintgrün – genau wie ein grünes
Redstone-Lämpchen."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎨 Panel-Hierarchie
Die Panels in `Loesung/index.html` liegen in einer `div.panel-stack`. Dadurch kannst du immer wieder
neue Sektionen hinzufügen, ohne dass das Layout kollabiert. Die Navigation im linken `aside` triggert
das Anzeigen oder Verstecken, ganz so wie Schalterleisten in Minecraft, die verschiedene Räume mit
Strom versorgen."""
        ),
        nbf.v4.new_markdown_cell(
            """## ⚡ Dashboard-Logik mit JavaScript
Der Ablauf in `Loesung/script.js` funktioniert wie eine kleine Pipeline:

```javascript
function handleSubmit(event) {
  event.preventDefault();
  const data = new FormData(orderForm);
  const newOrder = { kid: data.get('kidName'), priority: activePriority };
  demoOrders.unshift(newOrder);
  renderOrders();
  showToast('Neuer Wunsch wurde an die Maschinen gesendet ✨');
}
```

1. **FormData** sammelt alles ein – wie ein Elf, der den Wunschzettel scannt
2. **`demoOrders.unshift()`** legt den Wunsch ganz oben auf den Stapel, damit Express-Wünsche sofort
   sichtbar sind
3. **`renderOrders()`** malt die Karten neu, damit alle Panels frisch aussehen
4. **`showToast()`** ist die visuelle Bestätigung, dass nichts verloren ging"""
        ),
        nbf.v4.new_markdown_cell(
            """# 🧪 Ausprobieren
Starte ein Mini-Dashboard direkt im Notebook. Tipp ein paar Namen ein, spiele mit der Priorität und
sieh zu, wie die Preview sich verändert – genau wie später in deiner HTML-Seite."""
        ),
        nbf.v4.new_code_cell(interactive_demo),
        nbf.v4.new_markdown_cell(
            """# 🚀 Deine Aufgabe: Dashboard abrunden!
In `Aufgabe/` wartet eine fast fertige Oberfläche. Drei Stellen fehlen, damit der Werkstattleiter
mehr Vertrauen bekommt."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎯 Mission: 3 magische TODOs lösen
- Bring die Status-Badges im Hero-Bereich zurück
- Style den aktiven Prioritäts-Button in `Aufgabe/style.css`
- Ergänze in `Aufgabe/script.js`, dass neue Wünsche wirklich gespeichert & angezeigt werden"""
        ),
        nbf.v4.new_markdown_cell(
            """### 📝 TODO 1: HTML – Status-Badges zurückholen
**Datei:** `Aufgabe/index.html` (Hero-Panel)

Im Header steckt ein Kommentar `<!-- TODO 1 ... -->`. Dort müssen zwei kleine Karten hin, die
Nutzerfreundlichkeit und Validierungs-Licht anzeigen (siehe `Loesung/index.html`). Ohne sie fehlt das
Dashboard-Feeling. Kopiere die Struktur mit zwei `div`-Elementen und den Texten "Nutzerfreundlichkeit"
und "Validierungs-Licht"."""
        ),
        nbf.v4.new_markdown_cell(
            """### 🎨 TODO 2: CSS – Aktive Priorität hervorheben
**Datei:** `Aufgabe/style.css` (Bereich `.priority-pill`)

Damit Elfen sofort sehen, welche Maschinen-Stufe aktiv ist, brauchst du einen Stil für
`.priority-pill.is-active`. Nutze Mint- oder Peppermint-Farben und sorge für einen deutlichen Rahmen –
in `Loesung/style.css` findest du ein Beispiel."""
        ),
        nbf.v4.new_markdown_cell(
            """### ⚡ TODO 3: JavaScript – Neue Wünsche anzeigen
**Datei:** `Aufgabe/script.js`

In `handleSubmit()` befindet sich ein Kommentar `// TODO 3 ...`. Dort musst du den frisch erstellten
`newOrder` in `demoOrders` speichern, `renderOrders()` aufrufen und `showToast()` benutzen. Erst dann
fühlt sich das Formular lebendig an und zeigt, dass der Wunsch wirklich in der Liste landet."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🏆 Erfolgskontrolle
Wenn alle TODOs gelöst sind, solltest du sehen:

✅ Hero-Badges mit nutzerfreundlicher Anzeige

✅ Der ausgewählte Prioritäts-Button glüht sofort

✅ Neue Wünsche springen an den Anfang der Kartenliste und zeigen den Toast"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🌐 Teste deine Seite
- Aufgabe öffnen: `http://192.168.0.20:8000/2025_Adventskalender/Tag_10/Aufgabe/`
- Lösung vergleichen: `http://192.168.0.20:8000/2025_Adventskalender/Tag_10/Loesung/`
- Wenn Unterschiede sichtbar sind, überprüfe vor allem die TODO-Stellen"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🌟 Erfolg & Möglichkeiten
Du kannst jetzt Formularfelder logisch gruppieren, Validierungszustände visualisieren und Panels per
Schalter steuern. Als Nächstes könntest du weitere Panels hinzufügen (z.B. eine Geschenk-Historie),
mit DaisyUI-Komponenten experimentieren oder die Daten an ein echtes Backend schicken, sobald du
bereit dafür bist."""
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
    """Speichert das Notebook"""

    base_dir = Path(__file__).resolve().parent
    output_path = base_dir / filename
    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            nbf.write(nb, handle)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as exc:  # pylint: disable=broad-except
        print(f"❌ Fehler beim Speichern: {exc}")
        sys.exit(1)


def main():
    """Entry point"""

    print("🎄 Erstelle Lesson.ipynb...")
    notebook = create_lesson()
    save_notebook(notebook)
    print("🎉 Fertig! Die Lesson für Tag 10 wurde erzeugt.")


if __name__ == "__main__":
    main()
