from flask import Flask, request, jsonify
import math
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(n):
    if n < 1:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum([d ** len(digits) for d in digits]) == n

# Function to calculate the sum of digits of a number
def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))  # Handle negative numbers

# Function to determine if the number is odd or even
def determine_parity(n):
    return "odd" if n % 2 != 0 else "even"

# Fetch fun fact from Numbers API
def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}?json"
    try:
        response = requests.get(url, timeout=3)  # Add timeout for reliability
        if response.status_code == 200:
            return response.json().get('text', 'No fun fact available.')
        else:
            return "Fun fact could not be retrieved."
    except Exception:
        return "Fun fact could not be retrieved."

# Function to classify number properties
def classify_number_properties(n):
    properties = []
    
    if is_armstrong(n):
        properties.append("armstrong")
    else:
        properties.append(determine_parity(n))  # Include "odd" or "even"
    
    return properties

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Get number from query parameter
    number_param = request.args.get('number')

    # Validate input: Must be numeric and an integer
    if not number_param or not number_param.lstrip('-').isdigit():
        response = {
            "error": True,
            "message": "Invalid input. Please provide a valid integer."
        }
        return jsonify(response), 400

    # Convert string to integer
    number = int(number_param)

    # Classify properties
    properties = classify_number_properties(number)

    # Get fun fact
    fun_fact = get_fun_fact(number)

    # Construct response
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
