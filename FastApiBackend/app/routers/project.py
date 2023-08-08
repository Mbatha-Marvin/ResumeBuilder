from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.core.models import (
    Project,
    ProjectRead,
    ProjectCreate,
    ProjectUpdate,
    User,
)

# The `router` variable is creating an instance of the `APIRouter` class from the FastAPI framework.
# It is used to define the routes and endpoints for the project-related operations.
router = APIRouter(prefix="/users/{user_id}/project", tags=["Project"])


@router.get("/", response_model=List[ProjectRead])
def read_user_project(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    query_statement = (
        select(User).where(User.user_id == user_id).offset(offset).limit(limit)
    )
    user = session.exec(query_statement).one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User not Found")

    return user.project_details


@router.post("/", response_model=ProjectRead)
def create_user_project(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_project: ProjectCreate,
):
    # check if user exists
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    user_project.user_id = user_id
    user_project_db_create = Project.from_orm(user_project)

    session.add(user_project_db_create)
    session.commit()
    session.refresh(user_project_db_create)

    return user_project_db_create


@router.patch("/{project_id}", response_model=ProjectRead)
def update_user_project(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    project_id: int,
    update_project: ProjectUpdate,
):
    query_statement = (
        select(Project)
        .where(Project.user_id == user_id, Project.project_id == project_id)
        .limit(1)
    )
    user_project = session.exec(query_statement).one_or_none()
    if user_project is None:
        raise HTTPException(status_code=404, detail="User Project Details Not Found")

    new_user_project = update_project.dict(exclude_unset=True)
    for key, value in new_user_project.items():
        setattr(user_project, key, value)

    session.add(user_project)
    session.commit()
    session.refresh(user_project)

    return user_project


@router.delete("/{project_id}")
def delete_user_project(
    *, session: Session = Depends(get_db_session), user_id: int, project_id: int
):
    query_statement = (
        select(Project)
        .where(Project.user_id == user_id, Project.project_id == project_id)
        .limit(1)
    )
    user_project = session.exec(query_statement).one_or_none()
    if user_project is None:
        raise HTTPException(status_code=404, detail="User Project Details Not Found")

    session.delete(user_project)
    session.commit()

    return {"ok": True}
