# DevOps Stage 1: Number Classification API

DevOps Stage 1 - Number Classification API

## Overview
This API classifies numbers based on various mathematical properties and provides fun facts about the number. It is designed to help developers understand how to build, deploy, and interact with an API.

The core functionality of the API includes classifying numbers based on whether they are prime, perfect, or Armstrong. Additionally, it provides a fun fact from the Numbers API and performs other checks like determining if a number is even or odd, and calculating the sum of its digits.

## Features
The API supports the following functionality:
- **Prime Number Check**: Determines if the number is prime.
- **Perfect Number Check**: Determines if the number is perfect.
- **Armstrong Number Check**: Determines if the number is an Armstrong number.
- **Even/Odd Check**: Determines if the number is even or odd.
- **Sum of Digits Calculation**: Calculates the sum of the digits of the number.
- **Fun Fact**: Fetches an interesting fact about the number from the Numbers API.

## API Usage

### Endpoint:
`GET /api/classify-number?number={num}`

#### Example Request:
`GET https://number-api.onrender.com/api/classify-number?number=371`

#### Example Response:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "class_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}




# Error Handling

If an invalid number is provided, the API will return an error message:

## Example Error Response:


{
    "number": "abc",
    "error": true
}




