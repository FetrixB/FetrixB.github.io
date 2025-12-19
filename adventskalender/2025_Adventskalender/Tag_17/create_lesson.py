#!/usr/bin/env python3
"""Erstellt die finalisierte Lesson.ipynb für Tag 17."""

from pathlib import Path
import nbformat as nbf
import sys


def md_cell(text: str):
    """Hilfsfunktion für saubere Markdown-Zellen."""
    return nbf.v4.new_markdown_cell(text.strip())


def code_cell(code: str):
    """Hilfsfunktion für Python-Code-Zellen."""
    return nbf.v4.new_code_cell(code.strip())


def create_lesson():
    nb = nbf.v4.new_notebook()

    cells = [
        md_cell(
            """
            # 🎄 Tag 17 – Die Geschenk-Manufaktur braucht dich!

            Die Werkstatt der Weihnachts-Elfen klingelt wie eine überfüllte Minecraft-Schmiede.
            Geschenkewünsche ploppen schneller auf als Creeper in einer Nacht voller Gewitter.
            Du bist heute der Funkions-Zauberer: Mit smarten JavaScript-Rezepten erschaffst du
            neue Items genau so, wie ein Loot-Table in Minecraft Truhen füllt. Die Elfen zählen
            auf dich und deinen Kopf voller Parameter, Rückgabewerte und Zufallslogik!
            """
        ),
        md_cell(
            """
            ## 📚 Deine Lernmission heute

            - **Funktionen als Rezepte**: Du lernst, wie `function`-Deklarationen und Function-Expressions
              miteinander arbeiten, um lesbaren und wiederverwendbaren Code zu bauen.
            - **Parameter + Default-Werte**: Wie kann eine Funktion flexibel reagieren, wenn Spieler*innen
              andere Wünsche eingeben oder einfach nichts übergeben?
            - **Return-Statements mit Daten**: Unsere Funktionen liefern fertige Geschenk-Objekte zurück.
            - **Zufall mit Struktur**: `Math.random()` reicht – aber erst mit Gewichtungen wirkt der Loot echt.
            - **Dateiverknüpfung**: Du arbeitest parallel mit `Tag_17/Aufgabe/` und kontrollierst alles mit der
              Musterlösung in `Tag_17/Loesung/`.
            """
        ),
        md_cell(
            """
            ### 🏗️ Funktionen & Parameter verstehen

            In `Tag_17/Loesung/script.js` findest du den Herzschlag der Seite – die Funktion
            `generateGiftBatch`. Sie nimmt gleich mehrere Parameter entgegen und zerlegt sie Schritt für Schritt.

            ```javascript
            function generateGiftBatch(category, amount = 3, options = {}) {
              const { includeMystery = false, rarityBoost = 1 } = options;
              const safeAmount = clampAmount(amount);
              const gifts = [];

              for (let i = 0; i < safeAmount; i += 1) {
                const gift = rollItem(category, rarityBoost);
                if (gift) {
                  gifts.push({ ...gift, id: crypto.randomUUID(), category });
                }
              }

              if (includeMystery) {
                gifts.push({ ...createMysteryCube(), id: crypto.randomUUID(), category: "mystery" });
              }

              return gifts;
            }
            ```

            - `amount = 3` ist der **Default-Parameter**. Auch ohne Eingabe entstehen drei Geschenke.
            - Das Objekt `options` erlaubt flexible Zusätze, z. B. ob ein Überraschungswürfel auftaucht.
            - `return gifts;` liefert die fertige Liste zurück – ähnlich, wie wenn ein Hopper in Minecraft alle Items
              weitergibt.
            """
        ),
        md_cell(
            """
            ### 🎲 Gewichtete Zufälle statt wilder Chaos-Drops

            Damit legendäre Items selten bleiben, nutzt die Musterlösung eine zusätzliche Funktion `buildWeightedPool`.
            Sie dupliziert Einträge je nach Gewicht und Booster-Faktor. Das erhöht oder senkt Wahrscheinlichkeiten ohne
            komplizierte Mathe.

            ```javascript
            function buildWeightedPool(pool, rarityBoost = 1) {
              const weighted = [];
              pool.forEach((item) => {
                const boostMultiplier = item.rarity === "legendary" ? rarityBoost : 1;
                const copies = Math.max(1, Math.round(item.weight / boostMultiplier));
                for (let i = 0; i < copies; i += 1) {
                  weighted.push(item);
                }
              });
              return weighted;
            }
            ```

            > Minecraft-Analogie: Stell dir vor, du füllst einen Sack mit Karten. Häufige Items haben viele Kopien,
            > seltene Items nur wenige. Der Booster sorgt dafür, dass legendäre Karten (Goldkarten!) etwas öfter im Sack
            > landen – aber nur, wenn du ihn wirklich aufdrehst.
            """
        ),
        md_cell(
            """
            ### 🗂️ Überblick über deine Dateien

            | Datei | Inhalt | Hinweis |
            | --- | --- | --- |
            | `Tag_17/Loesung/index.html` | Voll ausgestaltete Oberfläche inkl. Status-Legende und Story | Nutze sie als Referenz beim Testen |
            | `Tag_17/Loesung/style.css` | Neon-Look, Pop-Animation für Loot-Karten, Schneefall-Hintergrund | Achte auf die Animation `pop` |
            | `Tag_17/Loesung/script.js` | Vollständige Funktionen inkl. Booster-Logik | Lies Kommentare für Erklärungen |
            | `Tag_17/Aufgabe/*` | 80 % fertig, 3 TODOs | Genau diese Stellen schließt du gleich |
            """
        ),
        md_cell(
            """
            ## 🧪 Verstehen & Ausprobieren

            Interaktive Demos helfen enorm, bevor du im Code arbeitest. Teste den folgenden Mini-Generator. Er nutzt
            dieselben Ideen wie die große Version, nur kompakter, damit du jeden Schritt nachvollziehen kannst.
            """
        ),
        code_cell(
            """
            from IPython.core.display import HTML

            HTML(\"\"\"
            <style>
              .demo-wrapper {
                font-family: \"Nunito\", sans-serif;
                background: radial-gradient(circle, #1d4ed8, #0f172a);
                border-radius: 18px;
                padding: 24px;
                color: #f8fafc;
                box-shadow: 0 20px 40px rgba(15, 23, 42, 0.7);
              }
              .demo-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
                gap: 12px;
                margin-top: 16px;
              }
              .demo-card {
                background: rgba(15, 23, 42, 0.85);
                border: 1px solid rgba(248, 250, 252, 0.2);
                border-radius: 14px;
                padding: 12px;
                text-align: center;
              }
              .demo-card span {
                font-size: 2rem;
              }
              .demo-controls {
                display: flex;
                gap: 12px;
                flex-wrap: wrap;
                margin-top: 16px;
              }
              .demo-controls select,
              .demo-controls button {
                padding: 10px 14px;
                border-radius: 10px;
                border: none;
                font-weight: 600;
              }
              .demo-controls button {
                background: linear-gradient(120deg, #4ade80, #38bdf8);
                color: #04111f;
                cursor: pointer;
              }
            </style>
            <div class=\"demo-wrapper\">
              <h3>Mini-Geschenk-Generator</h3>
              <p>Dieser Mini nutzt Math.random() genauso wie deine große Aufgabe. Probiere verschiedene Kategorien!</p>
              <div class=\"demo-controls\">
                <select id=\"demo-category\">
                  <option value=\"spielzeug\">Spielzeug</option>
                  <option value=\"buecher\">Bücher</option>
                  <option value=\"kleidung\">Kleidung</option>
                  <option value=\"games\">Games</option>
                </select>
                <button onclick=\"window.generateDemoLoot()\">Loot erzeugen</button>
              </div>
              <div id=\"demo-grid\" class=\"demo-grid\"></div>
            </div>
            <script>
              const demoPools = {
                spielzeug: [\"🤖 Robo\", \"🪃 Boomerang\", \"🧸 Plush\"],
                buecher: [\"📘 Koordinaten\", \"📕 Redstone\", \"📗 Winter\"],
                kleidung: [\"🧣 Poncho\", \"🥾 Boots\", \"🧥 Mantel\"],
                games: [\"🎮 PixelKart\", \"🕹️ Skyblock\", \"🎵 Rhythm\"]
              };

              window.generateDemoLoot = function() {
                const category = document.getElementById(\"demo-category\").value;
                const pool = demoPools[category];
                const picked = Array.from({ length: 3 }, () => pool[Math.floor(Math.random() * pool.length)]);
                document.getElementById(\"demo-grid\").innerHTML = picked
                  .map((emoji) => `<div class=\\"demo-card\\"><span>${emoji}</span><p>${category}</p></div>`)
                  .join(\"\");
              };

              window.generateDemoLoot();
            </script>
            \"\"\")
            """
        ),
        md_cell(
            """
            ## 🚀 Deine Aufgabe – 3 magische TODOs

            Öffne `Tag_17/Aufgabe/` im Editor und löse die drei markierten Stellen:

            1. **HTML (Status-Legende)** – Datei `index.html`, rund um den Generator-Status.
               - Suche nach `TODO 1`.
               - Baue die vier Badges (Gewöhnlich, Selten, Episch, Legendär) wieder ein.
               - Tipp: Schau dir die fertige Struktur in `Loesung/index.html` an – sie besteht aus einem `.legend`-Container
                 und vier `<span>`-Elementen.
            2. **CSS (Pop-Animation)** – Datei `style.css`, im Block `.gift-card`.
               - Dort findest du `TODO 2`.
               - Füge die `animation: pop 0.6s ease;` plus die zugehörige `@keyframes pop`-Definition wieder ein, damit jedes
                 neue Item wie eine Beutekiste aufploppt.
            3. **JavaScript (Gewichtete Pools)** – Datei `script.js`, Funktion `buildWeightedPool`.
               - `TODO 3` erinnert dich daran, legendäre Items mit dem Booster zu verstärken.
               - Implementiere die gleiche Logik wie in `Loesung/script.js`: Kopiere Items mehrfach je nach Gewicht und
                 reduziere die Kopienzahl, wenn `rarityBoost` größer als 1 ist.

            **Workflow-Tipp:** Löse TODO 3 zum Schluss. Du kannst das Verhalten direkt im Browser sehen, indem du das
            HTML aus dem Aufgabe-Ordner unter `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_17/Aufgabe/` öffnest.
            """
        ),
        md_cell(
            """
            ## ✅ Erfolgskontrolle

            - Beim Klick auf "✨ Geschenke erzeugen" erscheinen Karten mit Emoji, Titel und Beschreibung.
            - Die Legende erklärt sofort, welche Farbe zu welcher Seltenheit gehört.
            - Stellst du den Booster hoch, trudeln legendäre Items sichtbar häufiger ein.
            - Vergleich mit `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_17/Loesung/` zeigt identisches Verhalten.
            """
        ),
        code_cell(
            """
            from IPython.core.display import HTML

            HTML(\"\"\"
            <section style=\"font-family: 'Nunito', sans-serif; background:#020617; color:#f8fafc; padding:24px; border-radius:18px; border:1px solid rgba(148,163,184,0.3);\">
              <h3 style=\"margin-top:0;\">🌟 Was jetzt möglich ist</h3>
              <ul>
                <li>Du planst Funktionen wie Crafting-Rezepte und steuerst sie komplett über Parameter.</li>
                <li>Du nutzt Default-Werte, damit dein Code nicht abstürzt, wenn mal etwas fehlt.</li>
                <li>Du baust faire Zufallstabellen mit Gewichtung – perfekt für Mini-Games oder Lootboxen.</li>
                <li>Du kannst dieses System erweitern: Baue Filter für Rüstungssets oder füge Sounds hinzu.</li>
              </ul>
              <p>Neugierig? Als nächstes kannst du Statistik-Anzeigen ergänzen oder die Items in einer Datenbank speichern.
              So wird deine Werkstatt zu einem echten Weihnachts-Command-Block! 🎅</p>
            </section>
            \"\"\")
            """
        ),
    ]

    nb.cells = cells

    try:
        nbf.validate(nb)
    except nbf.ValidationError as error:
        print(f"❌ Validierungsfehler: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    base_path = Path(__file__).parent
    output_path = base_path / filename
    with open(output_path, "w", encoding="utf-8") as file:
        nbf.write(nb, file)
    print(f"✅ Lesson gespeichert: {output_path}")
    return output_path


def main():
    print("🎄 Erstelle Lesson.ipynb für Tag 17...")
    nb = create_lesson()
    save_notebook(nb)
    print("✨ Fertig! Öffne das Notebook in JupyterLab und starte durch.")


if __name__ == "__main__":
    main()
