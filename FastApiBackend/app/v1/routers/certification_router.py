from fastapi import APIRouter, Depends
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.v1.database.services.certification_services import CertificationCRUDService
from app.v1.database.models.certification_model import (
    CertificationV1,
    CertificationV1Update,
    CertificationV1Read,
    CertificationV1Create,
)

router = APIRouter(
    prefix="/user/{user_id}/certification", tags=["Certification Version 1"]
)


@router.get(path="/", response_model=List[CertificationV1Read])
def read_user_certification(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
):
    certification_crud_service = CertificationCRUDService(session=session)
    return certification_crud_service.read_user_certifications(user_id=user_id)


@router.post(path="/", response_model=CertificationV1Read)
def create_user_certification(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_certification: CertificationV1Create,
):
    certification_crud_service = CertificationCRUDService(session=session)
    return certification_crud_service.create_user_certifications(
        user_certification=user_certification, user_id=user_id
    )


@router.patch(path="/{certification_id}", response_model=CertificationV1Read)
def update_user_certification(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    certification_id: int,
    update_certification: CertificationV1Update,
):
    certification_crud_service = CertificationCRUDService(session=session)
    return certification_crud_service.update_user_certifications(
        user_id=user_id,
        certification_id=certification_id,
        update_certification=update_certification,
    )


@router.delete(path="/{certification_id}")
def delete_user_certification(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    certification_id: int,
):
    certification_crud_service = CertificationCRUDService(session=session)
    return certification_crud_service.delete_user_certifications(
        user_id=user_id, certification_id=certification_id
    )
