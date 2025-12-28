from app.database import db
from fastapi import Depends
from app.core.dependencies import get_current_user
from bson import ObjectId
import os

def buyProject(project_id:str,user:dict):
    project = db.projects.find_one({"_id":ObjectId(project_id)})

    if not project:
        raise HTTPException(404,"Project not found")
    
    already_baught = db.orders.find_one({"user_id":user["_id"],"project_id":project["_id"]})

    if(already_baught):
        raise HTTPException(400,"Already purchased")
    
    purchase = {
        "user_id":user["_id"],
        "project_id":project["_id"],
        "amount_paid":project["price"],
        "payment_status":"success",
        "payment_id":"arunchauhan@axisbank.in"
    }

    db.orders.insert_one(purchase)

    return {
        "message":"You have successfully buy the project"
    }

def getAllPurchases():
    order_cursor = db["orders"].find()
    orders = list(order_cursor)

    for p in orders:
        p["_id"] = str(p["_id"])
        p["user_id"] = str(p["user_id"])
        p["project_id"] = str(p["project_id"])

    return orders


def getPurchase(purchase_id:str):
    purchase = db.orders.find_one({"_id":ObjectId(purchase_id)})

    purchase["_id"] = str(purchase["_id"])
    purchase["user_id"] = str(purchase["user_id"])
    purchase["project_id"] = str(purchase["project_id"])

    return purcase

def createPaymentOrder(project_id: str,user: dict):
    project = db.projects.find_one({"_id":ObjectId(project_id)})

    if not project:
        raise Exception("Project not found")

    rs = int(project["price"])*100

    order = client.order.create({
        "amount":rs,
        "currency":"INR",
        "payment_capture":1
    })

    return {
        "order_id":order["id"],
        "amount":project["price"],
        "project_id":project_id
    }

def verify_payment(data: dict,user: dict):
    body = data["razorpay_order_id"]+"|"+data["razorpay_payment_id"]

    expected_signature = hmac.new(
        os.getenv("RAZORPAY_SECRET").encode(),
        body.encode(),
        hashlib.sha256
    ).hexdigit()

    if expected_signature != data["razorpay_signature"]:
        raise HTTPException(400,"Invalid payment")
    
    project = db.projects.find_one({"_id":ObjectId(data["project_id"])})

    purchase = {
        "user_id":user["_id"],
        "project_id":project["_id"],
        "amount_paid":project["price"],
        "payment_status":"success",
        "payment_id":data["razorpay_payment_id"]
    }

    db.orders.insert_one(purchase)

    return {
        "message":"You have successfully buy the project"
    }