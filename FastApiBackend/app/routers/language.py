from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.core.models import (
    Language,
    LanguageRead,
    LanguageCreate,
    LanguageUpdate,
    User,
)


router = APIRouter(prefix="/users/{user_id}/language", tags=["Language"])


@router.get("/", response_model=List[LanguageRead])
def read_user_language(
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

    return user.language_details


@router.post("/", response_model=LanguageRead)
def create_user_language(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_language: LanguageCreate,
):
    # check if user exists
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    user_language.user_id = user_id
    user_language_db_create = Language.from_orm(user_language)

    session.add(user_language_db_create)
    session.commit()
    session.refresh(user_language_db_create)

    return user_language_db_create


@router.patch("/{language_id}", response_model=LanguageRead)
def update_user_langauge(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    language_id: int,
    update_language: LanguageUpdate,
):
    query_statement = (
        select(Language)
        .where(Language.language_id == language_id, Language.user_id == user_id)
        .limit(1)
    )
    user_language = session.exec(query_statement).one_or_none()
    if user_language is None:
        raise HTTPException(status_code=404, detail="User Language Details Not Found")

    new_user_langauge = update_language.dict(exclude_unset=True)
    for key, value in new_user_langauge.items():
        setattr(user_language, key, value)

    session.add(user_language)
    session.commit()
    session.refresh(user_language)

    return user_language


@router.delete("/{language_id}")
def delete_user_language(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    language_id: int,
):
    query_statement = (
        select(Language)
        .where(Language.language_id == language_id, Language.user_id == user_id)
        .limit(1)
    )
    user_language = session.exec(query_statement).one_or_none()
    if user_language is None:
        raise HTTPException(status_code=404, detail="User Language Details Not Found")

    session.delete(user_language)
    session.commit()

    return {"ok": True}
