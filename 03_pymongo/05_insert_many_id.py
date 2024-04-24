import pymongo

# vytvoříme klienta
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# vytvoříme databázi "PythonRemoteCZ19"
mydb = myclient["PythonRemoteCZ19"]

# vytvoření kolekce
mycol = mydb["customers"]

mylist = [
    {"_id": 1, "name": "Lojza", "surname": "Strašný"},
    {"_id": 2, "name": "Jarda", "surname": "Hodný"},
    {"_id": 3, "name": "David", "surname": "Zlý"}
]

response = mycol.insert_many(mylist)
print(f"Inserted ids: {response.inserted_ids}")