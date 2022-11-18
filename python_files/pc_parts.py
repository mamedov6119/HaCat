from __main__ import app, db, request
from bson.json_util import dumps
from bson import ObjectId
from flask import jsonify, make_response
col = db["pc_parts"]




@app.route("/api/pc_parts/<name>", methods=["GET"]) 
def Find_Pc_Part(name):
    response = make_response(dumps({"Success" : 0}))
    try:

        response = make_response(dumps(list(col.find({"_id" : ObjectId(name)}))))
        response.status_code = 200
    except:
        response.status_code = 400
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route("/api/all_pc_parts", methods=["GET"]) 
def AllPcParts():
    response = make_response(dumps({"Success" : 0}))
    try:

        response = make_response(dumps(list(col.find({}))))
        response.status_code = 200
    except:
        response.status_code = 400
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response



@app.route("/api/pc_parts", methods=["POST"]) 
def CreatePcPart():
    response = make_response(dumps({"Success" : 0}))
    try:
        data = request.json
        col.insert_one( {
            "name" : data["name"],
            "category" : data["category"],
            "price" : data["price"]
            } )           
        response = make_response(dumps({"Success" : 1}))
        response.status_code = 200
    except:
        response.status_code = 400
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route("/api/update_pc_part/<id>", methods=["POST"]) 
def UpdatePcPart(id):
    response = make_response(dumps({"Success" : 0}))
    try:
        data = request.json
        col.update_one( {"_id" : ObjectId(id)},
            { "$set":
                {
                    "name" : data["name"], 
                    "category" : data["category"], 
                    "price" : data["price"]
                }
            }
        )         
        response = make_response(dumps({"Success" : 1}))
        response.status_code = 200
    except:
        response.status_code = 400
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response
    


@app.route("/api/del_pc_part/<id>", methods=["DELETE"]) 
def DeletePcPart(id):
    response = make_response(dumps({"Success" : 0}))
    try:
        col.delete_one( {"_id" : ObjectId(id)} )       
        response = make_response(dumps({"Success" : 1}))
        response.status_code = 200
    except:
        response.status_code = 400
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response

