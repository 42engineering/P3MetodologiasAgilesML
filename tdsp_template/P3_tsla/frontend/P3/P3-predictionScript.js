const API_URL = window.location.origin;
// const API_URL = "https://p3metodologiasagilesml-1.onrender.com";
// const API_URL = "https://p3metodologiasagilesml.onrender.com";

window.addEventListener("DOMContentLoaded", loadModels);

async function loadModels() {
    const select = document.getElementById("modelSelect");

    try {
        const response = await fetch(`${API_URL}/models`);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || `HTTP ${response.status}`);
        }

        select.innerHTML = "";
        data.models.forEach((model) => {
            const option = document.createElement("option");
            option.value = model;
            option.textContent = model;
            select.appendChild(option);
        });
    } catch (error) {
        console.error(error);
        select.innerHTML = '<option value="">Models unavailable</option>';
    }
}

async function predictMovement() {
    const startDate = document.getElementById("startDate").value;
    const modelName = document.getElementById("modelSelect").value;
    const resultBox = document.getElementById("resultBox");

    if (!startDate || !modelName) {
        resultBox.innerHTML = "<h2>Missing information</h2><p>Select a start date and model.</p>";
        return;
    }

    resultBox.innerHTML = "<h2>Loading prediction...</h2>";

    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({start_date: startDate, model_name: modelName})
        });

        const data = await response.json();

        if (!response.ok || data.error) {
            resultBox.innerHTML = `<h2>Prediction Error</h2><p>${escapeHTML(data.error || `HTTP ${response.status}`)}</p>`;
            return;
        }

        resultBox.innerHTML = `
            <h2>${escapeHTML(data.prediction)}</h2>
            <p><b>Model:</b> ${escapeHTML(data.model)}</p>
            <p><b>Probability:</b> ${(Number(data.probability) * 100).toFixed(2)}%</p>
            <p><b>Real Movement:</b> ${escapeHTML(data.real_movement)}</p>
            <p><b>Window Start:</b> ${escapeHTML(data.window_start)}</p>
            <p><b>Window End:</b> ${escapeHTML(data.window_end)}</p>
        `;
    } catch (error) {
        resultBox.innerHTML = `<h2>Connection Error</h2><p>${escapeHTML(error.message || error)}</p>`;
    }
}

function escapeHTML(value = "") {
    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}
