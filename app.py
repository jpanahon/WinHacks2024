from flask import Flask, render_template
import dummy_dict
import json

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/shop/")
def shop():
    data = dummy_dict.items
    data = json.dumps(data)
    return render_template("shop.html", items=data)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


@app.route("/pay/")
def pay():
    return render_template("pay.html")

@app.route("/budget/")
def budget():
    return render_template("budget.html")

if __name__ == '__main__':
	app.run(debug=True)