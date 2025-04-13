fetch("https://api.ipify.org?format=json")
  .then(response => response.json())
  .then(data => {
    document.getElementById("ip").textContent = `Your IP address: ${data.ip}`;
  });
