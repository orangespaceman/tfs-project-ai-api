# API - Products

Retrieve products for a team.

| | |
| :---                      | :---                                            |
| URL                       | `/products/{team}`|
| Method                    | `GET`                                           |
| Auth required             | No                                              |
| Permissions required      | None                                            |

## Parameters

### URL Parameters

- `{team}` (required): Specifies the team for which information is requested. Possible values: "wolf", "dragon", or "hedgehog".

### Query Parameters

- `query` (optional): The query string to search for products.

- `sort` (optional): Specifies the sorting criteria. Possible values: "price", "rating", or "title". Defaults to "title".

- `page-size` (optional): Specifies the number of products per page. Must be a positive integer.

- `page` (optional): Specifies the page number. Must be a positive integer.

### Example queries

```
https://[url]/product/wolf?query=shoes
https://[url]/product/hedgehog?sort=price
https://[url]/product/dragon?query=summer+jackets&sort=rating&page-size=2&page=2
```


## Success Response

### Products related to hedgehogs based on the query provided.

**HTTP Response Code** : `200 OK`

**Response data**

```json
{
    "products": [
        {
            "id": "43a8330b-87c3-4896-99c8-bf75942998a4",
            "title": "Product 4",
            "description": "A description",
            "image": "/images/products/hedgehog/product-4.jpg",
            "price": "0.07",
            "stars": 5
        },
        {
            "id": "91d545b3-967f-4b57-8fd9-bbbe30d9dd71",
            "title": "Product 1",
            "description": "A description",
            "image": "/images/products/hedgehog/product-1.jpg",
            "price": "0.02",
            "stars": 3
        },
        {
            "id": "92878fc0-109c-41ca-8768-91063a31b2b4",
            "title": "Product 2",
            "description": "A description",
            "image": "/images/products/hedgehog/product-2.jpg",
            "price": "0.04",
            "stars": 3
        },
        {
            "id": "c2449c1c-cc18-4e06-a58f-f96366e39f66",
            "title": "Product 5",
            "description": "A description",
            "image": "/images/products/hedgehog/product-5.jpg",
            "price": "1.11",
            "stars": 2
        }
    ]
}
```

### No products found

**HTTP Response Code** : `200 OK`

**Response data**

```json
{
    "results": []
}
```