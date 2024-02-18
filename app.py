from flask import Flask, render_template, request, jsonify, make_response
import dummy_dict
import json
from DataBase import *

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

@app.route("/register/")
def register():
   return render_template('register.html', name="")

@app.route("/login/")
def login():
   return render_template('login.html', name="")

@app.route('/setcookie1', methods = ['POST', 'GET'])
def setcookie1():
   if request.method == 'POST':
    user = request.form['nm']
    pasword = request.form['pswrd']
    bdget = request.form['bdgt']
    s=encookie(user,pasword)
    t=dregister(user,pasword,bdget)

   
    
   if (t==True):
    resp = make_response(render_template('readcookie.html', name=(user+" your was account created")))
    resp.set_cookie('userCookie', s)
    return resp
   else:
    resp = make_response(render_template('register.html', name="username is already taken"))
    return resp



@app.route('/setcookie2', methods = ['POST', 'GET'])
def setcookie2():
   if request.method == 'POST':
    user = request.form['nme']
    pasword = request.form['paswrd']
    s=encookie(user,pasword)
    t=dlogin(user,pasword)

   
   if (t==True):
    resp = make_response(render_template('readcookie.html', name=(user+", your are logged in.")))
    resp.set_cookie('userCookie', s)
    return resp
   else:
    resp = make_response(render_template('login.html', name="incorect username or password"))
    return resp

   

if __name__ == '__main__':
	app.run(debug=True)