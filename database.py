import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["shop_game"]
collection = database["user"]
collection2 = database["history"]

list_data = [
        { "_id": 1,
           "userid": "admin",
           "password": "admin",
           "email":"admin@hotmail.com",
           "phone":"0655495658",
           "wallet":1000
        },
        { "_id": 2,
           "userid": "test1",
           "password": "test1",
           "email":"test1@hotmail.com",
           "phone":"0655455555",
           "wallet":0
        }
]
list_history = [
        { "_id": 1,
           "userid": "admin",
           "Type" : "Topup",
           "Money" :50,
           "Into" : "wallet"
        },
        { "_id": 2,
           "userid": "admin",
           "Type" : "Buy",
           "Money" :50,
           "Into" : "ROV"
        }

]
collection.insert_many(list_data)
collection2.insert_many(list_history)

client.close()