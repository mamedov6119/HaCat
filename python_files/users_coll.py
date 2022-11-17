# from __main__ import app, mydbs, users_collection
# from bson.objectid import ObjectId # Converting a Cursor to an ObjectId.
# from bson.json_util import dumps
# @app.route("/<id>", methods=["GET"])
# def get_user_by_id(id):
#     try:
#         _id = ObjectId(id)
#         person = users_collection.find_one({"_id" : _id})
#         return person
#     except:
#         return []


# @app.route("/", methods=["GET"])
# def AllUsers():
#     try:
#         user = dumps(list(users_collection.find({})))
#         return user
#     except:
#         return []

from __main__ import app, db, request
from bson.json_util import dumps
from bson import ObjectId

col = db["users"]

@app.route("/api/get_user/<name>")
def user(name):
    try:
        user = dumps(list(col.find({"_id" : ObjectId(name)})))
        return user
    except:
        return []

#GET
@app.route("/api/all_users/", methods=["GET"])
def AllUsers():
    try:
        user = dumps(list(col.find({})))
        return user
    except:
        return []

#POST
@app.route("/api/create_user", methods=["POST"]) 
def CreateUser():
    data = request.json
    col.insert_one( {
        "name" : data["name"],
        "email" : data["email"],
        "password" : data["password"],
        "admin" : data["admin"]
    })
    return dumps({"Success" : 1})

#DELETE
@app.route("/api/del_by_id/<id>", methods=["DELETE"])
def DeleteUser(id):
    col.delete_one( {"_id" : ObjectId(id)} )
    return dumps({"Success" : 1})

#GET
@app.route("/api/login/<id>/<password>", methods=["GET"])
def LogIn(id, password):
    try:
        user = dumps(list(col.find({"_id" : ObjectId(id), "password" : password})))
        if user == "NULL":
            return []
        return user
    except:
        return []



    
