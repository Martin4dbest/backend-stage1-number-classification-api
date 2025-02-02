from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

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
    digits = [int(d) for d in str(n)]
    return sum([d**len(digits) for d in digits]) == n

@app.route('/')
def home():
    return "Welcome to the Number Classification API! Use /api/classify-number?number=<your_number> to classify a number."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Validate input
    if not number or not number.lstrip('-').isdigit():  # Handle negative numbers
        return jsonify({"number": number, "error": True, "message": "Invalid number format."}), 400

    number = int(number)
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

    digit_sum = sum(int(digit) for digit in str(abs(number)))  # Sum of digits

    # Get fun fact from Numbers API
    fun_fact = "No fact found."
    try:
        fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math?json", timeout=5)
        if fun_fact_response.status_code == 200:
            fun_fact = fun_fact_response.json().get("text", fun_fact)
    except requests.exceptions.RequestException:
        pass  

    return jsonify({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": f"{digit_sum}",  # return as string as requested
        "fun_fact": fun_fact
    }), 200  # Explicitly setting status code to 200 for valid input

if __name__ == '__main__':
    app.run(debug=True)
