from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.core.models import (
    UserContact,
    UserContactRead,
    UserContactCreate,
    UserContactUpdate,
    User,
)

router = APIRouter(prefix="/users/{user_id}/user_contact", tags=["UserContact"])


@router.get("/", response_model=List[UserContactRead])
def read_user_contact(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    query_statement = select(User).where(User.id == user_id).offset(offset).limit(limit)
    user = session.exec(query_statement).one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User not Found")

    return user.user_contact_details


@router.post("/", response_model=UserContactRead)
def create_user_contact(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_contact: UserContactCreate,
):
    # check if user exists
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    user_contact.user_id = user_id
    user_contact_db_create = UserContact.from_orm(user_contact)

    session.add(user_contact_db_create)
    session.commit()
    session.refresh(user_contact_db_create)

    return user_contact_db_create


@router.patch("/{user_contact_id}", response_model=UserContactRead)
def update_user_contact(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_contact_id: int,
    update_user_contact: UserContactUpdate,
):
    query_statement = (
        select(UserContact)
        .where(
            UserContact.user_id == user_id,
            UserContact.user_contact_id == user_contact_id,
        )
        .limit(1)
    )
    user_contact = session.exec(query_statement).one_or_none()
    if user_contact is None:
        raise HTTPException(status_code=404, detail="User Contact Details Not Found")

    new_user_contact = update_user_contact.dict(exclude_unset=True)
    for key, value in new_user_contact.items():
        setattr(user_contact, key, value)

    session.add(user_contact)
    session.commit()
    session.refresh(user_contact)

    return user_contact


@router.delete("/{user_contact_id}")
def delete_user_contact(
    *, session: Session = Depends(get_db_session), user_id: int, user_contact_id: int
):
    query_statement = (
        select(UserContact)
        .where(
            UserContact.user_id == user_id,
            UserContact.user_contact_id == user_contact_id,
        )
        .limit(1)
    )
    user_contact = session.exec(query_statement).one_or_none()
    if user_contact is None:
        raise HTTPException(status_code=404, detail="User Contact Details Not Found")

    session.delete(user_contact)
    session.commit()

    return {"ok": True}
