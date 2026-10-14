import * as THREE from 'https://esm.sh/three@0.169.0';
import Peer from 'https://esm.sh/peerjs@1.5.4?bundle';

const $ = (selector) => document.querySelector(selector);
const lobbyScreen = $('#lobbyScreen');
const waitingScreen = $('#waitingScreen');
const gameScreen = $('#gameScreen');
const statusText = $('#connectionStatus span:last-child');
const weapons = {
  sniper: { name: 'SNIPER', damage: 42, range: 24, cooldown: 650, color: 0xc8f169, radius: .7 },
  minigun: { name: 'MINIGUN', damage: 8, range: 13, cooldown: 105, color: 0xffd166, radius: .9 },
  bazooka: { name: 'BAZOOKA', damage: 56, range: 18, cooldown: 850, color: 0xff786d, radius: 1.05 },
  knife: { name: 'KNIFE', damage: 34, range: 2.45, cooldown: 430, color: 0xdce8da, radius: .95 }
};

let peer = null;
let connection = null;
let isHost = false;
let bestOf = 5;
let selectedWeapon = 'sniper';
let accepted = false;
let game = null;

function setStatus(message, error = false) {
  if (!statusText) return;
  statusText.textContent = message;
  statusText.style.color = error ? '#ff786d' : '';
}

function showScreen(screen) {
  [lobbyScreen, waitingScreen, gameScreen].forEach((element) => element.classList.add('hidden'));
  screen.classList.remove('hidden');
}

function makePeerId() {
  return `duel-${Math.random().toString(36).slice(2, 8)}`;
}

function setupPeer(id) {
  peer = new Peer(id, { debug: 1 });
  peer.on('error', (error) => {
    const messages = {
      'peer-unavailable': 'Spielercode nicht gefunden. Prüfe den Code und versuche es erneut.',
      'unavailable-id': 'Code bereits vergeben. Öffne die Arena erneut.',
      'network': 'Verbindung fehlgeschlagen. Prüfe WLAN und Internetverbindung.'
    };
    setStatus(messages[error.type] || `Verbindung: ${error.type}`, true);
    if (error.type === 'peer-unavailable' && !game) resetPeer();
  });
  peer.on('disconnected', () => setStatus('Verbindung unterbrochen. Versuche neu zu verbinden …', true));
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error('timeout')), 12000);
    peer.once('open', (peerId) => { clearTimeout(timer); resolve(peerId); });
    peer.once('error', (error) => { clearTimeout(timer); reject(error); });
  });
}

function resetPeer() {
  if (connection) { connection.close(); connection = null; }
  if (peer) { peer.destroy(); peer = null; }
  accepted = false;
}

function listenForChallenge(conn) {
  connection = conn;
  conn.on('data', (message) => {
    if (!message || typeof message !== 'object') return;
    if (message.type === 'challenge' && isHost) {
      $('#challengerName').textContent = 'Ein Spieler möchte antreten.';
      $('#requestCard').classList.remove('hidden');
      $('#inviteState').classList.add('hidden');
      conn.__challengerReady = true;
    }
    if (message.type === 'accepted' && !isHost) {
      accepted = true;
      bestOf = message.rounds;
      startMatch();
    }
    if (message.type === 'rejected' && !isHost) {
      setStatus('Deine Matchanfrage wurde abgelehnt.');
      resetPeer();
      showScreen(lobbyScreen);
    }
    if (message.type === 'state' && game) {
      const remote = isHost ? game.guest : game.host;
      remote.targetX = message.x;
      remote.targetZ = message.z;
      remote.health = message.health;
      remote.score = message.score;
      game.round = message.round;
      updateHud();
    }
    if (message.type === 'hit' && game) receiveHit(message.damage, message.weapon, message.x, message.z);
    if (message.type === 'round' && game) applyRound(message.winner, false);
    if (message.type === 'leave') endMatch('Dein Gegner hat das Match verlassen.');
  });
  conn.on('close', () => { if (game) endMatch('Die Verbindung zu deinem Gegner wurde getrennt.'); });
  conn.on('error', () => setStatus('Fehler in der Spielverbindung.', true));
}

