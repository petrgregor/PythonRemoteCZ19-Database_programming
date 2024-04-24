import pymongo

# vytvoříme klienta
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# vytvoříme databázi "PythonRemoteCZ19"
mydb = myclient["PythonRemoteCZ19"]

# vytvoření kolekce
mycol = mydb["customers"]

# vytvořím si dotaz
print("Najdeme dle jména (Martin)")
myquery = {"name": "Martin"}
response = mycol.find(myquery)
for customer in response:
    print(customer)

print("Najdeme dle jména (Lojza)")
response = mycol.find({"name": "Lojza"})
for customer in response:
    print(customer)

print("Najdeme dle příjmení, vypíšeme jméno a příjmení")
response = mycol.find({"surname": "Novák"}, {"_id": 0, "name": 1, "surname": 1})
for customer in response:
    print(customer)
