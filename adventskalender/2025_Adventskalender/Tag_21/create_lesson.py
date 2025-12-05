#!/usr/bin/env python3
"""
Erstellt eine (Beispiel-) Lesson.ipynb Datei basierend auf der Struktur
aus agenten_kontext.md und jupyter_notebook_guide.md
"""

import nbformat as nbf
import sys
from pathlib import Path


def create_lesson():
    """
    Erstellt ein Jupyter Notebook für einen Adventskalender-Tag.
    Folgt der Struktur: Lernen -> Verstehen -> Ausprobieren -> Aufgabe -> Weitere Ideen
    """
    
    # Neues Notebook erstellen
    nb = nbf.v4.new_notebook()
    
    # Zelle 1: Überschrift - Das lernst du heute
    cell1 = nbf.v4.new_markdown_cell("""# 📚 Das lernst du heute""")
    nb.cells.append(cell1)
    
    # Zelle 2: Hauptthema
    cell2 = nbf.v4.new_markdown_cell("""## 🎯 [Hauptthema] - [Kurzbeschreibung]

[Einleitung mit Minecraft-Geschichte] 🧱
""")
    nb.cells.append(cell2)
    
    # Zelle 3: Die wichtigsten Elemente
    cell3 = nbf.v4.new_markdown_cell("""### 🏗️ Die wichtigsten [HTML/CSS/JavaScript]-Elemente:

**`[Element/Konzept]`** 📜

[Beschreibung]

```[html/css/javascript]
[Code-Beispiel]
```

[Minecraft-Analogie]

**`[Element/Konzept 2]`** 📝

[Beschreibung]

```[html/css/javascript]
[Code-Beispiel]
```

[Minecraft-Analogie]
""")
    nb.cells.append(cell3)
    
    # Zelle 4: Weitere wichtige Konzepte
    cell4 = nbf.v4.new_markdown_cell("""### 🌐 [Weitere wichtige Konzepte]

**[Konzept]** ([Beschreibung]):
                                     
```[html/css/javascript]
[Code-Beispiel]
```
""")
    nb.cells.append(cell4)
    
    # Zelle 5: Praktisches WOW-Ziel
    cell5 = nbf.v4.new_markdown_cell("""## 🎨 Dein praktisches WOW-Ziel heute:

✅ **[Feature 1]** - [Beschreibung mit Minecraft-Bezug]

✅ **[Feature 2]** - [Beschreibung mit Minecraft-Bezug]

✅ **[Feature 3]** - [Beschreibung mit Minecraft-Bezug]

✅ **[Feature 4]** - [Beschreibung mit Minecraft-Bezug]

**Das Ergebnis:** [Beschreibung des finalen Ziels] 🎮✨
""")
    nb.cells.append(cell5)
    
    # Zelle 6: Überschrift - Verstehen
    cell6 = nbf.v4.new_markdown_cell("""# 🧪 Verstehen""")
    nb.cells.append(cell6)
    
    # Zelle 7: Konzept 1
    cell7 = nbf.v4.new_markdown_cell("""## 🔍 [Konzept 1] verstehen

[Erklärung mit Minecraft-Analogie]:

```[html/css/javascript]
[Strukturbeispiel mit Kommentaren]
```
""")
    nb.cells.append(cell7)
    
    # Zelle 8: Konzept 2
    cell8 = nbf.v4.new_markdown_cell("""## 🎨 [Konzept 2] - [Analogie]!

[Erklärung des Konzepts]:

```[css/javascript]
[Code-Beispiel mit Kommentaren]
```
""")
    nb.cells.append(cell8)
    
    # Zelle 9: Konzept 3
    cell9 = nbf.v4.new_markdown_cell("""## ⚡ [Konzept 3] - [Analogie]!

[Erklärung des Konzepts]:

```javascript
[Code-Beispiel mit Kommentaren]
```
""")
    nb.cells.append(cell9)
    
    # Zelle 10: Überschrift - Ausprobieren
    cell10 = nbf.v4.new_markdown_cell("""# 🧪 Ausprobieren

Führe die folgende Zelle aus:
""")
    nb.cells.append(cell10)
    
    # Zelle 11: Interaktives HTML-Demo (Python Code)
    cell11 = nbf.v4.new_code_cell("""from IPython.core.display import HTML
display(HTML(\"\"\"
<!DOCTYPE html>
<html>
  <head>
    <title>Demo</title>

    <!-- 🎨 Einfaches CSS -->
    <style>
      body {
        font-family: Arial, sans-serif;
        background: #fafafa;
        padding: 20px;
      }
      .demo-element {
        color: #333;
        padding: 10px;
      }
    </style>

    <!-- ⚡ Einfaches JavaScript -->
    <script>
      function demoFunction() {
        console.log("Demo ausgeführt!");
        alert("Demo-Funktion wurde aufgerufen!");
      }
    </script>

  </head>

  <body>
    <h1 class="demo-element">Demo-Überschrift</h1>
    <p>Demo-Text</p>

    <button onclick="demoFunction()">Klick mich!</button>
  </body>
</html>
\"\"\"))
""")
    nb.cells.append(cell11)
    
    # Zelle 12: Überschrift - Deine Aufgabe
    cell12 = nbf.v4.new_markdown_cell("""# 🚀 Deine Aufgabe: [Aufgabentitel]!""")
    nb.cells.append(cell12)
    
    # Zelle 13: Mission
    cell13 = nbf.v4.new_markdown_cell("""## 🎯 Mission: 3 magische TODOs lösen

In deinem `Tag_XX/Aufgabe/` Verzeichnis wartet eine **fast fertige Webseite** auf dich! Du musst nur **3 kleine Zauber** vervollständigen:
""")
    nb.cells.append(cell13)
    
    # Zelle 14: TODO 1
    cell14 = nbf.v4.new_markdown_cell("""### 📝 **TODO 1: HTML - [Beschreibung]** 
**Datei:** `index.html` (Zeile ~XX)

**Was zu tun ist:**
```html
<!-- TODO 1: [Aufgabenbeschreibung] -->
```

**Lösung:** [Detaillierte Anleitung]
""")
    nb.cells.append(cell14)
    
    # Zelle 15: TODO 2
    cell15 = nbf.v4.new_markdown_cell("""### 🎨 **TODO 2: CSS - [Beschreibung]**
**Datei:** `style.css` (Zeile ~XX)

**Was zu tun ist:**
```css
/* TODO 2: [Aufgabenbeschreibung] */
```

**Lösung:** [Detaillierte Anleitung]
""")
    nb.cells.append(cell15)
    
    # Zelle 16: TODO 3
    cell16 = nbf.v4.new_markdown_cell("""### ⚡ **TODO 3: JavaScript - [Beschreibung]**
**Datei:** `script.js` (Zeile ~XX)

**Was zu tun ist:**
```javascript
// TODO 3: [Aufgabenbeschreibung]
```

**Lösung:** [Detaillierte Anleitung]
""")
    nb.cells.append(cell16)
    
    # Zelle 17: Erfolgskontrolle
    cell17 = nbf.v4.new_markdown_cell("""## 🏆 Erfolgskontrolle

**Nach allen TODOs solltest du sehen:**

✅ [Erfolg 1]

✅ [Erfolg 2]  

✅ [Erfolg 3]  

✅ [Erfolg 4]

""")
    nb.cells.append(cell17)
    
    # Zelle 18: Testen deiner Lösung
    cell18 = nbf.v4.new_markdown_cell("""## 🌐 Testen deiner Lösung

**Öffne in deinem Browser:**

http://192.168.0.20:8000/2025_Adventskalender/Tag_XX/Aufgabe/

**Vergleiche mit der Musterlösung:**

http://192.168.0.20:8000/2025_Adventskalender/Tag_XX/Loesung/

**⚠️ Wichtig:** Die Dateien funktionieren nur über diese Server-URLs!
""")
    nb.cells.append(cell18)
    
    # Zelle 19: Überschrift - Weitere Ideen
    cell19 = nbf.v4.new_markdown_cell("""# Weitere Ideen""")
    nb.cells.append(cell19)
    
    # Zelle 20: Ideen-Liste
    cell20 = nbf.v4.new_markdown_cell("""- Verändere die Seite nach deinen Wünschen
- Experimentiere mit verschiedenen Farben und Effekten
- Füge eigene Elemente hinzu
- Kombiniere verschiedene Techniken aus vorherigen Tagen
""")
    nb.cells.append(cell20)
    
    # Notebook validieren
    try:
        nbf.validate(nb)
        print("✅ Notebook-Validierung erfolgreich!")
    except nbf.ValidationError as e:
        print(f"❌ Validierungsfehler: {e}")
        sys.exit(1)
    
    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    """
    Speichert das Notebook im aktuellen Verzeichnis.
    
    Args:
        nb: Das Notebook-Objekt
        filename: Name der Ausgabedatei
    """
    output_path = Path.cwd() / filename
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            nbf.write(nb, f)
        print(f"✅ Lesson erfolgreich erstellt: {output_path}")
        return output_path
    except Exception as e:
        print(f"❌ Fehler beim Speichern: {e}")
        sys.exit(1)


