import pymongo

# vytvoříme klienta
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# vytvoříme databázi "PythonRemoteCZ19"
mydb = myclient["PythonRemoteCZ19"]

# vytvoření kolekce
mycol = mydb["customers"]

for response in mycol.find():
    print(response)

# update jednoho záznamu
myquery = {"surname": "Svoboda"}
new_values = {"$set": {"surname": "Svobodný"}}
mycol.update_one(myquery, new_values)

print("-----------------")

for response in mycol.find():
    print(response)