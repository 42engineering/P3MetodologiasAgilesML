import sys
import tomllib
import subprocess
import importlib.metadata as metadata
from pathlib import Path
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.version import Version
from packaging.utils import canonicalize_name

def installProjectDependencies(pyprojectPath="./pyproject.toml"):

    # Librerías utilizadas en el notebook que deben instalarse
    notebookPackages = {
        "matplotlib",
        "yfinance",
        "scikit-learn",
        "mlflow",
        "keras",
        "joblib"
    }

    # Librerías excluidas que requieren verificación de versiones
    requeridasNotbookExcluded = {
        "numpy",
        "pandas",
        "python",
        "tensorflow-cpu"
    }

    # Librerías y componentes que no deben instalarse
    excludedPackages = {
        "numpy",
        "pandas",
        "python",
        "tensorflow-cpu",
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

    # Leer configuración del proyecto
    projectPath = Path(pyprojectPath)

    if not projectPath.is_file():
        raise FileNotFoundError(f"No se encontró: {projectPath.resolve()}")

    with projectPath.open("rb") as file:
        config = tomllib.load(file)

    project = config["project"]
    dependencies = project.get("dependencies", [])
    pythonRequired = project.get("requires-python", "")

    # Validar versión de Python
    pythonVersion = Version(".".join(map(str, sys.version_info[:3])))

    if pythonRequired and pythonVersion not in SpecifierSet(pythonRequired):
        raise RuntimeError(f"Python {pythonVersion} no cumple {pythonRequired}")

    # Normalizar nombres de librerías
    notebookPackages = {canonicalize_name(package) for package in notebookPackages}
    excludedPackages = {canonicalize_name(package) for package in excludedPackages}
    requeridasNotbookExcluded = {canonicalize_name(package) for package in requeridasNotbookExcluded}

    # Identificar dependencias declaradas
    projectDependencies = {
        canonicalize_name(Requirement(dependency).name): Requirement(dependency)
        for dependency in dependencies
    }

    selectedDependencies = []
    omittedDependencies = []

    for dependency in dependencies:

        requirement = Requirement(dependency)
        packageName = canonicalize_name(requirement.name)

        if packageName in excludedPackages:
            omittedDependencies.append(requirement.name)

        elif packageName in notebookPackages:
            selectedDependencies.append(dependency)

    selectedPackages = {canonicalize_name(Requirement(dependency).name) for dependency in selectedDependencies}
    missingPackages = notebookPackages - selectedPackages - excludedPackages

    print(f"Proyecto: {project.get('name', 'Sin nombre')}")
    print(f"Python: {pythonVersion}")
    print(f"Dependencias seleccionadas: {len(selectedDependencies)}", flush=True)

    if missingPackages:
        print(f"No declaradas: {', '.join(sorted(missingPackages))}", flush=True)


    results = []
    total = len(selectedDependencies)

    for index, dependency in enumerate(selectedDependencies, start=1):

        requirement = Requirement(dependency)
        packageName = requirement.name

        print(f"\n[{index}/{total}] Verificando {dependency}...", flush=True)

        # Comprobar si ya está instalada la versión requerida
        try:
            installedVersion = metadata.version(packageName)
            matches = Version(installedVersion) in requirement.specifier
        except metadata.PackageNotFoundError:
            installedVersion = "No instalado"
            matches = False

        if matches:
            status = "YA INSTALADO"
            print(f"  {status}: {packageName} {installedVersion}", flush=True)

        else:
            print(f"  Instalando {dependency}...", flush=True)

            installResult = subprocess.run(
                [sys.executable, "-m", "pip", "install", dependency],
                check=False
            )

            try:
                installedVersion = metadata.version(packageName)
                matches = Version(installedVersion) in requirement.specifier
            except metadata.PackageNotFoundError:
                installedVersion = "No instalado"
                matches = False

            if installResult.returncode == 0 and matches:
                status = "INSTALADO"
            else:
                status = "ERROR"

            print(f"  {status}: {packageName} {installedVersion}", flush=True)

        results.append({
            "Librería": packageName,
            "Versión requerida": str(requirement.specifier),
            "Versión instalada": installedVersion,
            "Estado": status
        })

    # Mostrar reporte de instalación sin Pandas
    columns = ["Librería", "Versión requerida", "Versión instalada", "Estado"]

    print("\nREPORTE DE INSTALACIÓN\n")

    if results:
        widths = [max(len(column), *(len(str(row[column])) for row in results)) for column in columns]

        print(" | ".join(column.ljust(width) for column, width in zip(columns, widths)))
        print("-+-".join("-" * width for width in widths))

        for result in results:
            print(" | ".join(str(result[column]).ljust(width) for column, width in zip(columns, widths)))

    excludedResults = []

    for packageName in sorted(requeridasNotbookExcluded):

        if packageName == "python":
            installedVersion = str(pythonVersion)
            requiredVersion = pythonRequired
            specifier = SpecifierSet(pythonRequired) if pythonRequired else None

        else:
            requirement = projectDependencies.get(packageName)
            requiredVersion = str(requirement.specifier) if requirement else ""
            specifier = requirement.specifier if requirement else None

            try:
                installedVersion = metadata.version(packageName)
            except metadata.PackageNotFoundError:
                installedVersion = "No instalado"

        if not requiredVersion:
            status = "NO DEFINIDO"

        elif installedVersion == "No instalado":
            status = "NO INSTALADO"

        else:
            currentVersion = Version(installedVersion)

            if currentVersion in specifier:
                status = "COINCIDE"

            else:
                lowerBounds = [
                    spec.version for spec in specifier
                    if spec.operator in (">=", ">")
                ]

                upperBounds = [
                    spec.version for spec in specifier
                    if spec.operator in ("<=", "<")
                ]

                exactVersions = [
                    spec.version for spec in specifier
                    if spec.operator in ("==", "===") and "*" not in spec.version
                ]

                if exactVersions:
                    referenceVersion = Version(exactVersions[0])

                    if currentVersion > referenceVersion:
                        status = "SUPERIOR"
                    else:
                        status = "INFERIOR"

                elif lowerBounds and currentVersion < max(Version(version) for version in lowerBounds):
                    status = "INFERIOR"

                elif upperBounds and currentVersion >= min(Version(version) for version in upperBounds):
                    status = "SUPERIOR"

                else:
                    status = "NO COINCIDE"

        excludedResults.append({
            "Librería": packageName,
            "Versión requerida": requiredVersion or "No definida",
            "Versión instalada": installedVersion,
            "Estado": status
        })

    # Mostrar reporte de librerías excluidas
    print("\nREPORTE DE LIBRERÍAS EXCLUIDAS REQUERIDAS\n")

    widths = [max(len(column), *(len(str(row[column])) for row in excludedResults)) for column in columns]

    print(" | ".join(column.ljust(width) for column, width in zip(columns, widths)))
    print("-+-".join("-" * width for width in widths))

    for result in excludedResults:
        print(" | ".join(str(result[column]).ljust(width) for column, width in zip(columns, widths)))

    # Resumen de instalación y verificación
    installed = sum(result["Estado"] == "INSTALADO" for result in results)
    alreadyInstalled = sum(result["Estado"] == "YA INSTALADO" for result in results)
    errors = sum(result["Estado"] == "ERROR" for result in results)
    excludedMatched = sum(result["Estado"] == "COINCIDE" for result in excludedResults)

    print("\nRESUMEN FINAL\n")
    print(f"Dependencias seleccionadas: {total}")
    print(f"Instaladas: {installed}")
    print(f"Ya instaladas: {alreadyInstalled}")
    print(f"Errores: {errors}")
    print(f"Excluidas requeridas que cumplen: {excludedMatched}/{len(excludedResults)}")
    print(f"Dependencias omitidas explícitamente: {len(omittedDependencies)}")

    if errors == 0 and not missingPackages:
        print("\nInstalación de dependencias seleccionadas completada.")
    else:
        print("\nExisten dependencias pendientes de revisar.")

    return {
        "installedDependencies": results,
        "excludedDependencies": excludedResults
    }