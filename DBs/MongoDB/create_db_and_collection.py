from pymongo import MongoClient

#creating client
client = MongoClient('localhost',27017)

#creating database
db = client['mysampledb1']
print("Your database has been created...")

# creating collection
coll = db['mycollection']
print("my collection has been created...")

print("my all databases names before insert:")
print(client.list_database_names())

data = [
   {"_id": "104", "name": "Ram", "age": "26", "city": "Hyderabad"},
   {"_id": "105", "name": "Rahim", "age": "27", "city": "Bangalore"},
   {"_id": "106", "name": "Robert", "age": "28", "city": "Mumbai"}
]

result = coll.insert_many(data)

print("my all databases names after insert:")
print(client.list_database_names())