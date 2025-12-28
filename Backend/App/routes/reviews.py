from fastapi import APIRouter,Depends,UploadFile,File, HTTPException,Form
from app.models.Project import Project
from app.Services.projects import create_new_project,get_all_projects,deleteProject,editProject
from app.core.dependencies import get_current_user,get_current_admin
from app.Services.reviews import getReviews,createReview,getReviewsForProject,deleteReview


router = APIRouter(prefix = "/reviews",tags=["Reviews"])

@router.get("/getallreviews")
def getallreviews():
    return getReviews()

@router.post("/createreview")
def createreview(project_id:str,rating:int,comment:str,user=Depends(get_current_user)):
    return createReview(project_id,rating,comment,user)

@router.get("/getreviewsforproject/{project_id}")
def getreviewsforproject(project_id:str):
    return getReviewsForProject(project_id)

@router.delete("/deleteReview/{review_id}")
def deletereview(review_id:str,user = Depends(get_current_admin)):
    return deleteReview(review_id)

