# Agenten-Kontext – Minecraft Weihnachts-Webentwicklungs-Adventskalender

Dieser Text definiert den vollständigen Kontext für Agenten, die Dateien, Inhalte oder Aufgaben für das Adventskalender-Webentwicklungsprojekt generieren sollen.

## 🎁 Projektbeschreibung

Ich erstelle einen **24-Tage Minecraft-Weihnachts-Webentwicklungs-Adventskalender** für meinen Sohn.  
Er soll innerhalb von 24 Tagen lernen, **Webseiten zu entwickeln**, auf motivierende, storybasierte und visuell beeindruckende Weise.

Jeder Tag enthält:
- Hintergrundgeschichte (Minecraft-Weihnachtswelt)
- Lernmaterial (HTML, CSS, JavaScript)
- Aufgaben
- Boilerplate als HTML/CSS/JS
- Musterlösung als HTML/CSS/JS

---

## 🧒 Zielgruppe

Mein Sohn Felix (12 Jahre alt) kann bereits mit GitHub arbeiten, hat aber Webentwicklung erst teilweise gelernt.  
Die Materialien müssen:
- persönlich und direkt an ihn gerichtet
- motivierend und ermutigend
- **ausführlich und pädagogisch erklärt** (nicht nur technisch korrekt!)
- **kindgerecht für einen 12-Jährigen**: Keine Fachbegriffe ohne Erklärung, Schritt-für-Schritt-Anleitungen, Analogien verwenden
- **Mit Kontext und Hintergrund**: Nicht nur WAS, sondern auch WARUM und WIE es funktioniert
- altersgerecht aber technisch fundiert

---

## 🧪 Jupyter Notebook Nutzung

**⚠️ WICHTIGER HINWEIS FÜR AGENTEN:**  
In jedem **`Tag_XX/`** Verzeichnis liegt eine **`create_lesson.py`** Datei. Diese muss editiert und ausgeführt werden, um das **`Lesson.ipynb`** Notebook zu erstellen. Die Datei verwendet `nbformat` zur programmatischen Notebook-Erstellung und enthält bereits die vollständige Template-Struktur.

Zu jedem Tag wird ein Notebook **Lesson.ipynb** erzeugt, das:
- Die Hintergrundgeschichte anschaulich und mit Emojis in jugendlicher Sprache erzählt
- Theorie erklärt
- Aufgaben stellt
- Referenzen auf Boilerplate-Dateien enthält
- kindgerechte Erklärungen und Beispiele bietet

Alle Dateien werden in **JupyterLab** geöffnet und müssen dafür optimiert sein. HTML-Seiten müssen im Browser geöffnet werden über den Server **`http://192.168.0.20:8000/2025_Adventskalender/Tag_XX/`**.

**🎯 KRITISCHER ENTWICKLUNGSHINWEIS:**  
**KEINE reinen Python-Code-Zellen verwenden!** Stattdessen muss pro Lerninhalt an einem Tag ein kleines, self-contained **IPython mit interaktivem HTML()** genutzt werden:
- `from IPython.core.display import HTML` importieren
- Alle Ausgaben über `HTML(html_content)` mit eingebetteten, modernen CSS-Stylings und Javascript-Elementen
- Interaktive Widgets statt simpler `print()` Ausgaben
- Responsive Layouts, Animationen und Hover-Effekte für bessere UX
- Visuelle Gamification-Elemente und ansprechende Designs
- **HTML-Strings quotation-safe**: Verwende Triple-Quotes `"""` für HTML-Content und escaped Quotes `\"` innerhalb der HTML-Strings
- **CSS-Properties sicher escapen**: Alle Anführungszeichen in CSS-Properties korrekt als `\"` schreiben
- **Kompakte Demo-Beispiele**: Kurze, fokussierte HTML-Strings für interaktive Demos um Quotation-Fehler zu vermeiden (ausführliche Inhalte in separaten Dateien)

---

## 📂 Verzeichnisstruktur

Für **jeden Tag (Tag_XX)** gilt folgende Struktur:

```
Tag_XX/
    Aufgabe/
        index.html
        style.css
        script.js
    Loesung/
        index.html
        style.css
        script.js
    Tag_XX.md
    create_lesson.py
    Lesson.ipynb
```

