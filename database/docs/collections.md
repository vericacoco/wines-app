# MongoDB Collections – Wine Platform

## wines
| Field        | Type   | Description                    |
|-------------|--------|--------------------------------|
| name        | string | Name of the wine               |
| country     | string | Country of origin              |
| type        | string | Red / White / Rose             |
| price       | number | Price in EUR                   |
| description | string | Optional description           |

## users
| Field | Type | Description |
|------|------|-------------|
| email | string | User email |

## ratings
| Field | Type | Description |
|------|------|-------------|
| wine | string | Wine name |
| rating | number | Rating 1–5 |
