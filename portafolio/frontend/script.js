const projectsList = document.getElementById("projectsList");

function setTextIfExists(id, value) {
    const element = document.getElementById(id);
    if (element && value != null) {
        element.textContent = value;
    }
}

function renderGeneralText(general) {
    setTextIfExists("textoBoldHero", general.textoBoldHero);
    setTextIfExists("textoEpitetoHero", general.textoEpitetoHero);
    setTextIfExists("titleProfile", general.titleProfile);
    setTextIfExists("parrafo1Profile", general.parrafo1Profile);
    setTextIfExists("parrafo2Profile", general.parrafo2Profile);
    setTextIfExists("parrafo3Profile", general.parrafo3Profile);
    setTextIfExists("ContactHeroText", general.ContactHeroText);
    setTextIfExists("ContactEpitetoText", general.ContactEpitetoText);
}

async function loadPortfolio() {
    try {
        const [generalResponse, projectsResponse] = await Promise.all([
            fetch("./general.json"),
            fetch("./projects.json")
        ]);

        if (!generalResponse.ok || !projectsResponse.ok) {
            throw new Error(
                `HTTP error: general=${generalResponse.status}, projects=${projectsResponse.status}`
            );
        }

        const general = await generalResponse.json();
        const projects = await projectsResponse.json();

        renderGeneralText(general);

        projectsList.innerHTML = "";

        projects.forEach((project) => {
            const item = document.createElement("article");
            item.className = "project-item";

            const technologies = Array.isArray(project.technologies)
                ? project.technologies
                : String(project.technologies || "")
                    .split(",")
                    .map((technology) => technology.trim())
                    .filter(Boolean);

            const stackHTML = technologies
                .map((technology) => `<span>${escapeHTML(technology)}</span>`)
                .join("");

            item.innerHTML = `
                <div class="project-meta">
                    <span class="project-number">
                        Project ${String(projects.indexOf(project) + 1).padStart(2, "0")}
                    </span>

                    <div class="project-short-title">
                        ${escapeHTML(project.shortTitle)}
                    </div>

                    <div class="project-category">
                        ${escapeHTML(project.category)}
                    </div>
                </div>

                <div class="project-content">
                    <h3 class="project-main-title">
                        ${escapeHTML(project.mainTitle)}
                    </h3>

                    <p class="project-description">
                        ${escapeHTML(project.description)}
                    </p>

                    <div class="stack">
                        ${stackHTML}
                    </div>

                    <div class="project-actions">
                        <a
                            class="github-repo"
                            href="./template/index.html?projectId=${encodeURIComponent(project.projectId)}"
                        >
                            View Project
                        </a>
                    </div>
                </div>
            `;

            projectsList.appendChild(item);
        });
    } catch (error) {
        console.error("Could not load portfolio data:", error);

        projectsList.innerHTML = `
            <div class="projects-status">
                Projects could not be loaded. Run the site from a local web server
                (for example VS Code Live Server) so that fetch() can read general.json and projects.json.
            </div>
        `;
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

loadPortfolio();
