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

myquery = {"surname": {"$regex": "^S"}}
response = mycol.delete_many(myquery)
print(f"Bylo smazáno {response.deleted_count} záznamů.")

for customer in mycol.find():
    print(customer)