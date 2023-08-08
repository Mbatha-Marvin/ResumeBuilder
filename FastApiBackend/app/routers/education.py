from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import EmailStr
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.core.models import (
    Education,
    EducationRead,
    EducationCreate,
    EducationUpdate,
    User,
)

# The line `router = APIRouter(prefix="/users/{user_id}/education", tags=["Education"])` is creating a
# new instance of the `APIRouter` class.
router = APIRouter(prefix="/users/{user_id}/education", tags=["Education"])


@router.get("/", response_model=List[EducationRead])
def read_user_education(
    *,
    user_id: int,
    session: Session = Depends(get_db_session),
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    query_statement = (
        select(User).where(User.user_id == user_id).offset(offset).limit(limit)
    )
    user = session.exec(query_statement).one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User not Found")

    return user.education_details


@router.post("/", response_model=EducationRead)
def create_user_education(
    *,
    user_id: int,
    session: Session = Depends(get_db_session),
    user_education: EducationCreate,
):
    # check if user exists
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    user_education.user_id = user_id
    user_education_db_create = Education.from_orm(user_education)

    session.add(user_education_db_create)
    session.commit()
    session.refresh(user_education_db_create)

    return user_education_db_create


@router.patch("/{education_id}", response_model=EducationRead)
def update_user_education(
    *,
    user_id: int,
    session: Session = Depends(get_db_session),
    education_id: int,
    education_update: EducationUpdate,
):
    query_statement = (
        select(Education)
        .where(Education.education_id == education_id, Education.user_id == user_id)
        .limit(1)
    )
    db_user_education_instance = session.exec(query_statement).one_or_none()

    if db_user_education_instance is None:
        raise HTTPException(status_code=404, detail="User Education Details Not Found")

    new_user_education = education_update.dict(exclude_unset=True)
    for key, value in new_user_education.items():
        setattr(db_user_education_instance, key, value)

    session.add(db_user_education_instance)
    session.commit()
    session.refresh(db_user_education_instance)

    return db_user_education_instance


@router.delete("/{education_id}")
def delete_user_education(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    education_id: int,
):
    query_statement = (
        select(Education)
        .where(Education.education_id == education_id, Education.user_id == user_id)
        .limit(1)
    )
    user_education = session.exec(query_statement).one_or_none()

    if user_education is None:
        raise HTTPException(status_code=404, detail="User Education Details Not Found")

    session.delete(user_education)
    session.commit()

    return {"ok": True}
