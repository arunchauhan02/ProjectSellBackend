from fastapi import APIRouter,Depends,UploadFile,File, HTTPException,Form
from app.models.Project import Project
from app.Services.projects import create_new_project,get_all_projects,deleteProject,editProject
from app.core.dependencies import get_current_user,get_current_admin
import cloudinary.uploader

router = APIRouter(prefix = "/projects",tags=["Project"])

async def uploadFile(file: UploadFile = File(...)):
    try:
        result = await run_in_threadpool(
            cloudinary.uploader.upload,
            file.file,
            folder="fastapi_uploads",
            verify=False
        )

        return {
                "success":True,
                "message":"Upload Successful",
                "url":result["secure_url"],
                "public_id":result["public_id"]
            }
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.get("/")
def getAllProjects():
    return get_all_projects()

@router.post("/createproject")
async def create_project(title: str = Form(...),
        description: str = Form(...),
        tech_stack: list = Form(...),
        difficulty:str = Form(...),
        url: str = Form(...),
        price: int = Form(...),
        Category:str = Form(...),
        file:UploadFile = File(...),admin:dict = Depends(get_current_admin)):
        
    result = uploadFile(file)

    return await create_new_project(title,description,difficulty,url,price,Category,file,result)

@router.put("/editprojects/{project_id}")
async def edit_project(
        project_id:str,
        title: str = Form(...),
        description: str = Form(...),
        tech_stack: list = Form(...),
        difficulty:str = Form(...),
        url: str = Form(...),
        price: int = Form(...),
        Category:str = Form(...),
        file:UploadFile=File(None),admin:dict = Depends(get_current_admin)):

    update_data = {}
    if file:
        result = uploadFile(file)
        update_data["fileUrl"] = result.url
        update_data["public_id"] = result.public_id

    return await editProject(update_data,project_id,title,description,tech_stack,difficulty,url,price,Category)

@router.delete("/deleteproject")
def delete_project(id: str,token: dict = Depends(get_current_admin)):
    return deleteProject(id)