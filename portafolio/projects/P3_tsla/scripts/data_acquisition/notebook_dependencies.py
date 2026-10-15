import sys
import tomllib
import subprocess
import importlib.metadata as metadata
from pathlib import Path
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.version import Version
from packaging.utils import canonicalize_name


notebookPackages = {
    "matplotlib",
    "yfinance",
    "scikit-learn",
    "mlflow",
    "keras",
    "joblib"
}

requiredExcludedPackages = {
    "numpy",
    "pandas",
    "python",
    "tensorflow-cpu"
}

excludedPackages = requiredExcludedPackages | {
    "pip",
    "setuptools",
    "setuptools-scm",
    "wheel",
    "tomllib",
    "pathlib",
    "sys",
    "os",
    "subprocess",
    "importlib",
    "json",
    "datetime",
    "time",
    "math",
    "collections"
}


def getInstalledVersion(packageName):
    if canonicalize_name(packageName) == "python":
        return Version(".".join(map(str, sys.version_info[:3])))

    try:
        return Version(metadata.version(packageName))
    except metadata.PackageNotFoundError:
        return None


def compareVersions(installedVersion, specifier):
    if installedVersion is None:
        return "NO INSTALADO"

    if specifier is None or not str(specifier):
        return "NO DEFINIDO"

    if installedVersion in specifier:
        return "COINCIDE"

    exactVersions = [
        Version(spec.version)
        for spec in specifier
        if spec.operator == "==" and "*" not in spec.version
    ]

    if exactVersions:
        referenceVersion = exactVersions[0]
        return "SUPERIOR" if installedVersion > referenceVersion else "INFERIOR"

    lowerBounds = [
        (Version(spec.version), spec.operator)
        for spec in specifier
        if spec.operator in (">=", ">")
    ]

    upperBounds = [
        (Version(spec.version), spec.operator)
        for spec in specifier
        if spec.operator in ("<=", "<")
    ]

    if lowerBounds:
        lowerVersion, lowerOperator = max(lowerBounds, key=lambda item: (item[0], item[1] == ">"))

        if installedVersion < lowerVersion or (installedVersion == lowerVersion and lowerOperator == ">"):
            return "INFERIOR"

    if upperBounds:
        upperVersion, upperOperator = min(upperBounds, key=lambda item: (item[0], item[1] == "<"))

        if installedVersion > upperVersion or (installedVersion == upperVersion and upperOperator == "<"):
            return "SUPERIOR"

    return "NO COINCIDE"


def installDependency(requirement):
    packageName = requirement.name
    installedVersion = getInstalledVersion(packageName)

    if installedVersion is not None and installedVersion in requirement.specifier:
        status = "YA INSTALADO"

    else:
        print(f"  Instalando {requirement}...", flush=True)
        # Mostrar salida de pip durante la instalación
        installResult = subprocess.run([sys.executable, "-m", "pip", "install", str(requirement)], check=False)

        installedVersion = getInstalledVersion(packageName)

        if installResult.returncode == 0 and installedVersion is not None and installedVersion in requirement.specifier:
            status = "INSTALADO"
        else:
            status = "ERROR"

    print(f"  {status}: {packageName} {installedVersion or 'No instalado'}", flush=True)

    return {
        "Librería": packageName,
        "Versión requerida": str(requirement.specifier) or "No definida",
        "Versión instalada": str(installedVersion) if installedVersion is not None else "No instalado",
        "Estado": status
    }


def verifyExcludedDependency(packageName, projectDependencies, pythonRequired):
    # Obtener requisitos sin instalar ni modificar directamente la librería
    if packageName == "python":
        requiredVersion = pythonRequired
        specifier = SpecifierSet(pythonRequired) if pythonRequired else None

    else:
        requirement = projectDependencies.get(packageName)
        requiredVersion = str(requirement.specifier) if requirement else ""
        specifier = requirement.specifier if requirement else None

    installedVersion = getInstalledVersion(packageName)
    status = compareVersions(installedVersion, specifier)

    return {
        "Librería": packageName,
        "Versión requerida": requiredVersion or "No definida",
        "Versión instalada": str(installedVersion) if installedVersion is not None else "No instalado",
        "Estado": status
    }

