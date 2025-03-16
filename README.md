Hello!

## Thank you for viewing my project, today i will describe how to the use the application

# Why did i create this?

## I wanted to give a real very very simple overview of how credit cards are processed in the backend.

# What does this do?

## This project uses Stripe back end, Python and Flask in order to process a dummy credit card.

# How to use this project

### 1. First you would need to clone the project

```
git clone git@github.com:nefariousjosiah/CreditCardPayment.git
```

### 2. After it is finished you would need to cd into the directory

```
cd CreditCardPayment
```

### 3. Open the python.py file in a text editor, for example

```
nano main.py
```

### From there you cna analyze the code, you can see how i have the token set to "tok_visa" because this not an actual credit card we are using.

### 4. Replace the stripe.api_key with your own **TESTING stripe api key on line 7**

```
# Use your own Stripe Secret key
stripe.api_key = ""  # Replace with your actual test key
```

### 5. Run this command to process a payment., change the "amount" or "currency" if needed.
```
curl -X POST http://127.0.0.1:5000/pay -H "Content-Type: application/json" -d "{\"amount\": 50.00, \"currency\": \"usd\"}"
```
### Essentially what is command does it that it sends a http request to your localhost on port 5000, processing the stripe payment.

### If successfull you should see the console output this.

```
{
  "charge_id": "yourChargeId",
  "status": "success"
}
```

## This process is essentially how online web pages are able to function credit card payments just in the backend.





