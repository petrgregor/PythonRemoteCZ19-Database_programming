import pymongo

# vytvoříme klienta
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
#myclient = pymongo.MongoClient("mongodb://localhost:27017")
#myclient = pymongo.MongoClient("localhost", 27017)
#myclient = pymongo.MongoClient("127.0.0.1", 27017)

# vytvoříme databázi "PythonRemoteCZ19"
mydb = myclient["PythonRemoteCZ19"]

print(f"myclient: {myclient}")
print(f"mydb: {mydb}")

