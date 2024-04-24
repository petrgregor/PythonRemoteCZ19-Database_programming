import pymongo

# vytvoříme klienta
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# vytvoříme databázi "PythonRemoteCZ19"
mydb = myclient["PythonRemoteCZ19"]

# vytvoření kolekce
mycol = mydb["customers"]

mylist = [
    {"name": "Martin", "surname": "Novák", "value": 2},
    {"name": "Lukáš", "surname": "Svoboda", "address": "Úzká 25, Praha"},
    {"surname": "Novotný", "address": "Hlavní 315, Pardubice"}
]

response = mycol.insert_many(mylist)
print(f"Inserted ids: {response.inserted_ids}")
