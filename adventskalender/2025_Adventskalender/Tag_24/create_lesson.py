#!/usr/bin/env python3
"""
Lesson Generation für Tag 24 - Das große Finale: Minecraft-Weihnachtsspiel
"""

import nbformat as nbf
import sys
from pathlib import Path


def create_lesson():
    nb = nbf.v4.new_notebook()
    cells = []

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🎄 Tag 24 – Das große Finale: Minecraft-Weihnachtsspiel 🎮

**🎯 Lieber Felix,**

Du hast es geschafft! 23 Tage hast du gelernt, programmiert und erstaunliche Webseiten gebaut. Heute ist der große Tag – das Finale deiner Webentwicklungsreise! 

Die Eishexe lächelt stolz: *"Felix, du bist bereit für dein Meisterstück! Mit allem was du gelernt hast – HTML, CSS, JavaScript und jetzt auch Three.js – erschaffst du heute dein eigenes 3D-Browserspiel!"*

Der Bürgermeister des Minecraft-Weihnachtsreichs ruft begeistert: *"Das gesamte Weihnachtsreich wartet auf dich! Sammle Geschenke, besiege Schneemänner mit Schneebällen und erreiche das magische Portal. Du wirst der Held unseres Reiches!"*

**🌟 Das ist mehr als nur Code – das ist dein digitales Kunstwerk!**"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎯 Was lernst du heute? Das ultimative Finale!

Heute vereinst du **alles** was du in 24 Tagen gelernt hast in einem großartigen 3D-Spiel:

### 🧠 **HTML** - Die Struktur deines Spiels
- Mehrere Bildschirme (Intro, Spiel, Victory)
- UI-Overlays für Score und Anweisungen
- Canvas für die 3D-Darstellung
- Audio-Elemente für Soundeffekte

### 🎨 **CSS** - Das Design und die Animationen
- Minecraft-Pixel-Ästhetik mit Orbitron-Font
- Komplexe Animationen und Übergänge
- Responsive Design für alle Bildschirmgrößen
- Gradient-Hintergründe und Glüh-Effekte

### ⚡ **JavaScript** - Die Spiellogik
- Objektorientierte Programmierung
- Event Handling für Maus und Tastatur
- Game Loop und Animation
- State Management für Spielzustände

### 🌐 **Three.js** - 3D-Grafik im Browser
- Scene, Camera und Renderer
- 3D-Geometrien und Materialien
- Beleuchtung und Schatten
- Physik und Kollisionserkennung"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🏗️ Three.js Game Development - Deine 3D-Welt zum Leben erwecken

**Was ist Three.js eigentlich?**

Stell dir vor, du könntest Minecraft direkt im Browser spielen, ohne Downloads! Three.js macht genau das möglich. Es ist eine JavaScript-Bibliothek, die deinem Browser beibringt, 3D-Welten zu verstehen.

**🎮 Die wichtigsten Konzepte:**

**Scene (Szene)** - Das ist wie ein leerer Minecraft-Chunk. Hier platzierst du alle deine 3D-Objekte:
```javascript
scene = new THREE.Scene();
scene.background = new THREE.Color(0x87CEEB); // Himmelblau wie in Minecraft
```

**Camera (Kamera)** - Das sind deine "Augen" im Spiel. Genau wie in Minecraft schaust du durch diese Kamera:
```javascript
camera = new THREE.PerspectiveCamera(75, width/height, 0.1, 1000);
// 75° Blickwinkel - das ist wie dein Sichtfeld in Minecraft!
```

**Renderer (Zeichner)** - Das ist der "Motor", der alles auf den Bildschirm malt. Wie Minecraft's Render-Engine:
```javascript
renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
```

**🏗️ Warum ist das so mächtig?**
- **Hardware-beschleunigt**: Nutzt deine Grafikkarte wie echte Spiele!
- **Cross-Platform**: Läuft auf PC, Mac, Handy, Tablet – überall!
- **Echte 3D-Physik**: Objekte können sich bewegen, kollidieren, Schatten werfen"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🌐 Game Development Patterns - Wie echte Spiele funktionieren

