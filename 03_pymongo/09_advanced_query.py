import pymongo

# vytvoříme klienta
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# vytvoříme databázi "PythonRemoteCZ19"
mydb = myclient["PythonRemoteCZ19"]

# vytvoření kolekce
mycol = mydb["customers"]

print("Vypíšeme klienty, jejichž příjmení začíná na 'S' a nebo dále:")
myquery = {"surname": {"$gt": "S"}}
response = mycol.find(myquery)
for customer in response:
    print(customer)

print("Vypíšeme klienty, jejichž příjmení začíná na 'N':")
myquery = {"surname": {"$regex": "^N"}}
response = mycol.find(myquery)
for customer in response:
    print(customer)

print("Vypíšeme všechny klienty z Prahy:")
myquery = {"address": {"$regex": "Praha"}}
response = mycol.find(myquery)
for customer in response:
    print(customer)
