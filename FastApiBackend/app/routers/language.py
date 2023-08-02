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


# The `router` variable is creating an instance of the `APIRouter` class from the FastAPI framework.
# It is used to define the routes and endpoints for the `/users/{user_id}/language` path.
router = APIRouter(prefix="/users/{user_id}/language", tags=["Language"])


@router.get("/", response_model=List[LanguageRead])
def read_user_language(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    """
    The function `read_user_language` retrieves the language details of a user from the database based
    on the provided user ID, offset, and limit parameters.

    :param session: The `session` parameter is used to pass the database session to the function. It is
    of type `Session` and is obtained using the `get_db_session` dependency
    :type session: Session
    :param user_id: The `user_id` parameter is an integer that represents the ID of the user whose
    language details we want to retrieve
    :type user_id: int
    :param offset: The `offset` parameter is used to specify the number of records to skip before
    returning the results. It is used for pagination purposes, allowing you to retrieve a specific
    subset of records, defaults to 0
    :type offset: int (optional)
    :param limit: The `limit` parameter is used to specify the maximum number of language details to be
    returned in the response. It has a default value of 10 and is constrained to a maximum value of 15
    :type limit: int
    :return: the language details of a user. The response is of type List[LanguageRead].
    """
    query_statement = (
        select(User).where(User.user_id == user_id).offset(offset).limit(limit)
    )
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
    """
    The above function creates a new user language entry in the database for a given user.

    :param session: The `session` parameter is used to access the database session. It is of type
    `Session` and is obtained using the `get_db_session` dependency
    :type session: Session
    :param user_id: The `user_id` parameter is an integer that represents the ID of the user for whom we
    want to create a language entry
    :type user_id: int
    :param user_language: The `user_language` parameter is of type `LanguageCreate`, which is a Pydantic
    model representing the data required to create a new user language. It contains the following
    fields:
    :type user_language: LanguageCreate
    :return: an instance of the `LanguageRead` model.
    """
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
    """
    The above function updates the language details of a user.

    :param session: The `session` parameter is of type `Session` and is used to interact with the
    database session. It is obtained using the `get_db_session` dependency
    :type session: Session
    :param user_id: The `user_id` parameter represents the ID of the user whose language details are
    being updated
    :type user_id: int
    :param language_id: The `language_id` parameter represents the ID of the language that needs to be
    updated. It is used to identify the specific language record in the database that needs to be
    updated
    :type language_id: int
    :param update_language: The `update_language` parameter is of type `LanguageUpdate`. It is used to
    specify the updated values for the language details of a user. The `LanguageUpdate` model likely
    contains fields that correspond to the language properties that can be updated, such as `name`,
    `level`, etc. By
    :type update_language: LanguageUpdate
    :return: the updated user language details as a response with the response model `LanguageRead`.
    """
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
    """
    The above function deletes a user's language details from the database.

    :param session: The `session` parameter is of type `Session` and is used to interact with the
    database. It is obtained using the `get_db_session` dependency
    :type session: Session
    :param user_id: The `user_id` parameter represents the ID of the user whose language details are
    being deleted
    :type user_id: int
    :param language_id: The `language_id` parameter represents the unique identifier of the language
    that you want to delete for a user
    :type language_id: int
    :return: a dictionary with the key "ok" and the value True.
    """
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
