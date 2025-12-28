from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.routes import auth, users, project,buyProject,reviews
from app.core import cloudinary_config

app = FastAPI(title="Student Project Marketplace")

@app.get("/")
def root():
    return {"Message":"Python is good"}

app.include_router(auth.router)
app.include_router(project.router)
app.include_router(buyProject.router)
app.include_router(reviews.router)


