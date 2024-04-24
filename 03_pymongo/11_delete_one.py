import pymongo

# vytvoříme klienta
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# vytvoříme databázi "PythonRemoteCZ19"
mydb = myclient["PythonRemoteCZ19"]

# vytvoření kolekce
mycol = mydb["customers"]

response = mycol.find()
for customer in response:
    print(customer)

# smažeme jeden záznam
myquery = {"name": "Martin"}
mycol.delete_one(myquery)

print("------------------------------")

response = mycol.find()
for customer in response:
    print(customer)