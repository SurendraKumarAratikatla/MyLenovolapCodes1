from pymongo import MongoClient

client = MongoClient("localhost",27017)
db = client['mongo_db']
coll = db['mongo_coll']

#delete one record
#results = coll.delete_one({'_id': '113'})

# delete many records
results = coll.delete_many({"age":{"by":"44"}})


for record in coll.find():
    print(record)