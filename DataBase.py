import json
import socket


def read():
        with open('database.json','r') as outfile:
                data = json.load(outfile)
        
        return data
        
def register(username,password,budget) : 


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
                                "sessionip" : 0,
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
        
def login(username,password):


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
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                sid=data["StaticData"]["user_table"][uid]["sessionid"]
                     

                data["SessionData"]["shopping_session"][sid]["sessionip"] = ip_address


                json_object = json.dumps(data, indent=4)

                with open("database.json", "w") as outfile:
                        outfile.write(json_object)
                return True #logged in
        else  :
                return False #incorect username or password

def cart (item,amount,section):
        with open('database.json','r') as outfile:
                data = json.load(outfile)  
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        x = len(data["SessionData"]["shopping_session"])
        while(x>0):
                x-=1
                if data["SessionData"]["shopping_session"][x]["sessionip"] == ip_address:
                        session = x

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
                return True #item added
        else :
                return False #out of budget

                        
def buy (payment):
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



