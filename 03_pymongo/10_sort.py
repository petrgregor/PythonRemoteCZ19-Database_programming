import pymongo

# vytvoříme klienta
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# vytvoříme databázi "PythonRemoteCZ19"
mydb = myclient["PythonRemoteCZ19"]

# vytvoření kolekce
mycol = mydb["customers"]

print("Vypíšeme klienty, jejichž příjmení začíná na 'S' a nebo dále:")
print("Bez uspořádání:")
myquery = {"surname": {"$gt": "S"}}
response = mycol.find(myquery)
for customer in response:
    print(customer)

print("Abecedně vzestupně dle příjmení")
myquery = {"surname": {"$gt": "S"}}
response = mycol.find(myquery).sort("surname")
for customer in response:
    print(customer)

print("Abecedně sestupně dle příjmení")
myquery = {"surname": {"$gt": "S"}}
response = mycol.find(myquery).sort("surname", -1)
for customer in response:
    print(customer)