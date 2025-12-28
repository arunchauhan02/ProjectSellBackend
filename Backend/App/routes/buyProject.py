from fastapi import APIRouter,Depends,UploadFile,File, HTTPException,Form,Depends
from app.Services.buyprojects import buyProject,getAllPurchases,getPurchase,createPaymentOrder
from app.core.dependencies import get_current_user,get_current_admin

router = APIRouter(prefix = "/projects",tags=["Buy Project"])

@router.post("/getallpurchases")
def get_all_purchases(user=Depends(get_current_admin)):
    return getAllPurchases()

@router.post("/getpurchase/{purchase_id}")
def getpurchase(purchase_id: str,user=Depends(get_current_user)):
    return getPurchase(purchase_id)

@router.post("/create-order/{project_id}")
def create_payment_order(project_id: str,user = Depends(get_current_user)):
    return createPaymentOrder(project_id,user)

    