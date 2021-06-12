from pymongo import MongoClient
from sqlalchemy import create_engine

client = MongoClient('localhost',27017)

db = client['mydb']

print("your database has been created.....")

print("list of databases after creating database:")
print(client.list_database_names())

collection = db["students"]
print("your collection has been created...")

doc1 = {"name": "Ram", "age": "26", "city": "Hyderabad"}

collection.insert_one(doc1)
print(collection.find_one())

