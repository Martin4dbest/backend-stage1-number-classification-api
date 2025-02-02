from flask import Flask, request, jsonify
from flask_cors import CORS
import math
import json

app = Flask(__name__)
CORS(app)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n

def is_armstrong(n):
    digits = [int(d) for d in str(abs(n))]  # Handle negative numbers correctly
    return sum([d**len(digits) for d in digits]) == abs(n)

@app.route('/')
def home():
    return "Welcome to the Number Classification API! Use /api/classify-number?number=<your_number> to classify a number."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    try:
        number = float(number)  # Convert input to float first
        if not number.is_integer():
            raise ValueError  # Reject non-integer values
        number = int(number)  # Convert back to int
    except (ValueError, TypeError):
        return jsonify({
            "number": number,
            "error": True
        }), 400

    properties = []
    
    if is_prime(number):
        properties.append("prime")
    if is_perfect(number):
        properties.append("perfect")
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    digit_sum = sum(int(digit) for digit in str(abs(number)))

    fun_fact = f"{number} is an Armstrong number because " + " + ".join([f"{d}^{len(str(number))}" for d in str(abs(number))]) + f" = {number}" if is_armstrong(number) else "No fact found."

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
