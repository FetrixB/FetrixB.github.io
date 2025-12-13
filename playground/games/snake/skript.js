const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');

const scale = 20; // size of one cell in pixels
const cols = canvas.width / scale;
const rows = canvas.height / scale;

let snake;
let food;
let dir;
let nextDir;
let score = 0;
let running = false;
let loopInterval = 100; // ms

function reset() {
  snake = [{ x: Math.floor(cols/2), y: Math.floor(rows/2) }];
  dir = { x: 1, y: 0 };
  nextDir = { x: 1, y: 0 };
  placeFood();
  score = 0;
  running = true;
  document.getElementById('score').textContent = `Score: ${score}`;
}

function placeFood() {
  while (true) {
    const fx = Math.floor(Math.random() * cols);
    const fy = Math.floor(Math.random() * rows);
    if (!snake.some(s => s.x === fx && s.y === fy)) {
      food = { x: fx, y: fy };
      return;
    }
  }
}

function gameStep() {
  if (!running) return;
  dir = nextDir;
  const head = { x: snake[0].x + dir.x, y: snake[0].y + dir.y };

  // wall wrap
  if (head.x < 0) head.x = cols - 1;
  if (head.x >= cols) head.x = 0;
  if (head.y < 0) head.y = rows - 1;
  if (head.y >= rows) head.y = 0;

  // collision with body
  if (snake.some(s => s.x === head.x && s.y === head.y)) {
    running = false;
    draw();
    return;
  }

  snake.unshift(head);

  // eat food
  if (head.x === food.x && head.y === food.y) {
    score++;
    document.getElementById('score').textContent = `Score: ${score}`;
    placeFood();
    // speed up slightly every 5 points
    if (score % 5 === 0 && loopInterval > 30) {
      loopInterval = Math.max(30, loopInterval - 8);
      restartLoop();
    }
  } else {
    snake.pop();
  }

  draw();
}

function draw() {
  // clear
  ctx.fillStyle = '#071022';
  ctx.fillRect(0,0,canvas.width,canvas.height);

  // draw food
  ctx.fillStyle = '#ff6b6b';
  ctx.fillRect(food.x*scale+2, food.y*scale+2, scale-4, scale-4);

  // draw snake
  for (let i = 0; i < snake.length; i++) {
    ctx.fillStyle = i === 0 ? '#6ef0a6' : '#3bd78f';
    const s = snake[i];
    ctx.fillRect(s.x*scale+1, s.y*scale+1, scale-2, scale-2);
  }

  if (!running) {
    ctx.fillStyle = 'rgba(0,0,0,0.6)';
    ctx.fillRect(0, canvas.height/2 - 30, canvas.width, 60);
    ctx.fillStyle = '#fff';
    ctx.textAlign = 'center';
    ctx.font = '20px system-ui, sans-serif';
    ctx.fillText('Game Over — Press Restart', canvas.width/2, canvas.height/2 + 7);
  }
}

function handleKey(e) {
  const key = e.key;
  if (key === 'ArrowUp' && dir.y !== 1) nextDir = { x: 0, y: -1 };
  if (key === 'ArrowDown' && dir.y !== -1) nextDir = { x: 0, y: 1 };
  if (key === 'ArrowLeft' && dir.x !== 1) nextDir = { x: -1, y: 0 };
  if (key === 'ArrowRight' && dir.x !== -1) nextDir = { x: 1, y: 0 };
}

let timerId;
function startLoop() {
  timerId = setInterval(gameStep, loopInterval);
}
function restartLoop() {
  clearInterval(timerId);
  startLoop();
}

document.getElementById('restart').addEventListener('click', () => {
  reset();
  restartLoop();
});

window.addEventListener('keydown', handleKey);

// init
reset();
startLoop();
draw();