const projectsList = document.getElementById("projectsList");

async function loadProjects() {
    try {
        const response = await fetch("./projects.json");

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const projects = await response.json();

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
                            href="./templateIndex.html?projectIndex=${projects.indexOf(project)}"
                        >
                            View Project
                        </a>
                    </div>
                </div>
            `;

            projectsList.appendChild(item);
        });
    } catch (error) {
        console.error("Could not load projects.json:", error);

        projectsList.innerHTML = `
            <div class="projects-status">
                Projects could not be loaded. Run the site from a local web server
                (for example VS Code Live Server) so that fetch() can read projects.json.
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

loadProjects();
