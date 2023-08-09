from fastapi import APIRouter, Depends
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session
from app.v1.database.services.experience_services import ExperienceCRUDServices
from app.v1.database.models.experience_model import (
    ExperienceV1,
    ExperienceV1Create,
    ExperienceV1Read,
    ExperienceV1Update,
)

# The line `router = APIRouter(prefix="/users/{user_id}/experience", tags=["Experience"])` creates a
# new instance of the `APIRouter` class with a specified prefix and tags.
router = APIRouter(prefix="/users/{user_id}/experience", tags=["Experience Version 1"])


@router.get("/", response_model=List[ExperienceV1Read])
def read_user_experience(
    *,
    user_id: int,
    session: Session = Depends(get_db_session),
):
    experience_crud_services = ExperienceCRUDServices(session=session)
    return experience_crud_services.read_user_experience_details(user_id=user_id)


@router.post("/", response_model=ExperienceV1Read)
def create_user_experience(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_experience: ExperienceV1Create,
):
    experience_crud_services = ExperienceCRUDServices(session=session)
    return experience_crud_services.create_user_experience(
        user_id=user_id, user_experience=user_experience
    )


@router.patch("/{experience_id}", response_model=ExperienceV1Read)
def update_user_experience(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    experience_id: int,
    experience: ExperienceV1Update,
):
    experience_crud_services = ExperienceCRUDServices(session=session)
    return experience_crud_services.update_user_experience(
        user_id=user_id, experience_id=experience_id, experience=experience
    )


@router.delete("/{experience_id}")
def delete_user_experience(
    *, session: Session = Depends(get_db_session), user_id: int, experience_id: int
):
    experience_crud_services = ExperienceCRUDServices(session=session)
    return experience_crud_services.delete_user_experience(
        user_id=user_id, experience_id=experience_id
    )
