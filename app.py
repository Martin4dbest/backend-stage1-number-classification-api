from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_properties(n):
    """Determine the properties of the number."""
    props = []
    if is_armstrong(n):
        props.append("armstrong")
    props.append("odd" if n % 2 else "even")
    return props

def get_digit_sum(n):
    """Calculate the sum of the digits."""
    return sum(int(d) for d in str(abs(n)))

def get_fun_fact(n):
    """Fetch a fun fact using the Numbers API."""
    url = f"http://numbersapi.com/{n}?json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('text', 'No fun fact available.')
    except requests.RequestException:
        return "Fun fact could not be retrieved."
    return "Fun fact could not be retrieved."

@app.route('/number-properties', methods=['POST'])
def number_properties():
    """API endpoint to return number properties."""
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'number' not in data or not isinstance(data['number'], int):
            return jsonify({
                "number": data.get("number", "invalid"),
                "error": True
            }), 400
        
        num = data['number']
        
        # Build response
        response = {
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": get_properties(num),
            "digit_sum": get_digit_sum(num),
            "fun_fact": get_fun_fact(num)
        }
        
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": True, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
