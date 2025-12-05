// Die Eishexe reagiert wie ein Entscheidungsbaum, daher sammeln wir alle DOM-Knoten
const playerInput = document.getElementById('player-input');
const toneSelect = document.getElementById('tone-select');
const crystalInput = document.getElementById('crystal-input');
const evaluateBtn = document.getElementById('evaluate-btn');
const shuffleBtn = document.getElementById('shuffle-btn');
const resetBtn = document.getElementById('reset-btn');
const portrait = document.getElementById('character-portrait');
const emotionIcon = document.getElementById('emotion-icon');
const statusChip = document.getElementById('status-chip');
const reactionText = document.getElementById('reaction-text');
const hintText = document.getElementById('hint-text');
const emotionLabel = document.getElementById('emotion-label');
const crystalLabel = document.getElementById('crystal-label');
const logList = document.getElementById('log-list');

const tips = [
  'Erwähne "Freundschaft" oder "Team" – das liebt die Hexe.',
  'Kristalle > 7 zeigen Großzügigkeit und schalten geheime Hinweise frei.',
  'Die Tonlage "Witz" hilft nur, wenn dein Text mindestens 8 Zeichen hat.',
  'Schreibe "Eis" oder "Nordlicht" für spannende Geschichten.',
];

const emotionClasses = ['emotion-calm', 'emotion-warm', 'emotion-curious', 'emotion-danger'];
const emotionEmojis = {
  calm: '❄️',
  impressed: '✨',
  curious: '🌀',
  warning: '⚠️',
};

const randomAnswers = [
  'Weise Aurora, ich suche den Nordlichtpfad.',
  'Ich bringe dir acht Kristalle und Respekt.',
  'Kannst du mir das Geheimnis des Frostwinds verraten?',
  'Ich grüße mit Humor und hoffe auf deine Hilfe.',
];

function sanitizeInput(value) {
  return value.trim().toLowerCase();
}

function setEmotion(type) {
  emotionClasses.forEach((className) => portrait.classList.remove(className));
  portrait.classList.add(type);
  switch (type) {
    case 'emotion-warm':
      emotionIcon.textContent = emotionEmojis.impressed;
      emotionLabel.textContent = 'beeindruckt';
      break;
    case 'emotion-curious':
      emotionIcon.textContent = emotionEmojis.curious;
      emotionLabel.textContent = 'neugierig';
      break;
    case 'emotion-danger':
      emotionIcon.textContent = emotionEmojis.warning;
      emotionLabel.textContent = 'misstrauisch';
      break;
    default:
      emotionIcon.textContent = emotionEmojis.calm;
      emotionLabel.textContent = 'ruhig';
  }
}

function describeCrystals(amount) {
  if (amount >= 8) {
    crystalLabel.textContent = 'beschenkt';
    return 'Sie spürt deine Großzügigkeit und öffnet winzige Portale im Eis.';
  }
  if (amount >= 4) {
    crystalLabel.textContent = 'ausgeglichen';
    return 'Dein Angebot ist vernünftig – gut genug für einen Hinweis.';
  }
  crystalLabel.textContent = 'unterfordert';
  return 'So wenig Kristallkraft? Das wirkt geizig wie ein leerer Redstone-Akku.';
}

function evaluateTone(tone, textLength) {
  let toneMessage = '';
  switch (tone) {
    case 'frage':
      toneMessage = 'Sie liebt gute Fragen und antwortet mit einem Hinweis.';
      break;
    case 'kompliment':
      toneMessage = 'Komplimente sind wie warme Fackeln – sie schmelzen ihr Misstrauen.';
      break;
    case 'witz':
      toneMessage =
        textLength > 7
          ? 'Dein Witz bringt sie zum Kichern, winzige Kristalle tanzen.'
          : 'Der Witz ist zu kurz, sie rollt nur mit den Augen.';
      break;
    case 'herausforderung':
      toneMessage = 'Mutig! Sie fordert dich nun zu präzisen Antworten heraus.';
      break;
    default:
      toneMessage = 'Sie bleibt neutral, weil sie die Stimmung nicht erkennt.';
  }
  return toneMessage;
}

function updateLogEntry(message) {
  const listItem = document.createElement('li');
  listItem.textContent = message;
  logList.prepend(listItem);
  while (logList.children.length > 5) {
    logList.removeChild(logList.lastChild);
  }
}

function evaluateAnswer() {
  const text = playerInput.value;
  const cleaned = sanitizeInput(text);
  const crystals = Number(crystalInput.value);
  const tone = toneSelect.value;

  if (cleaned.length === 0) {
    reactionText.textContent = 'Aurora hebt eine Augenbraue. Sag zuerst etwas, Lehrling!';
    hintText.textContent = 'Tipp: Verwende Wörter wie "Freundschaft", "Eis" oder "Geheimnis".';
    setEmotion('emotion-danger');
    portrait.classList.add('shake');
    setTimeout(() => portrait.classList.remove('shake'), 500);
    return;
  }

  let reaction = '';
  let hint = '';

  if (cleaned.includes('freund')) {
    reaction = 'Sie lächelt. "Verbündete sind selten – ich werde dir helfen."';
    setEmotion('emotion-warm');
    hint = 'Freundliche Worte öffnen viele Pfade.';
  } else if (cleaned.includes('eis') || cleaned.includes('schnee')) {
    reaction = 'Die Hexe erzählt dir vom geheimen Frostsee.';
    setEmotion('emotion-curious');
    hint = 'Nutze dein Wissen über ihre Welt.';
  } else if (cleaned.length > 60) {
    reaction = 'Sie streicht sich nachdenklich durchs Haar. "So viele Details!"';
    setEmotion('emotion-curious');
    hint = 'Lange Texte zeigen Planung, achte aber auf Klarheit.';
  } else {
    reaction = 'Sie bleibt skeptisch und wartet auf ein stärkeres Argument.';
    setEmotion('emotion-danger');
    hint = 'Versuch es mit mehr Emotion oder Wissen über sie.';
  }

  const crystalFeedback = describeCrystals(crystals);
  const toneFeedback = evaluateTone(tone, cleaned.length);

  reactionText.textContent = reaction;
  hintText.textContent = `${toneFeedback} ${crystalFeedback}`;
  statusChip.textContent = tone === 'herausforderung' ? 'aufmerksam' : 'berechnend';
  reactionText.classList.add('reaction-glow');
  setTimeout(() => reactionText.classList.remove('reaction-glow'), 1500);

  updateLogEntry(`➤ ${text || '...'} | Kristalle: ${crystals} | Ton: ${tone}`);
}

function setRandomAnswer() {
  const choice = randomAnswers[Math.floor(Math.random() * randomAnswers.length)];
  playerInput.value = choice;
}

function resetScene() {
  playerInput.value = '';
  crystalInput.value = 5;
  toneSelect.value = 'frage';
  reactionText.textContent = 'Die Hexe wartet geduldig auf deine Worte...';
  hintText.textContent = 'Tipps erscheinen hier, sobald du dich traust zu antworten.';
  emotionLabel.textContent = 'ruhig';
  crystalLabel.textContent = 'neutral';
  statusChip.textContent = 'berechnend';
  setEmotion('emotion-calm');
  logList.innerHTML = '';
}

evaluateBtn.addEventListener('click', evaluateAnswer);
shuffleBtn.addEventListener('click', () => {
  setRandomAnswer();
  evaluateAnswer();
});
resetBtn.addEventListener('click', resetScene);

playerInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter' && event.metaKey === false && event.shiftKey === false) {
    event.preventDefault();
    evaluateAnswer();
  }
});
