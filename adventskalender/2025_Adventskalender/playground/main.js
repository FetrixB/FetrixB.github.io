const canvas = document.getElementById('pong');
const ctx = canvas.getContext('2d');
const p1ScoreEl = document.getElementById('p1-score');
const p2ScoreEl = document.getElementById('p2-score');
const banner = document.getElementById('match-banner');

const settings = {
  width: 960,
  height: 540,
  paddle: { width: 14, height: 110, speed: 420 },
  ball: { radius: 10, speed: 380 },
  maxScore: 7,
};

canvas.width = settings.width;
canvas.height = settings.height;

const keys = new Set();
const state = {
  paddles: {
    p1: { x: 40, y: settings.height / 2 - settings.paddle.height / 2 },
    p2: { x: settings.width - 40 - settings.paddle.width, y: settings.height / 2 - settings.paddle.height / 2 },
  },
  ball: {
    x: settings.width / 2,
    y: settings.height / 2,
    vx: settings.ball.speed,
    vy: settings.ball.speed * 0.2,
  },
  scores: { p1: 0, p2: 0 },
  winner: null,
};

function resetBall(direction = Math.random() > 0.5 ? 1 : -1) {
  state.ball.x = settings.width / 2;
  state.ball.y = settings.height / 2;
  const angle = (Math.random() * 0.6 - 0.3) * Math.PI; // +/- ~30 deg
  state.ball.vx = Math.cos(angle) * settings.ball.speed * direction;
  state.ball.vy = Math.sin(angle) * settings.ball.speed;
}

function updateScoreboard() {
  p1ScoreEl.textContent = state.scores.p1;
  p2ScoreEl.textContent = state.scores.p2;
}

function declareWinner(player) {
  state.winner = player;
  banner.textContent = `${player === 'p1' ? 'Player One' : 'Player Two'} Wins! Tap Space to Restart`;
  banner.classList.remove('hidden');
}

function restartMatch() {
  state.scores.p1 = 0;
  state.scores.p2 = 0;
  state.winner = null;
  banner.classList.add('hidden');
  updateScoreboard();
  resetBall();
}

window.addEventListener('keydown', (event) => {
  if (event.code === 'Space' && state.winner) {
    restartMatch();
  }
  keys.add(event.code);
});

window.addEventListener('keyup', (event) => {
  keys.delete(event.code);
});

function movePaddles(delta) {
  const distance = settings.paddle.speed * delta;
  if (keys.has('KeyW')) state.paddles.p1.y -= distance;
  if (keys.has('KeyS')) state.paddles.p1.y += distance;
  if (keys.has('ArrowUp')) state.paddles.p2.y -= distance;
  if (keys.has('ArrowDown')) state.paddles.p2.y += distance;

  state.paddles.p1.y = Math.max(0, Math.min(settings.height - settings.paddle.height, state.paddles.p1.y));
  state.paddles.p2.y = Math.max(0, Math.min(settings.height - settings.paddle.height, state.paddles.p2.y));
}

function moveBall(delta) {
  state.ball.x += state.ball.vx * delta;
  state.ball.y += state.ball.vy * delta;

  if (state.ball.y < settings.ball.radius || state.ball.y > settings.height - settings.ball.radius) {
    state.ball.vy *= -1;
    state.ball.y = Math.max(settings.ball.radius, Math.min(settings.height - settings.ball.radius, state.ball.y));
  }

  // Basic overlap test for ball vs paddle that also adds english to ricochet
  const paddleCollision = (paddle) => {
    const withinY = state.ball.y + settings.ball.radius > paddle.y && state.ball.y - settings.ball.radius < paddle.y + settings.paddle.height;
    if (!withinY) return false;
    if (state.ball.x - settings.ball.radius <= paddle.x + settings.paddle.width && state.ball.x + settings.ball.radius >= paddle.x) {
      state.ball.vx *= -1.05; // add slight acceleration
      const impact = (state.ball.y - (paddle.y + settings.paddle.height / 2)) / (settings.paddle.height / 2);
      state.ball.vy = impact * settings.ball.speed;
      state.ball.x = paddle === state.paddles.p1 ? paddle.x + settings.paddle.width + settings.ball.radius : paddle.x - settings.ball.radius;
      return true;
    }
    return false;
  };

  if (state.ball.vx < 0) {
    paddleCollision(state.paddles.p1);
  } else {
    paddleCollision(state.paddles.p2);
  }

  if (state.ball.x < -settings.ball.radius) {
    state.scores.p2 += 1;
    updateScoreboard();
    if (state.scores.p2 >= settings.maxScore) {
      declareWinner('p2');
    }
    resetBall(1);
  }
  if (state.ball.x > settings.width + settings.ball.radius) {
    state.scores.p1 += 1;
    updateScoreboard();
    if (state.scores.p1 >= settings.maxScore) {
      declareWinner('p1');
    }
    resetBall(-1);
  }
}

function drawScene() {
  ctx.clearRect(0, 0, settings.width, settings.height);

  const gradient = ctx.createLinearGradient(0, 0, settings.width, settings.height);
  gradient.addColorStop(0, '#22d3ee20');
  gradient.addColorStop(1, '#34d39920');
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, settings.width, settings.height);

  ctx.setLineDash([12, 16]);
  ctx.lineWidth = 4;
  ctx.strokeStyle = '#ffffff22';
  ctx.beginPath();
  ctx.moveTo(settings.width / 2, 0);
  ctx.lineTo(settings.width / 2, settings.height);
  ctx.stroke();
  ctx.setLineDash([]);

  ctx.fillStyle = '#34d399';
  ctx.fillRect(state.paddles.p1.x, state.paddles.p1.y, settings.paddle.width, settings.paddle.height);
  ctx.fillStyle = '#22d3ee';
  ctx.fillRect(state.paddles.p2.x, state.paddles.p2.y, settings.paddle.width, settings.paddle.height);

  ctx.fillStyle = '#f8fafc';
  ctx.beginPath();
  ctx.arc(state.ball.x, state.ball.y, settings.ball.radius, 0, Math.PI * 2);
  ctx.fill();
}

let lastTime = performance.now();
function loop(now) {
  // Clamp delta to keep physics stable after tab switching
  const delta = Math.min((now - lastTime) / 1000, 0.02);
  lastTime = now;

  if (!state.winner) {
    movePaddles(delta);
    moveBall(delta);
  }

  drawScene();
  requestAnimationFrame(loop);
}

resetBall();
updateScoreboard();
requestAnimationFrame(loop);