- **Tag_XX.md** - Enthält die ursprüngliche Aufgabenstellung (vom Menschen erstellt)
- **create_lesson.py** - Python-Skript zur Notebook-Erstellung (muss editiert und ausgeführt werden)
- **Lesson.ipynb** - Interaktives Lernmaterial (von create_lesson.py generiert)
- **Aufgabe/** - Vereinfachte Boilerplate-Dateien mit 3 TODOs (vom Agenten erstellt)
- **Loesung/** - Vollständige Musterlösung (vom Agenten erstellt)

---

## 🟦 Verwendete Technologien

**Kein Build-Prozess. Nur CDNs.**

### Erlaubte Bibliotheken (nur via CDN):

**CSS/UI Libraries:**
- TailwindCSS (Hauptframework)
- Animate.css (einfache Animationen)
- Google Fonts (Orbitron für Minecraft-Look)

**JavaScript Libraries:**
- Anime.js (Animationen)
- GSAP (fortgeschrittene Animationen, ab Woche 3)
- Three.js (3D-Effekte, nur in Woche 4)

**🔧 Library-Validierung mit Context7 MCP:**
- **Vor Verwendung**: Nutze Context7 MCP Tools um CDN-URLs, Syntax und Best Practices für TailwindCSS, Anime.js, GSAP und Three.js zu prüfen
- **Dokumentation**: Lass dir von Context7 MCP aktuelle API-Beispiele und Verwendungsmuster zeigen
- **Kompatibilität**: Prüfe mit Context7 MCP ob die Library-Versionen zusammenpassen

**Design-Richtlinien:**
- Minecraft-Pixel-Ästhetik
- Weihnachtsfarben (Rot, Grün, Gold, Weiß)
- Orbitron/monospace Schriften
- Emoji-Integration für Jugend-Appeal

---

## 🟩 Pädagogischer Aufbau

### Woche 1 – HTML
Elemente, Strukturen, Navigation, Aufbau von Webseiten.

### Woche 2 – CSS
Design, Layout, Animationen, visuelle Effekte.

### Woche 3 – JavaScript
Variablen, Bedingungen, Funktionen, Arrays, DOM, Events.

### Woche 4 – Projekt
Finale komplette Webseite, GitHub Pages Deployment.

---

## 🧙 Story-Thema: Das Minecraft-Weihnachtsreich

Das gesamte Projekt ist eine magische Minecraft-Weihnachtsgeschichte.  
Jeder Tag ist ein Ort, ein Objekt oder ein Ereignis in dieser Welt.

---

## ⭐ Agentenaufgaben - Vollständiger Arbeitsablauf

### 🔄 **ZWINGEND: 4-Schritte-Prozess**

#### 1️⃣ **ZUERST: Musterlösung erstellen** (`Loesung/` Verzeichnis)
- Vollständige, beeindruckende HTML/CSS/JS-Dateien
- Alle Lerninhalte des Tag_XX.md umsetzen  
- Gut kommentierte, professionelle Lösung
- **Diese ist die Referenz für Aufgaben und Notebook!**

**🔍 Sofort-Validierung nach Schritt 1:**
- JavaScript Syntax: `node --check Tag_XX/Loesung/script.js`
- CSS Syntax: `stylelint Tag_XX/Loesung/style.css`
- HTML-Struktur: DOCTYPE, head, body korrekt
- **Playwright MCP Browser-Tests**: Lade die Webseite (`http://192.168.0.20:8000/2025_Adventskalender/Tag_XX/Loesung/`), teste zentrale UI-Funktionen (Interaktionen, Effekte, Layout, Stile und Fonts) mit Playwright MCP und erstelle dabei Screenshots zur visuellen Validierung jeder Anforderungen
- **Bei Fehlern: Schritt 1 korrigieren und erneut validieren**

#### 2️⃣ **DANN: Aufgaben-Boilerplate ableiten** (`Aufgabe/` Verzeichnis)
- **Vereinfachte Version** der Musterlösung (80% fertig)
- Genau **3 TODO-Stellen** (1× HTML, 1× CSS, 1× JS)
- Strategisches "Entfernen" von 3 Kernelementen aus der Lösung
- Klare TODO-Kommentare mit Hinweisen
- Maximal 15-20 Minuten Bearbeitungszeit

##### 🎯 **Aufgaben-Erstellung (Schritt-für-Schritt)**

**Schritt A: Musterlösung analysieren**
```
- Was sind die 3 wichtigsten/sichtbarsten Features?
- Welche können ohne Funktionsverlust temporär entfernt werden?
- Welche sind für den Lerneffekt am wertvollsten?
```

**Schritt B: Strategisches Entfernen**
```
- HTML: Ein wichtiges sichtbares Element auskommentieren
- CSS: Eine wichtige Style-Regel entfernen/deaktivieren  
- JS: Eine Funktion/Event unvollständig lassen
```

**Schritt C: TODO-Kommentare hinzufügen**
```
<!-- TODO 1: Füge hier den [spezifisches Element] hinzu -->
/* TODO 2: Aktiviere hier die [spezifische Style-Regel] */
// TODO 3: Vervollständige den [spezifische Funktion]
```

#### 3️⃣ **DANN: Jupyter Notebook erstellen** (`Lesson.ipynb`)
- Editiere die **`create_lesson.py`** im Tag_XX Verzeichnis
- Passe alle Platzhalter (markiert mit `[Brackets]`) mit den tatsächlichen Inhalten an
- Basiert komplett auf den fertigen Lösungs- UND Aufgabendateien
- **Ausführliche Lerninhalte**: Konzepte erklären, nicht nur zeigen
- Erklärt alle verwendeten Konzepte der Lösung mit Beispielen und Hintergründen
- Referenziert echte Dateien und Code-Beispiele aus BEIDEN Verzeichnissen
- Minecraft-Weihnachtsgeschichte mit Webentwicklungs-Bezug
- **Vertiefungshinweise**: Was jetzt möglich ist, ohne kommende Tage zu verraten
- Führe das Skript im `Tag_XX`-Ordner aus: `python create_lesson.py`

#### 4️⃣ **ABSCHLIESSEND: Finale Gesamtvalidierung** (Qualitätssicherung)

**Vollständige Validierungs-Checkliste (alle müssen bestanden werden):**

1. **JavaScript-Syntax**: `node --check Tag_XX/Loesung/script.js` & `node --check Tag_XX/Aufgabe/script.js`
2. **Notebook JSON-Syntax**: `python -c "import json; json.load(open('Tag_XX/Lesson.ipynb'))"`
3. **Browser-Funktionalität mit Playwright MCP**: Lade die Webseite (`http://192.168.0.20:8000/2025_Adventskalender/Tag_XX/Loesung/`), teste zentrale UI-Funktionen (Interaktionen, Effekte, Layout, Stile und Fonts) mit Playwright MCP und erstelle dabei Screenshots zur visuellen Validierung jeder Anforderungen
4. **Library-Integration mit Context7 MCP**: Prüfe mit Context7 MCP ob verwendete CSS/JS-Libraries korrekt eingebunden sind und funktionieren
5. **Workflow-Test**: Die 3 TODOs können zur Lösung führen (manuell testen)
6. **Notebook-Konsistenz**: Alle Dateipfad-Referenzen existieren
7. **Gesamtkonsistenz**: Notebook, Aufgaben und Lösung harmonieren perfekt

