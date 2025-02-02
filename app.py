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
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum([d ** len(digits) for d in digits]) == n

# Function to calculate the sum of digits of a number
def digit_sum(n):
    return sum(int(d) for d in str(n))

# Function to determine if the number is odd or even
def determine_parity(n):
    return "odd" if n % 2 != 0 else "even"

# Central function to fetch fun fact from Numbers API
def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}?json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('text', 'No fun fact available.')
        else:
            return "Fun fact could not be retrieved."
    except Exception as e:
        return f"Error fetching fun fact: {str(e)}"

# Function to classify the number based on mathematical properties
def classify_number_properties(n):
    properties = []
    
    if is_armstrong(n):
        properties.append("armstrong")
    
    # Check if the number is odd or even (not Armstrong)
    if not is_armstrong(n):
        properties.append(determine_parity(n))
    
    return properties

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Fetching number from query parameter
    number = request.args.get('number', type=str)
    
    # Input validation for number
    if not number.isdigit():
        response = {
            "number": number,
            "error": True,
            "message": "Input is not a valid number."
        }
        return jsonify(response), 200
    
    # Convert string to integer
    number = int(number)
    
    # Classify the number's properties
    properties = classify_number_properties(number)
    
    # Get the fun fact from Numbers API
    fun_fact = get_fun_fact(number)
    
    # Construct the response JSON matching the required format
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
