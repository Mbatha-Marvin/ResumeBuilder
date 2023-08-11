from fastapi import APIRouter, Depends
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session
from app.v1.database.services.language_services import LanguageCRUDServices
from app.v1.database.models.language_model import (
    LanguageV1CreateRequest,
    LanguageV1Update,
    LanguageV1Read,
)

router = APIRouter(prefix="/user/{user_id}/language", tags=["Language Version 1"])


@router.get("/", response_model=List[LanguageV1Read])
def read_user_language(*, session: Session = Depends(get_db_session), user_id: int):
    langauge_crud_services = LanguageCRUDServices(session=session)
    return langauge_crud_services.read_user_lanngauge_details(user_id=user_id)


@router.post("/", response_model=LanguageV1Read)
def create_user_language(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_language_request: LanguageV1CreateRequest,
):
    langauge_crud_services = LanguageCRUDServices(session=session)
    return langauge_crud_services.create_user_language(
        user_id=user_id, user_language_request=user_language_request
    )


@router.patch("/{language_id}", response_model=LanguageV1Read)
def update_user_langauge(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    language_id: int,
    update_language: LanguageV1Update,
):
    langauge_crud_services = LanguageCRUDServices(session=session)
    return langauge_crud_services.update_user_language(
        user_id=user_id, langauge_id=language_id, update_language=update_language
    )


@router.delete("/{language_id}")
def delete_user_language(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    language_id: int,
):
    langauge_crud_services = LanguageCRUDServices(session=session)
    return langauge_crud_services.delete_user_language(
        user_id=user_id, language_id=language_id
    )