$('#hostButton').addEventListener('click', async () => {
  resetPeer(); isHost = true;
  $('#hostButton').disabled = true;
  setStatus('Arena wird vorbereitet …');
  try {
    const id = await setupPeer(makePeerId());
    $('#hostCode').textContent = id;
    showScreen(waitingScreen);
    $('#waitingEyebrow').textContent = 'DEINE ARENA IST BEREIT';
    $('#waitingTitle').innerHTML = 'Warte auf<br><em>einen Herausforderer.</em>';
    $('#waitingDescription').textContent = 'Teile diesen Code mit deinem Gegner. Sobald die Anfrage kommt, kannst du sie annehmen.';
    $('#inviteState').innerHTML = '<span class="live-dot"></span> ARENA SUCHT SPIELER';
    $('#inviteState').classList.remove('hidden');
    $('#requestCard').classList.add('hidden');
    setStatus('Deine Arena ist bereit.');
    peer.on('connection', (conn) => {
      if (connection && connection.open) { conn.close(); return; }
      listenForChallenge(conn);
      conn.on('open', () => setStatus('Anfrage erhalten. Entscheide, ob du spielst.'));
    });
  } catch (error) {
    setStatus('Arena konnte nicht geöffnet werden. Prüfe deine Internetverbindung.', true);
    resetPeer();
  } finally { $('#hostButton').disabled = false; }
});

$('#joinButton').addEventListener('click', async () => {
  const id = $('#joinCode').value.trim().toLowerCase();
  if (!id) { setStatus('Gib zuerst den Spielercode ein.', true); $('#joinCode').focus(); return; }
  resetPeer(); isHost = false;
  $('#joinButton').disabled = true;
  setStatus('Spieler wird gesucht …');
  try {
    await setupPeer(makePeerId());
    connection = peer.connect(id, { reliable: true });
    listenForChallenge(connection);
    connection.on('open', () => {
      connection.send({ type: 'challenge', rounds: bestOf });
      showScreen(waitingScreen);
      $('#hostCode').textContent = id;
      $('#waitingEyebrow').textContent = 'MATCHANFRAGE';
      $('#waitingTitle').innerHTML = 'Anfrage gesendet.<br><em>Jetzt heißt es warten.</em>';
      $('#waitingDescription').textContent = 'Der Host muss deine Matchanfrage annehmen. Danach startet ihr direkt in die Arena.';
      $('#inviteState').innerHTML = '<span class="live-dot"></span> MATCHANFRAGE GESENDET';
      $('#requestCard').classList.add('hidden');
      setStatus('Anfrage gesendet. Warte auf Annahme …');
    });
  } catch (error) {
    setStatus('Spieler nicht erreichbar. Prüfe den Code und deine Verbindung.', true);
    resetPeer();
  } finally { $('#joinButton').disabled = false; }
});

$('#acceptButton').addEventListener('click', () => {
  if (!connection?.open) return;
  accepted = true;
  connection.send({ type: 'accepted', rounds: bestOf });
  startMatch();
});
$('#declineButton').addEventListener('click', () => {
  connection?.send({ type: 'rejected' });
  connection?.close();
  connection = null;
  $('#requestCard').classList.add('hidden');
  $('#inviteState').classList.remove('hidden');
  setStatus('Anfrage abgelehnt. Deine Arena bleibt offen.');
});
$('#cancelHost').addEventListener('click', () => { resetPeer(); showScreen(lobbyScreen); setStatus('Bereit für dein Match'); });
$('#copyCode').addEventListener('click', async () => {
  try { await navigator.clipboard.writeText($('#hostCode').textContent); $('#copyCode').textContent = 'KOPIERT ✓'; setTimeout(() => { $('#copyCode').textContent = 'KOPIEREN ↗'; }, 1400); }
  catch { setStatus('Code markieren und kopieren: ' + $('#hostCode').textContent); }
});
document.querySelectorAll('[data-rounds]').forEach((button) => button.addEventListener('click', () => {
  bestOf = Number(button.dataset.rounds);
  document.querySelectorAll('[data-rounds]').forEach((item) => item.classList.toggle('selected', item === button));
}));
document.querySelectorAll('[data-weapon]').forEach((button) => button.addEventListener('click', () => selectWeapon(button.dataset.weapon)));
function selectWeapon(weapon) {
  if (!weapons[weapon]) return;
  selectedWeapon = weapon;
  document.querySelectorAll('[data-weapon]').forEach((button) => button.classList.toggle('selected', button.dataset.weapon === weapon));
}

