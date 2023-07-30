from fastapi import APIRouter

# Api Prefixed Routers
from router.auth.user import router

auth_router = APIRouter(prefix="/auth")
auth_router.include_router(router)