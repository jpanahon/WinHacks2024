import json
import socket
import base64


def dread():
        with open('database.json','r') as outfile:
                data = json.load(outfile)
        
        return data
        
def dregister(username,password,budget) : 

        with open('database.json','r') as outfile:
                data = json.load(outfile)

        x = len(data["StaticData"]["user_table"])
        new = True

        while(x>0):
                x-=1
                if data["StaticData"]["user_table"][x]["Name"] == username:
                        new=False
                        
        if (new==True):
                i=len(data["StaticData"]["user_table"])
                x=len(data["SessionData"]["shopping_session"])
                newUser = [
                {       
                        "userid" : i,
                        "Name" : username,
                        "Password" : password,
                        "sessionid" : x
                }
                ]     
                data["StaticData"]["user_table"]+= newUser

                newData = [
                {    
                                "userid" : i,
                                "sessioncookie" : 0,
                                "budget" : int(budget),
                                "cart_items": []

                }
                ]
                data["SessionData"]["shopping_session"]+= newData


                json_object = json.dumps(data, indent=4)

                with open("database.json", "w") as outfile:
                        outfile.write(json_object)
                return True #account created
        else :
                return False #username already taken
        
def dlogin(username,password):


        with open('database.json','r') as outfile:
                data = json.load(outfile)

        x = len(data["StaticData"]["user_table"])
        RealUser = False
        session = 0

        while(x>0):
                x-=1
                if (data["StaticData"]["user_table"][x]["Name"] == username and data["StaticData"]["user_table"][x]["Password"] == password):
                        RealUser=True
                        uid = x
                

        if (RealUser==True):
                cookie = encookie(username,password)
                sid=data["StaticData"]["user_table"][uid]["sessionid"]
                     
                print(cookie)
                data["SessionData"]["shopping_session"][sid]["sessioncookie"] = cookie


                json_object = json.dumps(data, indent=4)

                with open("database.json", "w") as outfile:
                        outfile.write(json_object)
                return True #logged in
        else  :
                return False #incorect username or password

def dcart (item,amount,section,username,password):
        with open('database.json','r') as outfile:
                data = json.load(outfile)  
        cookie = encookie(username,password)

        x = len(data["SessionData"]["shopping_session"])
        while(x>0):
                x-=1
                if data["SessionData"]["shopping_session"][x]["sessioncookie"] == cookie:
                        session = x

        if (x!=0):
                price = "%.2f" % (data["StaticData"]["product_table"][section][int(item)]["price"]*int(amount))
                budget = data["SessionData"]["shopping_session"][session]["budget"]

                if (budget>float(price)):
                        name = data["StaticData"]["product_table"][section][int(item)]["name"]
                        newItem = {
                        "item" : name,
                        "amount" : amount,
                        "price" : price
                        }

                        budget-=float(price)
                        data["SessionData"]["shopping_session"][session]["cart_items"]+= newItem
                        data["SessionData"]["shopping_session"][session]["budget"] =budget

                        json_object = json.dumps(data, indent=4)

                        with open("database.json", "w") as outfile:
                                outfile.write(json_object)
                        return "item added"
                else :
                        return "out of budget"
        else:
                return "Please relogin"

                        
def dbuy (payment):
        with open('database.json','r') as outfile:
                data = json.load(outfile)  
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        x = len(data["SessionData"]["shopping_session"])
        while(x>0):
                x-=1
                if data["SessionData"]["shopping_session"][x]["sessionip"] == ip_address:
                        session = x

        budget = data["SessionData"]["shopping_session"][session]["budget"]
        cart = data["SessionData"]["shopping_session"][session]["cart_items"]

        if (payment != None):

                y = len(data["ProcessedData"]["order_details"])


                newData = [
                {
                      "paymentinfo" : payment,
                      "userid" : data["SessionData"]["shopping_session"][session]["userid"],
                      "cost" : data["SessionData"]["shopping_session"][session]["cart_items"]["price"],
                      "items" : data["SessionData"]["shopping_session"][session]["cart_items"]["item"],
                      "amount" : data["SessionData"]["shopping_session"][session]["cart_items"]["amount"],
                      "orderid" : y
                }
                ]

                data["ProcessedData"]["order_details"] +=newData
                data["SessionData"]["shopping_session"][session] = {}

                

                json_object = json.dumps(data, indent=4)

                with open("database.json", "w") as outfile:
                                outfile.write(json_object)
                return True #items bought
        else :
                return False #order failed       

def encookie(user, password):
        s=user+" "+password
        return str(s)

def decookie(cookie):
        info = cookie.split()
        return info