**🔄 Der Game Loop - Das Herz jedes Spiels**

Jedes Spiel (egal ob Minecraft, Fortnite oder dein Browser-Spiel) hat einen "Game Loop". Das ist wie ein Herzschlag - 60 mal pro Sekunde passiert das:

```javascript
function animate() {
    requestAnimationFrame(animate); // "Nächster Herzschlag bitte!"
    
    // 1. INPUT: Was macht der Spieler? (WASD, Mausklick)
    updatePlayerMovement();
    
    // 2. LOGIC: Was passiert in der Welt? (Schneebälle fliegen, Geschenke rotieren)
    updateSnowballs();
    updateGifts();
    
    // 3. RENDER: Zeige alles auf dem Bildschirm
    renderer.render(scene, camera);
}
```

**🎯 Collision Detection - Wann berühren sich Objekte?**

In deinem Spiel musst du wissen: "Berührt der Spieler ein Geschenk? Trifft der Schneeball den Schneemann?"

```javascript
const distance = player.position.distanceTo(gift.position);
if (distance < 3) {
    collectGift(gift); // Geschenk einsammeln!
}
```

Das ist wie in Minecraft: Der Server prüft ständig, ob du einen Block berührst, ein Item aufhebst oder Schaden nimmst.

**📊 State Management - Der Zustand deines Spiels**

Dein Spiel "merkt" sich alles Wichtige:
```javascript
let gameState = {
    isPlaying: false,        // Läuft das Spiel gerade?
    giftsCollected: 0,       // Wie viele Geschenke hast du?
    snowmenHit: 0,          // Wie viele Schneemänner besiegt?
    missionComplete: false   // Mission erfolgreich?
};
```

**💡 Warum ist das wichtig?**
Du lernst hier echte Game Development Techniken, die in Unity, Unreal Engine und anderen Profi-Tools genauso funktionieren!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎨 Dein Minecraft-Weihnachtsspiel: Ein komplettes 3D-Abenteuer!

**🌟 Was du heute erstellst:**

Ein vollständiges Browser-Spiel mit:
- **3D-Minecraft-Welt** mit Bäumen, Terrain und Portal
- **First-Person-Steuerung** (WASD + Maus wie in echten Spielen)
- **Sammle 10 Weihnachtsgeschenke** (sie rotieren und schweben!)
- **Bekämpfe 5 Schneemänner** mit geworfenen Schneebällen
- **Erreiche das Portal** wenn die Mission erfüllt ist
- **Victory Screen** mit deinen Statistiken
- **Fallender Schnee** und Weihnachtsatmosphäre

**🎯 Gameplay-Features:**
- **Score-System**: Verfolge deinen Fortschritt in Echtzeit
- **Mission-basiert**: Klare Ziele und Erfolgs-Feedback
- **Physik**: Schneebälle fliegen realistisch und fallen zu Boden
- **Animationen**: Geschenke rotieren, Schnee fällt, Portal leuchtet
- **Sound-Ready**: Bereit für Weihnachtsmusik und Effekte

Das ist kein einfaches "Hallo Welt" - das ist ein **echtes Spiel** das du stolz deinen Freunden zeigen kannst! 🚀"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🧪 Verstehen & Ausprobieren - Die Magie von 3D im Browser

Bevor du dein Spiel vervollständigst, lass uns verstehen wie die 3D-Magie funktioniert!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🔍 Scene Setup - Deine 3D-Welt erschaffen

**Wie baut man eine 3D-Szene auf?**

Think Step-by-Step: Stell dir vor, du baust eine Filmkulisse:

1. **Scene = Dein Filmstudio** (der leere 3D-Raum)
2. **Camera = Deine Filmkamera** (von wo aus schaust du?)  
3. **Objects = Schauspieler und Requisiten** (Bäume, Geschenke, Schneemänner)
4. **Lights = Beleuchtung** (ohne Licht siehst du nichts!)
5. **Renderer = Der Regisseur** (bringt alles zusammen auf den "Film")

**📦 Minecraft-Blöcke in Three.js:**

