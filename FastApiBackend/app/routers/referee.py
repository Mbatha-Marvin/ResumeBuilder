from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.core.models import (
    Referee,
    RefereeRead,
    RefereeCreate,
    RefereeUpdate,
    User,
)


# The `router` variable is creating an instance of the `APIRouter` class from the FastAPI framework.
# It is used to define the routes and endpoints for the `/users/{user_id}/Referee` path.
router = APIRouter(prefix="/users/{user_id}/referee", tags=["Referee"])


@router.get("/", response_model=List[RefereeRead])
def read_user_referee(
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

    return user.referee_details


@router.post("/", response_model=RefereeRead)
def create_user_referee(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_referee: RefereeCreate,
):
    # check if user exists
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    user_referee.user_id = user_id
    user_referee_db_create = Referee.from_orm(user_referee)

    session.add(user_referee_db_create)
    session.commit()
    session.refresh(user_referee_db_create)

    return user_referee_db_create


@router.patch("/{referee_id}", response_model=RefereeRead)
def update_user_langauge(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    referee_id: int,
    update_referee: RefereeUpdate,
):
    query_statement = (
        select(Referee)
        .where(
            Referee.referee_id == referee_id,
            Referee.user_id == user_id,
        )
        .limit(1)
    )
    user_referee = session.exec(query_statement).one_or_none()
    if user_referee is None:
        raise HTTPException(status_code=404, detail="User Referee Details Not Found")

    new_user_referee = update_referee.dict(exclude_none=True)
    for key, value in new_user_referee.items():
        setattr(user_referee, key, value)

    session.add(user_referee)
    session.commit()
    session.refresh(user_referee)

    return user_referee


@router.delete("/{referee_id}")
def delete_user_referee(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    referee_id: int,
):
    query_statement = (
        select(Referee)
        .where(
            Referee.referee_id == referee_id,
            Referee.user_id == user_id,
        )
        .limit(1)
    )
    user_referee = session.exec(query_statement).one_or_none()
    if user_referee is None:
        raise HTTPException(status_code=404, detail="User Referee Details Not Found")

    session.delete(user_referee)
    session.commit()

    return {"ok": True}
