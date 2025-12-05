import * as THREE from "https://unpkg.com/three@0.160.0/build/three.module.js";

// Kleine Hilfsfunktion für DOM-Zugriffe
const $ = (selector) => document.querySelector(selector);

const canvas = document.getElementById("snowPortal");
const snowLabel = document.querySelector("[data-snow-count]");
const portalMood = document.getElementById("portalMood");
const speedControl = document.getElementById("speedControl");
const burstButton = document.getElementById("burstButton");
const flakeCountLabel = document.getElementById("flakeCount");

const renderer = new THREE.WebGLRenderer({
  canvas,
  alpha: true,
  antialias: true,
});
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x030712, 0.015);
scene.background = null;

const camera = new THREE.PerspectiveCamera(60, 1, 0.1, 200);
camera.position.set(0, 10, 45);

const snowSettings = {
  count: 1600,
  spread: 70,
};

const snowGeometry = new THREE.BufferGeometry();
const snowPositions = new Float32Array(snowSettings.count * 3);
const snowVelocities = new Float32Array(snowSettings.count);

for (let i = 0; i < snowSettings.count; i += 1) {
  const i3 = i * 3;
  snowPositions[i3] = (Math.random() - 0.5) * snowSettings.spread;
  snowPositions[i3 + 1] = Math.random() * 40 - 15;
  snowPositions[i3 + 2] = (Math.random() - 0.5) * snowSettings.spread;
  snowVelocities[i] = 0.12 + Math.random() * 0.25;
}

snowGeometry.setAttribute("position", new THREE.BufferAttribute(snowPositions, 3));

const snowMaterial = new THREE.PointsMaterial({
  color: new THREE.Color(0xe0f2fe),
  size: 0.8,
  transparent: true,
  opacity: 0.85,
  depthWrite: false,
  blending: THREE.AdditiveBlending,
  sizeAttenuation: true,
});

const snowPoints = new THREE.Points(snowGeometry, snowMaterial);
scene.add(snowPoints);

// Portal-Objekte (Torus + Gate-Fläche)
const portalTorus = new THREE.Mesh(
  new THREE.TorusGeometry(12, 2.6, 32, 200),
  new THREE.MeshStandardMaterial({
    color: 0x38bdf8,
    emissive: 0x164e63,
    metalness: 0.4,
    roughness: 0.2,
    emissiveIntensity: 1.2,
  })
);
portalTorus.position.set(0, 5, 0);
scene.add(portalTorus);

const portalGate = new THREE.Mesh(
  new THREE.PlaneGeometry(24, 24),
  new THREE.MeshBasicMaterial({
    color: 0x0ea5e9,
    side: THREE.DoubleSide,
    transparent: true,
    opacity: 0.35,
  })
);
portalGate.position.copy(portalTorus.position);
portalGate.rotation.y = Math.PI / 2;
scene.add(portalGate);

// Beleuchtung für Tiefe
scene.add(new THREE.AmbientLight(0xb3c5ff, 0.35));
const rimLight = new THREE.PointLight(0x38bdf8, 2.4, 120);
rimLight.position.set(20, 20, 15);
scene.add(rimLight);

const warmLight = new THREE.PointLight(0xffedd5, 1.6, 100);
warmLight.position.set(-25, 8, -15);
scene.add(warmLight);

const clock = new THREE.Clock();
let time = 0;
let speedMultiplier = Number(speedControl?.value ?? 1);

const updateRendererSize = () => {
  const { clientWidth, clientHeight } = canvas;
  const width = clientWidth || window.innerWidth;
  const height = clientHeight || window.innerHeight * 0.8;
  renderer.setSize(width, height, false);
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
};

updateRendererSize();
window.addEventListener("resize", updateRendererSize);

const animate = () => {
  const delta = clock.getDelta();
  time += delta;

  for (let i = 0; i < snowSettings.count; i += 1) {
    const i3 = i * 3;
    snowPositions[i3 + 1] -= snowVelocities[i] * speedMultiplier * 10 * delta;
    snowPositions[i3] += Math.sin(time + i) * 0.03 * speedMultiplier;
    snowPositions[i3 + 2] += Math.cos(time * 0.5 + i) * 0.01;

    if (snowPositions[i3 + 1] < -30) {
      snowPositions[i3 + 1] = 25;
    }
  }

  snowGeometry.attributes.position.needsUpdate = true;

  portalTorus.rotation.y += 0.15 * delta * speedMultiplier;
  portalTorus.rotation.x = Math.sin(time * 0.4) * 0.35;
  portalGate.material.opacity = 0.3 + Math.sin(time * 0.8) * 0.15;

  renderer.render(scene, camera);
  requestAnimationFrame(animate);
};

requestAnimationFrame(animate);

// DOM-Interaktionen für Control-Panel
const describeSpeed = (value) => {
  if (value < 1.4) return "Aurora-Modus";
  if (value < 2.1) return "Schneesturm";
  return "Hyperblizzard";
};

const handleSpeedChange = (value) => {
  speedMultiplier = Number(value);
  snowLabel.textContent = `${Math.round(speedMultiplier * 100)}%`;
  portalMood.textContent = describeSpeed(speedMultiplier);
};

if (speedControl) {
  handleSpeedChange(speedControl.value);
  speedControl.addEventListener("input", (event) => {
    handleSpeedChange(event.target.value);
  });
}

if (flakeCountLabel) {
  flakeCountLabel.textContent = snowSettings.count.toString();
}

if (burstButton) {
  burstButton.addEventListener("click", () => {
    if (window.gsap) {
      window.gsap.fromTo(
        snowMaterial,
        { size: 0.8 },
        { size: 1.5, duration: 0.5, yoyo: true, repeat: 1, ease: "power2.out" }
      );
      window.gsap.to(".stat-card", { scale: 1.04, duration: 0.3, yoyo: true, repeat: 1 });
    }
  });
}

// Einstiegseffekte für Texte und Karten
if (window.gsap) {
  const tl = window.gsap.timeline({ defaults: { duration: 0.9, ease: "power3.out" } });
  tl.from(".hero h1", { opacity: 0, y: 40 })
    .from(".hero p", { opacity: 0, y: 20, stagger: 0.1 }, "<")
    .from(".glow-button", { opacity: 0, y: 20 }, "-=0.2")
    .from(".stat-card", { opacity: 0, y: 35, stagger: 0.15 }, "-=0.1");
}