def printDependencyReport(title, results):
    columns = ["Librería", "Versión requerida", "Versión instalada", "Estado"]

    print(f"\n{title}\n")

    if not results:
        print("No hay dependencias para mostrar.")
        return

    widths = [
        max(len(column), *(len(str(row[column])) for row in results))
        for column in columns
    ]

    print(" | ".join(column.ljust(width) for column, width in zip(columns, widths)))
    print("-+-".join("-" * width for width in widths))

    for result in results:
        print(" | ".join(str(result[column]).ljust(width) for column, width in zip(columns, widths)))


def showDependencyReport(dependencyReport):
    installedResults = dependencyReport["installedDependencies"]
    excludedResults = dependencyReport["excludedDependencies"]
    missingPackages = dependencyReport.get("missingDependencies", [])

    printDependencyReport("REPORTE DE INSTALACIÓN", installedResults)
    printDependencyReport("REPORTE DE LIBRERÍAS EXCLUIDAS REQUERIDAS", excludedResults)

    # Calcular estadísticas de instalación
    installed = sum(result["Estado"] == "INSTALADO" for result in installedResults)
    alreadyInstalled = sum(result["Estado"] == "YA INSTALADO" for result in installedResults)
    errors = sum(result["Estado"] == "ERROR" for result in installedResults)

    excludedMatched = sum(result["Estado"] == "COINCIDE" for result in excludedResults)
    excludedNotMatched = len(excludedResults) - excludedMatched

    print("\nRESUMEN FINAL\n")
    print(f"Proyecto: {dependencyReport.get('projectName', 'Sin nombre')}")
    print(f"Python: {dependencyReport.get('pythonVersion', 'Desconocida')}")
    print(f"Dependencias seleccionadas: {len(installedResults)}")
    print(f"Instaladas: {installed}")
    print(f"Ya instaladas: {alreadyInstalled}")
    print(f"Errores: {errors}")
    print(f"Excluidas requeridas que cumplen: {excludedMatched}/{len(excludedResults)}")
    print(f"Excluidas que no cumplen o faltan: {excludedNotMatched}")

    if missingPackages:
        print(f"Dependencias no declaradas: {', '.join(missingPackages)}")

    if errors == 0 and not missingPackages:
        print("\nInstalación de dependencias seleccionadas completada.")
    else:
        print("\nExisten dependencias pendientes de revisar.")


def installProjectDependencies(pyprojectPath="./pyproject.toml"):
    # Leer configuración del proyecto
    projectPath = Path(pyprojectPath)

    if not projectPath.is_file():
        raise FileNotFoundError(f"No se encontró: {projectPath.resolve()}")

    with projectPath.open("rb") as file:
        config = tomllib.load(file)

    project = config["project"]
    pythonRequired = project.get("requires-python", "")
    pythonVersion = getInstalledVersion("python")

    if pythonRequired and pythonVersion not in SpecifierSet(pythonRequired):
        raise RuntimeError(f"Python {pythonVersion} no cumple {pythonRequired}")

    # Obtener dependencias declaradas en pyproject.toml
    projectDependencies = {
        canonicalize_name(requirement.name): requirement
        for dependency in project.get("dependencies", [])
        for requirement in [Requirement(dependency)]
    }

    selectedPackages = {canonicalize_name(package) for package in notebookPackages}
    excludedNames = {canonicalize_name(package) for package in excludedPackages}
    selectedPackages -= excludedNames

    missingPackages = selectedPackages - projectDependencies.keys()

    selectedDependencies = [
        requirement
        for packageName, requirement in projectDependencies.items()
        if packageName in selectedPackages
    ]

    print(f"Proyecto: {project.get('name', 'Sin nombre')}")
    print(f"Python: {pythonVersion}")
    print(f"Dependencias seleccionadas: {len(selectedDependencies)}", flush=True)

    if missingPackages:
        print(f"No declaradas: {', '.join(sorted(missingPackages))}", flush=True)

    installedResults = []

    for index, requirement in enumerate(selectedDependencies, start=1):
        print(f"\n[{index}/{len(selectedDependencies)}] Verificando {requirement.name}...", flush=True)
        installedResults.append(installDependency(requirement))

    # Verificar librerías excluidas requeridas
    excludedResults = [
        verifyExcludedDependency(packageName, projectDependencies, pythonRequired)
        for packageName in sorted(requiredExcludedPackages)
    ]

    # Devolver los resultados sin imprimir los reportes
    return {
        "projectName": project.get("name", "Sin nombre"),
        "pythonVersion": str(pythonVersion),
        "installedDependencies": installedResults,
        "excludedDependencies": excludedResults,
        "missingDependencies": sorted(missingPackages)
    }

if __name__ == "__main__":
    installProjectDependencies()
    