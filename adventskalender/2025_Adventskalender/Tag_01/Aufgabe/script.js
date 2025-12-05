/*
🎄 MINECRAFT WEIHNACHTSDORF - SCRIPT.JS 🎄
Magische JavaScript-Zauber für interaktive Schneeflocken und Abenteuer-Button
*/

// Warten bis die Seite vollständig geladen ist
document.addEventListener('DOMContentLoaded', function() {
    console.log('🎮 Minecraft Weihnachtsdorf lädt... ⚡');
    
    // Schneeflocken-System initialisieren
    createSnowfall();
    
    // TODO 3: Vervollständige die Abenteuer-Button Funktionalität
    // Lösche die Kommentarzeichen (//) vor der nächsten Zeile:
    setupAdventureButton();
    
    // Willkommens-Animation
    playWelcomeAnimation();
    
    console.log('✨ Minecraft Weihnachtsdorf bereit! 🎄');
});

/**
 * 🌨️ SCHNEEFLOCKEN-SYSTEM 🌨️
 * Erstellt fallende Schneeflocken für winterliche Atmosphäre
 */
function createSnowfall() {
    const snowflakesContainer = document.getElementById('snowflakes-container');
    
    // Verschiedene Schneeflocken-Symbole für Abwechslung
    const snowflakeSymbols = ['❄️', '❅', '🌨️', '*', '•'];
    
    // Kontinuierlich neue Schneeflocken erstellen
    setInterval(function() {
        createSnowflake(snowflakesContainer, snowflakeSymbols);
    }, 300); // Alle 300ms eine neue Schneeflocke
    
    console.log('🌨️ Schneeflocken-System aktiviert!');
}

/**
 * 🌨️ EINZELNE SCHNEEFLOCKE ERSTELLEN 🌨️
 * Erstellt eine einzelne fallende Schneeflocke mit zufälligen Eigenschaften
 */
function createSnowflake(container, symbols) {
    const snowflake = document.createElement('div');
    
    // Zufälliges Schneeflocken-Symbol
    snowflake.textContent = symbols[Math.floor(Math.random() * symbols.length)];
    snowflake.className = 'snowflake';
    
    // Zufällige horizontale Position
    const startPosition = Math.random() * window.innerWidth;
    snowflake.style.left = startPosition + 'px';
    
    // Zufällige Größe (kleine bis große Flocken)
    const size = Math.random() * 1.5 + 0.5; // 0.5 bis 2em
    snowflake.style.fontSize = size + 'em';
    
    // Zufällige Fallgeschwindigkeit
    const fallDuration = Math.random() * 8 + 5; // 5 bis 13 Sekunden
    snowflake.style.animationDuration = fallDuration + 's';
    
    // Schneeflocke zum Container hinzufügen
    container.appendChild(snowflake);
    
    // Schneeflocke nach dem Fall automatisch entfernen (Speicher sparen)
    setTimeout(function() {
        if (snowflake.parentNode) {
            snowflake.parentNode.removeChild(snowflake);
        }
    }, fallDuration * 1000);
}

/**
 * 🚀 ABENTEUER-BUTTON FUNKTIONALITÄT 🚀
 * Macht den Button interaktiv und zeigt Erfolgsmeldung
 */
function setupAdventureButton() {
    const adventureBtn = document.getElementById('adventure-btn');
    const adventureMessage = document.getElementById('adventure-message');
    
    // Klick-Event für den Abenteuer-Button
    adventureBtn.addEventListener('click', function() {
        console.log('🚀 Abenteuer gestartet!');
        
        // Button-Text ändern
        adventureBtn.innerHTML = '⚡ Abenteuer läuft... ⚡';
        adventureBtn.disabled = true;
        
        // Erfolgsmeldung nach kurzer Verzögerung anzeigen
        setTimeout(function() {
            adventureMessage.classList.remove('hidden');
            adventureMessage.classList.add('animate-bounce');
            
            // Button wieder aktivieren mit neuer Nachricht
            setTimeout(function() {
                adventureBtn.innerHTML = '🎉 Weiter zu Tag 2! 🎉';
                adventureBtn.disabled = false;
                adventureBtn.classList.add('bg-green-600', 'hover:bg-green-700');
                adventureBtn.classList.remove('bg-red-600', 'hover:bg-red-700');
            }, 2000);
            
        }, 1000);
    });
    
    console.log('🚀 Abenteuer-Button konfiguriert!');
}

/**
 * 🌟 WILLKOMMENS-ANIMATION 🌟
 * Spielt eine kurze Begrüßungsanimation ab
 */
function playWelcomeAnimation() {
    // Titel mit Verzögerung einblenden
    setTimeout(function() {
        const title = document.querySelector('.minecraft-title');
        if (title) {
            title.style.transform = 'scale(1.1)';
            
            setTimeout(function() {
                title.style.transform = 'scale(1)';
            }, 500);
        }
    }, 500);
    
    // Kristall zum Pulsieren bringen
    setTimeout(function() {
        const crystal = document.querySelector('.animate-pulse');
        if (crystal) {
            crystal.style.animation = 'pulse 2s infinite, bounce 1s ease-out';
        }
    }, 1000);
    
    console.log('🌟 Willkommens-Animation abgespielt!');
}

/**
 * 🎮 BONUS: TASTATUR-SHORTCUTS 🎮
 * Versteckte Tastatur-Funktionen für Entwickler
 */
document.addEventListener('keydown', function(event) {
    // Geheime Tastenkombinationen
    if (event.ctrlKey && event.key === 'm') {
        // Ctrl+M: Mehr Schnee!
        console.log('🌨️ SCHNEE-BOOST aktiviert!');
        
        for (let i = 0; i < 20; i++) {
            setTimeout(function() {
                createSnowflake(
                    document.getElementById('snowflakes-container'),
                    ['❄️', '❅', '🌨️']
                );
            }, i * 50);
        }
        
        event.preventDefault();
    }
    
    if (event.key === 'Enter') {
        // Enter: Abenteuer-Button aktivieren
        const btn = document.getElementById('adventure-btn');
        if (btn && !btn.disabled) {
            btn.click();
        }
    }
});

// Minecraft-Style Konsolen-Begrüßung
console.log(`
🎄🎮 MINECRAFT WEIHNACHTSDORF 🎮🎄
=====================================
❄️  Willkommen zur Webentwicklungs-Reise!
⚡  Drücke Ctrl+M für mehr Schnee
🚀  Drücke Enter für Abenteuer-Start
🎉  Viel Spaß beim Lernen!
=====================================
`);