def main():
    """Hauptfunktion"""
    print("🎄 Erstelle Lesson.ipynb...")
    print("=" * 60)
    
    # Lesson erstellen
    nb = create_lesson()
    
    # Lesson speichern
    output_path = save_notebook(nb)
    
    print("=" * 60)
    print(f"🎉 Fertig! Lesson wurde erstellt.")
    print(f"📁 Pfad: {output_path}")
    print()
    print("📋 Struktur des Lesson:")
    print("  1. 📚 Das lernst du heute")
    print("  2. 🎯 [Hauptthema]")
    print("  3. 🏗️ Die wichtigsten Elemente")
    print("  4. 🌐 Weitere Konzepte")
    print("  5. 🎨 WOW-Ziel")
    print("  6. 🧪 Verstehen")
    print("  7. 🔍 [Konzept 1]")
    print("  8. 🎨 [Konzept 2]")
    print("  9. ⚡ [Konzept 3]")
    print("  10. 🧪 Ausprobieren")
    print("  11. [Code] Interaktives HTML-Demo")
    print("  12. 🚀 Deine Aufgabe")
    print("  13. 🎯 Mission")
    print("  14. 📝 TODO 1")
    print("  15. 🎨 TODO 2")
    print("  16. ⚡ TODO 3")
    print("  17. 🏆 Erfolgskontrolle")
    print("  18. 🌐 Testen")
    print("  19. Weitere Ideen")
    print("  20. [Ideen-Liste]")
    print()
    print("💡 Die Lesson folgt der Struktur aus agenten_kontext.md")
    print("💡 Alle Platzhalter sind mit [Brackets] markiert")
    print("💡 Jede Überschrift ist jetzt eine separate Zelle für bessere Übersicht")


if __name__ == "__main__":
    main()
