from http import client
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
from flask import Flask, request
from flask_cors import CORS
import pymongo 
load_dotenv(find_dotenv())


client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
db = client["mamedov6119"]
col = db["users"]


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add("Access-Control-Allow-Methods", "DELETE, POST, GET, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")
    return response


import users_coll, pc_parts # function from users @app.route("/<name>") def user(name):



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)




























# load_dotenv(find_dotenv())

# password = os.environ.get("MONGO_PWD") # Password of the database from the .env file.

# connection_string = f"mongodb+srv://Murad:{password}@project.xtsgpdq.mongodb.net/?retryWrites=true&w=majority" 

# client = MongoClient(connection_string)

# # dbs = client.list_database_names() # Listing of the names of the databases existing.
# mydbs = client.mamedov6119 # Database
# users_collection = mydbs.users
# # # collections = mydbs.list_collection_names() #Collections in the database.


# # Inserting a document into the existing collention.
# def insert_document(document): # Document should be a query.
#     collection = mydbs.users #accessing the collection.
#     # users_document = { # Format of the document to be inserted.
#     #     "name" : "Murad",
#     #     "type" : "User"
#     # }
#     inserted_id = collection.insert_one(document).inserted_id # Inserting as well as getting the ID of the object inserted.
#     # print(inserted_id)

# # insert_document()


# # Creating a collection.
# # 'production' is the name of the collection to be created.
# # production = client.production
# # person_collection = production.person_collection

# user_coll = mydbs.users # Accessing the users collection

# def create_documents():
#     first_names = ["Murad", "Tim", "Jennifer", "Jose"]
#     last_names = ["Mammadov", "Smith", "Bart", "Cater"]
#     ages = [19, 21, 40, 23]

#     docs = [] # List of documents.

#     # For Loop to insert the documents in the collection.
#     for first_name, last_name, age in zip(first_names, last_names, ages):
#         doc = {"first_name" : first_name, "last_name" : last_name, "age" : age}
#         docs.append(doc)
#         # person_collection.insert_one(doc).
#     user_coll.insert_many(docs)

# # create_documents()

# printer = pprint.PrettyPrinter() # Imported module to nicely print the objects in the database.



# def find_all_people():
#     people = user_coll.find() # Can't directly access poeple(Cursor). Cursor is something to be iterated over.

#     # Iterating over the Cursor named: 'people'.
#     for person in people:
#         printer.pprint(person)

# # find_all_people()

# def find_murad():
#     murad = user_coll.find_one({"name" : "Murad"})
#     printer.pprint(murad)

# # find_murad()

# def count_all_poeple(): 
#     count = user_coll.count_documents(filter={}) # Count the number of documents in a collection.
#     print("Number of people:", count)

# # count_all_poeple()
# def get_person_by_id(person_id):
#     from bson.objectid import ObjectId # Converting a Cursor to an ObjectId.

#     _id = ObjectId(person_id)
#     person = user_coll.find_one({"_id" : _id})
#     printer.pprint(person)

# # get_person_by_id("634460ccdf0bc3dd86c40d9b")

# def get_age_range(min_age, max_age):
#     query = {"$and" : [ #Something like an if statement.
#             {"age" : {"$gte" : min_age}}, # gte = greater or equal than
#             {"age" : {"$lte" : max_age}} # lte = less or equal than
#         ]}
#     people = user_coll.find(query).sort("age")

#     for person in people:
#         printer.pprint(person)


# # get_age_range(18, 35)

# # Function to display only specified columns.
# def project_columns():
#     columns = {"_id" : 0, "first_name" : 1, "last_name" : 1} # Selecting the columns that we want. 0 for "NO", 1 for "YES". 
#     people = user_coll.find({}, columns)

#     for person in people:
#         printer.pprint(person)    


# # project_columns()

# def update_person_by_id(person_id):
#     from bson.objectid import ObjectId # Converting a Cursor to an ObjectId.

#     _id = ObjectId(person_id)

#     # all_updates = {
#     #     "$set" : {"new_field" : True}, # $set sets a new field to be the value of our choice. Also can be used to override fields.
#     #     "$inc" : {"age" : 1}, # $inc to increment a field's value.
#     #     "$rename" : {"first_name" : "first", "last_name" : "last"} # $rname to rename a field.
#     # }

#     # user_coll.update_one({"_id" : _id}, all_updates)

#     user_coll.update_one({"_id" : _id}, {"$unset" : {"new_field" : ""}}) # $unset to remove a field.

# # update_person_by_id("63506bc8e0c702beef825c49")

# def replace_one(person_id):
#     from bson.objectid import ObjectId # Converting a Cursor to an ObjectId.
#     _id = ObjectId(person_id)  

#     new_doc = {
#         "first_name" : "new first name",
#         "last_name" : "new last name",
#         "age" : 100
#     }

#     user_coll.replace_one({"_id" : _id}, new_doc)
    
# # replace_one("63506bc8e0c702beef825c49")

# # Deleting a document by an ID.
# def delete_doc_by_id(person_id):
#     from bson.objectid import ObjectId # Converting a Cursor to an ObjectId.
#     _id = ObjectId(person_id) 

#     user_coll.delete_one({"_id" : _id})   
#     # user_coll.delete_name({}) # Empty query to delete all documents in a collection.

# delete_doc_by_id("63506bc8e0c702beef825c49")

# # -------------------------------------------------------------------------------------------

# address = {
#     "_id" : "576767757a5765757575ccqbb2",
#     "street" : "Erszebet krt",
#     "number" : 8,
#     "city" : "Budapest",
#     "country" : "Hungary",
#     "zip" : "1073",

# }

# # Storing a document inside of another document.
# person = {
#     "_id" : "878737868626asd887c7",
#     "first_name" : "Feyruz",

#     # If a document belongs only to this person.
#     # "address" : { 
#     #     "_id" : "576767757a5765757575ccqbb2",
#     #     "street" : "Erszebet krt",
#     #     "number" : 8,
#     #     "city" : "Budapest",
#     #     "country" : "Hungary",
#     #     "zip" : "1073"
#     # }
# }

# def add_address_embed(person_id, address):
#     from bson.objectid import ObjectId # Converting a Cursor to an ObjectId.
#     _id = ObjectId(person_id)  

#     user_coll.update_one({"_id" : _id}, {"$addToSet" : {'addresses' : address}})

# # add_address_embed("63506bc8e0c702beef825c4c", address)



# def add_address_relationship(person_id, address):
#     from bson.objectid import ObjectId # Converting a Cursor to an ObjectId.
#     _id = ObjectId(person_id)

#     address = address.copy()
#     address["owner_id"] = person_id

#     address_collection = mydbs.address
#     address_collection.insert_one(address)

# # add_address_relationship("63506bc8e0c702beef825c4b", address)