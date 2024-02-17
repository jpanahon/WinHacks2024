from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/shop/")
def shop():
    return render_template("shop.html")

@app.route("/pay/")
def pay():
    return render_template("pay.html")

@app.route("/budget/")
def budget():
    return render_template("budget.html")

if __name__ == '__main__':
	app.run(debug=True)