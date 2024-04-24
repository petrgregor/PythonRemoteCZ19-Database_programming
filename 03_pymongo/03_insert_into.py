import pymongo

# vytvoříme klienta
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# vytvoříme databázi "PythonRemoteCZ19"
mydb = myclient["PythonRemoteCZ19"]

# vytvoření kolekce
mycol = mydb["customers"]

# vložíme hodnotu do kolekce
response = mycol.insert_one({"name": "Petr", "surname": "Gregor", "value": 3})
print(f"Inserted id: {response.inserted_id}")
