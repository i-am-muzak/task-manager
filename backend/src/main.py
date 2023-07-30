from fastapi import FastAPI
from lib.settings import Settings
# Routers
from router.auth_router import auth_router

# Settings
settings = Settings()

app = FastAPI(title=settings.app_name)
app.include_router(auth_router)
