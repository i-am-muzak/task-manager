from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List

# Config
from sqlalchemy.orm import Session
from config.database import get_db

# Models
from db.models.user import User
from db.models.user_pages import UserPage

# Cruds
from db import cruds

# Schemas
from db.schemas.user_pages import UserPageRequestData, UserPageView

# Auth
from config.auth import get_current_user

# Lib
from lib.logger import logger
from lib.helper import create_slug

# Native
import time

router = APIRouter(tags=["user_pages"], prefix="/user-pages")


# Get all pages of logged user with selected project.
@router.get(
    "/all", description="Get all user pages...", response_model=List[UserPageView]
)
def getAll(
    project: int,
    user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    user_pages = (
        db.query(UserPage)
        .filter(UserPage.user_id == user["sub"])
        .filter(UserPage.project_id == project)
    )

    return user_pages


# Create a page for the logged user.
@router.post("/create", description="Create a user page.", response_model=UserPageView)
def createUserPage(
    data: UserPageRequestData,
    user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    slug = create_slug(text=data.title)

    instanceLength = (
        db.query(UserPage)
        .filter(UserPage.slug == slug)
        .filter(UserPage.user_id == user["sub"])
        .count()
    )

    if instanceLength > 0:
        slug = f"{slug}-{instanceLength + 1}"

    instance = cruds.user_pages.put(
        db=db,
        data={
            "title": data.title,
            "created_at": int(time.time()),
            "user_id": user["sub"],
            "project_id": data.project_id,
            "slug": slug,
        },
    )

    logger.info(
        f"Created page for user: {user['sub']} - Page title: {data.title} - Page ID: {instance.id}"
    )

    return instance
