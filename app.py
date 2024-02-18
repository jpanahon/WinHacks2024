from flask import Flask, render_template, request, jsonify
import dummy_dict
import json

app = Flask(__name__)

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
    
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    data = dummy_dict.items
    data = json.dumps(data)
    return render_template("checkout.html", items=data)


@app.route("/pay/")
def pay():
    return render_template("pay.html")

@app.route("/budget/")
def budget():
    return render_template("budget.html")

if __name__ == '__main__':
	app.run(debug=True)