```javascript
// Ein einfacher Minecraft-Block:
const blockGeometry = new THREE.BoxGeometry(1, 1, 1); // 1x1x1 Würfel
const blockMaterial = new THREE.MeshLambertMaterial({ color: 0x7EC850 }); // Grasgrün
const grassBlock = new THREE.Mesh(geometry, material);
grassBlock.position.set(x, y, z); // Position im 3D-Raum
scene.add(grassBlock); // Hinzufügen zur Szene
```

**🎨 Warum BoxGeometry?**
Minecraft ist berühmt für seine Würfel! BoxGeometry erstellt perfekte Quader - genau wie Minecraft-Blöcke. Du kannst die Breite, Höhe und Tiefe einzeln bestimmen."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎨 Materialien und Farben - Deine Blöcke zum Leben erwecken

**Was sind Materialien in 3D?**

Stell dir vor, du baust einen echten Minecraft-Block aus verschiedenen Materialien:
- **Holz** sieht anders aus als **Metall** 
- **Glas** reflektiert Licht anders als **Stein**
- **Lava** leuchtet, **Wasser** ist durchsichtig

In Three.js funktioniert das genauso:

**🔹 MeshLambertMaterial - Für matte Oberflächen:**
```javascript
const grassMaterial = new THREE.MeshLambertMaterial({ 
    color: 0x7EC850  // Minecraft-Grasgrün
});
```
Perfect für: Grasblöcke, Holz, Stein

**✨ Emissive Materials - Für leuchtende Objekte:**
```javascript
const starMaterial = new THREE.MeshLambertMaterial({
    color: 0xFFD700,           // Goldgelb
    emissive: 0xFFD700,        // Leuchtet goldgelb 
    emissiveIntensity: 0.3     // Wie stark das Leuchten ist
});
```
Perfect für: Sterne auf Bäumen, Portal-Effekte, Geschenke

**🌈 Farbcodes verstehen:**
- `0xFFFFFF` = Weiß (alle Farben an)
- `0xFF0000` = Rot (nur Rot-Kanal an)  
- `0x00FF00` = Grün (nur Grün-Kanal an)
- `0x0000FF` = Blau (nur Blau-Kanal an)
- `0x7EC850` = Minecraft-Grasgrün"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## ⚡ Player Controls - Bewegung wie in echten Spielen

**🎮 First-Person-Steuerung verstehen:**

In deinem Spiel bewegst du dich wie in Minecraft oder anderen First-Person-Spielen:

**🖱️ Maus-Steuerung (Camera-Rotation):**
```javascript
function onMouseMove(event) {
    if (document.pointerLockElement) { // Maus ist "gefangen"
        const sensitivity = 0.002; // Wie schnell du dich umschaust
        
        // Links/Rechts schauen (Y-Achse Rotation)
        player.rotation.y -= event.movementX * sensitivity;
        
        // Hoch/Runter schauen (X-Achse Rotation)  
        player.rotation.x -= event.movementY * sensitivity;
    }
}
```

**⌨️ Tastatur-Steuerung (WASD Movement):**
```javascript
function onKeyDown(event) {
    switch (event.code) {
        case 'KeyW': controls.moveForward = true; break;   // Vorwärts
        case 'KeyS': controls.moveBackward = true; break;  // Rückwärts  
        case 'KeyA': controls.moveLeft = true; break;      // Links
        case 'KeyD': controls.moveRight = true; break;     // Rechts
    }
}
```

**🚀 Bewegung in 3D-Raum:**
```javascript
const moveVector = new THREE.Vector3(0, 0, 0);
if (controls.moveForward) moveVector.z -= speed;
if (controls.moveBackward) moveVector.z += speed;

// Bewegung an Kamera-Rotation anpassen (du gehst in Blickrichtung!)
moveVector.applyQuaternion(camera.quaternion);
camera.position.add(moveVector);
```

**💡 Pointer Lock - Warum wichtig?**
`canvas.requestPointerLock()` "fängt" deine Maus ein, genau wie in echten Spielen. Ohne das würdest du aus dem Fenster "rausschauen"!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🧪 Live Demo - Experimentiere mit deinem Code!

