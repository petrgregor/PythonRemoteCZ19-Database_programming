import json
from pymongo import MongoClient

myclient = MongoClient("127.0.0.1", 27017)
mydb = myclient['medical-db']
collection_medical = mydb['medicaldata']

with open('medical-data.json') as f:
    file_data = json.load(f)
    collection_medical.insert_many(file_data)
