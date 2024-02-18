from flask import Flask, render_template, request, jsonify
import json
import DataBase

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/shop/", methods=['GET', 'POST'])
def shop():
    with open('./items.json') as f:
        data = json.load(f)
    return render_template("shop.html", items=data)

@app.route("/shop/category/<category_name>")
def category(category_name):
    with open('./items.json') as f:
        data = json.load(f)
          
    categoryItems = { "items": []}

    for item in data['items']:
        if item['category'] == category_name:
            categoryItems['items'].append(item)

    return render_template("shop.html", items=categoryItems)

@app.route("/filtered/", methods=['GET', 'POST'])
def filtered():
    filtered_data = request.json.get('filtered')

    # Handle the regular GET request
    return jsonify(items=filtered_data)
    # return render_template("shop.html", items=filtered_data)
    
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    with open('./items.json') as f:
        data = json.load(f)

    return render_template("checkout.html", items=data)


@app.route("/pay/")
def pay():
    return render_template("pay.html")

@app.route("/budget/")
def budget():
    return render_template("budget.html")

if __name__ == '__main__':
	app.run(debug=True)