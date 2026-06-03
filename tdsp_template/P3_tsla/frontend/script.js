const API_URL =
    "https://p3metodologiasagilesml.onrender.com";


async function predictMovement(){

    const startDate =
        document.getElementById(
            "startDate"
        ).value;

    const resultBox =
        document.getElementById(
            "resultBox"
        );

    if(!startDate){

        resultBox.innerHTML = `

            <h2>
                No Date Selected
            </h2>

            <p>
                Please select a valid date.
            </p>

        `;

        return;
    }

    resultBox.innerHTML = `

        <h2>
            Running Prediction...
        </h2>

        <p>
            Executing TensorFlow model.
        </p>

    `;

    try{

        const response =
            await fetch(

                `${API_URL}/predict`,

                {
                    method:"POST",

                    headers:{
                        "Content-Type":
                        "application/json"
                    },

                    body:JSON.stringify({

                        start_date:
                        startDate
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

                Prediction:
                ${data.prediction}

            </h2>

            <p>

                Predicted Class Probability:
                ${(data.probability * 100)
                    .toFixed(2)}%

            </p>

            <p>

                Real Movement:
                ${data.real_movement}

            </p>

            <p>

                Window:
                ${data.window_start}
                →
                ${data.window_end}

            </p>

            <p>

                Model:
                PT1_1_TSLA_30DAYS_LSTM

            </p>

        `;

    }catch(error){

        resultBox.innerHTML = `

            <h2>
                Connection Error
            </h2>

            <p>
                Unable to connect API.
            </p>

        `;

        console.error(error);
    }
}