function startMatch() {
  if (!connection?.open) { setStatus('Spielverbindung wurde geschlossen.', true); return; }
  showScreen(gameScreen);
  $('#roundLabel').textContent = `BEST OF ${bestOf}`;
  $('#selfName').innerHTML = `DU <span>${isHost ? 'SPIELER 1' : 'SPIELER 2'}</span>`;
  $('#opponentName').innerHTML = `GEGNER <span>${isHost ? 'SPIELER 2' : 'SPIELER 1'}</span>`;
  if (game?.renderer) game.renderer.dispose();
  game = createArena();
  syncHudNames();
  setStatus('Match läuft');
}

function createArena() {
  const mount = $('#gameCanvas');
  mount.replaceChildren();
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x171e19);
  scene.fog = new THREE.Fog(0x171e19, 23, 48);
  const camera = new THREE.PerspectiveCamera(47, 1, .1, 100);
  camera.position.set(0, 17, 20);
  camera.lookAt(0, 0, 0);
  const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.7));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.15;
  mount.appendChild(renderer.domElement);
  scene.add(new THREE.HemisphereLight(0xddebd5, 0x27312a, 2.1));
  const sun = new THREE.DirectionalLight(0xffe7c4, 3.1);
  sun.position.set(-7, 15, 7); sun.castShadow = true; sun.shadow.mapSize.set(1024, 1024); sun.shadow.camera.left = -18; sun.shadow.camera.right = 18; sun.shadow.camera.top = 18; sun.shadow.camera.bottom = -18; scene.add(sun);

  const floor = new THREE.Mesh(new THREE.PlaneGeometry(30, 22), new THREE.MeshStandardMaterial({ color: 0x303b31, roughness: .92 }));
  floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; scene.add(floor);
  const grid = new THREE.GridHelper(30, 30, 0x77856a, 0x4d594b); grid.position.y = .015; grid.material.transparent = true; grid.material.opacity = .18; scene.add(grid);
  const perimeter = new THREE.Mesh(new THREE.BoxGeometry(30.4, .16, 22.4), new THREE.MeshStandardMaterial({ color: 0x899b65, emissive: 0x344827, emissiveIntensity: .45 }));
  perimeter.position.set(0, .05, 0); scene.add(perimeter);
  const inner = new THREE.Mesh(new THREE.PlaneGeometry(29.5, 21.5), new THREE.MeshStandardMaterial({ color: 0x303b31, roughness: .92 }));
  inner.rotation.x = -Math.PI / 2; inner.position.y = .11; scene.add(inner);
  const obstaclePositions = [[-3.8, -2.7, 1.2, 1.4], [3.9, 2.5, 1.3, 1.3], [-7, 2.7, .8, 2.1], [7, -2.5, .8, 2.1], [0, -6.1, 2.1, .6], [0, 6.1, 2.1, .6]];
  obstaclePositions.forEach(([x, z, w, d], index) => {
    const height = index % 2 ? 1.1 : 1.45;
    const block = new THREE.Mesh(new THREE.BoxGeometry(w, height, d), new THREE.MeshStandardMaterial({ color: index % 2 ? 0x53604e : 0x475545, roughness: .83 }));
    block.position.set(x, height / 2, z); block.castShadow = true; block.receiveShadow = true; scene.add(block);
    const trim = new THREE.Mesh(new THREE.BoxGeometry(w * .92, .08, d * .92), new THREE.MeshStandardMaterial({ color: index % 2 ? 0x8fa06b : 0x778b5a, emissive: 0x1d2a15 }));
    trim.position.set(x, height + .02, z); scene.add(trim);
  });
  for (let i = 0; i < 24; i++) {
    const x = (Math.random() - .5) * 28, z = (Math.random() - .5) * 20;
    if (Math.abs(x) < 8 && Math.abs(z) < 6) continue;
    const rock = new THREE.Mesh(new THREE.DodecahedronGeometry(.12 + Math.random() * .18, 0), new THREE.MeshStandardMaterial({ color: 0x59634f, roughness: 1 }));
    rock.position.set(x, .08, z); rock.scale.y = .45; rock.rotation.y = Math.random() * 6; rock.castShadow = true; scene.add(rock);
  }

  const makeFighter = (color, accent) => {
    const group = new THREE.Group();
    const material = new THREE.MeshStandardMaterial({ color, roughness: .65 });
    const accentMat = new THREE.MeshStandardMaterial({ color: accent, emissive: accent, emissiveIntensity: .12, roughness: .5 });
    const torso = new THREE.Mesh(new THREE.CapsuleGeometry(.43, .62, 4, 8), material); torso.position.y = 1.05; torso.castShadow = true; group.add(torso);
    const head = new THREE.Mesh(new THREE.SphereGeometry(.31, 12, 10), new THREE.MeshStandardMaterial({ color: 0xd2bba1, roughness: .9 })); head.position.y = 1.74; head.castShadow = true; group.add(head);
    const visor = new THREE.Mesh(new THREE.BoxGeometry(.48, .12, .24), accentMat); visor.position.set(0, 1.78, .18); group.add(visor);
    const legs = new THREE.Mesh(new THREE.BoxGeometry(.52, .52, .38), new THREE.MeshStandardMaterial({ color: 0x242d28, roughness: .8 })); legs.position.y = .38; legs.castShadow = true; group.add(legs);
    const gun = new THREE.Mesh(new THREE.BoxGeometry(.15, .13, .78), new THREE.MeshStandardMaterial({ color: 0x282e29, metalness: .55, roughness: .35 })); gun.position.set(.42, 1.25, .36); gun.rotation.x = -.1; gun.castShadow = true; group.add(gun);
    const glow = new THREE.PointLight(accent, 1.8, 3); glow.position.y = 2; group.add(glow);
    scene.add(group);
    return { group, health: 100, score: 0, targetX: 0, targetZ: 0 };
  };
  const host = makeFighter(0x4e7593, 0x72a6ff);
  const guest = makeFighter(0x945248, 0xff786d);
  host.group.position.set(-9, 0, 0); guest.group.position.set(9, 0, 0); guest.group.rotation.y = Math.PI;

  const match = { scene, camera, renderer, host, guest, isHost, round: 1, keys: new Set(), aim: new THREE.Vector3(), lastShot: 0, pausedUntil: 0, raf: 0, bullets: [], resize: null, pointer: { x: 0, y: 0 }, running: true };
  const raycaster = new THREE.Raycaster();
  const ground = new THREE.Plane(new THREE.Vector3(0, 1, 0), 0);
  const local = isHost ? host : guest;
  const remote = isHost ? guest : host;
  const handleResize = () => {
    const width = mount.clientWidth || 1, height = mount.clientHeight || 1;
    renderer.setSize(width, height, false); camera.aspect = width / height; camera.updateProjectionMatrix();
  };
  match.resize = handleResize;
  window.addEventListener('resize', handleResize); handleResize();
  renderer.domElement.addEventListener('pointermove', (event) => {
    const rect = renderer.domElement.getBoundingClientRect();
    match.pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
    match.pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
    $('#crosshair').style.left = `${event.clientX - rect.left}px`;
    $('#crosshair').style.top = `${event.clientY - rect.top}px`;
  });
  renderer.domElement.addEventListener('pointerdown', (event) => { if (event.button === 0) shoot(match, local, remote); });
  renderer.domElement.addEventListener('contextmenu', (event) => event.preventDefault());
  const keydown = (event) => {
    if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', ' '].includes(event.key)) event.preventDefault();
    const key = event.key.toLowerCase();
    if (['w', 'a', 's', 'd', 'arrowup', 'arrowdown', 'arrowleft', 'arrowright', 'shift'].includes(key)) match.keys.add(key);
    if (['1', '2', '3', '4'].includes(key)) selectWeapon(['sniper', 'minigun', 'bazooka', 'knife'][Number(key) - 1]);
    if (key === 'shift') local.dashUntil = performance.now() + 180;
  };
  const keyup = (event) => match.keys.delete(event.key.toLowerCase());
  match.keydown = keydown; match.keyup = keyup;
  window.addEventListener('keydown', keydown); window.addEventListener('keyup', keyup);

  let lastTime = performance.now();
  const animate = (time) => {
    if (!match.running || !game) return;
    match.raf = requestAnimationFrame(animate);
    const dt = Math.min((time - lastTime) / 1000, .04); lastTime = time;
    if (time > match.pausedUntil) {
      let dx = 0, dz = 0;
      if (match.keys.has('w') || match.keys.has('arrowup')) dz -= 1;
      if (match.keys.has('s') || match.keys.has('arrowdown')) dz += 1;
      if (match.keys.has('a') || match.keys.has('arrowleft')) dx -= 1;
      if (match.keys.has('d') || match.keys.has('arrowright')) dx += 1;
      const length = Math.hypot(dx, dz) || 1;
      const speed = time < (local.dashUntil || 0) ? 13 : 6.2;
      local.group.position.x = THREE.MathUtils.clamp(local.group.position.x + (dx / length) * speed * dt, -13.7, 13.7);
      local.group.position.z = THREE.MathUtils.clamp(local.group.position.z + (dz / length) * speed * dt, -9.7, 9.7);
      if (dx || dz) local.group.rotation.y = Math.atan2(dx, dz);

      raycaster.setFromCamera(match.pointer, camera);
      raycaster.ray.intersectPlane(ground, match.aim);
      match.aim.x = THREE.MathUtils.clamp(match.aim.x, -15, 15); match.aim.z = THREE.MathUtils.clamp(match.aim.z, -11, 11);
      if (dx || dz) { const angle = Math.atan2(match.aim.x - local.group.position.x, match.aim.z - local.group.position.z); local.group.rotation.y = angle; }
      remote.group.position.x = THREE.MathUtils.damp(remote.group.position.x, remote.targetX, 12, dt);
      remote.group.position.z = THREE.MathUtils.damp(remote.group.position.z, remote.targetZ, 12, dt);
      remote.group.rotation.y = Math.atan2(local.group.position.x - remote.group.position.x, local.group.position.z - remote.group.position.z);
      local.group.position.y = Math.sin(time * .006) * .025;
      remote.group.position.y = Math.sin(time * .006 + 1) * .025;
      match.bullets = match.bullets.filter((bullet) => {
        bullet.life -= dt;
        bullet.mesh.position.addScaledVector(bullet.velocity, dt);
        if (bullet.life <= 0) { scene.remove(bullet.mesh); bullet.mesh.geometry.dispose(); bullet.mesh.material.dispose(); return false; }
        return true;
      });
      camera.position.x = THREE.MathUtils.damp(camera.position.x, local.group.position.x * .26, 2.5, dt);
      camera.position.z = THREE.MathUtils.damp(camera.position.z, 20 + local.group.position.z * .23, 2.5, dt);
      camera.lookAt(local.group.position.x * .17, 0, local.group.position.z * .17);
    }
    renderer.render(scene, camera);
    if (connection?.open && Math.floor(time / 70) !== match.lastSync) {
      match.lastSync = Math.floor(time / 70);
      connection.send({ type: 'state', x: local.group.position.x, z: local.group.position.z, health: local.health, score: local.score, round: match.round });
      updateHud();
    }
  };
  requestAnimationFrame(animate);
  updateHud();
  return match;
}

