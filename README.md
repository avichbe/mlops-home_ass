Web API Documentation for NER Service
Endpoints
1. POST /ner
Perform named entity recognition on the provided text.

Request:

Method: POST
Endpoint: /ner
Headers:
Content-Type: application/json
Authorization: Bearer {your_token_here}
Body:
json
Copy code
{
  "text": "Sample text that you want to analyze."
}
Response:

Content-Type: application/json
Body:
json
Copy code
{
  [
    {
        "entity": "O",
        "word": "Ġi"
    },
    {
        "entity": "O",
        "word": "Ġi"
    }
  ]
}
