from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import EmailStr
from app.helpers.services.user_endpoint import UserServices
from app.core.db import get_db_session
from typing import List, Optional
from sqlmodel import Session, select
from app.core.models import (
    Profile,
    ProfileRead,
    ProfileCreate,
    ProfileUpdate,
    User,
)

# The `router` variable is creating an instance of the `APIRouter` class from the FastAPI framework.
# It is used to define the routes and endpoints for the Profile API.
router = APIRouter(prefix="/users/{user_id}/profile", tags=["Profile"])


@router.get("/", response_model=List[ProfileRead])
def read_profile(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
):
    user_service = UserServices(session=session)
    user = user_service.get_user(email=None, user_id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not Found")

    return user.profile_details


@router.post("/", response_model=ProfileRead)
def create_profile(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    profile: ProfileCreate,
):
    # check if user exists
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    profile.user_id = user_id
    profile_db_create = Profile.from_orm(profile)

    session.add(profile_db_create)
    session.commit()
    session.refresh(profile_db_create)

    return profile_db_create


@router.patch("/{profile_id}", response_model=ProfileRead)
def update_profile(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    profile_id: int,
    update_profile: ProfileUpdate,
):
    query_statement = (
        select(Profile)
        .where(
            Profile.user_id == user_id,
            Profile.profile_id == profile_id,
        )
        .limit(1)
    )
    profile = session.exec(query_statement).one_or_none()
    if profile is None:
        raise HTTPException(status_code=404, detail="User Contact Details Not Found")

    new_profile = update_profile.dict(exclude_unset=True)
    for key, value in new_profile.items():
        setattr(profile, key, value)

    session.add(profile)
    session.commit()
    session.refresh(profile)

    return profile


@router.delete("/{profile_id}")
def delete_profile(
    *, session: Session = Depends(get_db_session), user_id: int, profile_id: int
):
    query_statement = (
        select(Profile)
        .where(
            Profile.user_id == user_id,
            Profile.profile_id == profile_id,
        )
        .limit(1)
    )
    profile = session.exec(query_statement).one_or_none()
    if profile is None:
        raise HTTPException(status_code=404, detail="User Contact Details Not Found")

    session.delete(profile)
    session.commit()

    return {"ok": True}
