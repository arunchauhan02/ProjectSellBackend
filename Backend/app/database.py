from pymongo import MongoClient
import os

MONGODB_URI = "mongodb+srv://arunchauhan02:Kinetic6251@restaurantmanagement.xxigg.mongodb.net/?appName=RestaurantManagement"
DB_NAME = os.getenv("MONGO_DB_NAME")

if not MONGODB_URI:
    raise RuntimeError("MONGODB_URI is not set")

client = MongoClient(MONGODB_URI)

db = client[DB_NAME]
