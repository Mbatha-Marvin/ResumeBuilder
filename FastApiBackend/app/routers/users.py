from fastapi import Depends, HTTPException, Query, APIRouter
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select

from app.core.models import (
    UserRead,
    User,
    UserCreate,
    UserUpdate,
)

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


@router.post("/{user_id}", response_model=UserRead)
def create_user(
    *,
    session: Session = Depends(get_db_session),
    user: UserCreate,
):
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
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    new_user_data = user.dict(exclude_unset=True)
    for key, value in new_user_data.items():
        setattr(db_user_instance, key, value)

    session.add(db_user_instance)
    session.commit()
    session.refresh(db_user_instance)

    return db_user_instance


@router.delete("/{user_id}")
def delete_user(*, session: Session = Depends(get_db_session), user_id: int):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not Found")

    session.delete(user)
    session.commit()

    return {"ok": True}
