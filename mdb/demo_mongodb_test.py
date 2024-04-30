import pymongo #first import pymongo

# to create a database in MongoDb, start by creating a MongoClient object
# then specify a connection URL with the correct ip address and the name
# of the database you want to create

# MongoDB will create the database if it does not exist, and make a connection to it

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# insert into database before checking if it exists

mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
 #insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted doc

print(x.inserted_id)

print("Hello")

# check if database exists

# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#     print("The database exists.")


# collist = mydb.list_collection_names()
# if "customers" in collist:
#     print("The collection exists")