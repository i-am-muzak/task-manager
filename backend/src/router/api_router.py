from fastapi import APIRouter

# Api Prefixed Routers
from router.api.user_projects import router as user_projects_router

api_router = APIRouter(prefix="/api")
api_router.include_router(user_projects_router)