Lass uns gemeinsam schauen, wie dein 3D-Spiel funktioniert! Öffne deine Dateien und schaue dir die wichtigsten Teile an."""
        )
    )

    cells.append(
        nbf.v4.new_code_cell(
            """# 🎮 Analysiere dein 3D-Spiel!
# Lass uns durch deinen Code schauen und verstehen was passiert

from IPython.display import HTML
import os

# Prüfe ob die Dateien existieren
aufgabe_path = "Aufgabe/"
loesung_path = "Loesung/"

aufgabe_exists = os.path.exists(aufgabe_path + "index.html")
loesung_exists = os.path.exists(loesung_path + "index.html")

html_content = f\"\"\"
<div style="background: linear-gradient(135deg, #1a472a 0%, #2d5aa0 50%, #1a472a 100%); 
            padding: 30px; border-radius: 15px; color: white; 
            font-family: 'Orbitron', monospace; border: 3px solid #ffcc00;">
    
    <h2 style="color: #ffcc00; text-align: center; margin-bottom: 25px; 
               text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">
        🎮 Dein Minecraft-Weihnachtsspiel Analyse 🎮
    </h2>
    
    <div style="background: rgba(0,0,0,0.6); padding: 20px; border-radius: 10px; 
                margin: 15px 0; border: 2px solid rgba(255,204,0,0.3);">
        <h3 style="color: #00ff00; margin-bottom: 15px;">📁 Datei-Check:</h3>
        <p style="margin: 8px 0;">
            <span style="color: {'#00ff00' if aufgabe_exists else '#ff0000'};">
                {'✅' if aufgabe_exists else '❌'} Aufgabe/index.html
                {'(Bereit zum Vervollständigen!)' if aufgabe_exists else '(Noch nicht erstellt)'}
            </span>
        </p>
        <p style="margin: 8px 0;">
            <span style="color: {'#00ff00' if loesung_exists else '#ff0000'};">
                {'✅' if loesung_exists else '❌'} Loesung/index.html  
                {'(Vollständige Lösung verfügbar!)' if loesung_exists else '(Noch nicht erstellt)'}
            </span>
        </p>
    </div>
    
    <div style="background: rgba(0,100,0,0.3); padding: 20px; border-radius: 10px; 
                margin: 15px 0; border: 2px solid #00ff00;">
        <h3 style="color: #ccffcc; margin-bottom: 15px;">🎯 Was dein Spiel kann:</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin: 8px 0; color: #ffffff;">🎄 <strong>3D-Minecraft-Welt</strong> - Bäume, Terrain, Portal</li>
            <li style="margin: 8px 0; color: #ffffff;">🕹️ <strong>First-Person-Controls</strong> - WASD + Maus wie echte Spiele</li>
            <li style="margin: 8px 0; color: #ffffff;">🎁 <strong>Geschenke sammeln</strong> - 12 bunte, rotierende Geschenke</li>
            <li style="margin: 8px 0; color: #ffffff;">⛄ <strong>Schneemänner bekämpfen</strong> - Mit geworfenen Schneebällen</li>
            <li style="margin: 8px 0; color: #ffffff;">🌟 <strong>Portal erreichen</strong> - Magisches Weihnachtsportal als Ziel</li>
            <li style="margin: 8px 0; color: #ffffff;">❄️ <strong>Schneefall-Animation</strong> - 1000 fallende Schneepartikel</li>
            <li style="margin: 8px 0; color: #ffffff;">🏆 <strong>Victory Screen</strong> - Erfolgsfeier mit Statistiken</li>
        </ul>
    </div>
    
    <div style="background: rgba(100,0,100,0.3); padding: 20px; border-radius: 10px; 
                margin: 15px 0; border: 2px solid #ff00ff;">
        <h3 style="color: #ffccff; margin-bottom: 15px;">⚡ Technische Features:</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
            <div>
                <p style="color: #ffffff; margin: 5px 0;"><strong>HTML:</strong> Multi-Screen UI</p>
                <p style="color: #ffffff; margin: 5px 0;"><strong>CSS:</strong> Minecraft-Pixelart</p>
                <p style="color: #ffffff; margin: 5px 0;"><strong>JavaScript:</strong> Game Loop</p>
            </div>
            <div>
                <p style="color: #ffffff; margin: 5px 0;"><strong>Three.js:</strong> 3D-Rendering</p>
                <p style="color: #ffffff; margin: 5px 0;"><strong>Physics:</strong> Kollisionserkennung</p>
                <p style="color: #ffffff; margin: 5px 0;"><strong>Audio:</strong> Sound-System</p>
            </div>
        </div>
    </div>
    
    <div style="text-align: center; margin-top: 25px;">
        <p style="color: #ffcc00; font-size: 1.2em; font-weight: bold; 
                 text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">
            🚀 Das ist kein kleines Projekt - das ist ein ECHTES SPIEL! 🚀
        </p>
        <p style="color: #ffffff; margin-top: 10px;">
            Felix, du hast in 24 Tagen mehr gelernt als viele in einem Jahr. 
            Darauf kannst du stolz sein! 🌟
        </p>
    </div>
    
