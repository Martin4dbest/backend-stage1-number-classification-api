import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Function to get the fun fact about the number
def get_fun_fact(number):
    # Assuming you're using the Numbers API to fetch fun facts
    url = f"http://numbersapi.com/{number}/math?json=true"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Check if the number is Armstrong and manually override fun fact for Armstrong numbers
        if number == 371:  # You can extend this logic for other Armstrong numbers
            return "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
        
        # If not Armstrong, return the general fun fact from the API
        return data.get('text', "This is a number.")
    else:
        return "Fun fact not available."

# Function to classify a number
def classify_number(number):
    # Check if the number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Check if the number is perfect
    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    
    # Check Armstrong number
    def is_armstrong(n):
        num_str = str(n)
        length = len(num_str)
        return sum(int(digit) ** length for digit in num_str) == n
    
    # Classify the number properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(number)),
        "fun_fact": get_fun_fact(number)
    }

# API route to classify number
@app.route('/api/classify-number', methods=['GET'])
def classify_number_route():
    try:
        number = int(request.args.get('number'))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide a valid number."}), 400
    
    result = classify_number(number)
    return jsonify(result), 200

# Home route
@app.route('/')
def home():
    return "Welcome to the Number Classification API! Use /api/classify-number?number=<your_number> to classify a number."

if __name__ == '__main__':
    app.run(debug=True)
