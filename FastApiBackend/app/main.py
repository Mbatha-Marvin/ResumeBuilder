import uvicorn
from fastapi import FastAPI
from app.routers import users, experience, education, language, project, user_contact

from app import settings
from app.core.models import HealthCheck
from fastapi.middleware.cors import CORSMiddleware

from app.core.db import initialize_db

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
app.include_router(user_contact.router)


@app.on_event("startup")
def on_startup():
    initialize_db()


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
