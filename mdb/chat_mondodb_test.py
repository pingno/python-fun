from pymongo import MongoClient

# Connect to the MongoDB server running on localhost at port 27017
client = MongoClient('mongodb://localhost:27017/')

# Access a specific database
db = client['mydatabase']

# Access a specific collection in that database
collection = db['mycollection']


# Insert a single document
collection.insert_one({'name': 'John', 'age': 30})

# Insert multiple documents
collection.insert_many([
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 35}
])

# Find a single document
result = collection.find_one({'name': 'John'})

# Find all documents that match a query
results = collection.find({'age': {'$gt': 30}})  # Find all documents where age is greater than 30


# Update a single document
collection.update_one({'name': 'John'}, {'$set': {'age': 31}})

# Update multiple documents
collection.update_many({'age': {'$lt': 30}}, {'$set': {'status': 'Young'}})  # Add a new field to documents where age is less than 30


# Delete a single document
collection.delete_one({'name': 'John'})

# Delete multiple documents
collection.delete_many({'age': {'$gt': 30}})  # Delete all documents where age is greater than 30

client.close()