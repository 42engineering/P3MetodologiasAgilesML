import json
from pathlib import Path
from urllib.parse import urlparse


scriptDir = Path(__file__).resolve().parent
jsonPath = scriptDir.parent / "projects.json"
readmePath = scriptDir / "README.md"

projectDirectories = {
    "P1": "P1",
    "P2": "P2",
    "P3": "P3_tsla"
}


def getNotebookFileName(notebookLink):
    parsedUrl = urlparse(notebookLink)

    return Path(parsedUrl.path).name


def getNotebookRelativePath(project):
    projectId = project["projectId"]
    notebookLink = project.get("notebookLink", "")

    if not notebookLink:
        return None

    projectDirectory = projectDirectories.get(projectId, projectId)
    notebookFileName = getNotebookFileName(notebookLink)

    return Path("../projects") / projectDirectory / "notebooks" / notebookFileName


def generateReadme(projects):
    lines = [
        "# Machine Learning Portfolio",
        "",
        "Collection of Machine Learning and Deep Learning projects.",
        ""
    ]

    for project in projects:
        mainTitle = project.get("mainTitle", "Untitled Project")
        category = project.get("category", "")
        description = project.get("description", "")
        notebookEnabled = project.get("notebookLinkEnabled", True)

        lines.append(f"## {mainTitle}")
        lines.append("")
        lines.append(f"**Category:** {category}")
        lines.append("")
        lines.append(description)
        lines.append("")

        if notebookEnabled:
            notebookPath = getNotebookRelativePath(project)

            if notebookPath:
                notebookLink = notebookPath.as_posix()
                lines.append(f"[View Notebook]({notebookLink})")
                lines.append("")

    return "\n".join(lines)


def main():
    with open(jsonPath, "r", encoding="utf-8") as file:
        projects = json.load(file)

    if not isinstance(projects, list):
        raise ValueError("projects.json must contain a list of projects.")

    readmeContent = generateReadme(projects)

    with open(readmePath, "w", encoding="utf-8") as file:
        file.write(readmeContent)

    print(f"README generated: {readmePath}")


if __name__ == "__main__":
    main()