from fastapi import Depends, HTTPException, Query, APIRouter
from app.core.db import get_db_session
from typing import List, Optional
from sqlmodel import Session, select
from app.helpers.services.user_endpoint import UserServices
from pydantic import EmailStr

from app.core.models import UserRead, User, UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[UserRead])
def read_users(
    *,
    session: Session = Depends(get_db_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.exec(select(User).offset(offset).limit(limit)).all()

    return users


@router.get("/{user_id}", response_model=UserRead)
def read_user(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    email: Optional[EmailStr] = None,
):
    user_service = UserServices(session=session)
    user_instance = user_service.get_user(email=email, user_id=user_id)
    if user_instance is None:
        raise HTTPException(status_code=404, detail="User not Found")
    else:
        return user_instance


@router.get("/{user_id}/full_profile")
def read_user_profile(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    email: Optional[EmailStr] = None,
):
    user_service = UserServices(session=session)
    user_instance = user_service.get_full_profile(email=email, user_id=user_id)

    if user_instance:
        return user_instance
    else:
        raise HTTPException(status_code=404, detail="User not Found")


@router.post("/", response_model=UserRead)
def create_user(
    *,
    session: Session = Depends(get_db_session),
    user: UserCreate,
):
    user_service = UserServices(session=session)
    new_user_instance = user_service.create_user(new_user=user)

    return new_user_instance


@router.patch("/{user_id}", response_model=UserRead)
def update_user(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user: UserUpdate,
):
    user_service = UserServices(session=session)
    db_user_instance = user_service.update_user(user_id=user_id, new_user=user)

    return db_user_instance


@router.delete("/{user_id}")
def delete_user(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    email: Optional[EmailStr] = None,
):
    user_service = UserServices(session=session)
    # if deletion is successfull
    if user_service.delete_user(user_id=user_id, email=email):
        return {"ok": True}
    else:
        raise HTTPException(status_code=404, detail="User not Found")
