from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.db import get_db_session
from typing import List, Optional
from sqlmodel import Session, select
from pydantic import EmailStr
from app.v1.database.services.referee_services import RefereeCRUDServices
from app.v1.database.models.referee_model import (
    RefereeV1,
    RefereeV1Update,
    RefereeV1Read,
    RefereeV1Create,
)

router = APIRouter(prefix="/users/{user_id}/referee", tags=["Referee Version 1"])


@router.get("/", response_model=List[RefereeV1Read])
def read_user_referee(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    referee_crud_services = RefereeCRUDServices(session=session)
    return referee_crud_services.read_user_referee_details(user_id=user_id)


@router.post("/", response_model=RefereeV1Read)
def create_user_referee(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_referee: RefereeV1Create,
):
    referee_crud_services = RefereeCRUDServices(session=session)
    return referee_crud_services.create_user_referee(
        user_id=user_id, user_referee=user_referee
    )


@router.patch("/{referee_id}", response_model=RefereeV1Read)
def update_user_langauge(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    referee_id: int,
    update_referee: RefereeV1Update,
):
    referee_crud_services = RefereeCRUDServices(session=session)
    return referee_crud_services.update_user_referee(
        user_id=user_id, referee_id=referee_id, update_referee=update_referee
    )


@router.delete("/{referee_id}")
def delete_user_referee(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    referee_id: int,
):
    referee_crud_services = RefereeCRUDServices(session=session)
    return referee_crud_services.delete_user_referee(
        user_id=user_id, referee_id=referee_id
    )
