from pymongo import MongoClient

client = MongoClient("localhost",27017)

db = client['mongo_db']

coll = db['mongo_coll']

#and
#records = coll.find({"city":"Pune","name":"a"})

#gt
#records = coll.find({"age":{"$gt":"50"}})

#lt
#records = coll.find({"age":{"$lt":"50"}})

#gte
#records = coll.find({"age":{"$gte":"45"}})

#lte
records = coll.find({"age":{"$lte":"45"}})

print(records)

for record in records:
    print(record)

# data = [
#     {"_id": "100", "name": "Ram", "age": "26", "city": "Hyderabad"},
# {"_id": "102", "name": "a", "age": "22", "city": "Hyderabad"},
# {"_id": "108", "name": "b", "age": "33", "city": "Pune"},
# {"_id": "109", "name": "c", "age": "44", "city": "Mohali"},
# {"_id": "110", "name": "d", "age": "22", "city": "Banglore"},
# {"_id": "111", "name": "a", "age": "43", "city": "Banglore"},
# {"_id": "112", "name": "d", "age": "45", "city": "Mohali"},
# {"_id": "113", "name": "d", "age": "12", "city": "Mohali"},
# {"_id": "114", "name": "m", "age": "18", "city": "Pune"},
# {"_id": "115", "name": "k", "age": "2", "city": "Mumbai"},
# {"_id": "116", "name": "l", "age": "56", "city": "Mumbai"},
# {"_id": "117", "name": "l", "age": "55", "city": "Hyderabad"},
# {"_id": "118", "name": "a", "age": "44", "city": "Pune"},
# {"_id": "119", "name": "a", "age": "22", "city": "Hyderabad"},
# {"_id": "120", "name": "c", "age": "22", "city": "Chennai"}
# ]
#
# coll.insert_many(data)



