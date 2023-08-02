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

# The `router` variable is creating an instance of the `APIRouter` class from the FastAPI framework.
# It is used to define the routes and endpoints for the UserContact API.
router = APIRouter(prefix="/users/{user_id}/user_contact", tags=["UserContact"])


@router.get("/", response_model=List[UserContactRead])
def read_user_contact(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    """
    The function `read_user_contact` retrieves user contact details from the database based on the
    provided user ID, offset, and limit parameters.

    :param session: The `session` parameter is used to access the database session. It is obtained using
    the `get_db_session` dependency, which is responsible for creating and managing the database session
    :type session: Session
    :param user_id: The `user_id` parameter is an integer that represents the ID of the user whose
    contact details we want to retrieve
    :type user_id: int
    :param offset: The `offset` parameter is used to specify the number of records to skip before
    returning the results. It is used for pagination purposes, allowing you to retrieve a specific
    subset of records, defaults to 0
    :type offset: int (optional)
    :param limit: The `limit` parameter is used to specify the maximum number of user contact details to
    be returned in the response. By default, it is set to 10, but it cannot exceed 15
    :type limit: int
    :return: a list of UserContactRead objects.
    """
    query_statement = (
        select(User).where(User.user_id == user_id).offset(offset).limit(limit)
    )
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
    """
    The function creates a new user contact record in the database for a given user.

    :param session: The `session` parameter is a dependency that represents the database session. It is
    obtained using the `get_db_session` function, which is likely defined elsewhere in the code. The
    session is used to interact with the database and perform CRUD operations
    :type session: Session
    :param user_id: The `user_id` parameter is an integer that represents the ID of the user for whom
    the contact is being created. It is used to associate the contact with the correct user in the
    database
    :type user_id: int
    :param user_contact: The `user_contact` parameter is of type `UserContactCreate`, which is a
    Pydantic model representing the data required to create a new user contact. It contains the
    following fields:
    :type user_contact: UserContactCreate
    :return: the created user contact as a response.
    """
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
    """
    The above function updates a user contact record in the database based on the provided user ID and
    user contact ID.

    :param session: The `session` parameter is the database session object used to interact with the
    database. It is obtained using the `get_db_session` dependency function
    :type session: Session
    :param user_id: The `user_id` parameter represents the ID of the user whose contact details are
    being updated
    :type user_id: int
    :param user_contact_id: The `user_contact_id` parameter represents the unique identifier of the user
    contact that needs to be updated. It is used to identify the specific user contact record in the
    database that needs to be modified
    :type user_contact_id: int
    :param update_user_contact: The `update_user_contact` parameter is of type `UserContactUpdate`,
    which is a Pydantic model representing the data to be updated for a user contact. It contains the
    fields and their corresponding types that can be updated for a user contact
    :type update_user_contact: UserContactUpdate
    :return: the updated user contact details as an instance of the `UserContactRead` model.
    """
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
    """
    The above function deletes a user contact from the database based on the user ID and user contact ID
    provided.

    :param session: The `session` parameter is a SQLAlchemy session object. It is used to interact with
    the database and perform database operations
    :type session: Session
    :param user_id: The `user_id` parameter represents the ID of the user whose contact details are
    being deleted
    :type user_id: int
    :param user_contact_id: The `user_contact_id` parameter is the unique identifier of the user contact
    that you want to delete. It is used to specify which user contact should be deleted from the
    database
    :type user_contact_id: int
    :return: a dictionary with the key "ok" and the value True.
    """
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