</div>
\"\"\"

HTML(html_content)"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🚀 Deine Aufgabe - Vervollständige dein 3D-Meisterstück!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎯 Mission: Das ultimative Finale!

**🌟 Felix, heute ist DER Tag!** 

Du hast 23 Tage lang HTML, CSS und JavaScript gelernt. Heute setzt du alles zusammen in einem spektakulären 3D-Browserspiel!

**🎮 Deine Mission:**
1. **Vervollständige den Victory Screen** (HTML)
2. **Aktiviere die Victory-Animationen** (CSS)  
3. **Verbinde den Neustart-Button** (JavaScript)

Nach diesen 3 TODOs hast du ein **vollständiges 3D-Spiel** erstellt! Das ist eine unglaubliche Leistung! 🚀

**🏆 Das Ziel:**
Ein spielbares Minecraft-Weihnachtsspiel wo du:
- In einer 3D-Welt herumläufst (First-Person wie in echten Spielen!)
- Geschenke sammelst (sie rotieren und schweben!)
- Schneebälle auf Schneemänner wirfst (mit echter Physik!)
- Das magische Portal erreichst (nach erfüllter Mission!)
- Den Victory Screen mit deinen Erfolgen siehst!

**💎 Warum ist das besonders?**
Du erstellst hier nicht nur eine Webseite - du programmierst ein **echtes Spiel** mit 3D-Grafik, Physik, Animationen und Interaktionen. Das können nicht viele!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 📝 **TODO 1: Victory Screen hinzufügen (HTML)**
**Datei:** `Tag_24/Aufgabe/index.html` (zwischen Game UI und Game Canvas)

**Was zu tun ist:**
```html
<!-- Füge hier den kompletten Victory Screen ein -->
<div id="victory-screen" class="victory-screen hidden">
    <div class="victory-content">
        <h1 class="victory-title">🏆 MISSION ERFOLGREICH! 🏆</h1>
        <p class="victory-subtitle">Du hast das Minecraft-Weihnachtsreich gerettet!</p>
        
        <div class="victory-stats">
            <div class="stat-item">
                <span class="stat-icon">🎁</span>
                <span>Geschenke gesammelt: <span id="final-gifts">0</span></span>
            </div>
            <div class="stat-item">
                <span class="stat-icon">⚔️</span>
                <span>Schneemänner besiegt: <span id="final-snowmen">0</span></span>
            </div>
            <div class="stat-item">
                <span class="stat-icon">⏱️</span>
                <span>Zeit: <span id="final-time">0</span> Sekunden</span>
            </div>
        </div>
        
        <div class="celebration-text">
            <p>🎉 Fantastisch, Felix!</p>
            <p>In 24 Tagen hast du HTML, CSS und JavaScript gemeistert!</p>
            <p>Du hast dein eigenes 3D-Spiel programmiert! 🚀</p>
            <p>Das Minecraft-Weihnachtsreich ist dank dir gerettet! 🌟</p>
        </div>
        
        <button id="play-again" class="play-again-button">
            🔄 Nochmal spielen
        </button>
    </div>
</div>
```

