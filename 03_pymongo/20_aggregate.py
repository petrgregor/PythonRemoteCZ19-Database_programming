import pymongo

myclient = pymongo.MongoClient("127.0.0.1", 27017)
mydb = myclient["PythonRemoteCZ19"]
mycol = mydb["cars"]

cars = [ {'name': 'Audi', 'price': 52642},
         {'name': 'Mercedes', 'price': 57127},
         {'name': 'Skoda', 'price': 9000},
         {'name': 'Volvo', 'price': 29000},
         {'name': 'Bentley', 'price': 350000},
         {'name': 'Citroen', 'price': 21000},
         {'name': 'Hummer', 'price': 41400},
         {'name': 'Volkswagen', 'price': 21600} ]
# mydb.cars.insert_many(cars)

agr = [{'$group': {'_id': 1, 'all': {'$sum': '$price'}}}]
val = list(mydb.cars.aggregate(agr))
print('The sum of prices is {}'.format(val[0]['all']))

agr = [{'$match':
            {'$or':
                 [{'name': "Audi"}, {'name': "Volvo"}]}},
       {'$group':
            {'_id': 1, 'sum2cars': {'$sum':"$price"}}}]
val = list(mydb.cars.aggregate(agr))
print('The sum of prices: {}'.format(val[0]['sum2cars']))