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