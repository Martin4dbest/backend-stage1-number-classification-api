from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

def get_digit_sum(n):
    return sum(int(digit) for digit in str(n))

def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}?json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('text', 'No fun fact available.')
    return "Fun fact could not be retrieved."

def classify_number(n):
    properties = []
    
    if is_armstrong(n):
        properties.append("armstrong")
    properties.append("odd" if n % 2 != 0 else "even")

    return {
        "number": n,
        "is_prime": is_prime(n),
        "is_perfect": is_perfect(n),
        "properties": properties,
        "digit_sum": get_digit_sum(n),
        "fun_fact": get_fun_fact(n)
    }

@app.route('/api/classify-number', methods=['GET', 'POST'])
def classify():
    try:
        if request.method == 'POST':
            data = request.get_json()
            if not data or "number" not in data:
                return jsonify({"error": True}), 400
            num = int(data["number"])
        else:  # Handle GET request
            num = request.args.get("number", type=int)
            if num is None:
                return jsonify({"error": True}), 400

        return jsonify(classify_number(num)), 200
    except (ValueError, TypeError):
        return jsonify({"error": True}), 400

if __name__ == '__main__':
    app.run(debug=True)
