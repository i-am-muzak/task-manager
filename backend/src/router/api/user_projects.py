from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List

# Config
from sqlalchemy.orm import Session
from config.database import get_db

# Models
from db.models.user import User
from db.models.user_projects import UserProject

# Cruds
from db import cruds

# Schemas
from db.schemas.user_projects import (
    UserProjectView,
    UserProjectRequestData
)

# Auth
from config.auth import get_current_user

# Lib
from lib.logger import logger
from lib.helper import create_slug

# Native
import time

router = APIRouter(tags=["user_projects"], prefix="/user-projects")


# Get all projects of logged user.
@router.get(
    "/all", description="Get all user projects...", response_model=List[UserProjectView]
)
def getAll(
    user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)
):
    user_projects = (
        db.query(UserProject).filter(UserProject.creator_id == user["sub"]).all()
    )

    return user_projects


# Create a project for the logged user.
@router.post(
    "/create", description="Create an user project.", response_model=UserProjectView
)
def createUserProject(
    data: UserProjectRequestData,
    user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    instance = db.query(UserProject).filter(UserProject.title == data.title).first()

    if instance:
        raise HTTPException(status_code=400, detail="There is already a project with given title.")

    instance = cruds.user_projects.put(db=db, data={
        "title": data.title,
        "created_at": int(time.time()),
        "creator_id": user["sub"],
        "slug": create_slug(text=data.title)
    })
    
    logger.info(f"Created project for user: {user['sub']} - Project title: {data.title} - Project ID: {instance.id}")

    return instance