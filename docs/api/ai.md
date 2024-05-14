# API - AI

Retrieve information from the AI.

| | |
| :---                      | :---                                          |
| URL                       | `/ai/{team}`    |
| Method                    | `GET`                                         |
| Auth required             | No                                            |
| Permissions required      | None                                          |

## Parameters

### URL Parameters

- `{team}` (required): Specifies the team for which information is requested. Possible values: "wolf", "dragon", or "hedgehog".

### Query Parameters

- `query` (required): The specific query to be processed by the AI system.

### Example queries

```
https://[url]/ai/wolf?query=Name+5+African+mammals
https://[url]/ai/hedgehog?query=Name+5+African+birds
```

## Success Response

### Information based on the query provided.

**HTTP Response Code** : `200 OK`

**Response data**

```json
{
    "results": [
        {
            "title": "Lion",
            "description": "Majestic predator known for its mane and powerful roar"
        },
        {
            "title": "Elephant",
            "description": "Gentle giant with a trunk and tusks, one of the largest land animals"
        },
        {
            "title": "Giraffe",
            "description": "Tall herbivore with a long neck and distinctive spotted coat"
        },
        {
            "title": "Hippopotamus",
            "description": "Large, barrel-shaped animal with a massive mouth and tusks"
        },
        {
            "title": "Cheetah",
            "description": "Sleek and fast predator, known for its black spots and long tail"
        }
    ]
}
```

## Error Responses

### No query specified

**HTTP Response Code** : `500 INTERNAL SERVER ERROR`

**Response data**

```json
{
    "error": "No query specified"
}
```

### Internal Server Error

**HTTP Response Code** : `500 INTERNAL SERVER ERROR`

**Response data**

```json
{
    "error": "Sorry, something went wrong, please try again"
}
```