import pymongo

# vytvoříme klienta
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# vytvoříme databázi "PythonRemoteCZ19"
mydb = myclient["PythonRemoteCZ19"]

# vytvoření kolekce
mycol = mydb["customers"]

for response in mycol.find():
    print(response)

myquery = {"surname": {"$regex": "^N"}}
new_values = {"$set": {"contact": "777123456"}}
response = mycol.update_many(myquery, new_values)
print(f"Bylo aktualizováno {response.modified_count} záznamů.")

for response in mycol.find():
    print(response)