**Lösungshinweis:** Kopiere den kompletten Victory Screen Code aus der Musterlösung und füge ihn nach dem Game UI Overlay ein. Achte darauf, dass alle IDs korrekt sind (final-gifts, final-snowmen, final-time, play-again)!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🎨 **TODO 2: Victory Screen Styles aktivieren (CSS)**
**Datei:** `Tag_24/Aufgabe/style.css` (ersetze den TODO-Kommentar)

**Was zu tun ist:**
```css
/* Victory Screen Styles - Spektakuläre Gewinn-Animation! */
.victory-screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: linear-gradient(135deg, #ffd700 0%, #ff6b35 50%, #f7931e 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2000;
    animation: victoryAppear 1.5s ease-in-out;
}

.victory-content {
    text-align: center;
    max-width: 900px;
    padding: 50px;
    background: rgba(0, 0, 0, 0.9);
    border: 6px solid #ffd700;
    border-radius: 20px;
    box-shadow: 
        0 0 60px rgba(255, 215, 0, 0.8),
        inset 0 0 30px rgba(255, 255, 255, 0.1);
}

/* Weitere Styles hier einfügen... */
```

**Lösungshinweis:** Kopiere alle Victory-Screen-Styles aus der Musterlösung, inklusive der @keyframes Animationen für victoryAppear und pulse. Das macht den Gewinn-Bildschirm richtig spektakulär!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### ⚡ **TODO 3: Play-Again Button verbinden (JavaScript)**
**Datei:** `Tag_24/Aufgabe/script.js` (in der init() Funktion)

**Was zu tun ist:**
```javascript
// Event Listeners für UI-Buttons
document.getElementById('start-game').addEventListener('click', startGame);
document.getElementById('play-again').addEventListener('click', restartGame);
```

**Lösungshinweis:** Füge die zweite Zeile in die init() Funktion ein, direkt nach dem start-game Event Listener. Das verbindet den "Nochmal spielen" Button mit der restartGame() Funktion, die bereits implementiert ist!

**🎯 Warum ist das wichtig?**
Ohne diesen Event Listener bleibt der "Nochmal spielen" Button stumm. Mit dieser einen Zeile Code wird dein Spiel endlos wiederholbar - echte Game-Experience! 🎮"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🏆 Erfolgs-Kriterien - Woran erkennst du dass es funktioniert?

**✅ Nach TODO 1 (HTML):**
- Victory Screen wird angezeigt wenn du das Portal erreichst
- Alle Statistiken (Geschenke, Schneemänner, Zeit) werden gezeigt
- Button "🔄 Nochmal spielen" ist sichtbar

**✅ Nach TODO 2 (CSS):**
- Victory Screen hat spektakuläre goldene Animationen
- Titel pulsiert und leuchtet mit Goldeffekt
- Hintergrund zeigt schönen Gradienten-Effekt
- Responsive Design funktioniert auch auf kleineren Bildschirmen

**✅ Nach TODO 3 (JavaScript):**
- "Nochmal spielen" Button startet das Spiel neu
- Alles wird zurückgesetzt (Score, Objekte, Position)
- Du kannst unendlich oft spielen und deinen Highscore verbessern!

**🌟 Vollständiger Test:**
1. Spiel starten → Intro-Screen erscheint
2. Klicke "🚀 Spiel Starten" → 3D-Welt lädt
3. Sammle 10 Geschenke und besiege 5 Schneemänner  
4. Erreiche das Portal → Victory Screen mit Animationen
5. Klicke "🔄 Nochmal spielen" → Spiel startet neu

**Das ist dann ein vollständiges 3D-Browserspiel! 🎮**"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🌐 Teste dein 3D-Spiel!

**📱 So testest du dein Minecraft-Weihnachtsspiel:**

1. **Öffne deinen Browser** und navigiere zu:
   ```
   https://web.tb-cloudlab.org/2025_Adventskalender/Tag_24/Aufgabe/
   ```

2. **Prüfe die Grundfunktionen:**
   - Intro-Screen lädt mit Minecraft-Design ✓
   - "🚀 Spiel Starten" aktiviert die 3D-Welt ✓
   - WASD-Bewegung funktioniert smooth ✓
   - Maus-Look (nach dem Klick auf Canvas) ✓

