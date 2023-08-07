import uvicorn
from fastapi import FastAPI
from app.routers import (
    users,
    experience,
    education,
    language,
    project,
    profile,
    certification,
    referee,
)

from app import settings
from app.core.models import HealthCheck
from fastapi.middleware.cors import CORSMiddleware

from app.core.db import initialize_db
from app.helpers.database.alembic_migrations import AlembicMigrations
from app.helpers.database.dummy_data import create_dummy_user
from pathlib import Path

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

app.include_router(users.router)
app.include_router(experience.router)
app.include_router(education.router)
app.include_router(language.router)
app.include_router(project.router)
app.include_router(profile.router)
app.include_router(certification.router)
app.include_router(referee.router)


@app.on_event("startup")
def on_startup():
    initialize_db()
    # alembic_instance = AlembicMigrations(config_path=str(ALEMBIC_CONFIG_FILE))
    # alembic_instance.upgrade_to_alembic_head()
    print(
        create_dummy_user(
            user_id=1, phone_number="+254711215654", email="test_1@email.com"
        )
    )
    print(
        create_dummy_user(
            user_id=2, phone_number="+254711215655", email="test_2@email.com"
        )
    )
    print(
        create_dummy_user(
            user_id=3, phone_number="+254711215634", email="test_3@email.com"
        )
    )


@app.get("/", response_model=HealthCheck, tags=["Status"])
def health_check() -> dict:
    return {
        "name": settings.project_name,
        "version": settings.version,
        "description": settings.description,
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=5000,
        host="0.0.0.0",
        reload=True,
        use_colors=True,
    )
