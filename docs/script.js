const API_BASE =
  "https://quick-poll-backend-f2dubwevafh8gsfz.centralindia-01.azurewebsites.net";

async function loadPoll() {
  const res = await fetch(`${API_BASE}/poll`);
  const data = await res.json();

  document.getElementById("question").innerText = data.question;

  const optionsDiv = document.getElementById("options");
  optionsDiv.innerHTML = "";

  Object.keys(data.options).forEach(option => {
    const btn = document.createElement("button");
    btn.innerText = option;
    btn.onclick = () => vote(option);
    optionsDiv.appendChild(btn);
  });
}

async function vote(option) {
  await fetch(`${API_BASE}/vote`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ option })
  });
}

function updateResults(results) {
  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "<h3>Live Results</h3>";

  Object.entries(results).forEach(([option, count]) => {
    const row = document.createElement("div");
    row.className = "result-row";
    row.innerHTML = `<span>${option}</span><strong>${count}</strong>`;
    resultsDiv.appendChild(row);
  });
}

// WebSocket connection
const ws = new WebSocket(
  "wss://quick-poll-backend-f2dubwevafh8gsfz.centralindia-01.azurewebsites.net/ws"
);

ws.onmessage = event => {
  const results = JSON.parse(event.data);
  updateResults(results);
};

loadPoll();

async function resetPoll() {
    await fetch(`${API_BASE}/reset`, {
        method: "POST"
    });
}