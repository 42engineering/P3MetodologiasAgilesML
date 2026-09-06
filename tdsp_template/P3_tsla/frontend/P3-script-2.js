const API_URL = window.location.origin;
// const API_URL = 
    // "https://p3metodologiasagilesml-1.onrender.com";
    // "https://p3metodologiasagilesml.onrender.com";


window.onload = async () => {

    try {

        const response = await fetch(
            `${API_URL}/models`
        );

        const data = await response.json();

        const select =
            document.getElementById(
                "modelSelect"
            );

        select.innerHTML = "";

        data.models.forEach(model => {

            const option =
                document.createElement(
                    "option"
                );

            option.value = model;

            option.textContent = model;

            select.appendChild(
                option
            );
        });

    } catch(error) {

        console.error(error);

    }

};

async function predictMovement() {

    const startDate =
        document.getElementById(
            "startDate"
        ).value;

    const modelName =
        document.getElementById(
            "modelSelect"
        ).value;

    const resultBox =
        document.getElementById(
            "resultBox"
        );

    resultBox.innerHTML =
        "<h2>Loading prediction...</h2>";

    try {

        const response = await fetch(
            `${API_URL}/predict`,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({

                    start_date:
                    startDate,

                    model_name:
                    modelName
                })
            }
        );

        const data =
            await response.json();

        if(data.error){

            resultBox.innerHTML = `

                <h2>
                    Prediction Error
                </h2>

                <p>
                    ${data.error}
                </p>

            `;

            return;
        }

        resultBox.innerHTML = `

            <h2>
                ${data.prediction}
            </h2>

            <p>
                <b>Model:</b>
                ${data.model}
            </p>

            <p>
                <b>Probability:</b>
                ${(data.probability * 100).toFixed(2)}%
            </p>

            <p>
                <b>Real Movement:</b>
                ${data.real_movement}
            </p>

            <p>
                <b>Window Start:</b>
                ${data.window_start}
            </p>

            <p>
                <b>Window End:</b>
                ${data.window_end}
            </p>

        `;

    } catch(error) {

        resultBox.innerHTML = `

            <h2>
                Connection Error
            </h2>

            <p>
                ${error}
            </p>

        `;

    }

}