3. **Teste das Gameplay:**
   - Geschenke sammeln durch Berührung ✓
   - Schneebälle werfen mit Linksklick ✓
   - Schneemänner treffen und besiegen ✓
   - UI zeigt korrekte Scores ✓

4. **Victory Test:**
   - Nach 10 Geschenken + 5 Schneemännern ✓
   - Portal leuchtet grün ✓
   - Victory Screen mit Animationen ✓
   - Neustart funktioniert ✓

**🚀 Tipp für beste Performance:**
Dein 3D-Spiel nutzt WebGL - das läuft am besten in Chrome, Firefox oder Edge. Auf älteren Handys könnte es langsamer laufen, aber auf PCs/Laptops sollte es smooth mit 60fps laufen!

**📱 Mobile Test:**
Das Spiel funktioniert auch auf Tablets! Auf Handys ist die Steuerung schwieriger (nur Touch, keine Maus), aber der Code ist responsive bereit."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🌟 Erfolg & Möglichkeiten - Du bist jetzt ein Game Developer!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🏆 GRATULATION FELIX! DU HAST ES GESCHAFFT! 🏆

**🎉 Was du in nur 24 Tagen erreicht hast ist UNGLAUBLICH!**

### 🚀 **Du bist jetzt Master in:**

**🌐 HTML** - Struktur und Semantik
- Von einfachen Texten zu komplexen Game-UIs
- Multi-Screen-Anwendungen mit Canvas-Integration
- Audio, Video und interaktive Elemente
- Responsive Design für alle Geräte

**🎨 CSS** - Design und Animationen  
- Von Basic-Styling zu Pixel-Art-Ästhetik
- Komplexe Animationen und Übergänge
- Grid, Flexbox und moderne Layouts
- Minecraft-Style und Gaming-Design

**⚡ JavaScript** - Programmierung und Logik
- Von Variablen zu objektorientierter Programmierung
- Event-Handling und User-Interaction
- Async Programming und API-Integration
- Game Development Patterns

**🌟 Three.js** - 3D-Grafik im Browser
- Scene, Camera, Renderer Setup
- 3D-Geometrien und Materialien
- Beleuchtung, Schatten und Physik
- Game Loop und Performance-Optimierung

### 🎯 **Dein Portfolio ist UNSCHLAGBAR:**

1. **HTML-Strukturen** - Von einfach bis komplex ✅
2. **CSS-Animations** - Smooth und beeindruckend ✅  
3. **JavaScript-Games** - Interaktiv und spaßig ✅
4. **3D-Browserspiel** - Das Highlight! ✅
5. **Responsive Design** - Funktioniert überall ✅
6. **Version Control** - Alles auf GitHub ✅

**💎 Du beherrschst jetzt den KOMPLETTEN Web-Stack für moderne Anwendungen!**"""
        )
    )

    # Add cells to notebook
    for cell in cells:
        nb.cells.append(cell)

    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as error:
        print(f"❌ Validierungsfehler: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    """Speichert das Notebook in die angegebene Datei."""
    output_path = Path.cwd() / filename

    try:
        with open(output_path, "w", encoding="utf-8") as file_handler:
            nbf.write(nb, file_handler)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as error:
        print(f"❌ Fehler beim Speichern: {error}")
        sys.exit(1)


def main():
    """Hauptfunktion - erstellt das Tag 24 Lesson Notebook."""
    print("🎄 Erstelle Tag 24 Lesson.ipynb - Das große Finale!")
    print("=" * 60)
    print("🎮 Minecraft-Weihnachtsspiel - 3D Game Development")
    print("⭐ HTML + CSS + JavaScript + Three.js")
    print("=" * 60)
    nb = create_lesson()
    output_path = save_notebook(nb)
    print("=" * 60)
    print("🏆 FINALE LESSON ERSTELLT! Tag 24 komplett!")
    print(f"📁 Pfad: {output_path}")
    print("🎉 Felix kann sein 3D-Spiel vervollständigen!")


if __name__ == "__main__":
    main()