**Bei Validierungs-Fehlern:**
- **Syntax/Browser-Fehler** → Zurück zu Schritt 1 (Musterlösung)
- **Library-Fehler** → Zurück zu Schritt 1, prüfe CDN-URLs und Syntax mit Context7 MCP
- **Workflow-Fehler** → Zurück zu Schritt 2 (Aufgaben-Boilerplate)
- **Konsistenz-Fehler** → Zurück zu Schritt 3 (Notebook)
- **Erfolgs-Kriterium**: Alle 7 Punkte bestanden ✅

### ✅ **Allgemeine Qualitätsregeln**
- **🚫 VERZEICHNIS-BESCHRÄNKUNG**: Agenten dürfen NUR im aktuellen Tag_XX Verzeichnis arbeiten - KEINE anderen Tag-Ordner öffnen!
- **Dateistruktur**: Niemals ändern (index.html, style.css, script.js)
- **Technologien**: Nur CDNs, keine Build-Prozesse, keine lokalen Module
- **Design**: Minecraft-Weihnachts-Thema durchgängig
- **Sprache**: **Kindgerecht für 12-Jährige!** Keine technischen Abkürzungen ohne Erklärung. Statt "Funktion X macht Y" → "Warum brauchen wir das? Was passiert Schritt für Schritt? Wie funktioniert das genau?"
- **Erklärungstiefe**: Immer mit Kontext, Beispielen und Analogien arbeiten (z.B. "Das ist wie wenn du in Minecraft...")
- **Konsistenz**: Notebook muss 1:1 mit echten Dateien übereinstimmen
- **Kreativität**: Erwünscht bei Story und Design, aber alle Lerninhalte aus Tag_XX.md beibehalten
- **Kommentare**: Boilerplate und Musterlösungen ausführlich und verständlich kommentieren

---

## ❗ Detailregeln für Agenten

### 📏 **Aufgaben-Dimensionierung (Adventskalender-gerecht)**