function shoot(match, local, remote) {
  const now = performance.now(), weapon = weapons[selectedWeapon];
  if (!game || now < match.pausedUntil || now - match.lastShot < weapon.cooldown || local.health <= 0) return;
  match.lastShot = now;
  const from = local.group.position.clone();
  const to = match.aim.clone();
  const vector = new THREE.Vector3(to.x - from.x, 0, to.z - from.z);
  const distance = vector.length();
  if (!distance) return;
  vector.normalize();
  local.group.rotation.y = Math.atan2(vector.x, vector.z);
  const color = weapon.color;
  const tracer = new THREE.Mesh(new THREE.CylinderGeometry(.025, .045, 1, 6), new THREE.MeshBasicMaterial({ color, transparent: true, opacity: .95 }));
  const muzzle = from.clone().add(new THREE.Vector3(vector.x * .65, 1.25, vector.z * .65));
  const end = new THREE.Vector3(to.x, .6, to.z);
  const delta = end.clone().sub(muzzle);
  tracer.position.copy(muzzle).add(end).multiplyScalar(.5); tracer.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), delta.clone().normalize()); tracer.scale.y = delta.length(); match.scene.add(tracer);
  setTimeout(() => { match.scene.remove(tracer); tracer.geometry.dispose(); tracer.material.dispose(); }, selectedWeapon === 'bazooka' ? 420 : 100);
  if (selectedWeapon === 'bazooka') {
    const glow = new THREE.PointLight(color, 2, 3); glow.position.copy(muzzle); match.scene.add(glow); setTimeout(() => match.scene.remove(glow), 300);
  }
  const target = remote.group.position;
  const toTarget = new THREE.Vector3(target.x - from.x, 0, target.z - from.z);
  const along = toTarget.dot(vector), side = Math.abs(toTarget.x * vector.z - toTarget.z * vector.x);
  const hit = along > 0 && along <= weapon.range && side <= weapon.radius && distance <= weapon.range + 2.5;
  if (hit) {
    const actualDamage = weapon.damage;
    connection?.send({ type: 'hit', damage: actualDamage, weapon: selectedWeapon, x: target.x, z: target.z });
    showToast(`TREFFER · ${weapon.name}`);
  } else if (selectedWeapon === 'knife') showToast('ZU WEIT ENTFERNT');
}

