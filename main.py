from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

# Use your own Stripe Secret key
stripe.api_key = ""  # Replace with your actual test key

@app.route('/pay', methods=['POST'])
def process_payment():
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type, send JSON"}), 415

    data = request.get_json()
    amount = data.get("amount", 0)
    currency = data.get("currency", "usd")

    try:
       
        token = "tok_visa"  

        
        charge = stripe.Charge.create(
            amount=int(amount * 100),  
            currency=currency,
            source=token,  
            description="Test Payment",
        )

        return jsonify({"status": "success", "charge_id": charge.id})

    except stripe.error.StripeError as e:
        return jsonify({"status": "failed", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

    # command to run payment, we use curl in order to send a http request,
    # from there we can chose the amount etc: $50.00 and the currency also.

# curl -X POST http://127.0.0.1:5000/pay -H "Content-Type: application/json" -d "{\"amount\": 50.00, \"currency\": \"usd\"}"