- **Zeitrahmen**: Maximal 15-20 Minuten Bearbeitungszeit pro Tag
- **3-TODO-Regel**: Exakt 3 konkrete Änderungen zum Erreichen der Lösung
- **80/20-Prinzip**: Boilerplate bereits 80% fertig, nur 20% zu ergänzen
- **Erfolgserlebnis**: Überforderung vermeiden, Motivation fördern
- **Progressive Schwierigkeit**: Tag 1 einfach → Tag 24 anspruchsvoll

### 🔍 **TODO-Verteilung (verpflichtend)**

```
1 × HTML-TODO: Element hinzufügen/ändern (z.B. Titel, Bild, Link)
1 × CSS-TODO: Style aktivieren/ändern (z.B. Farbe, Animation, Layout)  
1 × JS-TODO: Funktion vervollständigen (z.B. Event, Variable, Output)
```



## 📓 Jupyter Notebook Template

Jedes `Lesson.ipynb` muss folgender Struktur folgen:

### 🎯 Zellen-Reihenfolge (schlank für Adventskalender):

1. **Titel & Story** (Markdown): Tag-Nummer + Minecraft-Weihnachtsgeschichte aus `Tag_XX.md`
2. **Lern-Kapitel** (Markdown): Ausführliche Konzepterklärung + Theorie + Hintergründe + Was lernst du heute
3. **Verstehen & Ausprobieren** (Markdown + Code): Interaktive Demos + praktische Beispiele zum Experimentieren + Code-Übungen
4. **Deine Aufgabe** (Markdown): Die 3 TODOs Schritt-für-Schritt erklärt
5. **Erfolg & Möglichkeiten** (Python + Markdown): Was du jetzt kannst + Vertiefungsrichtungen

### 🎨 Stil-Richtlinien:

#### Markdown-Zellen:
- **Überschriften**: Immer mit passenden Emojis (🎄, 🎮, 💎, ⚡, 🌟)
- **Ansprache**: Direkt an Felix gerichtet ("Du", "Deine")
- **Tonfall**: Motivierend, freundlich, altersgerecht für 12-Jährige
- **Minecraft-Bezug**: Analogien zu Blöcken, Crafting, Redstone verwenden um Konzepte zu erklären
- **Struktur**: Kurze Absätze, Bullet Points, Code-Blöcke mit ausführlichen Erklärungen
- **Lerntiefe**: **SEHR WICHTIG!** Ausführliche, pädagogische Erklärungen mit Beispielen, Hintergründen und Schritt-für-Schritt-Anleitungen

#### 📚 Erklärungsstil (KRITISCH für 12-Jährige!):

**❌ NICHT SO (zu technisch, zu kurz):**
> "Die Funktion updateProgress(page, total) aktualisiert Label, Balkenbreite und den drehenden Sigil."

**✅ SONDERN SO (kindgerecht, ausführlich, pädagogisch):**
> "Schauen wir uns die Funktion `updateProgress()` genauer an - was macht sie eigentlich?
> 
> Stell dir vor, du spielst ein Spiel und es gibt eine Fortschrittsanzeige. Diese Funktion ist genau dafür da!
> 
> Sie bekommt zwei wichtige Informationen:
> - `page`: Auf welcher Seite bist du gerade? (z.B. Seite 3)
> - `total`: Wie viele Seiten gibt es insgesamt? (z.B. 10 Seiten)
> 
> Dann macht die Funktion drei Dinge:
> 1. **Aktualisiert das Text-Label**: Es zeigt dir 'Seite 3 von 10' an, damit du weißt wo du bist
> 2. **Verändert die Breite des Fortschrittsbalkens**: Wenn du bei 3 von 10 Seiten bist, dann ist der Balken zu 30% gefüllt. Das ist wie eine Erfahrungsleiste in Minecraft!
> 3. **Dreht das Sigil-Symbol**: Das ist ein cooles Detail - das Symbol dreht sich ein bisschen bei jeder Seite, damit du siehst dass sich was bewegt
> 
> Warum ist das wichtig? Weil Nutzer immer wissen wollen, wo sie gerade sind - genau wie du in Minecraft immer deine Koordinaten checken kannst!"

**Grundregeln für Erklärungen:**
- **Kontext geben**: Warum brauchen wir das überhaupt?
- **Analogien nutzen**: Vergleiche mit Minecraft, Spielen, Alltag
- **Schritt-für-Schritt**: Nicht alles auf einmal, sondern nacheinander erklären
- **Fachbegriffe erklären**: Nie ein Wort wie "DOM", "Callback", "Property" ohne Erklärung verwenden
- **Beispiele zeigen**: Konkrete Zahlen, echte Situationen beschreiben
- **Warum-Fragen beantworten**: Nicht nur WAS es macht, sondern WARUM es so gemacht wird

