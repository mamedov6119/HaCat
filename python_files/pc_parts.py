from __main__ import app, db, request
from bson.json_util import dumps
from bson import ObjectId

col = db["pc_parts"]

@app.route("/api/pc_parts/<name>")
def Find_Pc_Part(name):
    try:
        part = dumps(list(col.find({"_id" : ObjectId(name)})))
        return part
    except:
        return []


@app.route("/api/all_pc_parts", methods=["GET"])
def AllPcParts():
    try:
        pc_part = dumps(list(col.find({})))
        return pc_part
    except:
        return []


@app.route("/api/pc_parts", methods=["POST"])
def CreatePcPart():
    data = request.json
    col.insert_one( {
        "name" : data["name"],
        "category" : data["category"],
        "price" : data["price"]

    } )

    return dumps({"Success" : 1})
    

@app.route("/api/update_pc_part/<id>", methods=["POST"])
def UpdatePcPart(id):
    data = request.json
    col.update_one( {"_id" : ObjectId(id)},
        {
        "$set": 
            {
                "name" : data["name"], 
                "category" : data["category"], 
                "price" : data["price"]
            }
        }
    )

    return dumps({"Success" : 1})


@app.route("/api/del_pc_part/<id>", methods=["DELETE"])
def DeletePcPart(id):

    col.delete_one( {"_id" : ObjectId(id)} )

    return dumps({"Success" : 1})
