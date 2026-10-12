
import time
import requests

# Configuración de Render y Vercel Preview
apiUrl = "https://portafolio-pr-2-u0sm.onrender.com"
frontendOrigin = "https://portafolio1-cw4s6mfk3-42engineering-projects.vercel.app"

testResults = []


def registerTest(name, passed, detail=""):

    status = "PASS" if passed else "FAIL"
    testResults.append((name, status))

    print(f"[{status}] {name} {detail}")


def testHealth():

    response = requests.get(f"{apiUrl}/health", timeout=120)
    data = response.json()

    passed = (
        response.status_code == 200
        and data.get("status") == "running"
        and data.get("available_models") == 17
    )

    registerTest("Health endpoint", passed)


def testModels():

    response = requests.get(f"{apiUrl}/models", timeout=120)
    data = response.json()

    models = data.get("models", [])

    passed = (
        response.status_code == 200
        and isinstance(models, list)
        and len(models) == 17
        and "LSTM_5" in models
        and "LSTM_10" in models
    )

    registerTest("Models catalog", passed, f"Models: {len(models)}")


def testCors():

    response = requests.get(
        f"{apiUrl}/models",
        headers={"Origin": frontendOrigin},
        timeout=120
    )

    allowedOrigin = response.headers.get("access-control-allow-origin")

    passed = (
        response.status_code == 200
        and allowedOrigin == frontendOrigin
    )

    registerTest("CORS Preview", passed, f"Allowed origin: {allowedOrigin}")


def testPrediction(modelName):

    payload = {
        "start_date": "2023-01-01",
        "model_name": modelName
    }

    startTime = time.perf_counter()

    response = requests.post(
        f"{apiUrl}/predict",
        json=payload,
        timeout=180
    )

    duration = time.perf_counter() - startTime
    data = response.json()

    probability = data.get("probability")

    passed = (
        response.status_code == 200
        and "error" not in data
        and data.get("model") == modelName
        and data.get("prediction") in ["SUBIRÁ", "BAJARÁ"]
        and isinstance(probability, (int, float))
        and 0 <= probability <= 1
    )

    registerTest(
        f"Prediction {modelName}",
        passed,
        f"Time: {duration:.3f}s"
    )


def testInvalidModel():

    payload = {
        "start_date": "2023-01-01",
        "model_name": "INVALID_MODEL"
    }

    response = requests.post(
        f"{apiUrl}/predict",
        json=payload,
        timeout=120
    )

    data = response.json()

    passed = (
        "error" in data
        and "Unknown model" in data["error"]
    )

    registerTest("Invalid model", passed)


def testInvalidDate():

    payload = {
        "start_date": "fecha-invalida",
        "model_name": "LSTM_5"
    }

    response = requests.post(
        f"{apiUrl}/predict",
        json=payload,
        timeout=120
    )

    data = response.json()

    passed = "error" in data

    registerTest("Invalid date", passed)


def runTests():

    print("\nP3 TSLA - PREVIEW INTEGRATION TESTS\n")

    tests = [
        ("Health endpoint", testHealth),
        ("Models catalog", testModels),
        ("CORS Preview", testCors),
        ("Prediction LSTM_5 - First", lambda: testPrediction("LSTM_5")),
        ("Prediction LSTM_5 - Second", lambda: testPrediction("LSTM_5")),
        ("Prediction LSTM_10 - First", lambda: testPrediction("LSTM_10")),
        ("Prediction LSTM_10 - Second", lambda: testPrediction("LSTM_10")),
        ("Prediction LSTM_5 - Return", lambda: testPrediction("LSTM_5")),
        ("Invalid model", testInvalidModel),
        ("Invalid date", testInvalidDate)
    ]

    for name, testFunction in tests:

        try:
            testFunction()

        except Exception as error:
            registerTest(name, False, str(error))

    print("\nTEST SUMMARY\n")
    print(f"STATUS: EXPECTED RESULT")
    

    for name, status in testResults:
        print(f"{status}: {name}")

    failed = sum(status == "FAIL" for _, status in testResults)

    print(f"\nTotal: {len(testResults)}")
    print(f"Passed: {len(testResults) - failed}")
    print(f"Failed: {failed}")

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    runTests()
