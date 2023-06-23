# GenerateResponse

# API Documentation

This project implements an API endpoint that generates a response based on the provided input data.

## API Endpoint

The API endpoint accepts a POST request to the `/api/generate-response` endpoint.

### Request Format

The request should include the following JSON data in the request body:

```json
{
   "COMMAND_ID": "string",
   "NOM": "string",
   "PRENOM": "string",
   "DATE_NAISSANCE": "string",
   "SEXE": "string",
   "MESSAGE": "string",
   "CHEMIN_VIE": "string",
   "SIGNE_LUNAIRE": "string",
   "SIGNE_ASTROLOGIQUE": "string"
}

Response Format
The API responds with the following JSON data:

json
Copy code
{
   "REPONSE": "string"
}
