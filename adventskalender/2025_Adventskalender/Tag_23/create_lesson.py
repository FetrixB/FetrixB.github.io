#!/usr/bin/env python3
"""
Erstellt die Lesson.ipynb Datei für Tag 23.
"""

import nbformat as nbf
import sys
from pathlib import Path


def create_lesson():
    nb = nbf.v4.new_notebook()
    cells = []

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🎄 Tag 23 – Portal zur Schneeflocken-Dimension\n\nDu stehst vor dem schimmernden Portal in der verschneiten Minecraft-Welt. Dahinter schwebt ein dreidimensionales Biom, in dem Schneeflocken nicht einfach nur fallen, sondern in alle Richtungen tanzen. Der Portal-Wächter grinst: *\"Nur wer Scene, Camera und Partikel beherrscht, kann dieses Tor stabil halten!\"* Heute lernst du genau diese Magie."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎯 Was du heute meisterst\n- **Scene + Camera + Renderer** als Grundpfeiler jeder Three.js-Welt\n- **Point-Geometrie & Shader-Material** für leichte Partikelwolken\n- **Animation-Loops** mit `requestAnimationFrame` für kontinuierliche Bewegung\n- **DOM-Überlagerungen + GSAP** für hybride Interfaces wie im echten Portal-HUD"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🏗️ Die wichtigsten Three.js-Bausteine\n\n**`Scene + Camera + Renderer`** – das Trio, das du auch in `Loesung/script.js` findest. Stelle dir die Szene wie deine Minecraft-Welt vor, die Kamera wie deine Augen und den Renderer wie die Grafikkarte, die alles auf den Canvas zeichnet.\n\n```javascript\nconst scene = new THREE.Scene();\nscene.fog = new THREE.FogExp2(0x030712, 0.015);\n\nconst camera = new THREE.PerspectiveCamera(60, 1, 0.1, 200);\ncamera.position.set(0, 10, 45);\n\nconst renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });\nrenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));\n```\n\n*Minecraft-Analogie:* Scene = Biome, Camera = dein Kopf in Ego-Perspektive, Renderer = die tickende Redstone-Maschine, die alles sichtbar macht."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🌐 Partikelsystem + Shader-Magie\n\n**`BufferGeometry` + `PointsMaterial`** halten den Schneesturm super leicht. In der Lösung erzeugst du 1600 Koordinatenpunkte, speicherst pro Flocke eine Geschwindigkeit und lässt sie im Loop neu erscheinen.\n\n```javascript\nconst snowGeometry = new THREE.BufferGeometry();\nconst snowPositions = new Float32Array(count * 3);\nconst snowVelocities = new Float32Array(count);\n\nfor (let i = 0; i < count; i += 1) {\n  const i3 = i * 3;\n  snowPositions[i3] = (Math.random() - 0.5) * spread;\n  snowPositions[i3 + 1] = Math.random() * 40 - 15;\n  snowPositions[i3 + 2] = (Math.random() - 0.5) * spread;\n  snowVelocities[i] = 0.12 + Math.random() * 0.25;\n}\n```\n\n*Analogie:* Jede Schneeflocke ist wie ein Minecraft-Schneeball mit eigener Flugbahn, die du selbst festlegst."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎨 Dein praktisches WOW-Ziel heute:\n\n✅ **3D-Canvas im Header** – Das Portal läuft hinter deinem Text, genau wie in `Loesung/index.html`.\n\n✅ **Portal-HUD mit Statistiken** – Karten zeigen Partikelzahl und Lichtmodus.\n\n✅ **Speed-Slider + GSAP-Burst** – DOM-Kontrolle, die direkt auf die Partikel reagiert.\n\n✅ **Responsive Renderer** – Fenstergröße ändert sich? Dein Canvas passt sich automatisch an.\n\n**Endergebnis:** Ein lebendiger Schneesturm, der beim Öffnen der Seite sofort wie ein Bosskampf aussieht."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🧠 Verstehen\nBevor du in den Code springst, schau dir an, wie die einzelnen Bausteine zusammenspielen. Alles, was du hier lernst, findest du 1:1 in `Loesung/script.js` wieder."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🔍 Scene + Camera – dein Koordinatenkompass\n\n- Die Szene sammelt Portal, Partikel und Licht.\n- Die Kamera bestimmt den Blickwinkel (60° wirkt wie ein leichtes Weitwinkel).\n- Du aktualisierst `camera.aspect` jedes Mal, wenn du die Canvasgröße änderst (`updateRendererSize` in der Lösung).\n\n```javascript\nconst updateRendererSize = () => {\n  const { clientWidth, clientHeight } = canvas;\n  renderer.setSize(clientWidth, clientHeight, false);\n  camera.aspect = clientWidth / clientHeight;\n  camera.updateProjectionMatrix();\n};\n```\n\n*Minecraft-Vergleich:* Wenn du im Creative-Modus die Kamera wechselst, musst du auch deine Sicht anpassen, sonst siehst du zu wenig von deiner Base."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎨 Materialien & Portallicht\n\n- `MeshStandardMaterial` + Emissive-Farben lassen den Torus wie Glowstone strahlen.\n- Zwei PointLights geben Tiefe: ein frostiges Blau rechts, ein warmes Licht links.\n- `FogExp2` sorgt dafür, dass entfernte Partikel verschwimmen wie Schnee im Sturm.\n\n```javascript\nconst portalTorus = new THREE.Mesh(\n  new THREE.TorusGeometry(12, 2.6, 32, 200),\n  new THREE.MeshStandardMaterial({\n    color: 0x38bdf8,\n    emissive: 0x164e63,\n    metalness: 0.4,\n    roughness: 0.2,\n    emissiveIntensity: 1.2,\n  })\n);\n```\n\n*Analogie:* Du platzierst Laternen im Dorf, damit jeder Block Tiefe bekommt."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## ⚡ DOM-Kontrollen & GSAP Feedback\n\nDer Slider (`#speedControl`) in beiden Verzeichnissen verbindet HTML und 3D. Über ein Event änderst du `speedMultiplier`, passt das HUD an und lässt GSAP die Karten aufflackern. In `Aufgabe/script.js` fehlt genau dieses Event noch – das wird dein drittes TODO!\n\n```javascript\nconst handleSpeedChange = (value) => {\n  speedMultiplier = Number(value);\n  snowLabel.textContent = `${Math.round(speedMultiplier * 100)}%`;\n  portalMood.textContent = describeSpeed(speedMultiplier);\n};\n```\n\n*Minecraft-Vergleich:* Stell dir vor, du schiebst einen Redstone-Regler, der sofort den Schneefall im Biom verstärkt."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🧪 Ausprobieren – baue ein Mini-Kontrollfeld\nFühre die folgende Zelle aus und spiele mit dem Slider. Du siehst sofort, wie DOM-Events Text und Effekte verändern können."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """from IPython.core.display import HTML\nHTML(\"\"\"\n<style>\n  .demo-shell {\n    font-family: 'Space Grotesk', sans-serif;\n    background: radial-gradient(circle at top, rgba(56,189,248,.2), rgba(2,6,23,.95));\n    border: 1px solid rgba(56,189,248,.4);\n    border-radius: 24px;\n    padding: 24px;\n    color: white;\n    max-width: 420px;\n    margin: 1rem auto;\n    box-shadow: 0 25px 50px rgba(2,6,23,.6);\n  }\n  .demo-ring {\n    width: 140px;\n    aspect-ratio: 1/1;\n    border-radius: 50%;\n    margin-inline: auto;\n    margin-block: 1rem;\n    background: radial-gradient(circle, rgba(14,165,233,.8), rgba(3,7,18,.2));\n    box-shadow: 0 0 35px rgba(14,165,233,.6);\n    transition: transform .3s ease, box-shadow .3s ease;\n  }\n  .demo-slider {\n    width: 100%;\n    accent-color: #38bdf8;\n  }\n</style>\n<div class='demo-shell'>\n  <p style='letter-spacing:.3em;text-transform:uppercase;color:rgba(224,242,254,.8);font-size:.75rem;'>Portal-HUD</p>\n  <h3 style='font-family: "Orbitron", sans-serif;'>Kontrolliere die Schneesphäre</h3>\n  <div class='demo-ring' id='demoRing'></div>\n  <p id='demoLabel'>Portalenergie: 60%</p>\n  <input id='demoSlider' class='demo-slider' type='range' min='40' max='140' step='5' value='60' />\n</div>\n<script>\n  const slider = document.getElementById('demoSlider');\n  const label = document.getElementById('demoLabel');\n  const ring = document.getElementById('demoRing');\n  slider.addEventListener('input', (event) => {\n    const value = Number(event.target.value);\n    label.textContent = `Portalenergie: ${value}%`;\n    ring.style.transform = `scale(${1 + (value - 60) / 120})`;\n    ring.style.boxShadow = `0 0 ${20 + (value - 40)}px rgba(14,165,233,.7)`;\n  });\n</script>\n\"\"\")\n"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🚀 Deine Aufgabe: Portalsteuerung fertigstellen\nIm Ordner `Tag_23/Aufgabe/` wartet eine fast fertige Version der Seite. Drei gezielte TODOs machen aus dem Rohbau dein finales Portal."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎯 Mission: 3 magische TODOs lösen\n1. **HTML (index.html):** Der Slider fehlt noch – ohne ihn bleibt der Sturm statisch.\n2. **CSS (style.css):** Der Glow-Effekt des Buttons muss aktiviert werden, damit das Interface leuchtet.\n3. **JavaScript (script.js):** Das `input`-Event muss `speedMultiplier` wirklich verändern.\n\nMit diesen drei Zaubern erreichst du das Niveau der Musterlösung."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 📝 **TODO 1: HTML – Slider einsetzen**\n**Datei:** `Aufgabe/index.html`, Bereich `#control`.\n\n**Was zu tun ist:**\n```html\n<!-- TODO 1: Füge hier das Range-Input mit der ID \"speedControl\" ein (min 1, max 3, Schritt 0.1, Startwert 1.2). -->\n```\n**So löst du es:** Nutze `<input type="range">`, gib die Attribute `min`, `max`, `step` und `value` an und vergiss die ID `speedControl` nicht. So kann dein Script das Element später finden."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🎨 **TODO 2: CSS – Portal-Glow aktivieren**\n**Datei:** `Aufgabe/style.css`, Klasse `.glow-button`.\n\n**Was zu tun ist:**\n```css\n/* TODO 2: Ergänze hier einen auffälligen box-shadow, damit der Button leuchtet wie ein Portal. */\n```\n**So löst du es:** Gib dem Button einen `box-shadow` wie `0 12px 40px rgba(56, 189, 248, 0.45)`. Damit bekommt Felix sofort optisches Feedback, genau wie im fertigen HUD."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### ⚡ **TODO 3: JavaScript – Slider-Event verdrahten**\n**Datei:** `Aufgabe/script.js`, dort wo `speedControl` abgefragt wird.\n\n**Was zu tun ist:**\n```javascript\nif (speedControl) {\n  updateHUD(speedMultiplier);\n  // TODO 3: Reagiere hier auf das \"input\"-Event des Sliders und rufe updateHUD + die neue speedMultiplier-Belegung auf.\n}\n```\n**So löst du es:** Lege einen Event-Listener auf `input`, setze `speedMultiplier = Number(event.target.value)` und rufe `updateHUD(speedMultiplier);` auf. Danach rauschen die Partikel schneller – du steuerst das Portal wirklich!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🏆 Erfolgskontrolle\nNach den drei TODOs solltest du folgendes sehen:\n\n✅ Der Slider bewegt sich und ändert den HUD-Text.\n\n✅ Die Button-Leiste glüht wie ein echtes Portal.\n\n✅ Die Partikel beschleunigen oder verlangsamen sich merkbar.\n\n✅ Beim Klick auf \"Schneepower\" pulsiert das HUD dank GSAP."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🌐 Testen deiner Lösung\n- Aufgabe öffnen: `http://192.168.0.20:8000/2025_Adventskalender/Tag_23/Aufgabe/`\n- Lösung vergleichen: `http://192.168.0.20:8000/2025_Adventskalender/Tag_23/Loesung/`\n- Prüfe die Konsole auf Fehler und achte auf FPS, wenn du den Slider auf Maximum schiebst."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🌟 Weitere Ideen\n- Erhöhe `count` auf 3000 und teste, ob dein Gerät es schafft.\n- Erstelle zusätzliche DOM-Karten (z. B. Windrichtung) und binde sie ans Script.\n- Tausche `PointsMaterial` gegen ein ShaderMaterial mit Textur aus, um noch realistischere Flocken zu zeichnen.\n- Füge eine zweite Kamera hinzu und baue eine Mini-Minimap im DOM, die die Szene von oben zeigt."""
        )
    )

    nb.cells = cells

    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as error:
        print(f"❌ Validierungsfehler: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    output_path = Path.cwd() / filename
    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            nbf.write(nb, handle)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as exc:  # noqa: BLE001
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