#### Code-Zellen:
- **Kommentare**: **Sehr ausführlich und kindgerecht!** Jede Zeile sollte für einen 12-Jährigen verständlich sein. Nicht nur "Was" sondern auch "Warum"
- **Demos**: Mehrere praktische Beispiele zum Ausprobieren mit ausführlichen Erklärungen vor und nach dem Code
- **Interaktivität**: Code zum Experimentieren und Verstehen - ermutige zum Ändern und Ausprobieren
- **Validierung**: File-Checks und Fortschritt-Tracking mit positiver Bestärkung
- **Lerneffekt**: **WICHTIG!** Nicht nur zeigen, sondern ausführlich erklären WARUM es funktioniert und WIE die einzelnen Teile zusammenspielen

### 🔑 Wichtige Template-Regeln:

- **Konsistenz**: Jedes Notebook folgt exakt der Template-Struktur
- **Lerntiefe**: Ausführliche, aber verständliche Erklärungen mit Beispielen
- **Zeitrahmen**: Notebook-Lesezeit 15-20 Min + Aufgaben 15-20 Min = max. 40 Minuten pro Tag
- **Dateipfade**: Immer relative Pfade zu `Aufgabe/` und `Loesung/` (das Notebook liegt schon im `Tag_XX/` Verzeichnis)
- **Verstehen vor Machen**: Konzepte erklären, dann anwenden
- **Erfolgsfeier**: Feiern was erreicht wurde + zeigen was jetzt möglich ist
- **Vertiefung**: Hinweise auf weiterführende Möglichkeiten ohne Spoiler

---

## 🎄 Ziel des gesamten Projekts

Am Ende soll mein Sohn:

- HTML/CSS/JS verstanden haben  
- mit Bibliotheken umgehen können  
- Animationen, Mini-Games und Effekte umsetzen können  
- eine vollständige Minecraft-Weihnachts-Webseite gebaut haben  
- diese auf **GitHub Pages** veröffentlichen  

---

## 📋 Agenten-Checkliste (Schnellreferenz)

### ✅ **Vor dem Start:**
- [ ] Tag_XX.md gelesen und alle Lerninhalte verstanden
- [ ] Schwierigkeitsgrad dem Wochenziel angepasst (W1: HTML → W4: Projekt)

### ✅ **Schritt 1 - Musterlösung (`Loesung/`):**
- [ ] Alle 3 Dateien erstellt: index.html, style.css, script.js
- [ ] Alle Lerninhalte aus Tag_XX.md implementiert
- [ ] Minecraft-Weihnachtsdesign durchgängig
- [ ] Gut kommentiert und funktionsfähig
- [ ] Nur CDN-Bibliotheken verwendet

### ✅ **Schritt 2 - Aufgaben-Boilerplate (`Aufgabe/`):**
- [ ] 80% der Musterlösung bereits implementiert
- [ ] Genau 3 TODOs: 1× HTML, 1× CSS, 1× JS
- [ ] Klare TODO-Kommentare mit Hinweisen
- [ ] Maximal 15-20 Minuten Bearbeitungszeit
- [ ] Funktionsfähig auch mit TODOs

### ✅ **Schritt 3 - Jupyter Notebook (`Lesson.ipynb`):**
- [ ] Template-Struktur eingehalten (strukturiert aber lehrreich!)
- [ ] Minecraft-Geschichte kurz und motivierend
- [ ] **Ausführliche, kindgerechte Lerninhalte**: Alle Konzepte für 12-Jährige erklärt mit Analogien, Beispielen und Schritt-für-Schritt-Anleitungen
- [ ] **Erklärungsqualität geprüft**: Keine technischen Abkürzungen ohne Erklärung, keine zu knappen Beschreibungen
- [ ] Referenzen zu echten Dateien aus BEIDEN Verzeichnissen (Aufgabe + Lösung)
- [ ] Maximal 15-20 Minuten Lesezeit (ausführlich aber fokussiert)
- [ ] Vertiefungshinweise ohne Spoiler für kommende Tage

### ✅ **Schritt 4 - Finale Validierung (siehe Schritt 4️⃣ oben):**
- [ ] Alle 7 Validierungspunkte durchgeführt (inkl. Playwright MCP & Context7 MCP)
- [ ] Bei Fehlern zurück zum entsprechenden Schritt (1-3)
- [ ] Erfolgs-Kriterium: Alle Validierungen bestanden ✅

---
