# Backend Stage 1: 

Create an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Overview

The Number Classification API is a project created as part of my HNG Stage 2 DevOps task. This API is designed to classify numbers based on various mathematical properties, providing fun facts that make learning about numbers more engaging and interactive.

As part of my journey in mastering DevOps, this project demonstrates my ability to build, deploy, and maintain a fully functional API. The core functionality of the API includes classifying numbers in several ways:

## Features
The API supports the following functionality:
- **Prime Number Check**: Determines if the number is prime.
- **Perfect Number Check**: Determines if the number is perfect.
- **Armstrong Number Check**: Determines if the number is an Armstrong number.
- **Even/Odd Check**: Determines if the number is even or odd.
- **Sum of Digits Calculation**: Calculates the sum of the digits of the number.
- **Fun Fact**: Fetches an interesting fact about the number from the Numbers API.

Additionally, it provides a fun fact from the Numbers API and performs other checks like determining if a number is even or odd, and calculating the sum of its digits.

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

```

#### Error Handling:

If an invalid number is provided, the API will return an error message:

## Example Error Response:


{
    "number": "abc",
    "error": true
}



# Deployment

This API is deployed on Render.

## How to Run Locally

### Step 1: Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/Martin4dbest/backend-stage1-number-classification-api
cd backend-stage1-number-classification-api


### Step 2: Install Dependencies
Install the necessary dependencies using pip:

pip install flask flask-cors requests


### Step 3: Run the Server
Start the Flask server by running:

flask run

Step 4: Test the API Locally
Once the server is running, open your browser or use a tool like cURL to access the following URL to test the endpoint:


http://127.0.0.1:5000/api/classify-number?number=371


## Contributing

Feel free to fork the repository and contribute improvements to the API. Here are some suggestions for contributions:

- Add more mathematical properties or fun facts.
- Improve error handling for different types of inputs.
- Optimize the performance of calculations.

### Steps for Contributing:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit and push your changes.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Final Steps

- ✅ Push everything to GitHub
- ✅ Test the API
- ✅ Submit on Slack using /submit
