const API_URL = "https://p3metodologiasagilesml-1.onrender.com";

const MAX_PREDICTION_DATE = "2025-12-30";

const MODEL_CATALOG = {
    LSTM: {
        fullName: "Long Short-Term Memory",
        description: "A recurrent neural network LSTM simple layers that predicts  using historical market data and sequential time windows.",
        features: 5
    },
    DeepLSTM: {
        fullName: "Deep Long Short-Term Memory",
        description: "A multi-layer (Deep) LSTM network designed to learn complex temporal patterns.",
        features: 5
    },
    LSTMCNN: {
        fullName: "Long Short-Term Memory + Convolutional Neural Network",
        description: "A hybrid neural network combining CNN feature extraction with LSTM temporal pattern learning.",
        features: 5
    },
    DeepLSTMIndicators: {
        fullName: "Deep LSTM with Technical Indicators",
        description: "A deep recurrent network that incorporates OHLCV data and technical indicators such as RSI, MACD, ATR, and EMA.",
        features: 10
    }
};

const WEAK_SIGNAL_THRESHOLD = 5; // Distancia máxima al 50%, en puntos porcentuales.

let isPredicting = false;

window.addEventListener("DOMContentLoaded", () => {
    loadModels();

    document.getElementById("startDate").addEventListener("change", resetPredictionResult);
    document.getElementById("modelSelect").addEventListener("change", resetPredictionResult);
});

async function loadModels() {
    const select = document.getElementById("modelSelect");

    try {
        const response = await fetch(`${API_URL}/models`);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();

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
    if (isPredicting) return;

    const startDate = document.getElementById("startDate").value;
    const modelName = document.getElementById("modelSelect").value;
    const resultBox = document.getElementById("resultBox");
    const predictButton = document.getElementById("predictButton");

    if (!startDate || !modelName) {
        showResultMessage("Missing information", "Select a start date and model.");
        return;
    }

    if (startDate > MAX_PREDICTION_DATE) {
        showResultMessage("Invalid date", "Select a date on or before December 30, 2025.");
        return;
    }

    isPredicting = true;
    predictButton.disabled = true;
    predictButton.textContent = "Predicting...";
    resultBox.setAttribute("aria-busy", "true");
    showResultMessage("Loading prediction...", "Please wait while the model runs.");

    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({start_date: startDate, model_name: modelName})
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();

        if (data.error) {
            showResultMessage("Prediction Error", data.error);
            return;
        }

        renderPredictionDashboard(data);
    } catch (error) {
        showResultMessage("Connection Error", error.message || error);
    } finally {
        isPredicting = false;
        predictButton.disabled = false;
        predictButton.textContent = "Predict Movement";
        resultBox.setAttribute("aria-busy", "false");
    }
}

function parseDirection(value) {
    if (value === 1 || value === true) return "up";
    if (value === 0 || value === false) return "down";

    const normalized = String(value ?? "").trim().toLowerCase();
    if (["1", "up", "rise", "rises", "increase", "increased", "bullish", "subirá", "subio", "subió"].includes(normalized)) return "up";
    if (["0", "down", "fall", "falls", "decrease", "decreased", "bearish", "bajará", "bajo", "bajó", "not rise", "no rise"].includes(normalized)) return "down";
    return null;
}

function getModelInfo(modelName, sequenceLength) {
    const family = String(modelName ?? "").split("_")[0].toUpperCase();
    const model = MODEL_CATALOG[family];
    const sessions = Number(sequenceLength);
    const sessionsText = Number.isInteger(sessions) && sessions > 0 ? `${sessions} days` : "days unavailable";
    const featuresText = model?.features ? `${model.features} financial variables` : "Feature count unavailable";
    const description = model
        ? `${model.fullName} (${family}) is ${model.description.charAt(0).toLowerCase()}${model.description.slice(1)}`
        : "A machine learning model used to estimate the direction of TSLA's price movement.";
    return {family, description, sessionsText, featuresText};
}

