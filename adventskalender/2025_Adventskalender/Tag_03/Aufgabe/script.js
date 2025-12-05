/**
 * TAG 03 - ELF-INVENTAR SYSTEM - JAVASCRIPT
 * Minecraft-Weihnachts-Adventskalender
 * 
 * Lernziele:
 * - DOM-Manipulation und Event-Handling
 * - Dynamische Inhalte mit Listen-Strukturen
 * - Hover-Effekte und Interaktive Elemente
 * - Datenstrukturen für Inventar-Management
 */

// =============================================================================
// GLOBALE VARIABLEN UND DATENSTRUKTUREN
// =============================================================================

// Inventar-Items als JavaScript-Objekt-Array
const inventoryItems = [
    { id: 'diamond-sword', icon: '⚔️', name: 'Diamant-Schwert', rarity: 'legendary', value: 250, count: 1 },
    { id: 'christmas-tree', icon: '🎄', name: 'Weihnachtsbaum', rarity: 'common', value: 10, count: 12 },
    { id: 'candy-cane', icon: '🍭', name: 'Zuckerstange', rarity: 'common', value: 2, count: 64 },
    { id: 'snowball', icon: '⛄', name: 'Schneeball', rarity: 'common', value: 1, count: 32 },
    { id: 'gift-box', icon: '🎁', name: 'Geschenkbox', rarity: 'rare', value: 25, count: 5 },
    { id: 'magic-star', icon: '⭐', name: 'Magischer Stern', rarity: 'epic', value: 100, count: 1 },
    { id: 'bell', icon: '🔔', name: 'Weihnachtsglocke', rarity: 'common', value: 5, count: 8 },
    { id: 'cookie', icon: '🍪', name: 'Lebkuchen', rarity: 'common', value: 3, count: 24 },
    { id: 'ice-crystal', icon: '❄️', name: 'Eiskristall', rarity: 'rare', value: 15, count: 16 },
    { id: 'golden-apple', icon: '🍎', name: 'Goldener Apfel', rarity: 'epic', value: 75, count: 3 },
    { id: 'reindeer-horn', icon: '🦌', name: 'Rentier-Horn', rarity: 'rare', value: 30, count: 2 },
    { id: 'wreath', icon: '🎀', name: 'Adventskranz', rarity: 'common', value: 8, count: 6 },
    { id: 'holly', icon: '🌿', name: 'Stechpalme', rarity: 'common', value: 4, count: 18 },
    { id: 'christmas-light', icon: '💡', name: 'Weihnachtslicht', rarity: 'common', value: 2, count: 48 },
    { id: 'mittens', icon: '🧤', name: 'Warme Handschuhe', rarity: 'common', value: 12, count: 1 },
    { id: 'hot-chocolate', icon: '☕', name: 'Heiße Schokolade', rarity: 'common', value: 6, count: 7 },
    { id: 'magic-wand', icon: '🪄', name: 'Zauberstab', rarity: 'legendary', value: 300, count: 1 },
    { id: 'snow-globe', icon: '🔮', name: 'Schneekugel', rarity: 'epic', value: 50, count: 4 },
    { id: 'ornament', icon: '🎈', name: 'Christbaumkugel', rarity: 'common', value: 3, count: 25 },
    { id: 'garland', icon: '🎊', name: 'Girlande', rarity: 'common', value: 7, count: 10 },
    { id: 'angel', icon: '👼', name: 'Weihnachtsengel', rarity: 'epic', value: 80, count: 1 },
    { id: 'mistletoe', icon: '💚', name: 'Mistelzweig', rarity: 'rare', value: 20, count: 3 },
    { id: 'fireplace', icon: '🔥', name: 'Kamin', rarity: 'rare', value: 40, count: 1 },
    { id: 'stockings', icon: '🧦', name: 'Weihnachtsstrümpfe', rarity: 'common', value: 9, count: 6 }
];

// Globale Variablen für DOM-Elemente
let inventoryGrid;
let filledSlotsCounter;
let emptySlotsCounter;
let totalValueCounter;

