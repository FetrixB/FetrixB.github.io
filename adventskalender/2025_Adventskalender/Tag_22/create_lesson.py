#!/usr/bin/env python3
"""Erstellt das Lesson.ipynb für Tag 22."""

from pathlib import Path
import sys
import nbformat as nbf


def create_lesson():
    """Baut das Notebook mit Story, Theorie, Aufgaben und Demo."""

    nb = nbf.v4.new_notebook()

    cells = [
        nbf.v4.new_markdown_cell(
            """# 🎄 Tag 22 – Frostbyte Command Deck\n\nFelix, der Bürgermeister und die KI-Elfe Pixalia stehen vor dem unfertigen Kontrollzentrum.\nAlle Bewohner warten auf eine Landing Page, die nicht nur hübsch aussieht, sondern klug auf Fragen antwortet.\nHeute richtest du die Einsatzzentrale ein: Navigation, Inhalte, Schneesturm-Hintergrund und ein Chat mit echtem LLM-Zauber!"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🎯 Missionslogbuch\n- **Projektstruktur aufräumen:** HTML, CSS und JS bleiben getrennt, damit jedes Modul wie ein eigenes Minecraft-Biom gepflegt werden kann.\n- **LLM-Integration meistern:** Mit `fetch()` sprichst du die REST-API `https://api.llm7.io/v1/chat/completions` an und nutzt JSON für Fragen + Antworten.\n- **Moderne Landing Page bauen:** Hero-Section, Navigation, Roadmap-Kacheln, CTA-Buttons und ein frei scrollender Chat-Bereich sorgen für Profi-UX."""
        ),
        nbf.v4.new_markdown_cell(
            """### 🧱 Saubere Projektstruktur = stabile Redstone-Schaltung\nSo liegen die Dateien in `Tag_22/` – ein Blick in `Tag_22/Loesung/` zeigt dir die fertige Referenz:\n```text\nTag_22/\n ├─ Aufgabe/ (80 % fertig + TODOs)\n │   ├─ index.html\n │   ├─ style.css\n │   └─ script.js\n ├─ Loesung/ (fertige Version)\n │   ├─ index.html\n │   ├─ style.css\n │   └─ script.js\n ├─ create_lesson.py\n ├─ Lesson.ipynb (wird gleich erstellt)\n └─ Tag_22.md\n```\nDiese Trennung folgt exakt dem, was große Web-Projekte tun: HTML ist die Welt, CSS malt sie aus, JavaScript bringt Leben hinein."""
        ),
        nbf.v4.new_markdown_cell(
            """### 🧭 Hero, Navigation & Call-to-Action\nDer Einstieg stellt sofort klar, was Besucher tun sollen. In `Loesung/index.html` findest du dieses Muster:\n```html\n<header class=\"glass-panel\">\n  <nav class=\"flex gap-4\">\n    <a class=\"nav-link\" href=\"#hero\">Hero</a>\n    <a class=\"nav-link\" href=\"#chat\">KI-Chat</a>\n  </nav>\n  <button class=\"cta-button\" data-scroll=\"#chat\">✨ Chat starten</button>\n</header>\n```\n- Die Links verwenden klare IDs (`#hero`, `#chat`).\n- Das `data-scroll` Attribut wird im Script genutzt, um Smooth-Scrolling zu aktivieren.\n- Eine zweite CTA führt direkt zum Chat – das entspricht einem geführten User-Journey wie bei einem Quest-Log in Minecraft."""
        ),
        nbf.v4.new_markdown_cell(
            """### 💬 Chat mit gpt-4o-mini verstehen\n🎉 **LLMv7 Free Tier:** Keine API-Key erforderlich! Du kannst direkt loslegen.\n\nWir senden strukturierte Daten an die API `https://api.llm7.io/v1/chat/completions`.\nSo sieht der JSON-Body aus, den `script.js` erzeugt:\n```json\n{\n  \"model\": \"gpt-4o-mini-2024-07-18\",\n  \"temperature\": 0.7,\n  \"messages\": [\n    { \"role\": \"system\", \"content\": \"Du bist Pixalia...\" },\n    { \"role\": \"user\", \"content\": \"Ich brauche eine CTA-Idee\" }\n  ]\n}\n```\nWichtig:\n1. **Free Tier:** Funktioniert ohne API-Key! Nur `Content-Type` Header nötig.\n2. **Optional:** API-Key für erweiterte Features: `Authorization: Bearer <key>`\n3. **Antwort auslesen:** `choices[0].message.content` enthält den Text.\n4. **Fallback:** Wenn die API nicht antwortet, zeigen wir eine freundliche Offline-Hilfe."""
        ),
        nbf.v4.new_markdown_cell(
            """### ⚙️ `requestCompletion()` Schritt für Schritt\nIm fertigen `Loesung/script.js` steckt die komplette Logik mit **LLMv7 Free Tier Support**:\n```javascript\nasync function requestCompletion() {\n  const payload = [{ role: \"system\", content: systemPrompt }, ...chatState.messages];\n  \n  const headers = { \"Content-Type\": \"application/json\" };\n  if (chatState.apiKey) {\n    headers.Authorization = `Bearer ${chatState.apiKey}`;\n  }\n  \n  const response = await fetch(\"https://api.llm7.io/v1/chat/completions\", {\n    method: \"POST\",\n    headers,\n    body: JSON.stringify({\n      model: \"gpt-4o-mini-2024-07-18\",\n      temperature: 0.7,\n      messages: payload,\n      max_tokens: 220,\n    }),\n  });\n  if (!response.ok) throw new Error(await response.text());\n  const data = await response.json();\n  return data.choices[0].message.content.trim();\n}\n```\n- **Free Tier:** Funktioniert ohne API-Key! 🎉\n- **Optional:** API-Key nur für erweiterte Features hinzufügen\n- Alle bisherigen Nachrichten werden mitgeschickt – so kennt die KI den Kontext.\n- Durch `trim()` verhinderst du überflüssige Leerzeilen im Chat-Panel."""
        ),
        nbf.v4.new_markdown_cell(
            """### ❄️ Schnee + Motion für das WOW-Erlebnis\nZwei Bibliotheken erledigen die visuelle Magie:\n```javascript\nwindow.tsParticles.load(\"snow-canvas\", {\n  particles: { number: { value: 140 }, size: { value: { min: 1.5, max: 4 } } },\n  move: { direction: \"bottom\", speed: { min: 0.4, max: 1.4 } }\n});\n\nwindow.gsap.from(\".module-card\", {\n  y: 40, opacity: 0, duration: 1, stagger: 0.15, ease: \"power2.out\"\n});\n```\n- `tsparticles` erzeugt das Schneefall-Canvas hinter dem Inhalt (`#snow-canvas`).\n- `GSAP` belebt Karten und Feature-Blöcke, damit die Seite sich so lebendig anfühlt wie eine bewohnte Stadt in Minecraft."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🧪 Probier die Kommandozentrale in Miniatur\nFühre die nächste Zelle aus. Sie zeigt dir eine verkleinerte Hero+Chat-Komponente.\nDu kannst Fragen anklicken und sehen, wie ein simuliertes LLM freundlich antwortet."""
        ),
        nbf.v4.new_code_cell(
            """from IPython.core.display import HTML\nHTML(\"\"\"\n<style>\n  .demo-shell {\n    font-family: \"Space Grotesk\", sans-serif;\n    background: radial-gradient(circle at top, #132033, #030712);\n    color: white;\n    padding: 24px;\n    border-radius: 24px;\n    border: 1px solid rgba(255, 255, 255, 0.2);\n    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45);\n    max-width: 640px;\n    margin: 0 auto;\n  }\n  .demo-nav {\n    display: flex;\n    gap: 12px;\n    margin-bottom: 20px;\n    text-transform: uppercase;\n    font-size: 12px;\n    letter-spacing: 0.3em;\n  }\n  .demo-nav button {\n    background: transparent;\n    border: 1px solid rgba(255, 255, 255, 0.25);\n    border-radius: 999px;\n    padding: 6px 14px;\n    color: inherit;\n    cursor: pointer;\n  }\n  .demo-chat {\n    background: rgba(255, 255, 255, 0.05);\n    border-radius: 18px;\n    padding: 16px;\n    display: flex;\n    flex-direction: column;\n    gap: 12px;\n  }\n  .demo-bubble {\n    background: rgba(125, 211, 252, 0.15);\n    border: 1px solid rgba(125, 211, 252, 0.35);\n    border-radius: 14px;\n    padding: 12px;\n  }\n  .demo-bubble.user {\n    align-self: flex-end;\n    background: rgba(248, 250, 252, 0.08);\n    border-color: rgba(248, 250, 252, 0.4);\n  }\n  .demo-actions {\n    display: flex;\n    gap: 8px;\n    flex-wrap: wrap;\n  }\n  .demo-actions button {\n    flex: 1;\n    min-width: 140px;\n    border-radius: 12px;\n    border: none;\n    padding: 10px 12px;\n    background: linear-gradient(135deg, #ff5f6d, #ffd479);\n    color: #0f172a;\n    font-weight: 600;\n    cursor: pointer;\n  }\n</style>\n<div class=\"demo-shell\">\n  <p class=\"badge\">Mini-Kommandozentrale</p>\n  <div class=\"demo-nav\">\n    <button type=\"button\">Hero</button>\n    <button type=\"button\">Roadmap</button>\n    <button type=\"button\">Chat</button>\n  </div>\n  <div class=\"demo-actions\">\n    <button type=\"button\" data-question=\"Wie gestalte ich die Navi?\">Navigation fragen</button>\n    <button type=\"button\" data-question=\"Welche CTA-Texte passen?\">CTA fragen</button>\n    <button type=\"button\" data-question=\"Wie nutze ich Schnee-Effekte?\">Schnee fragen</button>\n  </div>\n  <div class=\"demo-chat\" id=\"demoChat\">\n    <div class=\"demo-bubble\">Pixalia wartet auf deine Frage! ✨</div>\n  </div>\n</div>\n<script>\n  const replies = {\n    \"Wie gestalte ich die Navi?\": \"Nutze maximal vier Links mit klaren IDs und lasse Buttons sanft nach unten scrollen – wie Wegpunkte im Kompass!\",\n    \"Welche CTA-Texte passen?\": \"Arbeite mit Verben: \u201eQuest starten\u201c oder \u201eKI befragen\u201c. So wissen Besucher sofort, welcher Klick Magie ausl\u00f6st.\",\n    \"Wie nutze ich Schnee-Effekte?\": \"Lege ein eigenes div mit id snow-canvas an und lass tsparticles den Hintergrund f\u00fcllen, unabh\u00e4ngig vom Content.\"\n  };\n  document.querySelectorAll('.demo-actions button').forEach((btn) => {\n    btn.addEventListener('click', () => {\n      const question = btn.dataset.question;\n      const chat = document.getElementById('demoChat');\n      const userBubble = document.createElement('div');\n      userBubble.className = 'demo-bubble user';\n      userBubble.textContent = question;\n      chat.appendChild(userBubble);\n      setTimeout(() => {\n        const answer = document.createElement('div');\n        answer.className = 'demo-bubble';\n        answer.textContent = replies[question];\n        chat.appendChild(answer);\n        chat.scrollTop = chat.scrollHeight;\n      }, 400);\n    });\n  });\n</script>\n\"\"\")\n"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🚀 Deine Aufgabe – 3 magische TODOs\nIm Verzeichnis `Tag_22/Aufgabe/` ist die Seite zu 80 % fertig.\nDamit alles so beeindruckend wird wie in `Loesung/`, löst du drei klar markierte TODOs."""
        ),
        nbf.v4.new_markdown_cell(
            """### 📝 TODO 1 – HTML: Status-Panel zurückholen\n**Datei:** `Tag_22/Aufgabe/index.html` (Sektion `#hero`, rund um Zeile 80)\n```html\n<!-- TODO 1: Baue hier das Statuspanel mit Live-Daten nach ... -->\n```\nSo gehst du vor:\n1. Ersetze den Kommentar durch das komplette `<div class=\"hero-panel\">` aus der Lösung.\n2. Achte auf die Liste (`<ul class=\"mt-4 ...\">`) mit drei Status-Zeilen.\n3. Ergänze die kleine Infobox mit Überschrift **Projektauftrag**.\nDamit bekommt der Hero wieder die wichtige Übersicht, ob Navigation, LLM und Schneesturm aktiv sind."""
        ),
        nbf.v4.new_markdown_cell(
            """### 🎨 TODO 2 – CSS: Glas-Effekt für das Status-Panel\n**Datei:** `Tag_22/Aufgabe/style.css` (Mitte der Datei)\n```css\n/* TODO 2: Style hier das hero-panel mit Glas-Optik ... */\n```\nSetze hier die Eigenschaften aus der Lösung ein:\n- `border-radius: 2rem;` für die abgerundete Karte.\n- Halbtransparentes Blau (`background: rgba(14, 165, 233, 0.08)`).\n- Dezenter Rahmen + innerer Glow, damit das Panel wie eine Kommando-Konsole wirkt.\nOhne dieses Styling fehlt dem Panel der hochwertige Look und der Kontrast zur restlichen Seite."""
        ),
        nbf.v4.new_markdown_cell(
            """### ⚡ TODO 3 – JavaScript: `fetch()` zur LLM-API ergänzen\n**Datei:** `Tag_22/Aufgabe/script.js` (Funktion `requestCompletion`)\n```javascript\n// TODO 3: Implementiere hier den echten fetch()-Aufruf ...\nreturn \"TODO: Echter KI-Output fehlt noch\";\n```\nDeine Aufgabe:\n1. Baue den vollständigen `fetch()`-Request mit **LLMv7 Free Tier Support**!\n2. Header: Nur `Content-Type` erforderlich. API-Key optional für erweiterte Features.\n3. Verwende das Endpoint `https://api.llm7.io/v1/chat/completions` und übergib `model`, `temperature`, `messages` und `max_tokens`.\n4. Prüfe `response.ok`, lies JSON und gib `choices[0].message.content.trim()` zurück.\n🎉 **Vorteil:** Dank Free Tier antwortet die Chatbox sofort – ohne API-Key-Eingabe!"""
        ),
        nbf.v4.new_markdown_cell(
            """## 🏆 Erfolgskontrolle\nNach allen TODOs solltest du sehen:\n- Das Status-Panel mit Live-Dots glänzt rechts im Hero.\n- Das Panel besitzt die Glas-Optik und wirkt wie ein echtes Dashboard.\n- Der Chat liefert Antworten direkt aus gpt-4o-mini (kein Platzhalter mehr).\n- Schneefall, Navigation und CTA-Buttons bleiben weiterhin responsiv."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🌐 Teste deine Seite im Browser\n1. **Aufgabe vergleichen:** `http://192.168.0.20:8000/2025_Adventskalender/Tag_22/Aufgabe/`\n2. **Lösung ansehen:** `http://192.168.0.20:8000/2025_Adventskalender/Tag_22/Loesung/`\n3. **LLMv7 Free Tier testen:** 🎉 Direkt Frage eingeben – kein API-Key erforderlich!\n4. **Optional:** API-Key für erweiterte Features ausprobieren.\n5. **Fallback testen:** Zieh kurz das Netzwerkkabel – es muss eine freundliche Offline-Nachricht erscheinen."""
        ),
        nbf.v4.new_markdown_cell(
            """## 🌟 Bonus-Ideen ohne Spoiler\n- Ergänze ein weiteres Feature-Card, z. B. \"Server-Status\" mit kleinen Pixel-Icons.\n- Lass GSAP auch den Chat-Verlauf einblenden (`gsap.from('#chatHistory', ...)`).\n- Speichere den Namen des Besuchers und begrüße ihn im Hero.\n- Baue eine Option, mit der Nutzer das Schneetempo verändern können – kleine Slider reichen völlig aus."""
        ),
    ]

    nb.cells.extend(cells)

    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as error:
        print(f"❌ Validierungsfehler: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    """Speichert das Notebook im Tag-Ordner, egal von wo das Skript gestartet wird."""

    output_path = Path(__file__).resolve().parent / filename
    try:
        with output_path.open("w", encoding="utf-8") as file_handle:
            nbf.write(nb, file_handle)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as error:  # pylint: disable=broad-except
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
