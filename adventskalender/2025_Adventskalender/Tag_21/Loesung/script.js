(() => {
  const $ = (selector) => document.querySelector(selector);
  const feedTemplate = document.getElementById("feed-template");
  const feedContainer = document.getElementById("hitFeed");
  const overlay = document.getElementById("arenaOverlay");
  const zoneState = document.getElementById("zoneState");
  const windValue = document.getElementById("windValue");
  const loopBadge = document.getElementById("loopBadge");
  const statusBadge = document.getElementById("statusBadge");
  const comboFill = document.getElementById("comboFill");
  const shotCount = document.getElementById("shotCount");
  const hitCount = document.getElementById("hitCount");
  const accuracyValue = document.getElementById("accuracyValue");
  const deltaValue = document.getElementById("deltaValue");
  const clockValue = document.getElementById("clockValue");
  const activeSnowballs = document.getElementById("activeSnowballs");
  const angleInput = document.getElementById("angleInput");
  const powerInput = document.getElementById("powerInput");
  const angleValue = document.getElementById("angleValue");
  const powerValue = document.getElementById("powerValue");
  const launchButton = document.getElementById("launchButton");
  const autoFireToggle = document.getElementById("autoFireToggle");
  const targetChips = new Map(
    Array.from(document.querySelectorAll("[data-chip]")).map((chip) => [
      chip.dataset.chip,
      chip,
    ])
  );

  const scoreboard = {
    shots: 0,
    hits: 0,
    combo: 0,
    points: 0,
    clock: 0,
    wind: 0,
  };

  const snowballs = new Set();
  let autoFireTimer = null;
  let lastTimestamp = 0;

  const {
    Engine,
    Render,
    Runner,
    Bodies,
    Body,
    Composite,
    World,
    Events,
  } = Matter;

  const width = 690;
  const height = 420;

  const engine = Engine.create({ enableSleeping: false });
  engine.world.gravity.y = 1;

  const render = Render.create({
    element: document.getElementById("arena"),
    engine,
    options: {
      width,
      height,
      background: "#010b19",
      wireframes: false,
      pixelRatio: Math.min(window.devicePixelRatio, 2),
    },
  });

  Render.run(render);
  const runner = Runner.create();
  Runner.run(runner, engine);

  // Boundaries and décor
  const ground = Bodies.rectangle(width / 2, height + 20, width + 100, 40, {
    isStatic: true,
    render: { fillStyle: "#083344" },
  });
  const ceiling = Bodies.rectangle(width / 2, -20, width, 40, {
    isStatic: true,
    render: { fillStyle: "transparent" },
  });
  const leftWall = Bodies.rectangle(-20, height / 2, 40, height, {
    isStatic: true,
  });
  const rightWall = Bodies.rectangle(width + 20, height / 2, 40, height, {
    isStatic: true,
  });
  const launcherPlate = Bodies.rectangle(120, 360, 180, 30, {
    isStatic: true,
    angle: -0.12,
    chamfer: { radius: 12 },
    render: { fillStyle: "#0f172a" },
  });
  const snowPile = Bodies.rectangle(40, 420, 160, 100, {
    isStatic: true,
    render: { fillStyle: "#f8fafc" },
  });

  const targetConfig = [
    { id: "ember", x: 520, y: 190, radius: 28, color: "#f87171", points: 120 },
    { id: "mint", x: 600, y: 260, radius: 32, color: "#4ade80", points: 150 },
    { id: "aqua", x: 470, y: 320, radius: 26, color: "#22d3ee", points: 200 },
  ];

  const targets = targetConfig.map((target) => {
    const circle = Bodies.circle(target.x, target.y, target.radius, {
      isStatic: true,
      label: `target-${target.id}`,
      render: {
        fillStyle: target.color,
        strokeStyle: "#ffffff",
        lineWidth: 3,
      },
    });
    circle.plugin = { type: "target", ...target };
    return circle;
  });

  World.add(engine.world, [
    ground,
    ceiling,
    leftWall,
    rightWall,
    launcherPlate,
    snowPile,
    ...targets,
  ]);

  function updateHUD() {
    shotCount.textContent = scoreboard.shots;
    hitCount.textContent = scoreboard.hits;
    const accuracy = scoreboard.shots === 0
      ? 0
      : Math.round((scoreboard.hits / scoreboard.shots) * 100);
    accuracyValue.textContent = `${accuracy}%`;
    comboFill.style.width = `${Math.min(scoreboard.combo, 100)}%`;

    const comboMode = scoreboard.combo > 75;
    statusBadge.textContent = comboMode ? "Combo brennt" : "Bereit";
    statusBadge.classList.toggle("status-chip--active", comboMode);
    statusBadge.classList.toggle("status-chip--idle", !comboMode);

    zoneState.textContent =
      scoreboard.hits >= targets.length ? "Arena gemeistert!" : "Ziele bereit";
  }

  function pushFeed(message, variant = "") {
    if (!feedTemplate) return;
    const entry = feedTemplate.content.firstElementChild.cloneNode(true);
    entry.querySelector(".feed-text").textContent = message;
    if (variant) entry.classList.add(variant);
    feedContainer.prepend(entry);
    while (feedContainer.children.length > 4) {
      feedContainer.removeChild(feedContainer.lastChild);
    }
  }

  function spawnFloatingText(text, x, y) {
    const marker = document.createElement("span");
    marker.className = "floating-text";
    marker.textContent = text;
    marker.style.left = `${x - 10}px`;
    marker.style.top = `${y - 10}px`;
    overlay.appendChild(marker);
    setTimeout(() => marker.remove(), 1200);
  }

  function spawnSplash(x, y, color) {
    const splash = document.createElement("span");
    splash.className = "impact-splash";
    splash.style.left = `${x - 30}px`;
    splash.style.top = `${y - 30}px`;
    splash.style.borderColor = color;
    overlay.appendChild(splash);
    setTimeout(() => splash.remove(), 900);
  }

  function updateControls() {
    angleValue.textContent = `${angleInput.value}°`;
    powerValue.textContent = powerInput.value;
  }

  function cleanupSnowball(body) {
    if (!snowballs.has(body)) return;
    snowballs.delete(body);
    Composite.remove(engine.world, body);
    activeSnowballs.textContent = snowballs.size;
  }

  function launchSnowball(custom) {
    const angleDeg = custom?.angle ?? Number(angleInput.value);
    const angleRad = (angleDeg * Math.PI) / 180;
    const power = custom?.power ?? Number(powerInput.value);

    scoreboard.shots += 1;
    scoreboard.combo = Math.max(0, scoreboard.combo - 10);
    updateHUD();
    pushFeed(`❄️ Wurf ${scoreboard.shots}: ${angleDeg}° / Power ${power}`, "");

    const snowball = Bodies.circle(120, 330, 16, {
      label: "snowball",
      restitution: 0.8,
      friction: 0.01,
      frictionAir: 0.01,
      density: 0.0015,
      render: {
        fillStyle: "#e0f2fe",
        strokeStyle: "#bae6fd",
        lineWidth: 2,
      },
    });
    snowball.plugin = { type: "snowball", scoredTargets: new Set() };

    const velocityScale = 0.55;
    Body.setVelocity(snowball, {
      x: Math.cos(angleRad) * power * velocityScale,
      y: Math.sin(angleRad) * -power * velocityScale,
    });
    Body.setAngularVelocity(snowball, 0.3);

    snowballs.add(snowball);
    activeSnowballs.textContent = snowballs.size;
    World.add(engine.world, snowball);

    setTimeout(() => cleanupSnowball(snowball), 9000);
  }

  Events.on(engine, "collisionStart", (event) => {
    for (const pair of event.pairs) {
      const bodies = [pair.bodyA, pair.bodyB];
      const target = bodies.find((b) => b.plugin?.type === "target");
      const snowball = bodies.find((b) => b.plugin?.type === "snowball");
      if (!target || !snowball) continue;
      if (snowball.plugin.scoredTargets.has(target.plugin.id)) continue;

      snowball.plugin.scoredTargets.add(target.plugin.id);
      scoreboard.hits += 1;
      scoreboard.combo = Math.min(100, scoreboard.combo + 35);
      updateHUD();

      const chip = targetChips.get(target.plugin.id);
      if (chip) {
        chip.classList.add("target-chip--hit");
        setTimeout(() => chip.classList.remove("target-chip--hit"), 1200);
      }

      pushFeed(`💥 Treffer! +${target.plugin.points} Punkte`, "hit");
      spawnFloatingText(`+${target.plugin.points}`, target.position.x, target.position.y);
      spawnSplash(target.position.x, target.position.y, target.plugin.color);
    }
  });

  function handleAutoFireToggle() {
    if (autoFireToggle.checked) {
      scheduleAutoFire();
    } else if (autoFireTimer) {
      clearTimeout(autoFireTimer);
      autoFireTimer = null;
    }
  }

  function scheduleAutoFire() {
    const delay = 1800 + Math.random() * 1600;
    autoFireTimer = setTimeout(() => {
      if (!autoFireToggle.checked) return;
      const randomAngle = Math.round(30 + Math.random() * 40);
      const randomPower = Math.round(14 + Math.random() * 8);
      angleInput.value = randomAngle;
      powerInput.value = randomPower;
      updateControls();
      launchSnowball({ angle: randomAngle, power: randomPower });
      scheduleAutoFire();
    }, delay);
  }

  function gameLoop(timestamp) {
    if (!lastTimestamp) lastTimestamp = timestamp;
    const delta = (timestamp - lastTimestamp) / 1000;
    lastTimestamp = timestamp;

    scoreboard.clock += delta;
    clockValue.textContent = `${scoreboard.clock.toFixed(1)} s`;
    deltaValue.textContent = `${(delta * 1000).toFixed(1)} ms`;

    scoreboard.combo = Math.max(0, scoreboard.combo - delta * 8);
    comboFill.style.width = `${Math.min(scoreboard.combo, 100)}%`;

    scoreboard.wind = Math.sin(scoreboard.clock / 2) * 8;
    const windArrow = scoreboard.wind >= 0 ? "➡️" : "⬅️";
    windValue.textContent = `${windArrow} ${Math.abs(scoreboard.wind).toFixed(1)} km/h`;

    snowballs.forEach((ball) => {
      if (ball.position.y > height + 40 || ball.position.x > width + 40) {
        cleanupSnowball(ball);
        return;
      }
      Body.applyForce(ball, ball.position, {
        x: scoreboard.wind * 0.00002,
        y: 0,
      });
    });

    loopBadge.textContent = delta * 1000 > 20 ? "Loop boost" : "Loop stabil";

    requestAnimationFrame(gameLoop);
    updateHUD();
  }

  launchButton.addEventListener("click", () => launchSnowball());
  angleInput.addEventListener("input", updateControls);
  powerInput.addEventListener("input", updateControls);
  autoFireToggle.addEventListener("change", handleAutoFireToggle);

  updateControls();
  updateHUD();
  requestAnimationFrame(gameLoop);
})();
