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
    data = json.dumps(data)
    return render_template("shop.html", items=data)

@app.route("/filtered/", methods=['GET', 'POST'])
def filtered():
        # Get the filtered data from the request
    filtered_data = request.json.get('filtered')
    print(filtered_data)
        
        # Process the filtered data (optional)
        # ...

        # Return the filtered data as JSON

    # Handle the regular GET request
    return jsonify(items=filtered_data)
    # return render_template("shop.html", items=filtered_data)


@app.route("/pay/")
def pay():
    return render_template("pay.html")

@app.route("/budget/")
def budget():
    return render_template("budget.html")

if __name__ == '__main__':
	app.run(debug=True)