import * as THREE from "https://unpkg.com/three@0.160.0/build/three.module.js";

const canvas = document.getElementById("snowPortal");
const snowLabel = document.querySelector("[data-snow-count]");
const portalMood = document.getElementById("portalMood");
const speedControl = document.getElementById("speedControl");
const burstButton = document.getElementById("burstButton");

const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x030712, 0.02);
const camera = new THREE.PerspectiveCamera(58, 1, 0.1, 200);
camera.position.set(0, 8, 42);

const snowGeometry = new THREE.BufferGeometry();
const count = 1400;
const spread = 65;
const snowPositions = new Float32Array(count * 3);
const snowSpeeds = new Float32Array(count);

for (let i = 0; i < count; i += 1) {
  const i3 = i * 3;
  snowPositions[i3] = (Math.random() - 0.5) * spread;
  snowPositions[i3 + 1] = Math.random() * 36 - 12;
  snowPositions[i3 + 2] = (Math.random() - 0.5) * spread;
  snowSpeeds[i] = 0.1 + Math.random() * 0.25;
}

snowGeometry.setAttribute("position", new THREE.BufferAttribute(snowPositions, 3));
const snowMaterial = new THREE.PointsMaterial({
  size: 0.75,
  color: 0xe0f2fe,
  transparent: true,
  opacity: 0.85,
  blending: THREE.AdditiveBlending,
  depthWrite: false,
});
const snowPoints = new THREE.Points(snowGeometry, snowMaterial);
scene.add(snowPoints);

const portalRing = new THREE.Mesh(
  new THREE.TorusGeometry(11, 2.2, 32, 160),
  new THREE.MeshStandardMaterial({ color: 0x38bdf8, emissive: 0x0f172a, emissiveIntensity: 1.1 })
);
portalRing.position.set(0, 4, 0);
scene.add(portalRing);

scene.add(new THREE.AmbientLight(0xbcd4ff, 0.4));
const keyLight = new THREE.PointLight(0x3b82f6, 2, 90);
keyLight.position.set(26, 18, 10);
scene.add(keyLight);

const rendererSize = () => {
  const width = canvas.clientWidth || window.innerWidth;
  const height = canvas.clientHeight || window.innerHeight * 0.8;
  renderer.setSize(width, height, false);
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
};
rendererSize();
window.addEventListener("resize", rendererSize);

let speedMultiplier = Number(speedControl?.value ?? 1);

const updateHUD = (value) => {
  const readable = value < 1.4 ? "Standard" : value < 2.1 ? "Sturm" : "Orkan";
  snowLabel.textContent = `${Math.round(value * 100)}%`;
  portalMood.textContent = readable;
};

if (speedControl) {
  updateHUD(speedMultiplier);
  // TODO 3: Reagiere hier auf das "input"-Event des Sliders und rufe updateHUD + die neue speedMultiplier-Belegung auf.
}

if (burstButton) {
  burstButton.addEventListener("click", () => {
    if (window.gsap) {
      window.gsap.to(".stat-card", { scale: 1.05, duration: 0.25, yoyo: true, repeat: 1 });
    }
  });
}

const clock = new THREE.Clock();
const animate = () => {
  const delta = clock.getDelta();

  for (let i = 0; i < count; i += 1) {
    const i3 = i * 3;
    snowPositions[i3 + 1] -= snowSpeeds[i] * speedMultiplier * 9 * delta;
    if (snowPositions[i3 + 1] < -28) {
      snowPositions[i3 + 1] = 24;
    }
  }

  snowGeometry.attributes.position.needsUpdate = true;
  portalRing.rotation.y += 0.1 * delta * speedMultiplier;
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
};

requestAnimationFrame(animate);
