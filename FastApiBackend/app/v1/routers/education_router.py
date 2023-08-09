from fastapi import APIRouter, Depends
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session
from app.v1.database.services.education_services import EducationCRUDService
from app.v1.database.models.education_model import (
    EducationV1,
    EducationV1Update,
    EducationV1Read,
    EducationV1Create,
)

router = APIRouter(prefix="/user/{user_id}/eduaction", tags=["Education Version 1"])


@router.get(path="/", response_model=List[EducationV1Read])
def read_user_education_details(
    *, session: Session = Depends(get_db_session), user_id: int
):
    education_crud_service = EducationCRUDService(session=session)
    return education_crud_service.read_user_education_details(user_id=user_id)


@router.post("/", response_model=EducationV1Read)
def create_user_education(
    *,
    user_id: int,
    session: Session = Depends(get_db_session),
    user_education: EducationV1Create,
):
    education_crud_service = EducationCRUDService(session=session)
    return education_crud_service.create_user_education(
        user_id=user_id, user_education=user_education
    )


@router.patch("/{education_id}", response_model=EducationV1Read)
def update_user_education(
    *,
    user_id: int,
    session: Session = Depends(get_db_session),
    education_id: int,
    education_update: EducationV1Update,
):
    education_crud_service = EducationCRUDService(session=session)
    return education_crud_service.update_user_Education(
        user_id=user_id, education_id=education_id, education_update=education_update
    )


@router.delete("/{education_id}")
def delete_user_education(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    education_id: int,
):
    education_crud_service = EducationCRUDService(session=session)
    return education_crud_service.delete_user_education(
        user_id=user_id, education_id=education_id
    )
