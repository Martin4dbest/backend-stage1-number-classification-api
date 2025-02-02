from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d**length for d in digits) == n

def classify_number(n):
    """Classify a number and return its properties."""
    properties = []
    if is_prime(n):
        properties.append("prime")
    if is_perfect(n):
        properties.append("perfect")
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

@app.route('/api/classify-number', methods=['GET'])
def classify_number_api():
    number = request.args.get('number')
    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    properties = classify_number(number)
    class_sum = sum(int(d) for d in str(abs(number)))
    fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math")
    fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else "No fun fact available."

    return jsonify({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "class_sum": class_sum,
        "fun_fact": fun_fact
    })

if __name__ == '__main__':
    app.run(debug=True)