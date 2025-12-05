// Tag 04 – Interaktive Karte
// Dieses Skript verbindet die Bildkarte, Tooltips und die erklärenden Abschnitte.
// Felix kann hier sehen, wie interne Verlinkung + visuelles Feedback zusammenarbeiten.

document.addEventListener('DOMContentLoaded', () => {
    // Dataset mit Story-Infos für jedes Reiseziel.
    const locations = {
        portal: {
            title: 'Portal zur Schneewelt',
            description: 'Das Portal ist dein Ausgangspunkt. Es verlinkt direkt zu Abschnitt #portal und erklärt, wohin der Spieler teleportiert.',
            tip: 'Nutze <a href="#portal">Ankerlinks</a>, um Besucher exakt zu positionieren.',
            color: '#f472b6'
        },
        markt: {
            title: 'Schneemarkt der Händler',
            description: 'Hier lernen Reisende, warum Tooltips wichtig sind und wie Koordinaten in &lt;area&gt;-Tags funktionieren.',
            tip: 'Halte Tooltips kurz und hilfreich – wie Questtexte!',
            color: '#bef264'
        },
        schmiede: {
            title: 'Redstone-Schmiede',
            description: 'Absolut positionierte Buttons legen sich über die Karte und zeigen mit Animationen ihre Treffpunkte.',
            tip: 'Experimentiere mit CSS-Variablen wie <code>--x</code> und <code>--y</code>.',
            color: '#67e8f9'
        },
        bibliothek: {
            title: 'Kristall-Bibliothek',
            description: 'Der Ruheort für alle Navigationstipps – ideal, um Good Practices zu sammeln.',
            tip: 'Füge weitere Sektionen hinzu, damit jedes Dörfchen seinen eigenen Wissenstresor bekommt.',
            color: '#facc15'
        }
    };

    const infoTitle = document.getElementById('infoTitle');
    const infoDescription = document.getElementById('infoDescription');
    const infoTip = document.getElementById('infoTip');
    const hotspots = document.querySelectorAll('.map-hotspot');
    const mapAreas = document.querySelectorAll('area[data-location]');
    const navLinks = document.querySelectorAll('[data-location-link]');

    /**
     * Aktualisiert Info-Panel, Hotspots und Navigationslinks.
     * @param {string} locationId - Schlüssel des Ziels
     * @param {boolean} scrollToSection - ob zusätzlich gescrollt werden soll
     */
    const setActiveLocation = (locationId, scrollToSection = false) => {
        const data = locations[locationId];
        if (!data) return;

        infoTitle.textContent = data.title;
        infoDescription.innerHTML = data.description;
        infoTip.innerHTML = data.tip;

        hotspots.forEach((button) => {
            const isActive = button.dataset.location === locationId;
            button.setAttribute('aria-pressed', isActive);
            button.classList.toggle('active', isActive);
        });

        navLinks.forEach((link) => {
            const isActive = link.dataset.locationLink === locationId;
            link.classList.toggle('active', isActive);
        });

        if (scrollToSection) {
            // TODO 3: Scrolle sanft zur passenden Sektion (scrollIntoView) und markiere sie kurz mit der Klasse "focus-glow".
        }

        document.documentElement.style.setProperty('--active-location-color', data.color);
    };

    // Interaktive Buttons auf der Karte.
    hotspots.forEach((button) => {
        const { location } = button.dataset;
        button.setAttribute('aria-label', locations[location]?.title || 'Unbenannter Ort');

        button.addEventListener('click', () => setActiveLocation(location, true));
        button.addEventListener('mouseenter', () => setActiveLocation(location));
        button.addEventListener('focus', () => setActiveLocation(location));
    });

    // Klassische Image-Map-Bereiche reagieren ebenfalls.
    mapAreas.forEach((area) => {
        const { location } = area.dataset;
        area.addEventListener('mouseenter', () => setActiveLocation(location));
        area.addEventListener('focus', () => setActiveLocation(location));
        area.addEventListener('click', () => setActiveLocation(location));
    });

    // Navigation oben synchron halten.
    navLinks.forEach((link) => {
        const { locationLink } = link.dataset;
        link.addEventListener('click', (event) => {
            event.preventDefault();
            setActiveLocation(locationLink, true);
        });
    });

    // Initialen Zustand setzen, damit das Panel nicht leer ist.
    setActiveLocation('portal');
});
