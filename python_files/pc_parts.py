from __main__ import app, db, request
import random
from bson.json_util import dumps
from bson import ObjectId
from flask import jsonify, make_response
import json
import os
col = db["pc_parts"]

path = os.path.dirname(os.path.abspath(__file__)).replace("python_files", "pc_comps")

case_accessory = json.loads(open(os.path.join(path, "case-accessory.json"), "r").read())
case_fan = json.loads(open(os.path.join(path, "case-fan.json"), "r").read())
case = json.loads(open(os.path.join(path, "case.json"), "r").read())
cpu_cooler = json.loads(open(os.path.join(path, "cpu-cooler.json"), "r").read())
cpu = json.loads(open(os.path.join(path, "cpu.json"), "r").read())
external_hard_drive = json.loads(open(os.path.join(path, "external-hard-drive.json"), "r").read())
heaphones = json.loads(open(os.path.join(path, "headphones.json"), "r").read())
internal_hard_drive = json.loads(open(os.path.join(path, "internal-hard-drive.json"), "r").read())
keyboards = json.loads(open(os.path.join(path, "keyboard.json"), "r").read())
memory = json.loads(open(os.path.join(path, "memory.json"), "r").read())
monitor = json.loads(open(os.path.join(path, "monitor.json"), "r").read())
motherboard = json.loads(open(os.path.join(path, "motherboard.json"), "r").read())
mouse = json.loads(open(os.path.join(path, "mouse.json"), "r").read())
power_supply = json.loads(open(os.path.join(path, "power-supply.json"), "r").read())
speakers = json.loads(open(os.path.join(path, "speakers.json"), "r").read())
thermal_paste = json.loads(open(os.path.join(path, "thermal-paste.json"), "r").read())
video_card = json.loads(open(os.path.join(path, "video-card.json"), "r").read())
webcam = json.loads(open(os.path.join(path, "webcam.json"), "r").read())
wireless_network_card = json.loads(open(os.path.join(path, "wireless-network-card.json"), "r").read())

def select_rand (array): 
    user = array[random.randint(0, len(array) - 1)]
    while(user["price_usd"] == None):
        user = array[random.randint(0, len(array) - 1)]
    return user

@app.route("/api/pc_parts/random_build/<price>", methods=["GET"])
def build_pc_rand(price):
    response = make_response(dumps({"Success": 0}))
    try:
        
        result = create(price)
        while (result["Money_left"] * -1 > 3500):
            result = create(price)
        response = make_response(dumps(result))
        response.status_code = 200
    except Exception as e:
        print(e)
        response.status_code = 400
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response

def create(price):
    result ={}
    price = float(price)



    # case accessory
    user_case_accessory = select_rand(case_accessory)
    result['case_accessory'] = user_case_accessory
    price -= float(user_case_accessory["price_usd"])
    
    
    # case accessory
    
    # case fan
    user_case_fan = select_rand(case_fan)
    result['case_fan'] = user_case_fan
    price -= float(user_case_fan["price_usd"])

    # case fan 

    # case
    user_case = select_rand (case)
    result['case'] = user_case
    price -= float(user_case["price_usd"])

    # case

    # cpu cooler 
    user_cpu_cooler = select_rand (cpu_cooler) 
    result['cpu_cooler'] = user_cpu_cooler
    price -= float(user_cpu_cooler["price_usd"])

    # cpu cooler

    # cpu
    user_cpu = select_rand (cpu)
    result['cpu'] = user_cpu
    price -= float(user_cpu["price_usd"])
    
    # cpu

    # user video card
    user_video_card = select_rand (video_card)
    result['video_card'] = user_video_card
    price -= float(user_video_card["price_usd"])

    # user video card

    # external hard drive
    user_external_hard_drive = select_rand (external_hard_drive)
    result['external_hard_drive'] = user_external_hard_drive
    price -= float(user_external_hard_drive["price_usd"])

    # external hard drive

    # headphones
    user_headphones = select_rand (heaphones)
    result['headphones'] = user_headphones
    price -= float(user_headphones["price_usd"])

    # headphones

    # internal hard drive
    user_internal_hard_drive = select_rand (internal_hard_drive)
    result['internal_hard_drive'] = user_internal_hard_drive
    price -= float(user_internal_hard_drive["price_usd"])

    # internal hard drive

    # keyboard
    user_keyboard = select_rand (keyboards)
    result['keyboard'] = user_keyboard
    price -= float(user_keyboard["price_usd"])

    # keyboard 

    # memory
    user_memory = select_rand (memory)
    result['memory'] = user_memory
    price -= float(user_memory["price_usd"])
    
    # memory

    # monitor
    user_monitor = select_rand (monitor)
    result['monitor'] = user_monitor
    price -= float(user_monitor["price_usd"])

    # monitor

    # motherboard
    user_motherboard = select_rand (motherboard)
    result['motherboard'] = user_motherboard
    price -= float(user_motherboard["price_usd"])

    # motherboard

    # mouse
    user_mouse = select_rand (mouse)
    result['mouse'] = user_mouse
    price -= float(user_mouse["price_usd"])

    # mouse

    # power supply
    user_power_supply = select_rand (power_supply)
    result['power_supply'] = user_power_supply
    price -= float(user_power_supply["price_usd"])

    # power supply

    # speakers
    user_speakers = select_rand (speakers)
    result['speakers'] = user_speakers
    price -= float(user_speakers["price_usd"])

    # speakers

    # thermal paste
    user_thermal_paste = select_rand (thermal_paste)
    result['thermal_paste'] = user_thermal_paste
    price -= float(user_thermal_paste["price_usd"])

    # thermal paste

    # webcam
    user_webcam = select_rand (webcam)
    result['webcam'] = user_webcam
    price -= float(user_webcam["price_usd"])

    # webcam

    # wireless network card
    user_wireless_network_card = select_rand (wireless_network_card)
    result['wireless_network_card'] = user_wireless_network_card
    price -= float(user_wireless_network_card["price_usd"])

    # wireless network card
    return {"Money_left": price, "data": result}









@app.route("/api/pc_parts/<name>", methods=["GET"])
def Find_Pc_Part(name):
    response = make_response(dumps({"Success": 0}))
    try:

        response = make_response(
            dumps(list(col.find({"_id": ObjectId(name)}))))
        response.status_code = 200
    except:
        response.status_code = 400
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route("/api/all_pc_parts", methods=["GET"])
def AllPcParts():
    response = make_response(dumps({"Success": 0}))
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
    response = make_response(dumps({"Success": 0}))
    try:
        data = request.json
        col.insert_one({
            "name": data["name"],
            "category": data["category"],
            "price": data["price"]
        })
        response = make_response(dumps({"Success": 1}))
        response.status_code = 200
    except:
        response.status_code = 400
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route("/api/update_pc_part/<id>", methods=["POST"])
def UpdatePcPart(id):
    response = make_response(dumps({"Success": 0}))
    try:
        data = request.json
        col.update_one({"_id": ObjectId(id)},
                       {"$set":
                        {
                            "name": data["name"],
                            "category": data["category"],
                            "price": data["price"]
                        }
                        }
                       )
        response = make_response(dumps({"Success": 1}))
        response.status_code = 200
    except:
        response.status_code = 400
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route("/api/del_pc_part/<id>", methods=["DELETE"])
def DeletePcPart(id):
    response = make_response(dumps({"Success": 0}))
    try:
        col.delete_one({"_id": ObjectId(id)})
        response = make_response(dumps({"Success": 1}))
        response.status_code = 200
    except:
        response.status_code = 400
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response
