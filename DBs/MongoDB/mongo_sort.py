from pymongo import MongoClient

client = MongoClient("localhost",27017)
db = client['mongo_db']
coll = db['mongo_coll']

#ascending
#results = coll.find().sort('city',1)

#descending
#results = coll.find().sort('city',-1)

results = coll.find().sort('age')

for result in results:
    print(result)


