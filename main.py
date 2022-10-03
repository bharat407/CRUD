import pymongo
myClient = pymongo.MongoClient('mongodb://localhost:27017/')
print(myClient.list_database_names())
