function requestAI() {
    const apiEl = document.querySelector("input[name='url']");
    const api = apiEl.value;

    const params = {};

    const aiQueryEl = document.querySelector("input[name='ai-query']");
    params.query = aiQueryEl.value;

    const searchParams = new URLSearchParams(params);

    const teamEl = document.querySelector("input[name='team']");
    var team = teamEl.value;

    fetch(`${api}/ai/${team}?${searchParams.toString()}`, {
        headers: {
            'Accept': 'application/json'
        }
    })
        .then((response) => response.json())
        .then((data) => {
            console.log('ai data :', data);

            var aiResultElement = document.querySelector(".ai-result");
            aiResultElement.textContent = JSON.stringify(data.results, null, 4);
        })
        .catch((error) => {
            console.error('ai error:', error);
        });
}

// listen for clicks on the button
var aiButton = document.querySelector('.ai-submit');
aiButton.addEventListener("click", requestAI);
