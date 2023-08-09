from fastapi import APIRouter
from app import settings
from app.v1.database.models.health_status_model import HealthCheck
from app.v1.routers import (
    user_router,
    profile_router,
    education_router,
    experience_router,
    language_router,
    certification_router,
    referee_router,
    project_router,
)

v1_router = APIRouter(prefix="/api/v1")


@v1_router.get("/", response_model=HealthCheck, tags=["StatusV1"])
def health_check() -> dict:
    return {
        "name": settings.project_name,
        "version": "1.0.0",
        "description": settings.description,
    }


v1_router.include_router(user_router.router)
v1_router.include_router(profile_router.router)
v1_router.include_router(education_router.router)
v1_router.include_router(experience_router.router)
v1_router.include_router(language_router.router)
v1_router.include_router(certification_router.router)
v1_router.include_router(referee_router.router)
v1_router.include_router(project_router.router)
