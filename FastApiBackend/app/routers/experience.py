from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.core.models import (
    Experience,
    ExperienceRead,
    ExperienceCreate,
    ExperienceUpdate,
    User,
)

router = APIRouter(prefix="/users/{user_id}/experience", tags=["Experience"])


@router.get("/", response_model=List[ExperienceRead])
def read_user_experience(
    *,
    user_id: int,
    session: Session = Depends(get_db_session),
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    query_statement = select(User).where(User.id == user_id).offset(offset).limit(limit)
    user = session.exec(query_statement).one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User not Found")

    return user.experience_details


@router.post("/", response_model=ExperienceRead)
def create_user_experience(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_experience: ExperienceCreate,
):
    # check if user exists
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    user_experience.user_id = user_id
    user_experience_db_create = Experience.from_orm(user_experience)

    session.add(user_experience_db_create)
    session.commit()
    session.refresh(user_experience_db_create)

    return user_experience_db_create


@router.patch("/{experience_id}", response_model=ExperienceRead)
def update_user_experience(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    experience_id: int,
    experience: ExperienceUpdate,
):
    query_statement = (
        select(Experience)
        .where(Experience.experience_id == experience_id, Experience.user_id == user_id)
        .limit(1)
    )
    user_experience = session.exec(query_statement).one_or_none()
    if user_experience is None:
        raise HTTPException(status_code=404, detail="User Experience Details Not Found")

    new_user_experience = experience.dict(exclude_unset=True)
    for key, value in new_user_experience.items():
        setattr(user_experience, key, value)

    session.add(user_experience)
    session.commit()
    session.refresh(user_experience)

    return user_experience


@router.delete("/{experience_id}")
def delete_user_experience(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    experience_id: int,
):
    query_statement = (
        select(Experience)
        .where(Experience.experience_id == experience_id, Experience.user_id == user_id)
        .limit(1)
    )
    user_experience = session.exec(query_statement).one_or_none()
    if user_experience is None:
        raise HTTPException(status_code=404, detail="User Experience Not Found")

    session.delete(user_experience)
    session.commit()

    return {"ok": True}
