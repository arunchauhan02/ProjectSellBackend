from pymongo import MongoClient
import os

MONGODB_URI = "mongodb+srv://arunchauhan02:Kinetic6251@restaurantmanagement.xxigg.mongodb.net/?appName=RestaurantManagement"
DB_NAME = "MyDatabase"

if not MONGODB_URI:
    raise RuntimeError("MONGODB_URI is not set")

client = MongoClient(MONGODB_URI)

db = client[DB_NAME]
