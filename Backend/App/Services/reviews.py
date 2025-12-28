from app.database import db
from bson import ObjectId


def getReviews():
    reviews_cursor = db["reviews"].find()
    reviews_list = list(reviews_cursor)

    for r in reviews_list:
        r["_id"] = str(r["_id"])
        r["project_id"] = str(r["project_id"])
        r["user_id"] = str(r["user_id"])

    return reviews_list

def createReview(project_id:str,rating:int,comment:str,user:dict):
    review = {
        "project_id":project_id,
        "user_id":user["_id"],
        "userName":user["name"],
        "rating":rating,
        "comment":comment
    }

    db["reviews"].insert_one(review)

    Project = db.projects.find_one({"_id":ObjectId(project_id)})
    oldRating = Project.get("rating")
    noOfReviews = Project.get("noOfReviews")
    newRating = (oldRating*noOfReviews+rating)/(noOfReviews+1)
    result = db.projects.update_one(
        {"_id":ObjectId(project_id)},
        {
            "$set":{
                "rating":newRating,
                "noOfReviews":(noOfReviews+1)
            }
        }
    )

    return {
        "success":True,
        "message":"Thanks! for adding the review"
    }


def getReviewsForProject(project_id: str):
    reviews_cursor = db["reviews"].find({"project_id":project_id})

    reviews_list = list(reviews_cursor)

    for r in reviews_list:
        r["_id"] = str(r["_id"])
        r["project_id"] = str(r["project_id"])
        r["user_id"] = str(r["user_id"])

    return reviews_list

def deleteReview(review_id):
    result = db.reviews.delete_one({"_id":ObjectId(review_id)})

    if(result.deleted_count == 0):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            details="Review not found")

    return {"message":"Review Deleted Successfully"}