// =============================================================================
// INITIALISIERUNG - Code wird ausgeführt wenn die Seite geladen ist
// =============================================================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('🎄 Elf-Inventar System wird initialisiert...');
    
    // AOS (Animate On Scroll) initialisieren
    AOS.init({
        duration: 800,
        easing: 'ease-out',
        once: true
    });
    
    // DOM-Elemente referenzieren
    inventoryGrid = document.querySelector('.inventory-grid');
    filledSlotsCounter = document.getElementById('filled-slots');
    emptySlotsCounter = document.getElementById('empty-slots');
    totalValueCounter = document.getElementById('total-value');
    
    // TODO 3: Vervollständige die Inventar-Initialisierung
    // Hinweis: Rufe hier die Funktionen initializeInventory() und setupEventListeners() auf
    initializeInventory();
    setupEventListeners();
    
    // Statistiken berechnen und anzeigen
    updateInventoryStats();
    
    console.log('✅ Feeeeeeelix ist hier!');
    console.log('✅ Inventar-System erfolgreich geladen!');
});

// =============================================================================
// INVENTAR-INITIALISIERUNG
// =============================================================================

/**
 * Erstellt das 8x8 Grid und füllt es mit Items und leeren Slots
 */
function initializeInventory() {
    console.log('📦 Inventar-Grid wird erstellt...');
    
    // Berechne wie viele leere Slots wir noch brauchen (64 total - bereits vorhandene)
    const existingSlots = inventoryGrid.querySelectorAll('.inventory-slot').length;
    const remainingSlots = 64 - existingSlots;
    
    // Füge die fehlenden leeren Slots hinzu
    for (let i = 0; i < remainingSlots; i++) {
        const emptySlot = createEmptySlot();
        inventoryGrid.appendChild(emptySlot);
    }
    
    console.log(`✅ ${remainingSlots} zusätzliche Slots erstellt! Inventar vollständig mit 64 Slots.`);
}

/**
 * Erstellt einen leeren Inventar-Slot
 * @returns {HTMLLIElement} Das erstellte leere Slot-Element
 */
function createEmptySlot() {
    const slot = document.createElement('li');
    slot.className = 'inventory-slot';
    slot.innerHTML = '<div class="empty-slot-hint" style="opacity: 0.3; font-size: 16px;">📦</div>';
    return slot;
}

/**
 * Konvertiert Seltenheits-IDs zu lesbaren Namen
 * @param {string} rarity - Die Seltenheits-ID
 * @returns {string} Lesbarer Seltenheits-Name
 */
function getRarityDisplayName(rarity) {
    const rarityNames = {
        'common': 'Gewöhnlich',
        'rare': 'Selten',
        'epic': 'Episch',
        'legendary': 'Legendär'
    };
    return rarityNames[rarity] || 'Unbekannt';
}

// =============================================================================
// EVENT-LISTENER UND INTERAKTIONEN
// =============================================================================

/**
 * Richtet alle Event-Listener für Inventar-Interaktionen ein
 */
function setupEventListeners() {
    console.log('🎮 Event-Listener werden eingerichtet...');
    
    // Hover-Effekte für alle Slots
    inventoryGrid.addEventListener('mouseenter', handleSlotHover, true);
    inventoryGrid.addEventListener('mouseleave', handleSlotLeave, true);
    
    // Click-Events für Slot-Interaktionen
    inventoryGrid.addEventListener('click', handleSlotClick);
    
    console.log('✅ Event-Listener erfolgreich eingerichtet!');
}

/**
 * Behandelt Hover-Events auf Inventar-Slots
 * @param {Event} event - Das Mouse-Event
 */
function handleSlotHover(event) {
    if (event.target.closest('.inventory-slot')) {
        const slot = event.target.closest('.inventory-slot');
        
        // Sound-Effekt (simuliert)
        playHoverSound();
        
        // Zusätzliche Hover-Animation
        slot.style.filter = 'brightness(1.2) drop-shadow(0 0 15px rgba(74, 222, 128, 0.6))';
        
        // Andere Slots leicht dimmen für Fokus-Effekt
        const allSlots = inventoryGrid.querySelectorAll('.inventory-slot');
        allSlots.forEach(otherSlot => {
            if (otherSlot !== slot) {
                otherSlot.style.opacity = '0.7';
            }
        });
    }
}

