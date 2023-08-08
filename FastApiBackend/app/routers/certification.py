from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.core.models import (
    Certification,
    CertificationRead,
    CertificationCreate,
    CertificationUpdate,
    User,
)


# The `router` variable is creating an instance of the `APIRouter` class from the FastAPI framework.
# It is used to define the routes and endpoints for the `/users/{user_id}/Certification` path.
router = APIRouter(prefix="/users/{user_id}/certification", tags=["Certification"])


@router.get("/", response_model=List[CertificationRead])
def read_user_certification(
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

    return user.certification_details


@router.post("/", response_model=CertificationRead)
def create_user_certification(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_certification: CertificationCreate,
):
    # check if user exists
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    user_certification.user_id = user_id
    user_certification_db_create = Certification.from_orm(user_certification)

    session.add(user_certification_db_create)
    session.commit()
    session.refresh(user_certification_db_create)

    return user_certification_db_create


@router.patch("/{certification_id}", response_model=CertificationRead)
def update_user_langauge(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    certification_id: int,
    update_certification: CertificationUpdate,
):
    query_statement = (
        select(Certification)
        .where(
            Certification.certification_id == certification_id,
            Certification.user_id == user_id,
        )
        .limit(1)
    )
    user_certification = session.exec(query_statement).one_or_none()
    if user_certification is None:
        raise HTTPException(
            status_code=404, detail="User Certification Details Not Found"
        )

    new_user_certification = update_certification.dict(exclude_none=True)
    for key, value in new_user_certification.items():
        setattr(user_certification, key, value)

    session.add(user_certification)
    session.commit()
    session.refresh(user_certification)

    return user_certification


@router.delete("/{certification_id}")
def delete_user_Certification(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    certification_id: int,
):
    query_statement = (
        select(Certification)
        .where(
            Certification.certification_id == certification_id,
            Certification.user_id == user_id,
        )
        .limit(1)
    )
    user_certification = session.exec(query_statement).one_or_none()
    if user_certification is None:
        raise HTTPException(
            status_code=404, detail="User Certification Details Not Found"
        )

    session.delete(user_certification)
    session.commit()

    return {"ok": True}