function receiveHit(damage, weapon, x, z) {
  if (!game || game.pausedUntil > performance.now()) return;
  const local = game.isHost ? game.host : game.guest;
  local.health = Math.max(0, local.health - damage);
  if (weapon === 'bazooka') {
    const target = local.group.position;
    const awayX = target.x - x, awayZ = target.z - z;
    const length = Math.hypot(awayX, awayZ) || 1;
    target.x = THREE.MathUtils.clamp(target.x + (awayX / length) * .8, -13.7, 13.7);
    target.z = THREE.MathUtils.clamp(target.z + (awayZ / length) * .8, -9.7, 9.7);
  }
  updateHud();
  showToast(`−${damage} HP · ${weapons[weapon]?.name || 'TREFFER'}`);
  if (local.health <= 0) {
    const winner = game.isHost ? 'guest' : 'host';
    connection?.send({ type: 'round', winner });
    applyRound(winner, false);
  }
}

function applyRound(winner, send) {
  if (!game || game.pausedUntil > performance.now()) return;
  game.pausedUntil = performance.now() + 2800;
  const winnerPlayer = winner === 'host' ? game.host : game.guest;
  winnerPlayer.score += 1;
  game.round += 1;
  const won = winner === (game.isHost ? 'host' : 'guest');
  $('#roundEyebrow').textContent = won ? 'RUNDE GEWONNEN' : 'RUNDE VERLOREN';
  $('#roundMessage').textContent = won ? 'NICE SHOT.' : 'NEXT ROUND.';
  $('#roundSub').textContent = 'Nächste Runde startet gleich …';
  $('#roundOverlay').classList.remove('hidden');
  updateHud();
  if (send) connection?.send({ type: 'round', winner });
  const needed = Math.ceil(bestOf / 2);
  if (winnerPlayer.score >= needed) {
    $('#roundMessage').textContent = won ? 'DU GEWINNST.' : 'MATCH VERLOREN.';
    $('#roundSub').textContent = `${game.host.score} : ${game.guest.score} — Best of ${bestOf}`;
    setTimeout(() => endMatch(won ? 'Du hast das Match gewonnen.' : 'Dein Gegner gewinnt das Match.'), 2600);
    return;
  }
  setTimeout(() => {
    if (!game) return;
    game.host.health = 100; game.guest.health = 100;
    game.host.group.position.set(-9, 0, 0); game.guest.group.position.set(9, 0, 0);
    game.host.targetX = -9; game.host.targetZ = 0; game.guest.targetX = 9; game.guest.targetZ = 0;
    game.pausedUntil = 0;
    $('#roundOverlay').classList.add('hidden');
    updateHud();
  }, 2800);
}

