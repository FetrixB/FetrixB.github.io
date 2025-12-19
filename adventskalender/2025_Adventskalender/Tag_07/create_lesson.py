#!/usr/bin/env python3
"""Erzeugt das Lesson.ipynb für Tag 07 – Scrollbasierte Story."""

from pathlib import Path
import sys
from textwrap import dedent
import nbformat as nbf


def md_cell(text: str):
    """Hilfsfunktion für dedentete Markdown-Zellen."""
    return nbf.v4.new_markdown_cell(dedent(text).strip())


def create_lesson():
    nb = nbf.v4.new_notebook()

    nb.cells.append(
        md_cell(
            """
            # 🎄 Tag 07 · Der Scroll-Schlitten erwacht

            Felix, der Chefelf hat dich zum Schneehof gerufen: Der legendäre Zauberschlitten steht wie versteinert herum! Er bewegt sich nur, wenn jemand seine Entstehung **von oben nach unten** liest und dabei die Scroll-Runen aktiviert. Deine Aufgabe: Baue eine Webseite, die wie eine magische Schriftrolle funktioniert. Jedes Scrollen lässt ein neues Schlittenteil auftauchen – genau wie im Story-Text aus `Tag_07.md`.
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            ## 🎯 Lernreise: Scroll-Story perfekt choreografieren

            - **Scroll-basierte Storytelling-Elemente**: Du lernst, wie man Inhalte schrittweise enthüllt, damit Zuschauer nicht alles auf einmal sehen.
            - **Intersection Observer API**: Dein unsichtbarer Wächter, der meldet, welches Element gerade im Fokus liegt.
            - **AOS.js (Animate On Scroll)**: Mit kleinen Daten-Attributen setzt du eine komplette Animationsbibliothek ein, ohne selbst Animationsfunktionen zu schreiben.
            - **Mobile-First Denken**: Die Story soll auf Tablets und Handys genauso cool wirken wie am großen Monitor.

            👉 Stell dir die Seite wie eine Minecraft-Quest vor: Jede Rolle im Inventar zeigt erst beim Scrollen ihren Bonus. Genau so fühlst du dich nach diesem Tag!
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            ### 🏗️ Die wichtigsten Bausteine

            **`<section data-aos="fade-up">`** ✨

            Mit AOS kannst du jedem Block eine eigene Animation geben. Ob `fade-up`, `zoom-in` oder `flip-up` – du entscheidest mit Daten-Attributen, was beim Scrollen passieren soll.

            ```html
            <section class="story-card" data-aos="zoom-in" data-aos-delay="200">
              <h3>Der Sternen-Antrieb</h3>
              <p>Er erscheint leicht zeitversetzt und wirkt dadurch lebendig.</p>
            </section>
            ```

            🔧 Minecraft-Vergleich: Wie die aktivierten Redstone-Fackeln – ohne das passende Signal (Scrollposition) tut sich nichts.

            **Intersection Observer** 🛰️

            ```javascript
            const observer = new IntersectionObserver((entries) => {
              entries.forEach((entry) => {
                if (entry.isIntersecting) {
                  entry.target.classList.add('sichtbar');
                }
              });
            }, { threshold: 0.55 });

            observer.observe(document.querySelector('.story-card'));
            ```

            Hier entscheidest du, ab wie viel sichtbarer Fläche (threshold) dein "Magie-Event" ausgelöst wird. In Minecraft würdest du sagen: "Nur wenn mehr als die Hälfte des Blocks frei liegt, funktioniert die Rune."
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            ### 🌐 Weitere wichtige Konzepte

            **Data-Attribute planen** (Animationen):

            ```html
            <article data-aos="fade-left" data-aos-duration="900" data-aos-delay="250"></article>
            ```

            - `data-aos` bestimmt den Typ (z.B. `fade-left`).
            - `data-aos-duration` legt fest, wie lange es dauert (in Millisekunden).
            - `data-aos-delay` wartet kurz, bevor der Effekt startet – perfektes Timing wie bei einer Redstone-Uhr.

            **Mobile-First Scrollbereiche**:

            ```css
            .story-card {
              min-height: 70vh; /* 70% der sichtbaren Höhe, damit auch auf dem Handy genug Fläche bleibt */
            }
            ```

            Je höher das Panel, desto leichter lässt sich die Scrollmagie auslösen, auch wenn Felix das Tablet schräg hält.
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            ## 🎨 Dein heutiges WOW-Ziel

            ✅ **Fortschritts-Rune** – Eine Leiste zeigt an, wie viel Magie bereits aktiviert ist.

            ✅ **Vier Story-Panels** – Gestell, Turbinen, Geschenkkammer und Probeflug erscheinen nacheinander.

            ✅ **AOS-Choreografie** – Jede Karte hat eine eigene Animation mit Delay und Dauer.

            ✅ **Sparkle-Schalter** – Ein Button sorgt für zusätzliche Sternenfunken (reiner Spaßfaktor!).

            🎮 **Endergebnis**: Eine vertikale Story-Seite, die aussieht wie ein animiertes Minecraft-Questlog.
            """
        )
    )

    nb.cells.append(md_cell("# 🧠 Verstehen"))

    nb.cells.append(
        md_cell(
            """
            ## 🔍 Konzept 1: Scroll-basierte Storytelling

            Eine gute Scroll-Story baut Spannung auf. Statt alles gleichzeitig zu zeigen, platzierst du deine Abschnitte untereinander und gibst jedem eine Mindesthöhe.

            ```html
            <main>
              <section class="story-card">Gestell</section>
              <section class="story-card">Antrieb</section>
              <section class="story-card">Laderaum</section>
              <section class="story-card">Probeflug</section>
            </main>
            ```

            🔑 Warum? Genau wie beim Erkunden eines Tempels willst du nicht schon hinter die dritte Tür schauen, bevor du den ersten Raum gelöst hast. Scrollen = Türen öffnen.
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            ## 🎨 Konzept 2: AOS.js als Animationsbibliothek

            Mit AOS (Animate On Scroll) brauchst du keine eigenen Keyframes. Du verknüpfst einfach Daten-Attribute mit Effekten.

            ```html
            <link rel="stylesheet" href="https://unpkg.com/aos@2.3.4/dist/aos.css">
            <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
            <script>
              AOS.init({ once: false, easing: 'ease-out-quart', offset: 160 });
            </script>
            ```

            - **`once: false`**: Die Animation wiederholt sich, wenn der Spieler zurückscrollt.
            - **`offset: 160`**: Startet den Effekt ein bisschen früher (160px bevor das Element die Mitte erreicht).

            🎁 Vergleich: Du legst fest, wann ein Redstone-Kolben loslegt – nicht sobald du ihn siehst, sondern kurz davor, damit alles flüssig wirkt.
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            ## ⚡ Konzept 3: Intersection Observer als Runenleser

            Der Intersection Observer überprüft ständig, ob ein Element gerade sichtbar ist. Kein `scroll`-Event-Spam nötig!

            ```javascript
            const activated = new Set();
            const observer = new IntersectionObserver((entries) => {
              entries.forEach((entry) => {
                if (entry.isIntersecting) {
                  activated.add(entry.target.dataset.index);
                } else {
                  activated.delete(entry.target.dataset.index);
                }
              });
              updateProgressBar();
            }, { threshold: 0.55 });
            ```

            - **`threshold: 0.55`** bedeutet: Mindestens 55% des Elements müssen sichtbar sein.
            - Mit einem `Set` vermeidest du doppelte Einträge und kannst schnell zählen, wie viele Karten aktiv sind.

            📟 Minecraft-Vergleich: Wie ein Beobachter-Block, der checkt, ob ein Feld wächst. Nur wenn genug Wachstum sichtbar ist, sendet er ein Signal.
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            # 🧪 Ausprobieren

            Starte die nächste Zelle, um eine Mini-Demo mit HTML, CSS und JavaScript zu sehen. Du kannst den Code später als Mini-Labor nutzen, indem du Werte in der Ausgabe änderst (Doppelklick ⇒ bearbeiten ⇒ `Ctrl+Enter`).
            """
        )
    )

    demo_html = dedent(
        '''
        from IPython.core.display import HTML
        HTML("""
        <!DOCTYPE html>
        <html lang="de">
          <head>
            <style>
              body {
                font-family: 'Inter', sans-serif;
                background: #020617;
                color: #e2e8f0;
                min-height: 100vh;
                margin: 0;
                padding: 32px;
              }
              .panel {
                border-radius: 18px;
                padding: 32px;
                margin-bottom: 24px;
                background: rgba(15,23,42,0.85);
                border: 1px solid rgba(148,163,184,0.3);
                transition: border-color 0.3s ease, box-shadow 0.3s ease;
                min-height: 45vh;
              }
              .panel.glow {
                border-color: #6ee7b7;
                box-shadow: 0 12px 35px rgba(14,165,233,0.35);
              }
              .progress {
                height: 12px;
                border-radius: 999px;
                background: rgba(15,118,110,0.35);
                overflow: hidden;
                margin-bottom: 24px;
              }
              .progress span {
                display: block;
                height: 100%;
                width: 0%;
                background: linear-gradient(90deg,#34d399,#a5f3fc);
                transition: width 0.4s ease;
              }
            </style>
          </head>
          <body>
            <div class="progress"><span id="progressFill"></span></div>
            <section class="panel" data-index="0">Gestell</section>
            <section class="panel" data-index="1">Antrieb</section>
            <section class="panel" data-index="2">Laderaum</section>
            <section class="panel" data-index="3">Probeflug</section>

            <script>
              const panels = document.querySelectorAll('.panel');
              const fill = document.getElementById('progressFill');
              const activated = new Set();

              const update = () => {
                const percent = (activated.size / panels.length) * 100;
                fill.style.width = `${percent}%`;
              };

              const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                  if (entry.isIntersecting) {
                    activated.add(entry.target.dataset.index);
                    entry.target.classList.add('glow');
                  } else {
                    activated.delete(entry.target.dataset.index);
                    entry.target.classList.remove('glow');
                  }
                });
                update();
              }, { threshold: 0.6 });

              panels.forEach((panel) => observer.observe(panel));
            </script>
          </body>
        </html>
        """)
        '''
    ).strip()

    nb.cells.append(nbf.v4.new_code_cell(demo_html))

    nb.cells.append(md_cell("# 🚀 Deine Aufgabe: Vertikale Scroll-Story bauen"))

    nb.cells.append(
        md_cell(
            """
            ## 🎯 Mission: 3 magische TODOs lösen

            Im Ordner `Tag_07/Aufgabe/` findest du eine fast fertige Version. Dir fehlen nur drei Runen, um die Scrollmagie komplett zu machen:

            1. **HTML** – Die Rune-Icons fehlen noch, damit der Fortschritt sichtbar ist.
            2. **CSS** – Der Fortschrittsbalken braucht wieder seinen Glow.
            3. **JavaScript** – Der Intersection Observer muss aktivierte Karten tracken.

            Sobald du diese Stellen ergänzt, sieht deine Seite aus wie die Lösung in `Tag_07/Loesung/`.
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            ### 📝 TODO 1: HTML – Rune-Icons ergänzen
            **Datei:** `Tag_07/Aufgabe/index.html` (ca. Zeile 48)

            ```html
            <!-- TODO 1: Füge hier die vier Rune-Icons (Rahmen, Triebwerk, Laderaum, Testflug) wie in der Lösung hinzu. -->
            ```

            💡 Ergänze ein `<div class="rune-icons">` mit vier `<span>`-Elementen und den passenden Emojis. Diese Spans werden später im Skript eingefärbt, sobald die Abschnitte sichtbar sind.
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            ### 🎨 TODO 2: CSS – Glow & Gradient zurückbringen
            **Datei:** `Tag_07/Aufgabe/style.css` (ca. Zeile 32)

            ```css
            /* TODO 2: Gib dem Fortschrittsbalken wieder seinen hellen Verlauf und lass aktive Karten schweben. */
            .rune-progress-fill {
              background: #16a34a;
              box-shadow: none;
            }
            ```

            ✨ Setze hier wieder den zweifarbigen Verlauf (`linear-gradient`) und einen weichen Box-Shadow ein. Direkt darunter solltest du außerdem `story-card-active` so stylen, dass die Karten leicht schweben. Schau dir zum Vergleich `Tag_07/Loesung/style.css` an.
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            ### ⚡ TODO 3: JavaScript – Sichtbarkeitslogik einfügen
            **Datei:** `Tag_07/Aufgabe/script.js` (ca. Zeile 32)

            ```javascript
            // TODO 3: Ergänze hier die komplette Sichtbarkeitslogik (aktive Karten ins Set, Klasse "story-card-active" setzen und wieder entfernen).
            ```

            👉 Ergänze an dieser Stelle beide Fälle (`isIntersecting` = wahr/falsch). Du brauchst:
            - `activated.add(cardIndex)` wenn die Karte sichtbar ist
            - `activated.delete(cardIndex)` wenn sie verschwindet
            - `entry.target.classList.add('story-card-active')` bzw. `remove`

            Danach aktualisiert `updateProgress()` automatisch den Balken und die Rune-Icons.
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            ## 🏆 Erfolgskontrolle

            Wenn alle TODOs erledigt sind, solltest du sehen:

            ✅ Die Fortschritts-Rune füllt sich während des Scrollens

            ✅ Jede Karte erhält beim Sichtbarwerden einen Glow

            ✅ Die Emojis (Rahmen, Triebwerk, Laderaum, Testflug) springen nacheinander nach oben

            ✅ Der Sternenfunken-Schalter reagiert weiterhin
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            ## 🌐 Teste deine Version

            - **Aufgabe:** https://web.tb-cloudlab.org/2025_Adventskalender/Tag_07/Aufgabe/
            - **Musterlösung:** https://web.tb-cloudlab.org/2025_Adventskalender/Tag_07/Loesung/

            Öffne beide Tabs nebeneinander und scrolle gleichzeitig. So siehst du sofort, ob alle Runen bei dir im gleichen Moment aufleuchten.
            """
        )
    )

    nb.cells.append(
        md_cell(
            """
            # 🌟 Weitere Ideen

            - Baue eine Mini-Navigation, die zu jedem Story-Abschnitt springt.
            - Lass Schneeflocken mit Anime.js langsamer schweben, wenn die Scrollgeschwindigkeit sinkt.
            - Erstelle ein Logbuch, das mitzählt, wie oft jedes Panel sichtbar war – perfekte Daten für Statistiken.
            - Probiere andere `data-aos`-Effekte wie `fade-up-right`, um diagonale Bewegungen einzubauen.
            """
        )
    )

    try:
        nbf.validate(nb)
    except nbf.ValidationError as error:
        print(f"❌ Validierungsfehler: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename: str = "Lesson.ipynb"):
    output = Path(__file__).with_name(filename)
    try:
        with open(output, "w", encoding="utf-8") as handle:
            nbf.write(nb, handle)
        print(f"✅ Lesson gespeichert: {output}")
        return output
    except OSError as exc:
        print(f"❌ Fehler beim Speichern: {exc}")
        sys.exit(1)


def main():
    print("🎄 Erstelle Lesson.ipynb für Tag 07...")
    notebook = create_lesson()
    save_notebook(notebook)
    print("✨ Fertig! Viel Spaß beim Scroll-Zauber.")


if __name__ == "__main__":
    main()
