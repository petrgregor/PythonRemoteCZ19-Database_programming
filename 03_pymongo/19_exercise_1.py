from pymongo import MongoClient

myclient = MongoClient("127.0.0.1", 27017)
mydb = myclient['medical-db']
collection_medical = mydb['medicaldata']

print("Find all rows with procedure_code equal 0F1F4ZC")
for response in collection_medical.find({"procedure_code": "0F1F4ZC"}):
    print(response)

print("Find patient with patient_id equal 74, print his full name")
for response in collection_medical.find({"patient_id": 74}, {"_id": 0, "first_name": 1, "last_name": 1}):
    # TODO: ošetřit výpis, pokud nemá vyplněné jméno nebo příjmení
    print(f'{response["first_name"]} {response["last_name"]}')
    print(response)

print("Find a procedure performed on 2019-05-24T01:52:37.000Z and update its procedure code to 0F1F4ZC")
myquery = {"visit_date.date": "2019-05-24T01:52:37.000Z"}
print("Old record:")
for response in collection_medical.find(myquery):
    print(response)

print("Updated record:")
new_value = {"$set": {"procedure_code": "0F1F4ZC"}}
collection_medical.update_many(myquery, new_value)
for response in collection_medical.find(myquery):
    print(response)
