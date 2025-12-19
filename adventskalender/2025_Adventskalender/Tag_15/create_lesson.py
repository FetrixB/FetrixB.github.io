#!/usr/bin/env python3
"""Erstellt die Lesson.ipynb für Tag 15 mit Story, Theorie und Aufgaben."""

import nbformat as nbf
import sys
from pathlib import Path


def create_lesson():
    """Erzeugt ein kindgerechtes Notebook auf Basis der Agentenrichtlinien."""

    nb = nbf.v4.new_notebook()

    cells = [
        nbf.v4.new_markdown_cell(
            """# 🎄 Tag 15 – Webstone-Lampenlabor\n\nHey Felix! Der Redstone-Ingenieur des Dorfes hat seinen Schaltkreis ruiniert und bittet dich um Hilfe.\nDu erkennst sofort: Was für ihn Hebel und Lampen sind, sind für uns Variablen, Datentypen und if-Abfragen.\nGemeinsam baut ihr in `Tag_15/Loesung/` eine glühende Steuerzentrale, die Hebel klickt, Stärke misst und\nLampen wie in Minecraft schalten lässt – nur dass dein JavaScript noch schneller reagiert als jeder Redstone-Repeater.\n"""
        ),
        nbf.v4.new_markdown_cell(
            """## 📚 Lern-Kapitel – Redstone-Logik = JavaScript\n\n### 🔁 Variablen als Hebelschalter\n- `let powerLever = false;` verhält sich wie ein Hebel auf AUS. Du kannst ihn durch einen Klick auf AN setzen.\n- `const engineerName = ""Stollmann"";` bleibt konstant, genau wie ein Dorfbewohner-Name auf einem Namensschild.\n- Du findest alle Zustände gesammelt im Objekt `const circuitState = { power, signal, override, strength };`.\n  Das ist wie eine Truhe, in der alle Hebelpositionen und die Redstone-Stärke liegen.\n\n### 🧱 Datentypen = Blockarten\n- **Boolean** (`true`/`false`) entspricht einem Hebel, der nur zwei Zustände kennt.\n- **Number** speichert Werte von 0 bis 15 – exakt wie Redstone-Stärke in Minecraft.\n- **String** wird genutzt, um Nachrichten zu bauen, z. B. `"Tor hebt sich majestätisch!"`.\n\n### ⚖️ Logik-Operatoren = Redstone-Gatter\n```javascript\nconst gateActive = circuitState.power && circuitState.signal && circuitState.strength >= 8;\nconst alarmActive = circuitState.power || circuitState.override;\nconst secretActive = circuitState.power && !circuitState.override;\n```\n- `&&` ist wie ein UND-Gatter: alle Eingänge müssen glühen.\n- `||` arbeitet wie ein ODER-Gatter: ein Funken reicht.\n- `!` dreht einen Zustand um – wie ein Inverter in Minecraft.\n\n### 🕹️ DOM-Zauber\n- `document.querySelectorAll('[data-lever]')` sucht alle Buttons mit einem bestimmten Attribut.\n- `button.addEventListener('click', ...)` lauscht auf Klicks wie ein Redstone-Observer.\n- `element.classList.toggle('lamp-on', gateActive)` färbt eine Lampe sofort ein, sobald die Logik stimmt.\n"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🧪 Verstehen & Ausprobieren\n\n1. **State aktualisieren** – jede Funktion arbeitet auf dem gemeinsamen `circuitState`.\n   Wenn du die Stärke veränderst, wird `circuitState.strength = Number(event.target.value);` gesetzt.\n2. **Alle Lampen prüfen** – `updateLamps()` berechnet zuerst `gateActive`, `alarmActive`, `secretActive`\n   und `moodWarmth` und färbt anschließend jede Karte neu ein.\n3. **Story erzählen** – der Abschnitt `logicNarration.textContent = narration.join(' ');` fasst zusammen,\n   was deine Logik gerade entschieden hat. Das ist wie ein Redstone-Statusbuch für den Ingenieur.\n\nSo verstehst du nicht nur den Code, sondern auch, warum er geschrieben wurde.\n"""
        ),
        nbf.v4.new_code_cell(
            """from IPython.core.display import HTML\ndisplay(HTML(\"\"\"\n<!DOCTYPE html>\n<html lang=\"de\">\n  <head>\n    <style>\n      #webstone-demo {\n        font-family: 'Orbitron', sans-serif;\n        background: #0f172a;\n        color: #e2e8f0;\n        border-radius: 18px;\n        padding: 18px;\n        border: 2px solid #22d3ee;\n        max-width: 520px;\n      }\n      #webstone-demo .controls {\n        display: flex;\n        gap: 10px;\n        flex-wrap: wrap;\n        margin-bottom: 12px;\n      }\n      #webstone-demo button {\n        flex: 1;\n        min-width: 120px;\n        padding: 10px;\n        border-radius: 12px;\n        border: 2px solid #64748b;\n        background: #020617;\n        color: #e2e8f0;\n        text-transform: uppercase;\n        letter-spacing: 0.08em;\n        cursor: pointer;\n      }\n      #webstone-demo button[data-active=\"true\"] {\n        border-color: #3af5a8;\n        background: #134e4a;\n      }\n      #webstone-demo .lamp {\n        height: 90px;\n        border-radius: 18px;\n        background: radial-gradient(circle, rgba(148,163,184,0.5), rgba(2,6,23,0.9));\n        border: 2px solid rgba(148,163,184,0.6);\n        margin-bottom: 12px;\n        transition: all 0.3s ease;\n      }\n      #webstone-demo .lamp[data-on=\"true\"] {\n        background: radial-gradient(circle, rgba(250,204,21,0.7), rgba(249,115,22,0.4));\n        border-color: #fde68a;\n        box-shadow: 0 0 25px rgba(250,204,21,0.6);\n      }\n      #webstone-demo input[type=range] {\n        width: 100%;\n      }\n    </style>\n  </head>\n  <body>\n    <div id=\"webstone-demo\">\n      <h3>Mini-Labor: Hebel + Stärke</h3>\n      <p>Tippe die Buttons oder bewege die Stärke. Die Lampe zeigt dir live die AND/OR-Logik.</p>\n      <div class=\"controls\">\n        <button data-role=\"power\" data-active=\"false\">Strom AUS</button>\n        <button data-role=\"override\" data-active=\"false\">Override AUS</button>\n      </div>\n      <label>Redstone-Stärke: <span id=\"demo-strength\">7</span></label>\n      <input type=\"range\" min=\"0\" max=\"15\" value=\"7\" id=\"demo-slider\" />\n      <div class=\"lamp\" data-on=\"false\"></div>\n      <p id=\"demo-text\">Schalte beide Hebel für das Tor oder nutze Override als Notlösung.</p>\n    </div>\n    <script>\n      (function() {\n        const state = { power: false, override: false, strength: 7 };\n        const wrapper = document.getElementById('webstone-demo');\n        const buttons = wrapper.querySelectorAll('button');\n        const lamp = wrapper.querySelector('.lamp');\n        const output = document.getElementById('demo-text');\n        const slider = document.getElementById('demo-slider');\n        const strengthText = document.getElementById('demo-strength');\n\n        function updateLamp(extraMessage) {\n          const torOffen = state.power && state.strength >= 8;\n          const alarmAn = state.power || state.override;\n          lamp.dataset.on = String(torOffen || alarmAn);\n          output.textContent = extraMessage || (torOffen\n            ? 'Alle Bedingungen erfüllt: Tor geht auf!'\n            : alarmAn\n              ? 'Override rettet die Anlage.'\n              : 'Zu wenig Signal – Hebel prüfen!');\n        }\n\n        buttons.forEach((button) => {\n          button.addEventListener('click', () => {\n            const role = button.dataset.role;\n            state[role] = !state[role];\n            button.dataset.active = String(state[role]);\n            button.textContent = `${role === 'power' ? 'Strom' : 'Override'} ${state[role] ? 'AN' : 'AUS'}`;\n            updateLamp();\n          });\n        });\n\n        slider.addEventListener('input', (event) => {\n          state.strength = Number(event.target.value);\n          strengthText.textContent = state.strength;\n          updateLamp('Signal-Stärke ist jetzt ' + state.strength + '/15.');\n        });\n\n        updateLamp('Starte mit Stärke 7 und beobachte, was passiert.');\n      })();\n    </script>\n  </body>\n</html>\n\"\""))"""
        ),
        nbf.v4.new_markdown_cell(
            """# 🚀 Deine Aufgabe – 3 magische TODOs\n\nDu findest eine fast fertige Version im Ordner `Tag_15/Aufgabe/`. Mit drei Reparaturen verwandelst du sie\nin die Musterlösung. Arbeite Schritt für Schritt und teste nach jedem Erfolg über den eingebauten Server.\n\n### 📝 TODO 1 – HTML Hebel ergänzen\n**Datei:** `Tag_15/Aufgabe/index.html`, Bereich `#leverPanel` (ca. Zeile 70).\n\n- Füge wieder den dritten Button für den Override-Hebel ein.\n- Verwende die Klasse `lever-button` und das Attribut `data-lever="override"`, damit das Skript den Button automatisch findet.\n- Denk an die `<span class="label">` und `<span class="state">`, damit die Anzeige "AN/AUS" aktualisiert wird.\n\n### 🎨 TODO 2 – CSS Glow aktivieren\n**Datei:** `Tag_15/Aufgabe/style.css`, direkt unter `.lever-button`.\n\n- Ersetze den Kommentar durch eine Regel für `.lever-button[data-active="true"]`.\n- Ziel: Wenn ein Button aktiv ist, soll er eine grün leuchtende Umrandung erhalten (siehe Lösung).\n- Nutze `border-color`, `background` und einen kleinen `transform`, um das Feedback spürbar zu machen.\n\n### ⚡ TODO 3 – Geheimtür-Logik schreiben\n**Datei:** `Tag_15/Aufgabe/script.js`, Funktion `updateLamps()` (ca. Zeile 50).\n\n- Berechne `secretActive` so, dass die Geheimtür nur öffnet, wenn `power` an ist, `override` aus ist **und** die Stärke mindestens 4 beträgt.\n- Tipp: Kombiniere `&&`, `!` und einen Vergleich wie `>= 4`.\n- Dadurch spürt Felix, warum Negation (`!override`) so wichtig ist.\n\nWenn alle drei TODOs erledigt sind, verhält sich deine Aufgabe genau wie die Musterlösung.\nÖffne beide Versionen unter `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_15/...` und vergleiche sie.\n"""
        ),
        nbf.v4.new_code_cell(
            """from IPython.core.display import HTML\ndisplay(HTML(\"\"\"\n<div style=\"font-family:'Roboto',sans-serif;background:#020617;color:#e2e8f0;padding:18px;border-radius:18px;border:2px solid #3af5a8;\">\n  <h3 style=\"margin-top:0;color:#3af5a8;\">🏆 Erfolgskontrolle</h3>\n  <ul style=\"list-style:none;padding-left:0;line-height:1.6;\">\n    <li>✅ Lampen lassen sich über alle Hebel steuern.</li>\n    <li>✅ Override-Hebel zeigt deutlich, was NOT macht.</li>\n    <li>✅ Console-Log erklärt jede Aktion wie eine Debug-Lampe.</li>\n    <li>✅ Aufgabe und Lösung verhalten sich identisch nach dem Fix.</li>\n  </ul>\n  <p style=\"margin-bottom:0;\">Feiere jeden Schritt – du hast heute echte Logik-Schaltungen im Browser gebaut!</p>\n</div>\n\"\""))"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🌟 Möglichkeiten nach Tag 15\n- Baue weitere Lampen mit eigenen Bedingungen, z. B. `if (strength === 15) { ... }`.\n- Lass das Console-Log zusätzlich in ein eigenes Panel schreiben, damit Spieler:innen nichts verpassen.\n- Kombiniere das Panel später mit Audio-Effekten oder Partikeln – genau wie Redstone, nur mit mehr Kreativität.\n\nDu bist jetzt ein echter Webstone-Ingenieur!\n"""
        ),
    ]

    nb.cells = cells

    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as error:  # pragma: no cover
        print(f"❌ Validierungsfehler: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    """Speichert das Notebook neben dem Skript, egal von wo aus es gestartet wird."""

    script_dir = Path(__file__).resolve().parent
    output_path = script_dir / filename

    try:
        with open(output_path, "w", encoding="utf-8") as file_handle:
            nbf.write(nb, file_handle)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as error:  # pragma: no cover
        print(f"❌ Fehler beim Speichern: {error}")
        sys.exit(1)


def main():
    """CLI-Einstiegspunkt."""

    print("🎄 Erstelle Lesson.ipynb...")
    print("=" * 60)

    notebook = create_lesson()
    output_path = save_notebook(notebook)

    print("=" * 60)
    print("🎉 Fertig! Lesson wurde erstellt.")
    print(f"📁 Pfad: {output_path}")


if __name__ == "__main__":
    main()
