from __main__ import app, db, request
from bson.json_util import dumps
from bson import ObjectId
from flask import jsonify, make_response
from flask_cors import cross_origin

col = db["users"]

# GET SPECIFIC USER
@app.route("/api/get_user/<name>")
def user(name):
    response = make_response()
    try:
        response = make_response(dumps(col.find({"_id" : ObjectId(name)})))
    except:
        pass
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


#GET
@app.route("/api/all_users/", methods=["GET"])
def AllUsers():
    response = make_response()
    try:
        response = make_response(dumps(col.find({})))
    except:
        pass
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


#POST
@app.route("/api/create_user", methods=["POST"]) 
def CreateUser():
    response = make_response(dumps({"Success" : 0}))
    try:
        data = request.json
        col.insert_one( {
            "name" : data["name"],
            "email" : data["email"],
            "password" : data["password"],
            "admin" : data["admin"]
        })
        response = make_response(dumps({"Success" : 1}))
        response.status_code = 200
    except:
        response.status_code = 201
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


# DELETE
@app.route("/api/del_by_id/<id>", methods=["DELETE"])
def DeleteUser(id):
    response = make_response(dumps({"Success" : 0}))
    try:
        col.delete_one( {"_id" : ObjectId(id)} )
        response = make_response(dumps({"Success" : 1}))
        response.status_code = 200
    except:
        response.status_code = 201
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response

# #GET
@app.route("/api/login/<email>/<password>", methods=["GET"])
def LogIn(email, password):
    response = make_response()
    try:
        response = make_response(dumps(list(col.find({"email" : email, "password" : password}))))
    except:
        pass
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response



    
