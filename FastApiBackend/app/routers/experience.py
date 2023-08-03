from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.core.models import (
    Experience,
    ExperienceRead,
    ExperienceCreate,
    ExperienceUpdate,
    User,
)

# The line `router = APIRouter(prefix="/users/{user_id}/experience", tags=["Experience"])` creates a
# new instance of the `APIRouter` class with a specified prefix and tags.
router = APIRouter(prefix="/users/{user_id}/experience", tags=["Experience"])


@router.get("/", response_model=List[ExperienceRead])
def read_user_experience(
    *,
    user_id: int,
    session: Session = Depends(get_db_session),
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    """
    The function `read_user_experience` retrieves a user's experience details from the database based on
    the provided user ID, offset, and limit parameters.

    :param user_id: The `user_id` parameter is an integer that represents the unique identifier of the
    user whose experience details we want to retrieve
    :type user_id: int
    :param session: The `session` parameter is of type `Session` and is used to interact with the
    database. It is obtained using the `get_db_session` dependency, which is responsible for creating a
    new database session for each request
    :type session: Session
    :param offset: The `offset` parameter is used to specify the number of records to skip before
    returning the results. It is used for pagination purposes. For example, if `offset` is set to 10,
    the first 10 records will be skipped and the results will start from the 11th record, defaults to 0
    :type offset: int (optional)
    :param limit: The `limit` parameter is used to specify the maximum number of results to be returned
    in the response. It has a default value of 10 and is constrained to a maximum value of 15. This
    means that if the `limit` parameter is not provided in the request, the API will return
    :type limit: int
    :return: the experience details of a user with the specified user_id. The returned data is of type
    List[ExperienceRead].
    """
    query_statement = (
        select(User).where(User.user_id == user_id).offset(offset).limit(limit)
    )
    user = session.exec(query_statement).one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User not Found")

    return user.experience_details


@router.post("/", response_model=ExperienceRead)
def create_user_experience(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_experience: ExperienceCreate,
):
    """
    The function creates a user experience record in the database for a given user.

    :param session: The `session` parameter is used to access the database session. It is of type
    `Session` and is obtained using the `get_db_session` dependency
    :type session: Session
    :param user_id: The `user_id` parameter is an integer that represents the ID of the user for whom
    the experience is being created. It is used to associate the experience with the corresponding user
    in the database
    :type user_id: int
    :param user_experience: The `user_experience` parameter is of type `ExperienceCreate`, which is a
    Pydantic model representing the data required to create a new user experience. It contains the
    following fields:
    :type user_experience: ExperienceCreate
    :return: the created user experience as an instance of the `ExperienceRead` model.
    """
    # check if user exists
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    user_experience.user_id = user_id
    user_experience_db_create = Experience.from_orm(user_experience)

    session.add(user_experience_db_create)
    session.commit()
    session.refresh(user_experience_db_create)

    return user_experience_db_create


@router.patch("/{experience_id}", response_model=ExperienceRead)
def update_user_experience(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    experience_id: int,
    experience: ExperienceUpdate,
):
    """
    The function updates a user's experience details in the database.

    :param session: The `session` parameter is of type `Session` and is used to interact with the
    database session. It is obtained using the `get_db_session` dependency function
    :type session: Session
    :param user_id: The `user_id` parameter represents the ID of the user whose experience is being
    updated
    :type user_id: int
    :param experience_id: The `experience_id` parameter represents the unique identifier of the
    experience that needs to be updated. It is used to identify the specific experience record in the
    database that needs to be modified
    :type experience_id: int
    :param experience: The `experience` parameter is of type `ExperienceUpdate`, which is a Pydantic
    model representing the updated experience details. It contains the fields that can be updated for a
    user's experience. The `dict(exclude_unset=True)` method is used to convert the `ExperienceUpdate`
    object into a
    :type experience: ExperienceUpdate
    :return: the updated user experience details as an instance of the `ExperienceRead` model.
    """
    query_statement = (
        select(Experience)
        .where(Experience.experience_id == experience_id, Experience.user_id == user_id)
        .limit(1)
    )
    user_experience = session.exec(query_statement).one_or_none()
    if user_experience is None:
        raise HTTPException(status_code=404, detail="User Experience Details Not Found")

    new_user_experience = experience.dict(exclude_unset=True)
    for key, value in new_user_experience.items():
        setattr(user_experience, key, value)

    session.add(user_experience)
    session.commit()
    session.refresh(user_experience)

    return user_experience


@router.delete("/{experience_id}")
def delete_user_experience(
    *, session: Session = Depends(get_db_session), user_id: int, experience_id: int
):
    """
    The above function deletes a user experience from the database based on the provided user ID and
    experience ID.

    :param session: The `session` parameter is an instance of the database session that is used to
    interact with the database
    :type session: Session
    :param user_id: The `user_id` parameter represents the ID of the user whose experience is being
    deleted
    :type user_id: int
    :param experience_id: The `experience_id` parameter is the unique identifier of the user experience
    that needs to be deleted
    :type experience_id: int
    :return: a dictionary with a single key-value pair. The key is "ok" and the value is True.
    """
    query_statement = (
        select(Experience)
        .where(Experience.experience_id == experience_id, Experience.user_id == user_id)
        .limit(1)
    )
    user_experience = session.exec(query_statement).one_or_none()
    if user_experience is None:
        raise HTTPException(status_code=404, detail="User Experience Not Found")

    session.delete(user_experience)
    session.commit()

    return {"ok": True}
