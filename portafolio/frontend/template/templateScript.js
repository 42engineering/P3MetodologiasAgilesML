const params = new URLSearchParams(window.location.search);
const requestedProjectId = (params.get("projectId") || "").trim();
const requestedProjectIndex = Number.parseInt(params.get("projectIndex"), 10);

window.addEventListener("DOMContentLoaded", initializeTemplate);


function getElement(id) {
    return document.getElementById(id);
}

function setTextIfExists(id, value) {
    const element = getElement(id);
    if (element) {
        element.textContent = value ?? "";
    }
}

async function initializeTemplate() {
    try {
        const [generalResponse, projectsResponse] = await Promise.all([
            fetch("../general.json"),
            fetch("../projects.json")
        ]);

        if (!generalResponse.ok || !projectsResponse.ok) {
            throw new Error("Could not load template data.");
        }

        const general = await generalResponse.json();
        const projects = await projectsResponse.json();

        let project = null;
        let resolvedProjectIndex = -1;

        if (requestedProjectId) {
            resolvedProjectIndex = projects.findIndex(
                (item) => String(item.projectId || "").toUpperCase() === requestedProjectId.toUpperCase()
            );
        } else if (Number.isInteger(requestedProjectIndex) && requestedProjectIndex >= 0) {
            resolvedProjectIndex = requestedProjectIndex;
        } else {
            resolvedProjectIndex = 0;
        }

        project = projects[resolvedProjectIndex];

        if (!project) {
            throw new Error(
                requestedProjectId
                    ? `Project ID ${requestedProjectId} does not exist.`
                    : `Project index ${resolvedProjectIndex} does not exist.`
            );
        }

        renderProject(general, project, resolvedProjectIndex);
    } catch (error) {
        console.error(error);
        setTextIfExists("projectMainTitle", "Project could not be loaded");
        setTextIfExists("projectCategory", error.message);
    }
}

function renderProject(general, project, resolvedProjectIndex) {
    setTextIfExists("logoText", general.logoTex || "MyPortafolio");
    setTextIfExists("footerText", general.footerText || "© 2026 Portfolio");
    setTextIfExists(
        "projectEyebrow",
        `Portfolio / ${project.projectId || `Project ${String(resolvedProjectIndex + 1).padStart(2, "0")}`}: ${project.shortTitle || ""}`
    );
    setTextIfExists("projectMainTitle", project.mainTitle || "");
    setTextIfExists("projectCategory", project.category || "");
    setTextIfExists("overviewShortTitle", project.shortTitle || "Project");
    setTextIfExists("projectDescription", project.description || "");
    setTextIfExists("modelInterpretationText", project.modelInterpretation || "");

    document.title = `${project.shortTitle || "Project"} | Portfolio`;

    renderPrediction(project.prediction || {});
    renderGraphSection("interpretationGraphs", project.interpretationGraphs || {});
    renderGraphSection("trainingGraphs", project.trainingGraphs || {});
    renderGraphSection("mainGraphs", project.mainGraphs || {});
}

function renderPrediction(prediction) {
    const visual = getElement("predictionVisual");
    const text = getElement("predictionText");
    const button = getElement("launchPredictionButton");

    if (!visual || !text || !button) return;

    const layout = prediction.layout || {};
    const enabled = layout.enabled !== false;
    const size = normalizeSize(layout.size || "100%");

    visual.innerHTML = "";
    visual.style.display = enabled ? "flex" : "none";
    visual.style.width = size;
    visual.style.maxWidth = size;

    if (enabled) {
        if (prediction.imagePath) {
            const image = document.createElement("img");
            image.src = prediction.imagePath;
            image.alt = prediction.imageAlt || "Prediction preview";
            image.loading = "lazy";
            visual.appendChild(image);
        } else {
            const placeholder = document.createElement("div");
            placeholder.className = "prediction-placeholder";
            placeholder.textContent = "Prediction image — image path pending";
            visual.appendChild(placeholder);
        }
    }

    text.textContent = prediction.text || "";
    button.textContent = prediction.buttonText || "Launch Prediction App";

    if (prediction.launchUrl) {
        button.href = prediction.launchUrl;
        button.classList.remove("is-disabled");
        button.removeAttribute("aria-disabled");
    } else {
        button.href = "#";
        button.classList.add("is-disabled");
        button.setAttribute("aria-disabled", "true");
    }
}

function renderGraphSection(containerId, sectionConfig) {
    const container = getElement(containerId);
    if (!container) return;

    container.innerHTML = "";

    const allGraphs = Array.isArray(sectionConfig.graphs) ? sectionConfig.graphs : [];
    const visibleGraphs = allGraphs.filter(graph => graph.enabled !== false);
    const section = container.closest(".project-section");

    if (!visibleGraphs.length) {
        section?.classList.add("section-is-off");
        return;
    }

    section?.classList.remove("section-is-off");

    let i = 0;

    while (i < visibleGraphs.length) {
        const firstGraph = visibleGraphs[i];
        const perRow = normalizeImagesPerRow(firstGraph.numberImagesPerRow);

        const row = document.createElement("div");
        row.className = "media-row";
        if (perRow === 1) {
            row.classList.add("media-row-single");
        }
        row.style.setProperty("--images-per-row", perRow);

        for (let slot = 0; slot < perRow && i < visibleGraphs.length; slot += 1, i += 1) {
            const graph = visibleGraphs[i];

            // If the next graph declares a different row count, start a new row.
            if (slot > 0 && normalizeImagesPerRow(graph.numberImagesPerRow) !== perRow) {
                break;
            }

            row.appendChild(createGraphCard(graph));
        }

        container.appendChild(row);
    }
}

function createGraphCard(graph) {
    const card = document.createElement("article");
    card.className = "graph-card";

    const size = normalizeSize(graph.size || "100%");
    card.style.width = size;
    card.style.maxWidth = size;

    const label = graph.alt || "Graph";

    if (graph.path) {
        const image = document.createElement("img");
        image.src = graph.path;
        image.alt = label;
        image.loading = "lazy";
        card.appendChild(image);
    } else {
        const placeholder = document.createElement("div");
        placeholder.className = "graph-placeholder";
        placeholder.textContent = `${label} — image path pending`;
        card.appendChild(placeholder);
    }

    if (graph.text) {
        const paragraph = document.createElement("p");
        paragraph.textContent = graph.text;
        card.appendChild(paragraph);
    }

    return card;
}

function normalizeImagesPerRow(value) {
    const number = Number.parseInt(value, 10);
    return [1, 2, 3, 4].includes(number) ? number : 1;
}

function normalizeSize(value) {
    const allowed = new Set(["25%", "33.333%", "50%", "66.667%", "75%", "100%"]);
    const size = String(value || "100%").trim();
    return allowed.has(size) ? size : "100%";
}
