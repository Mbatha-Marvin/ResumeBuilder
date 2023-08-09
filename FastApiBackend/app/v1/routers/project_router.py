from fastapi import APIRouter, Depends
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session
from pydantic import EmailStr
from app.v1.database.services.project_services import ProjectCRUDServices
from app.v1.database.models.project_model import (
    ProjectV1,
    ProjectV1Update,
    ProjectV1Read,
    ProjectV1Create,
)

router = APIRouter(prefix="/users/{user_id}/project", tags=["Project Version 1"])


@router.get("/", response_model=List[ProjectV1Read])
def read_user_project(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
):
    project_crud_services = ProjectCRUDServices(session=session)
    return project_crud_services.read_user_project_details(user_id=user_id)


@router.post("/", response_model=ProjectV1Read)
def create_user_project(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_project: ProjectV1Create,
):
    project_crud_services = ProjectCRUDServices(session=session)
    return project_crud_services.create_user_project(
        user_id=user_id, user_project=user_project
    )


@router.patch("/{project_id}", response_model=ProjectV1Read)
def update_user_project(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    project_id: int,
    update_project: ProjectV1Update,
):
    project_crud_services = ProjectCRUDServices(session=session)
    return project_crud_services.update_user_project(
        user_id=user_id, project_id=project_id, update_project=update_project
    )


@router.delete("/{project_id}")
def delete_user_project(
    *, session: Session = Depends(get_db_session), user_id: int, project_id: int
):
    project_crud_services = ProjectCRUDServices(session=session)
    return project_crud_services.delete_user_project(
        user_id=user_id, project_id=project_id
    )
