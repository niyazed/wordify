# Wordify

Wordify is a simple tool to convert Image or PDF to a Wortart and extract keywords from it.


## Start the server

```bash
$ docker compose up -d
```
Omit the `-d` flag to see the logs.

## Response

The response is a JSON object with the following structure:

```json
{
  "wordart_url": "The URL of the wordart image",
  "top_ten_keywords": [
    "keyword1",
    "keyword2",
    "keyword3"
    ...
    ...
  ]
}
```