function renderPredictionDashboard(data) {
    const resultBox = document.getElementById("resultBox");
    const predictedDirection = parseDirection(data.prediction);
    const actualDirection = parseDirection(data.real_movement);
    const modelName = String(data.model ?? "Unknown model");
    const modelInfo = getModelInfo(modelName, data.sequence_length);
    const probabilityValue = Number(data.probability);
    const hasProbability = data.probability !== null && data.probability !== undefined && data.probability !== "" && Number.isFinite(probabilityValue) && probabilityValue >= 0 && probabilityValue <= 1;
    const hasComparison = predictedDirection !== null && actualDirection !== null;
    const isMatch = hasComparison && predictedDirection === actualDirection;
    const directionLabel = predictedDirection === "up" ? "WILL RISE" : predictedDirection === "down" ? "WILL FALL" : String(data.prediction ?? "Unavailable");
    const directionClass = predictedDirection === "up" ? "direction-up" : predictedDirection === "down" ? "direction-down" : "direction-neutral";
    const directionIcon = predictedDirection === "up" ? "↑" : predictedDirection === "down" ? "↓" : "–";
    const actualLabel = actualDirection === "up" ? "ROSE" : actualDirection === "down" ? "FELL" : String(data.real_movement ?? "Unavailable");
    const actualClass = actualDirection === "up" ? "direction-up" : actualDirection === "down" ? "direction-down" : "direction-neutral";
    const actualIcon = actualDirection === "up" ? "↑" : actualDirection === "down" ? "↓" : "–";
    const upProbability = hasProbability ? probabilityValue * 100 : null;
    const downProbability = hasProbability ? 100 - upProbability : null;
    const weakSignal = hasProbability && Math.abs(upProbability - 50) <= WEAK_SIGNAL_THRESHOLD;
    const probabilityText = hasProbability ? `${upProbability.toFixed(2)}%` : "Unavailable";
    const probabilityHtml = hasProbability ? `
        <div class="probability-track" role="img" aria-label="Probability of falling ${downProbability.toFixed(2)} percent; probability of rising ${upProbability.toFixed(2)} percent">
            <span class="probability-down" style="width:${downProbability.toFixed(2)}%"></span>
            <span class="probability-up" style="width:${upProbability.toFixed(2)}%"></span>
        </div>
        <div class="probability-legend"><span>Will fall · ${downProbability.toFixed(2)}%</span><span>Will rise · ${upProbability.toFixed(2)}%</span></div>
        ${weakSignal ? '<p class="probability-note">The probability is close to 50%: this is a weak directional signal.</p>' : '<p class="probability-note">Model output is an estimate, not a guarantee of market movement.</p>'}
    ` : '<p class="probability-note">The API did not provide a valid probability.</p>';

    const comparisonHtml = hasComparison
        ? `<p class="comparison-status ${isMatch ? "match" : "mismatch"}">${isMatch ? "✓ Direction correctly predicted" : "✕ Prediction does not match actual movement"}</p>`
        : '<p class="comparison-status">Actual movement is not available for comparison.</p>';

    resultBox.innerHTML = `
        <div class="dashboard" aria-label="TSLA prediction dashboard">
            <header class="dashboard-heading">
                <h2>TSLA Direction Prediction</h2>
                <p>Neural network analysis</p>
            </header>
            <section class="dashboard-section dashboard-main" aria-label="Prediction direction">
                <div><span class="dashboard-eyebrow">PREDICTION RESULT</span>
                    <p class="dashboard-direction ${directionClass}"><span aria-hidden="true">${directionIcon}</span> ${escapeHTML(directionLabel)}</p></div>
                <div class="dashboard-model"><span>Selected model</span><strong>${escapeHTML(modelName)}</strong></div>
            </section>
            <section class="dashboard-section model-summary" aria-label="Model description">
                <h3>Model description</h3>
                <p>${escapeHTML(modelInfo.description)}</p>
                <div class="model-tags"><span>${escapeHTML(modelInfo.family)}</span><span>${escapeHTML(modelInfo.sessionsText)}</span><span>${escapeHTML(modelInfo.featuresText)}</span></div>
            </section>
            <section class="dashboard-section" aria-label="Estimated probability">
                <div class="dashboard-section-header"><div><h3>Estimated probability</h3><p>Model probability of an upward movement</p></div><strong class="probability-value">${probabilityText}</strong></div>
                ${probabilityHtml}
            </section>
            <section class="dashboard-section" aria-label="Prediction versus reality">
                <div class="comparison-grid">
                    <div class="comparison-card"><span>Prediction</span><strong class="${directionClass}"><span aria-hidden="true">${directionIcon}</span> ${escapeHTML(directionLabel)}</strong></div>
                    <div class="comparison-card"><span>Actual movement</span><strong class="${actualClass}"><span aria-hidden="true">${actualIcon}</span> ${escapeHTML(actualLabel)}</strong></div>
                </div>
                ${comparisonHtml}
            </section>
            <section class="dashboard-section history-panel" aria-label="Historical window analyzed">
                <h3>Historical window analyzed</h3>
                <div class="history-grid">
                    <div><span>Start date</span><strong>${escapeHTML(formatPredictionDate(data.window_start))}</strong></div><div><span>End date</span><strong>${escapeHTML(formatPredictionDate(data.window_end))}</strong></div></div>
                <div class="history-sessions"><span>Model window</span><strong>${escapeHTML(modelInfo.sessionsText)}</strong></div>
            </section>
        </div>
    `;
}

function formatPredictionDate(value) {
    if (value === null || value === undefined || value === "") return "Unavailable";
    const text = String(value);
    const match = text.match(/^(\d{4})-(\d{2})-(\d{2})/);
    if (!match) return text;
    const date = new Date(Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3])));
    if (Number.isNaN(date.getTime())) return text;
    return new Intl.DateTimeFormat("en-GB", {day: "2-digit", month: "short", year: "numeric", timeZone: "UTC"}).format(date);
}

function resetPredictionResult() {
    if (isPredicting) return;
    showResultMessage("Prediction result", "Select a date and model, then run the prediction.");
}

function showResultMessage(title, message) {
    document.getElementById("resultBox").innerHTML = `<h2>${escapeHTML(title)}</h2><p>${escapeHTML(message)}</p>`;
}

function escapeHTML(value = "") {
    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}
