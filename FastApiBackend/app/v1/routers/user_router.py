from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.db import get_db_session
from typing import List, Optional
from sqlmodel import Session, select
from pydantic import EmailStr
from app.v1.database.services.user_services import UserCRUDService
from app.v1.database.models.user_model import (
    UserV1,
    UserV1Update,
    UserV1Read,
    UserV1Create,
)
from app.v1.database.services.verification_services import CreateVerificationDetails


router = APIRouter(tags=["Users Version 1"])


@router.get(path="/users", response_model=List[UserV1Read])
def read_users(
    *,
    session: Session = Depends(get_db_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.exec(select(UserV1).offset(offset).limit(limit)).all()

    return users


@router.get(path="/user/{user_id}", response_model=UserV1Read)
def read_user(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    email: Optional[EmailStr] = None,
):
    user_crud_service = UserCRUDService(session=session)
    user_in_db = user_crud_service.get_user(email=email, user_id=user_id)

    if user_in_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return user_in_db


@router.get(path="/user/{user_id}/full_profile")
def read_full_profile(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    email: Optional[EmailStr] = None,
):
    user_crud_service = UserCRUDService(session=session)
    return user_crud_service.get_full_user_details(email=email, user_id=user_id)


@router.post("/user/", response_model=UserV1Read)
def create_user(
    *,
    session: Session = Depends(get_db_session),
    user: UserV1Create,
):
    user_crud_service = UserCRUDService(session=session)
    new_user_instance = user_crud_service.create_user(new_user=user)

    return new_user_instance


@router.patch("/user/{user_id}", response_model=UserV1Read)
def update_user(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user: UserV1Update,
):
    user_crud_service = UserCRUDService(session=session)
    db_user_instance = user_crud_service.update_user(user_id=user_id, new_user=user)

    return db_user_instance


@router.delete("/user/{user_id}")
def delete_user(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    email: Optional[EmailStr] = None,
):
    user_crud_service = UserCRUDService(session=session)
    user_crud_service.delete_user(user_id=user_id, email=email)
    return {"Status": "Successfully deleted"}
