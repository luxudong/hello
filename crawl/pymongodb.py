import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient("localhost",27017)
db = client.local
collection = db.startup_log
print collection.count()

document = {
	"auther" : "lxd",
	"age" : 24,
	"data" : datetime.datetime.utcnow(),
	"tall" : 175.5
}

mydb = client.pytest
mycollection = mydb.pycollectioin
post_id = mycollection.insert(document)
print post_id