function updateHud() {
  if (!game) return;
  const self = game.isHost ? game.host : game.guest, opponent = game.isHost ? game.guest : game.host;
  $('#selfHealth').style.width = `${self.health}%`; $('#opponentHealth').style.width = `${opponent.health}%`;
  $('#selfScore').textContent = self.score; $('#opponentScore').textContent = opponent.score;
  $('#scoreA').textContent = game.host.score; $('#scoreB').textContent = game.guest.score;
  $('#roundNumber').textContent = `RUNDE ${Math.min(game.round, bestOf)}`;
}
function syncHudNames() { updateHud(); }
function showToast(message) {
  const toast = $('#gameToast'); toast.textContent = message; toast.classList.remove('hidden');
  clearTimeout(showToast.timer); showToast.timer = setTimeout(() => toast.classList.add('hidden'), 950);
}
function endMatch(message) {
  if (!game) { setStatus(message); return; }
  connection?.send({ type: 'leave' });
  game.running = false; cancelAnimationFrame(game.raf);
  window.removeEventListener('resize', game.resize);
  window.removeEventListener('keydown', game.keydown); window.removeEventListener('keyup', game.keyup);
  game.renderer.dispose(); game.renderer.domElement.remove();
  game = null; resetPeer(); showScreen(lobbyScreen); setStatus(message);
}

$('#leaveMatch').addEventListener('click', () => endMatch('Du hast das Match verlassen.'));
$('#joinCode').addEventListener('keydown', (event) => { if (event.key === 'Enter') $('#joinButton').click(); });

