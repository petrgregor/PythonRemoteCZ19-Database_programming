import pymongo

# vytvoříme klienta
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# vytvoříme databázi "PythonRemoteCZ19"
mydb = myclient["PythonRemoteCZ19"]

# vytvoření kolekce
mycol = mydb["customers"]

print("Find all")
for response in mycol.find():
    print(response)

print("Find all - only id and name")
for response in mycol.find({}, {"name": True}):
    print(response)

print("Find all - only name")
for response in mycol.find({}, {"_id": False, "name": True}):
    print(response)

print("Find all - only name and surname")
for response in mycol.find({}, {"_id": 0, "surname": 1, "name": 1}):
    print(response)