from fastapi import Depends, HTTPException, Query, APIRouter
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.helpers.DataValidations.user_endpoint import UserEndpointValidations

from app.core.models import UserRead, User, UserCreate, UserUpdate, UserProfileRead

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
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not Found")

    return user


@router.get("/{user_id}/profile", response_model=UserProfileRead)
def read_user_profile(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not Found")

    return user


@router.post("/", response_model=UserRead)
def create_user(
    *,
    session: Session = Depends(get_db_session),
    user: UserCreate,
):
    user_validation = UserEndpointValidations(session=session)

    if user_validation.email_exists(email=user.email):
        raise HTTPException(status_code=409, detail="Email already exists")
    db_user = User.from_orm(user)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.patch("/{user_id}", response_model=UserRead)
def update_user(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user: UserUpdate,
):
    user_validation = UserEndpointValidations(session=session)
    db_user_instance = user_validation.update_user(user_id=user_id, new_user=user)

    return db_user_instance


@router.delete("/{user_id}")
def delete_user(*, session: Session = Depends(get_db_session), user_id: int):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not Found")

    session.delete(user)
    session.commit()

    return {"ok": True}
