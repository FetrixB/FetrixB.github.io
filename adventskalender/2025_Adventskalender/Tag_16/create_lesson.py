#!/usr/bin/env python3
"""Generiert Lesson.ipynb für Tag 16 nach Adventskalender-Vorgaben."""

from pathlib import Path

import nbformat as nbf

BASE_PATH = Path(__file__).parent


def create_lesson():
    nb = nbf.v4.new_notebook()

    title_story = nbf.v4.new_markdown_cell(
        """# 🎄 Tag 16 – Die Eishexe testet dich

Hi Felix! Im tiefsten Frostwald wartet Aurora Eisflüstern auf kluge Antworten. Sie reagiert
wie ein perfekter if/else-Zauber: Sagst du etwas Freundliches, wird sie warmherzig. Bietest du
wenig Kristallenergie an, funkeln Warnlichter wie bei einem Minecraft-Alarmsystem. Heute lernst du,
wie du mit JavaScript-Bedingungen eine Figur mit echten Gefühlen steuerst – genau das passiert in
`Tag_16/Loesung/index.html`."""
    )

    learn_markdown = nbf.v4.new_markdown_cell(
        """## 💡 Lern-Kapitel – Entscheidungsbäume im Frostwald

### 🌲 Bedingte Logik als Entscheidungsbaum
- `if/else` entscheidet sofort, welches Textfeedback Aurora zeigt.
- `else if` Ketten sortieren zusätzliche Fälle, z. B. lange Texte oder Schnee-Schlüsselwörter.
- `switch` hilft, Tonlagen sauber zu vergleichen.

```javascript
if (cleaned.includes('freund')) {
  reaction = 'Sie lächelt.';
} else if (cleaned.includes('eis')) {
  reaction = 'Sie erzählt dir vom Frostsee.';
} else {
  reaction = 'Sie bleibt skeptisch.';
}
```

### ⚖️ Vergleichsoperatoren für Rückmeldungen
- `===` prüft exakt, welche Tonlage im Dropdown gewählt wurde.
- `>=` und `<` bewerten die Anzahl deiner Kristalle (`crystalInput.value`).
- Stringvergleiche werden vorher in Kleinbuchstaben umgewandelt (`sanitizeInput`), damit `"Freund"`
und `"freund"` gleich wirken.

```javascript
const crystals = Number(crystalInput.value);
if (crystals >= 8) {
  crystalLabel.textContent = 'beschenkt';
} else if (crystals >= 4) {
  crystalLabel.textContent = 'ausgeglichen';
} else {
  crystalLabel.textContent = 'unterfordert';
}
```

### 💠 Code-gesteuerte Emotionen
- In `Loesung/style.css` stehen Klassen wie `.emotion-warm` oder `.emotion-danger`.
- `setEmotion()` entfernt erst alle Klassen und fügt dann die passende hinzu – so bleibt der
Glow sauber.
- Über `textContent` wechselst du Emojis (`❄️`, `✨`, `⚠️`) für klare Gefühle.
- Tipp: Stell dir jede Emotion wie Minecraft-Rüstungsschichten vor. Du ziehst genau die
Rüstung an, die zur Situation passt.

### 🔁 Switch für Tonlagen
```javascript
switch (tone) {
  case 'frage':
    toneMessage = 'Sie liebt gute Fragen...';
    break;
  case 'witz':
    toneMessage = textLength > 7
      ? 'Sie kichert.'
      : 'Witz zu kurz!';
    break;
  case 'herausforderung':
    toneMessage = 'Mutig!';
    break;
  default:
    toneMessage = 'Neutral';
}
```
Der `default` Teil ist dein Sicherheitsnetz, falls eine Eingabe fehlt – genau wie ein fallback
bei einem Redstone-Schaltkreis."""
    )

    understand_markdown = nbf.v4.new_markdown_cell(
        """## 🧪 Verstehen & Ausprobieren
1. Tippe eigene Texte ein und vergleiche sofort mit der Logik aus `Loesung/script.js`.
2. Wähle unterschiedliche Tonlagen, um zu beobachten, wie der `switch` reagiert.
3. Schiebe den Kristall-Regler: Damit spürst du direkt, wie Vergleichsoperatoren Zahlen lesen.
4. Achte auf die Klassen im Ergebnis: `.emotion-warm` = tapferer Glow, `.emotion-danger` = rote
Warnung. Das siehst du sofort im folgenden Mini-Demo.

> Analogie: Stell dir vor, du programmierst einen Dorfbewohner. Jede Antwort prüft eine
Koordinate (Text), eine Ressource (Kristalle) und eine Stimmung (Select)."""
    )

    interactive_code = nbf.v4.new_code_cell(
        '''from IPython.core.display import HTML

interactive_html = """
<!DOCTYPE html>
<html lang=\"de\">
  <head>
    <style>
      body {
        font-family: \"Montserrat\", sans-serif;
        background: radial-gradient(circle at top, #0f172a, #020617);
        color: #e0f2fe;
        margin: 0;
        padding: 20px;
      }
      .demo-shell {
        max-width: 720px;
        margin: 0 auto;
        border-radius: 24px;
        padding: 24px;
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(94, 234, 212, 0.3);
        box-shadow: 0 20px 40px rgba(2, 6, 23, 0.8);
      }
      .demo-title {
        font-family: \"Orbitron\", sans-serif;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #67e8f9;
        margin-bottom: 16px;
      }
      label {
        display: block;
        font-size: 0.8rem;
        letter-spacing: 0.1em;
        margin-bottom: 6px;
        color: #bae6fd;
        text-transform: uppercase;
      }
      textarea,
      select,
      input[type=\"range\"] {
        width: 100%;
        border-radius: 16px;
        border: 1px solid rgba(125, 211, 252, 0.4);
        padding: 12px;
        background: rgba(15, 23, 42, 0.9);
        color: #f8fafc;
        margin-bottom: 14px;
      }
      button {
        border: none;
        border-radius: 999px;
        padding: 12px 28px;
        font-family: \"Orbitron\", sans-serif;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        background: linear-gradient(120deg, #22d3ee, #a5b4fc);
        color: #020617;
        cursor: pointer;
      }
      .reaction-card {
        margin-top: 18px;
        padding: 18px;
        border-radius: 18px;
        background: rgba(8, 47, 73, 0.9);
        min-height: 140px;
      }
      .emotion-tag {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 16px;
        border-radius: 999px;
        font-size: 0.85rem;
        margin-top: 10px;
      }
      .emotion-calm {
        background: rgba(59, 130, 246, 0.3);
      }
      .emotion-warm {
        background: rgba(250, 250, 250, 0.7);
        color: #0f172a;
      }
      .emotion-danger {
        background: rgba(248, 113, 113, 0.35);
      }
    </style>
  </head>
  <body>
    <div class=\"demo-shell\">
      <p class=\"demo-title\">Mini-Eishexe</p>
      <label for=\"demo-text\">Deine Worte</label>
      <textarea id=\"demo-text\" rows=\"3\">Ich bringe dir acht Kristalle, Aurora!</textarea>

      <label for=\"demo-tone\">Tonlage</label>
      <select id=\"demo-tone\">
        <option value=\"frage\">Frage</option>
        <option value=\"kompliment\">Kompliment</option>
        <option value=\"witz\">Witz</option>
        <option value=\"herausforderung\">Herausforderung</option>
      </select>

      <label for=\"demo-crystals\">Kristallenergie</label>
      <input id=\"demo-crystals\" type=\"range\" min=\"0\" max=\"10\" value=\"8\" />

      <button id=\"demo-btn\">Antwort testen</button>

      <div class=\"reaction-card\" id=\"demo-reaction\">
        <p>Hier erscheint Auroras Stimmung.</p>
        <span class=\"emotion-tag emotion-calm\" id=\"demo-emotion\">❄️ ruhig</span>
      </div>
    </div>

    <script>
      const demoText = document.getElementById('demo-text');
      const demoTone = document.getElementById('demo-tone');
      const demoCrystals = document.getElementById('demo-crystals');
      const demoReaction = document.getElementById('demo-reaction');
      const demoEmotion = document.getElementById('demo-emotion');

      function describeEmotion(state) {
        demoEmotion.className = 'emotion-tag ' + state;
        if (state === 'emotion-warm') {
          demoEmotion.textContent = '✨ beeindruckt';
        } else if (state === 'emotion-danger') {
          demoEmotion.textContent = '⚠️ skeptisch';
        } else {
          demoEmotion.textContent = '❄️ ruhig';
        }
      }

      document.getElementById('demo-btn').addEventListener('click', () => {
        const text = demoText.value.trim().toLowerCase();
        const tone = demoTone.value;
        const crystals = Number(demoCrystals.value);
        let message = '';

        if (text.includes('freund') || text.includes('hilfe')) {
          message = 'Aurora nickt dankbar – das if erfüllt die Bedingung.';
          describeEmotion('emotion-warm');
        } else if (text.includes('eis') || text.length > 50) {
          message = 'Die else-if Spur erzählt dir vom geheimen Frostsee.';
          describeEmotion('emotion-calm');
        } else {
          message = 'Der else-Fall warnt dich: Gib mehr Kontext!';
          describeEmotion('emotion-danger');
        }

        switch (tone) {
          case 'witz':
            message += ' (Switch sagt: Witze lockern sie auf.)';
            break;
          case 'herausforderung':
            message += ' (Switch sagt: Herausforderung erkannt!)';
            break;
          default:
            message += ' (Switch liefert neutrale Stimmung.)';
        }

        if (crystals >= 7) {
          message += ' Außerdem merkt sie: Kristallangebot hoch!';
        } else if (crystals <= 2) {
          message += ' Nur wenige Kristalle – das else-if reagiert enttäuscht.';
        }

        demoReaction.firstElementChild.textContent = message;
      });
    </script>
  </body>
</html>
"""

HTML(interactive_html)
'''
    )

    tasks_markdown = nbf.v4.new_markdown_cell(
        """# 🚀 Deine Aufgabe in `Tag_16/Aufgabe/`
Deine Boilerplate zeigt schon alle Panels, aber drei Kernelemente fehlen. Löse jeden TODO nacheinander.

### 📝 TODO 1 – HTML: Logbuch sichtbar machen
- **Datei:** `Tag_16/Aufgabe/index.html`, Abschnitt "Auroras Logbuch".
- **Hinweis:** Ersetze den Kommentar durch eine `<ul>` mit der ID `log-list` und Klassen wie in der
Musterlösung (`space-y-3 text-sm text-slate-100`). Das Element braucht `aria-live="polite"`, damit
Aurora neue Einträge ansagen kann.
- **Warum?** Ohne Container landen die gesammelten Nachrichten im Nichts.

### 🎨 TODO 2 – CSS: Warnende Emotion gestalten
- **Datei:** `Tag_16/Aufgabe/style.css`, Bereich "Emotion colors".
- **Aufgabe:** Schreibe eine `.emotion-danger` Regel mit einem rötlichen Glow, leichtem Scale oder
Rotation. Orientiere dich an `Tag_16/Loesung/style.css` und kombiniere Schatten + Transform.
- **Ergebnis:** Wenn die Hexe misstrauisch ist, sieht man das sofort.

### ⚡ TODO 3 – JavaScript: Logbuch auffüllen
- **Datei:** `Tag_16/Aufgabe/script.js`
- **Codeblock:** Funktion `updateLogEntry(message)`.
- **Schritte:**
  1. Prüfe, ob `logList` existiert (ist bereits vorbereitet).
  2. Erstelle ein `<li>`, füge `textContent = message` hinzu und stelle es mit `prepend` oben ein.
  3. Begrenze die Liste auf höchstens fünf Einträge (`while (logList.children.length > 5) ...`).
- **Tipp:** Schau in `Tag_16/Loesung/script.js` nach, dort erledigt die gleiche Funktion den Job.

Wenn du fertig bist, öffne `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_16/Aufgabe/` und vergleiche
mit der Lösung auf dem gleichen Serverpfad."""
    )

    success_markdown = nbf.v4.new_markdown_cell(
        """## 🌟 Erfolg & Möglichkeiten
- Du kannst jetzt Bedingungen stapeln wie Pfade in einem Minecraft-Labyrinth.
- Du weißt, wie CSS-Klassen dynamisch Emotionen wechseln lassen.
- Du kombinierst Texte, Zahlen und Dropdowns zu einer lebendigen Figur.
- Nächster Schritt? Ergänze weitere Emotionen, arbeite mit Audiofeedback oder triggere Partikel,
ohne die Geheimnisse der kommenden Tage zu spoilern.

> Bonus-Ideen: Lass Aurora mit einer `switch`-Erweiterung verschiedene Elemente animieren oder
baue einen zweiten Charakter, der auf andere Schlüsselwörter reagiert."""
    )

    success_code = nbf.v4.new_code_cell(
        '''from IPython.core.display import HTML

status_card = """
<div style=\"font-family: \"Montserrat\", sans-serif; background: linear-gradient(135deg,#0369a1,#0ea5e9); color: #f8fafc; padding: 24px; border-radius: 24px; box-shadow: 0 20px 45px rgba(2,6,23,0.65);\">
  <h2 style=\"font-family: \"Orbitron\", sans-serif; letter-spacing: 0.2em; text-transform: uppercase; font-size: 1rem; margin: 0 0 12px;\">Frostwald-Level Up ✅</h2>
  <p style=\"margin: 0 0 8px;\">If/Else? Beherrscht. Else-if-Ketten? Aktiviert. Switch? Stabil.</p>
  <ul style=\"margin: 0; padding-left: 18px; line-height: 1.6;\">
    <li>Teste <strong>Aufgabe/index.html</strong> und <strong>Loesung/index.html</strong> nacheinander.</li>
    <li>Nutze das Logbuch, um wie ein echter Quest-Geber Feedback zu geben.</li>
    <li>Überlege, wie du `describeCrystals()` um neue Belohnungsstufen erweitern könntest.</li>
  </ul>
</div>
"""

HTML(status_card)
'''
    )

    nb.cells = [
        title_story,
        learn_markdown,
        understand_markdown,
        interactive_code,
        tasks_markdown,
        success_markdown,
        success_code,
    ]

    nbf.validate(nb)
    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    output_path = BASE_PATH / filename
    with output_path.open("w", encoding="utf-8") as f:
        nbf.write(nb, f)
    print(f"✅ Lesson gespeichert unter: {output_path}")
    return output_path


def main():
    print("🎄 Erstelle Lesson.ipynb für Tag 16...")
    nb = create_lesson()
    save_notebook(nb)
    print("✨ Fertig! Viel Spaß beim Unterrichten.")


if __name__ == "__main__":
    main()
