const spielbereich = document.getElementById('spielbereich');
const spieler1 = document.getElementById('spieler1');
const spieler2 = document.getElementById('spieler2');
const ball = document.getElementById('ball');

let spieler1Y = 150;
let spieler2Y = 150;

let ballX = 390;
let ballY = 190;
let ballSpeedX = 4;
let ballSpeedY = 3;

const paddleHeight = 100;
const paddleWidth = 20;
const ballSize = 20;

// Steuerung
const keys = {};
document.addEventListener('keydown', (e) => keys[e.key] = true);
document.addEventListener('keyup', (e) => keys[e.key] = false);

function update() {
    // Prevent arrow keys and space from scrolling the page
    document.addEventListener('keydown', function(e) {
        if(["ArrowUp","ArrowDown","ArrowLeft","ArrowRight"," "].includes(e.key)) {
            e.preventDefault(); // Stop default scrolling
        }
        keys[e.key] = true;
        });

    document.addEventListener('keyup', function(e) {
        keys[e.key] = false;
    });

    
    // Spieler 1: W/S
    if(keys['w'] && spieler1Y > 0) spieler1Y -= 5;
    if(keys['s'] && spieler1Y < 400 - paddleHeight) spieler1Y += 5;

    // Spieler 2: Pfeiltasten
    if(keys['ArrowUp'] && spieler2Y > 0) spieler2Y -= 5;
    if(keys['ArrowDown'] && spieler2Y < 400 - paddleHeight) spieler2Y += 5;

    // Paddle Position aktualisieren
    spieler1.style.top = spieler1Y + 'px';
    spieler2.style.top = spieler2Y + 'px';

    // Ball bewegen
    ballX += ballSpeedX;
    ballY += ballSpeedY;

    // Obere / untere Wand
    if(ballY <= 0 || ballY >= 400 - ballSize) ballSpeedY *= -1;

    // Paddle Kollision Spieler 1
    if(ballX <= paddleWidth && ballY + ballSize >= spieler1Y && ballY <= spieler1Y + paddleHeight) {
        ballSpeedX *= -1;
        ballX = paddleWidth; // Korrektur, damit Ball nicht hängen bleibt
    }

    // Paddle Kollision Spieler 2
    if(ballX + ballSize >= 800 - paddleWidth && ballY + ballSize >= spieler2Y && ballY <= spieler2Y + paddleHeight) {
        ballSpeedX *= -1;
        ballX = 800 - paddleWidth - ballSize;
    }

    // Ball aus dem Spielfeld (Score)
    if(ballX < 0 || ballX > 800 - ballSize) {
        ballX = 390;
        ballY = 190;
        ballSpeedX *= -1; // Richtung wechseln
    }

    ball.style.left = ballX + 'px';
    ball.style.top = ballY + 'px';

    requestAnimationFrame(update);
}

update();
