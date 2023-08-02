from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import EmailStr
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.core.models import (
    Education,
    EducationRead,
    EducationCreate,
    EducationUpdate,
    User,
)

# The line `router = APIRouter(prefix="/users/{user_id}/education", tags=["Education"])` is creating a
# new instance of the `APIRouter` class.
router = APIRouter(prefix="/users/{user_id}/education", tags=["Education"])


@router.get("/", response_model=List[EducationRead])
def read_user_education(
    *,
    user_id: int,
    session: Session = Depends(get_db_session),
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    """
    The function `read_user_education` retrieves the education details of a user based on their user ID,
    with optional parameters for pagination.

    :param user_id: The `user_id` parameter is an integer that represents the unique identifier of the
    user whose education details we want to retrieve
    :type user_id: int
    :param session: The `session` parameter is used to access the database session. It is obtained using
    the `get_db_session` dependency, which is responsible for creating and managing the database session
    :type session: Session
    :param offset: The `offset` parameter is used to specify the number of records to skip before
    returning the results. It is used for pagination purposes. For example, if `offset` is set to 10,
    the first 10 records will be skipped and the results will start from the 11th record, defaults to 0
    :type offset: int (optional)
    :param limit: The `limit` parameter is used to specify the maximum number of education details to be
    returned in the response. It has a default value of 10 and is constrained to a maximum value of 15.
    This means that if the `limit` parameter is not provided in the request, the API will
    :type limit: int
    :return: the education details of a user with the specified user_id. The education details are
    returned as a list of EducationRead objects.
    """
    query_statement = (
        select(User).where(User.user_id == user_id).offset(offset).limit(limit)
    )
    user = session.exec(query_statement).one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User not Found")

    return user.education_details


@router.post("/", response_model=EducationRead)
def create_user_education(
    *,
    user_id: int,
    session: Session = Depends(get_db_session),
    user_education: EducationCreate,
):
    """
    The above function creates a new user education record in the database and associates it with an
    existing user.

    :param user_id: The `user_id` parameter is an integer that represents the ID of the user for whom
    the education information is being created
    :type user_id: int
    :param session: The `session` parameter is of type `Session` and is used to interact with the
    database. It is obtained using the `get_db_session` dependency, which is responsible for creating a
    new session and managing the database connection
    :type session: Session
    :param user_education: The `user_education` parameter is of type `EducationCreate`, which is a
    Pydantic model representing the data required to create a new education entry for a user. It
    contains the following fields:
    :type user_education: EducationCreate
    :return: an instance of the `EducationRead` model.
    """
    # check if user exists
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    user_education.user_id = user_id
    user_education_db_create = Education.from_orm(user_education)

    session.add(user_education_db_create)
    session.commit()
    session.refresh(user_education_db_create)

    return user_education_db_create


@router.patch("/{education_id}", response_model=EducationRead)
def update_user_education(
    *,
    user_id: int,
    session: Session = Depends(get_db_session),
    education_id: int,
    education_update: EducationUpdate,
):
    """
    The function updates a user's education details in the database.

    :param user_id: The `user_id` parameter represents the ID of the user whose education details are
    being updated
    :type user_id: int
    :param session: The `session` parameter is a dependency that represents the database session. It is
    obtained using the `get_db_session` function, which is likely defined elsewhere in the code. The
    session is used to interact with the database and perform CRUD operations
    :type session: Session
    :param education_id: The `education_id` parameter is the unique identifier of the education record
    that needs to be updated. It is used to identify the specific education record in the database
    :type education_id: int
    :param education_update: The parameter `education_update` is of type `EducationUpdate`. It is used
    to update the education details of a user. It contains the new values for the education fields that
    need to be updated
    :type education_update: EducationUpdate
    :return: an instance of the `EducationRead` model.
    """
    query_statement = (
        select(Education)
        .where(Education.education_id == education_id, Education.user_id == user_id)
        .limit(1)
    )
    db_user_education_instance = session.exec(query_statement).one_or_none()

    if db_user_education_instance is None:
        raise HTTPException(status_code=404, detail="User Education Details Not Found")

    new_user_education = education_update.dict(exclude_unset=True)
    for key, value in new_user_education.items():
        setattr(db_user_education_instance, key, value)

    session.add(db_user_education_instance)
    session.commit()
    session.refresh(db_user_education_instance)

    return db_user_education_instance


@router.delete("/{education_id}")
def delete_user_education(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    education_id: int,
):
    """
    The above function deletes a user's education details from the database.

    :param session: The `session` parameter is a dependency that represents the database session. It is
    obtained using the `get_db_session` function, which is likely defined elsewhere in the code
    :type session: Session
    :param user_id: The `user_id` parameter represents the ID of the user whose education details are
    being deleted
    :type user_id: int
    :param education_id: The `education_id` parameter is the unique identifier of the education record
    that you want to delete
    :type education_id: int
    :return: a dictionary with the key "ok" and the value True.
    """
    query_statement = (
        select(Education)
        .where(Education.education_id == education_id, Education.user_id == user_id)
        .limit(1)
    )
    user_education = session.exec(query_statement).one_or_none()

    if user_education is None:
        raise HTTPException(status_code=404, detail="User Education Details Not Found")

    session.delete(user_education)
    session.commit()

    return {"ok": True}
