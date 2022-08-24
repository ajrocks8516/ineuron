import pymongo


client = pymongo.MongoClient('mongodb+srv://Amanjain12:Amanjain12@anshit.5aeevdi.mongodb.net/?retryWrites=true&w=majority')
db = client.test

print(db)
d1 = {
    "username": "Anshit",
    "phone-number": "9559277726",
    "age": "21"
}
d = {
    "username": "Anshit",
    "phone-number": "9559277726",
    "age": "21"
}
d2 = {
    "username": "Anshit",
    "phone-number": "9559277726",
    "age": "21"
}
d3 = {
    "username": "Anshit",
    "phone-number": "9559277726",
    "age": "21"
}



db1 = client['mongo']
coll = db1['test']
coll.insert_one(d1)
