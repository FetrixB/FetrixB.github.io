document.addEventListener("DOMContentLoaded", () => {
  const scrollButtons = document.querySelectorAll("[data-scroll]");
  const chatHistoryEl = document.getElementById("chatHistory");
  const chatForm = document.getElementById("chatForm");
  const messageInput = document.getElementById("messageInput");
  const sendBtn = document.getElementById("sendBtn");
  const clearChatBtn = document.getElementById("clearChatBtn");
  const chatStatus = document.getElementById("chatStatus");
  const template = document.getElementById("chat-bubble-template");
  const saveKeyBtn = document.getElementById("saveKeyBtn");
  const apiKeyInput = document.getElementById("apiKeyInput");
  const keyStatus = document.getElementById("keyStatus");

  const STORAGE_KEYS = {
    api: "tag22_llm_key",
    chat: "tag22_chat_log",
  };

  const chatState = {
    messages: [],
    apiKey: localStorage.getItem(STORAGE_KEYS.api) ?? "",
  };

  const systemPrompt = "Du bist Pixalia, eine freundliche Minecraft-KI-Elfe. Beantworte Fragen extrem positiv, beschreibe Ideen Schritt für Schritt und verbinde alles mit weihnachtlichen Minecraft-Metaphern.";

  function loadPersistedMessages() {
    const cached = localStorage.getItem(STORAGE_KEYS.chat);
    if (cached) {
      try {
        const parsed = JSON.parse(cached);
        if (Array.isArray(parsed)) {
          chatState.messages = parsed;
          return;
        }
      } catch (error) {
        console.warn("Konnte Chat nicht laden", error);
      }
    }

    chatState.messages = [
      {
        role: "assistant",
        content:
          "Hey du, ich bin Pixalia, deine weihnachtliche KI-Elfe! Frag mich nach Navigationsideen, CTA-Texten oder wie du Schneeflocken noch magischer machen kannst.",
      },
    ];
  }

  function persistMessages() {
    localStorage.setItem(STORAGE_KEYS.chat, JSON.stringify(chatState.messages));
  }

  function renderChat() {
    chatHistoryEl.innerHTML = "";
    chatState.messages
      .filter((message) => message.role !== "system")
      .forEach((message) => {
        const bubble = template.content.cloneNode(true);
        const wrapper = bubble.querySelector(".chat-bubble");
        const roleEl = bubble.querySelector(".chat-role");
        const textEl = bubble.querySelector(".chat-text");

        roleEl.textContent = message.role === "user" ? "Du" : "Pixalia";
        wrapper.classList.toggle("user", message.role === "user");
        textEl.textContent = message.content;

        chatHistoryEl.appendChild(bubble);
      });

    chatHistoryEl.scrollTop = chatHistoryEl.scrollHeight;
    persistMessages();
  }

  function setStatus(text, tone = "info") {
    chatStatus.textContent = text;
    chatStatus.dataset.tone = tone;
  }

  function setKeyStatus(text) {
    keyStatus.textContent = text;
  }

  function addMessage(role, content) {
    chatState.messages.push({ role, content });
    renderChat();
  }

  async function requestCompletion() {
    // TODO 3: Implementiere hier den echten fetch()-Aufruf zur gpt-4o-mini API
    // LLMv7 Free Tier: Kein API-Key erforderlich! Nur Content-Type Header nötig
    // Optional: API-Key kann für erweiterte Features hinzugefügt werden
    return "TODO: Echter KI-Output fehlt noch – baue hier deinen fetch()-Aufruf ein!";
  }

  async function handleChatSubmit(event) {
    event.preventDefault();
    const text = messageInput.value.trim();

    if (!text) {
      setStatus("Bitte gib erst eine Frage ein.", "warn");
      return;
    }

    // LLMv7 Free Tier - kein API-Key erforderlich!
    // Die API funktioniert auch ohne Authentifizierung

    sendBtn.disabled = true;
    setStatus("Ich frage gerade die KI-Elfe ...", "info");
    addMessage("user", text);
    messageInput.value = "";

    try {
      const reply = await requestCompletion();
      addMessage("assistant", reply);
      setStatus("Antwort erfolgreich erhalten!", "success");
    } catch (error) {
      console.error(error);
      const fallback =
        "Pixalia hat gerade keinen Kontakt zum Nordpol-Server. Überlege solange selbst: " +
        `${text} → Beginne mit dem wichtigsten Ziel, nutze klare Überschriften und füge anschließend Buttons hinzu.`;
      addMessage("assistant", fallback);
      setStatus("Offline-Ratschlag wurde erstellt.", "warn");
    } finally {
      sendBtn.disabled = false;
    }
  }

  function handleScroll(event) {
    const selector = event.currentTarget.getAttribute("data-scroll");
    const target = document.querySelector(selector);

    if (target) {
      target.scrollIntoView({ behavior: "smooth" });
    }
  }

  function loadParticles() {
    if (!window.tsParticles) {
      return;
    }

    window.tsParticles.load("snow-canvas", {
      background: { color: "transparent" },
      fpsLimit: 60,
      detectRetina: true,
      particles: {
        number: { value: 140, density: { enable: true, area: 800 } },
        color: { value: ["#ffffff", "#7be0ff"] },
        opacity: { value: { min: 0.2, max: 0.8 } },
        size: { value: { min: 1.5, max: 4 } },
        move: {
          enable: true,
          speed: { min: 0.4, max: 1.4 },
          direction: "bottom",
          outModes: { default: "out" },
        },
        shape: { type: "circle" },
      },
      interactivity: {
        events: {
          onHover: { enable: true, mode: "bubble" },
        },
        modes: {
          bubble: { distance: 120, size: 6, duration: 1, opacity: 0.8 },
        },
      },
    });
  }

  function initGsap() {
    if (!window.gsap) {
      return;
    }

    window.gsap.from(".module-card", {
      y: 40,
      opacity: 0,
      duration: 1,
      stagger: 0.15,
      ease: "power2.out",
    });

    window.gsap.from(".feature-card", {
      y: 30,
      opacity: 0,
      duration: 1,
      stagger: 0.1,
      ease: "power2.out",
      delay: 0.2,
    });
  }

  function clearChat() {
    const intro = chatState.messages.find((msg) => msg.role === "assistant");
    chatState.messages = intro ? [intro] : [];
    renderChat();
    setStatus("Chat wurde geleert. Pixalia wartet auf neue Fragen!", "info");
  }

  function initKeyInput() {
    if (chatState.apiKey) {
      setKeyStatus("API-Key gespeichert - Erweiterte Features verfügbar! ✔️");
    } else {
      setKeyStatus("LLMv7 Free Tier aktiv - Kein API-Key erforderlich! 🎉");
    }

    saveKeyBtn.addEventListener("click", () => {
      const value = apiKeyInput.value.trim();
      if (!value) {
        setKeyStatus("Bitte gib deinen API-Key ein.");
        return;
      }

      chatState.apiKey = value;
      localStorage.setItem(STORAGE_KEYS.api, value);
      apiKeyInput.value = "";
      setKeyStatus("API-Key aktualisiert! Die nächste Anfrage nutzt ihn sofort.");
    });
  }

  scrollButtons.forEach((button) => button.addEventListener("click", handleScroll));
  chatForm.addEventListener("submit", handleChatSubmit);
  clearChatBtn.addEventListener("click", clearChat);

  loadPersistedMessages();
  renderChat();
  initKeyInput();
  loadParticles();
  initGsap();
});
