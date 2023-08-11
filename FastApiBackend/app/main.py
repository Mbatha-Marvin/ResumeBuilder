from fastapi import FastAPI

# imports below are essential in loading version 1 models to avoid circular import error
from app.v1.database.models.user_model import UserV1
from app.v1.database.models.profile_model import ProfileV1
from app.v1.database.models.project_model import ProjectV1
from app.v1.database.models.language_model import LanguageV1
from app.v1.database.models.education_model import EducationV1
from app.v1.database.models.experience_model import ExperienceV1
from app.v1.database.models.referee_model import RefereeV1
from app.v1.database.models.certification_model import CertificationV1
from app.v1.database.models.verification_model import VerificationV1
from app.v1.database.models.health_status_model import HealthCheck

from app import settings

# from app.core.models import HealthCheck
from fastapi.middleware.cors import CORSMiddleware
from app.v1.database.dummy_data.loader import LoadDummyData

from app.core.db import initialize_db
from app.v1 import v1_router
from pathlib import Path
import uvicorn

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ALEMBIC_CONFIG_FILE = BASE_DIR / "alembic.ini"


app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    debug=settings.debug,
)

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(v1_router.v1_router)


@app.on_event("startup")
def on_startup():
    initialize_db()
    # initialize dummy data generator class
    dummy_data_loader_1 = LoadDummyData(
        user_id=1,
        dummy_email="test_email_1@email.com",
        dummy_phone_number="+254711215654",
    )
    dummy_data_loader_2 = LoadDummyData(
        user_id=2,
        dummy_email="test_email_2@email.com",
        dummy_phone_number="+254711217654",
    )
    dummy_data_loader_3 = LoadDummyData(
        user_id=3,
        dummy_email="test_email_3@email.com",
        dummy_phone_number="+254712215654",
    )

    print(dummy_data_loader_1.create_user())
    print(dummy_data_loader_2.create_user())
    print(dummy_data_loader_3.create_user())


@app.get("/", response_model=HealthCheck, tags=["Status"])
def health_check() -> dict:
    return {
        "name": settings.project_name,
        "version": settings.version,
        "description": settings.description,
    }