/**
 * Behandelt Mouse-Leave Events
 * @param {Event} event - Das Mouse-Event
 */
function handleSlotLeave(event) {
    if (event.target.closest('.inventory-slot')) {
        const slot = event.target.closest('.inventory-slot');
        
        // Filter zurücksetzen
        slot.style.filter = '';
        
        // Alle Slots wieder normal anzeigen
        const allSlots = inventoryGrid.querySelectorAll('.inventory-slot');
        allSlots.forEach(otherSlot => {
            otherSlot.style.opacity = '';
        });
    }
}

/**
 * Behandelt Click-Events auf Slots
 * @param {Event} event - Das Mouse-Event
 */
function handleSlotClick(event) {
    const slot = event.target.closest('.inventory-slot');
    if (!slot) return;
    
    const itemId = slot.getAttribute('data-item');
    
    if (itemId) {
        // Item-Details anzeigen
        showItemDetails(itemId);
        
        // Click-Animation
        slot.style.transform = 'scale(0.95)';
        setTimeout(() => {
            slot.style.transform = '';
        }, 150);
    } else {
        // Leerer Slot - Easter Egg
        showEmptySlotMessage();
    }
}

/**
 * Simuliert einen Hover-Sound-Effekt
 */
function playHoverSound() {
    // In einer echten Anwendung würde hier ein Audio-Element abgespielt
    console.log('🔊 *Minecraft Inventar-Sound*');
}

/**
 * Zeigt Details zu einem Item an
 * @param {string} itemId - Die ID des Items
 */
function showItemDetails(itemId) {
    const item = inventoryItems.find(i => i.id === itemId);
    if (!item) return;
    
    // Einfache Alert-Box (in einer echten App wäre das ein Modal)
    const totalValue = item.count * item.value;
    alert(`📋 ITEM-DETAILS\n\n` +
          `${item.icon} ${item.name}\n` +
          `Anzahl: ${item.count}\n` +
          `Wert pro Stück: ⭐ ${item.value}\n` +
          `Gesamtwert: ⭐ ${totalValue}\n` +
          `Seltenheit: ${getRarityDisplayName(item.rarity)}`);
}

/**
 * Zeigt eine Nachricht für leere Slots
 */
function showEmptySlotMessage() {
    const messages = [
        '📦 Dieser Slot wartet auf ein neues Item!',
        '✨ Hier könnte dein neues Item stehen!',
        '🎁 Platz für weitere Schätze!',
        '⭐ Bereit für das nächste Abenteuer!'
    ];
    
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    alert(randomMessage);
}

// =============================================================================
// STATISTIKEN UND BERECHNUNGEN
// =============================================================================

/**
 * Aktualisiert die Inventar-Statistiken
 */
function updateInventoryStats() {
    console.log('📊 Statistiken werden berechnet...');
    
    // Anzahl belegter und leerer Slots
    const filledSlots = inventoryItems.length;
    const emptySlots = 64 - filledSlots;
    
    // Gesamtwert berechnen
    const totalValue = inventoryItems.reduce((sum, item) => {
        return sum + (item.count * item.value);
    }, 0);
    
    // UI aktualisieren
    if (filledSlotsCounter) filledSlotsCounter.textContent = filledSlots;
    if (emptySlotsCounter) emptySlotsCounter.textContent = emptySlots;
    if (totalValueCounter) totalValueCounter.textContent = `⭐ ${totalValue.toLocaleString()}`;
    
    console.log(`✅ Statistiken: ${filledSlots} Items, Wert: ⭐${totalValue}`);
}

// =============================================================================
// DEBUGGING UND ENTWICKLER-TOOLS
// =============================================================================

// Hilfsfunktionen für die Browser-Konsole
window.debugInventory = {
    showAllItems: () => console.table(inventoryItems),
    getInventoryStats: updateInventoryStats,
    version: '1.0.0 - Aufgabe'
};

console.log('🎄 Elf-Inventar System geladen! Verwende window.debugInventory für Debug-Funktionen.');