from flask import Flask, request, jsonify
from flask_cors import CORS
import math
import json
import requests  # For calling the Numbers API

app = Flask(__name__)
CORS(app)

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n

# Function to check if a number is Armstrong
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum([d**len(digits) for d in digits]) == n

# Function to get a fun fact from the Numbers API
def get_fun_fact(number):
    try:
        response = requests.get(f"http://numbersapi.com/{number}?json")
        if response.status_code == 200:
            return response.json().get("text", "")
        else:
            return f"No fact found for number {number}"
    except Exception as e:
        return f"Error fetching fun fact: {str(e)}"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Input validation
    if number is None or not number.lstrip('-').isdigit():
        return jsonify({
            "number": number,
            "error": True
        }), 400

    # Convert the string input to an integer
    number = int(number)
    properties = []
    
    # Check Armstrong status
    armstrong_status = is_armstrong(number)
    if armstrong_status:
        properties.append("armstrong")
    
    # Check if number is odd or even
    if number % 2 == 0:
        if not armstrong_status:
            properties = ["even"]
        else:
            properties.append("even")
    else:
        if not armstrong_status:
            properties = ["odd"]
        else:
            properties.append("odd")

    # Calculate the digit sum
    digit_sum = sum(int(digit) for digit in str(abs(number)))
    
    # Get the fun fact from Numbers API
    fun_fact = get_fun_fact(number)

    # Construct the response
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    # Return the response as a compact JSON string
    return app.response_class(
        response=json.dumps(response, separators=(',', ':')),  # Ensure compact JSON response
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True)
