from app.models.Project import Project
from app.database import db
from bson import ObjectId
from fastapi import UploadFile,File, HTTPException,Form
import cloudinary.uploader

async def create_new_project(title: str = Form(...),
        description: str = Form(...),
        tech_stack: list = Form(...),
        difficulty:str = Form(...),
        url: str = Form(...),
        price: int = Form(...),
        Category:str = Form(...),resut: dict = {}):

    project_data = {
        "title": title,
        "description": description,
        "tech_stack": tech_stack,
        "difficulty": difficulty,
        "url": "tyuioiuyt",
        "createdAt": "2025-12-19T15:12:44.664473",
        "fileUrl":result.url,
        "public_id":result.public_id,
        "price": price,
        "category":Category,
        "rating":0,
        "noOfReviews":0
    }

    db.projects.insert_one(project_data)
    return {
        "message":"Project created successfully"
    }

def get_all_projects():
    project_cursor = db["projects"].find()
    projects = list(project_cursor)

    for p in projects:
        p["_id"] = str(p["_id"])

    return projects

def deleteProject(id: str):
    result = db.projects.delete_one({"_id":ObjectId(id)})

    if(result.deleted_count == 0):
        raise HTTPException(
            status_code=404,
            detail="Project not found")
    
    reviews_result = db.reviews.delete_many(
        {"project_id":id}
    )

    return {
        "success":True,
        "message":"Project deleted successfully",
        "reviews_result":reviews_result.deleted_count
    }


async def editProject(update_data:dict,
        project_id:str,
        title: str = Form(...),
        description: str = Form(...),
        tech_stack: list = Form(...),
        difficulty:str = Form(...),
        url: str = Form(...),
        price: int = Form(...),
        Category:str = Form(...)):

    print(tech_stack)
    if title: update_data["title"] = title
    if description:update_data["description"] = description
    if tech_stack:update_data["tech_stack"] = tech_stack
    if price is not None: update_data["price"] = price
    if Category:update_data["category"] = "poiu"
    if url:update_data["url"] = url

    result =  db.projects.update_one(
        {"_id":ObjectId(project_id)},
        {"$set":update_data}
    )
    if(result.matched_count == 0):
        raise HTTPException(status_code = 404,
        detail="Project not found")
    return {
        "success":True,
        "message":"Project edited successfully"
        }