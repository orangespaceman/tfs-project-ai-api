function requestProducts() {
    const apiEl = document.querySelector("input[name='url']");
    const api = apiEl.value;

    const params = {};

    const productsQueryEl = document.querySelector("input[name='products-query']");
    params.query = productsQueryEl.value;

    const productsSortEl = document.querySelector("input[name='products-sort']:checked");
    params.sort = productsSortEl.value;

    const productsPageEl = document.querySelector("input[name='products-page']");
    if (productsPageEl.value) {
        params.page = productsPageEl.value
    }
    const productsPageSizeEl = document.querySelector("input[name='products-page-size']");
    if (productsPageSizeEl.value) {
        params['page-size'] = productsPageSizeEl.value
    }

    const searchParams = new URLSearchParams(params);

    const teamEl = document.querySelector("select[name='team']");
    var team = teamEl.options[teamEl.selectedIndex].value;

    fetch(`${api}/products/${team}?${searchParams.toString()}`, {
        headers: {
            'Accept': 'application/json'
        }
    })
        .then((response) => response.json())
        .then((data) => {
            console.log('Products data :', data);

            var productsResultElement = document.querySelector(".products-result");
            productsResultElement.textContent = JSON.stringify(data.products, null, 4);
        })
        .catch((error) => {
            console.error('Products error:', error);
        });
}

// listen for clicks on the button
var productsButton = document.querySelector('.products-submit');
productsButton.addEventListener("click", requestProducts);
