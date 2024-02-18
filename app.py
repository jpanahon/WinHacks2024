from flask import Flask, render_template, request, jsonify
import dummy_dict
import json
import DataBase

app = Flask(__name__)

purchase_history = []

def calculate_total_price(cart):
    return sum(item['price'] * item['quantity'] for item in cart)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/shop/", methods=['GET', 'POST'])
def shop():
    data = dummy_dict.items
    data_json = json.dumps(data)
    return render_template("shop.html", items = data_json)

@app.route("/filtered/", methods=['GET', 'POST'])
def filtered():
    filtered_data = request.json.get('filtered')

    # Handle the regular GET request
    return jsonify(items=filtered_data)
    # return render_template("shop.html", items=filtered_data)
    
@app.route("/checkout")
def checkout():
    data = dummy_dict.items
    data = json.dumps(data)
    return render_template("checkout.html")

# @app.route("/pay/")
# def pay():
#     return render_template("pay.html")

@app.route("/purchasehistory/")
def history():
    return render_template("purchasehistory.html")

@app.route("/budget/")
def budget():
    return render_template("budget.html")

if __name__ == '__main__':
	app.run(debug=True)