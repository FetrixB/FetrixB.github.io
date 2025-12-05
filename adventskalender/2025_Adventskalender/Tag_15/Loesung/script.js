// Tag 15 - Redstone inspiriertes Logik-Labor
// Dieses Skript verbindet Minecraft-Analogien mit echten JavaScript-Grundlagen:
// - Variablen speichern Zustände wie bei Redstone-Schaltungen
// - Booleans dienen als Hebel, Numbers messen Signal-Stärke
// - Logische Operatoren entscheiden, welche Lampe leuchtet

const circuitState = {
  power: false,
  signal: false,
  override: false,
  strength: 7,
};

const leverButtons = document.querySelectorAll('[data-lever]');
const strengthSlider = document.getElementById('strength');
const strengthValue = document.getElementById('strengthValue');
const logList = document.getElementById('logList');
const lampCards = document.querySelectorAll('.lamp-card');
const logicNarration = document.getElementById('logicNarration');
const logicChips = {
  and: document.querySelector('[data-logic="and"]'),
  or: document.querySelector('[data-logic="or"]'),
  not: document.querySelector('[data-logic="not"]'),
};

function formatBool(value) {
  return value ? 'AN' : 'AUS';
}

function logAction(message) {
  const timestamp = new Date().toLocaleTimeString('de-DE', { minute: '2-digit', second: '2-digit' });
  const item = document.createElement('li');
  item.textContent = `${timestamp} → ${message}`;
  logList.prepend(item);
  while (logList.children.length > 4) {
    logList.removeChild(logList.lastElementChild);
  }
  console.log(`[Webstone] ${message}`);
}

function updateLeverButtons() {
  leverButtons.forEach((button) => {
    const leverType = button.dataset.lever;
    const isActive = circuitState[leverType];
    button.dataset.active = String(isActive);
    button.querySelector('.state').textContent = formatBool(isActive);
  });
}

function updateLamps() {
  const gateActive = circuitState.power && circuitState.signal && circuitState.strength >= 8;
  const alarmActive = circuitState.power || circuitState.override;
  const secretActive = circuitState.power && !circuitState.override && circuitState.strength >= 4;
  const moodWarmth = circuitState.strength / 15;

  lampCards.forEach((card) => {
    const lampType = card.dataset.lamp;
    const statusText = card.querySelector('.status-text');
    const lampCore = card.querySelector('.lamp-core');

    if (lampType === 'gate') {
      toggleLamp(card, gateActive);
      statusText.textContent = gateActive
        ? 'Status: Tor hebt sich majestätisch!'
        : 'Status: Tor bleibt blockiert.';
    }

    if (lampType === 'alarm') {
      toggleLamp(card, alarmActive);
      statusText.textContent = alarmActive
        ? 'Status: Schneegolems sind alarmiert!'
        : 'Status: Alles ruhig im Dorf.';
    }

    if (lampType === 'secret') {
      toggleLamp(card, secretActive);
      statusText.textContent = secretActive
        ? 'Status: Geheimtür offen – psst!'
        : 'Status: Tür getarnt.';
    }

    if (lampType === 'mood') {
      toggleLamp(card, circuitState.strength > 0);
      const warmthColor = `rgba(250, 204, 21, ${0.2 + moodWarmth * 0.6})`;
      lampCore.style.boxShadow = `0 0 ${12 + moodWarmth * 35}px ${warmthColor}`;
      lampCore.style.borderColor = warmthColor;
      statusText.textContent = `Status: Stimmung bei Stärke ${circuitState.strength}/15`;
    }
  });

  logicChips.and.classList.toggle('logic-active', gateActive);
  logicChips.or.classList.toggle('logic-active', alarmActive);
  logicChips.not.classList.toggle('logic-active', !circuitState.override);

  const narration = [];
  narration.push(
    gateActive
      ? 'Das Dorf-Tor fühlt sich wie ein echtes Redstone-AND-Gatter an – alles leuchtet!'
      : 'Hebel checken: Für das Tor müssen Strom, Signal und Stärke zusammenarbeiten.'
  );
  narration.push(
    alarmActive
      ? 'Der Alarm reagiert sofort auf jedes Signal – klassisches OR-Verhalten.'
      : 'Der Alarm wartet geduldig auf mindestens einen aktiven Hebel.'
  );
  narration.push(
    circuitState.override
      ? 'Override ist aktiv, NOT sorgt dafür, dass die Geheimtür geschützt bleibt.'
      : 'Override ist aus, also wirkt NOT wie eine Schutzzauberbarriere.'
  );

  logicNarration.textContent = narration.join(' ');
}

function toggleLamp(card, isActive) {
  card.classList.toggle('lamp-on', isActive);
}

function attachEvents() {
  leverButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const leverType = button.dataset.lever;
      circuitState[leverType] = !circuitState[leverType];
      updateLeverButtons();
      updateLamps();
      logAction(`${button.querySelector('.label').textContent}: ${formatBool(circuitState[leverType])}`);
    });
  });

  strengthSlider.addEventListener('input', (event) => {
    circuitState.strength = Number(event.target.value);
    strengthValue.textContent = circuitState.strength;
    updateLamps();
    logAction(`Signal-Stärke verändert auf ${circuitState.strength}`);
  });
}

function init() {
  attachEvents();
  updateLeverButtons();
  strengthValue.textContent = circuitState.strength;
  updateLamps();
  logAction('Webstone-Labor initialisiert. Hebel stehen auf AUS, Stärke bei 7.');
}

init();
