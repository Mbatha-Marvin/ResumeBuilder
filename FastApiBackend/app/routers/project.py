from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.db import get_db_session
from typing import List
from sqlmodel import Session, select
from app.core.models import (
    Project,
    ProjectRead,
    ProjectCreate,
    ProjectUpdate,
    User,
)

# The `router` variable is creating an instance of the `APIRouter` class from the FastAPI framework.
# It is used to define the routes and endpoints for the project-related operations.
router = APIRouter(prefix="/users/{user_id}/project", tags=["Project"])


@router.get("/", response_model=List[ProjectRead])
def read_user_project(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    offset: int = 0,
    limit: int = Query(default=10, lte=15),
):
    """
    The function `read_user_project` retrieves a user's project details from the database based on the
    provided user ID, offset, and limit parameters.

    :param session: The `session` parameter is used to pass the database session to the function. It is
    of type `Session` and is obtained using the `get_db_session` dependency
    :type session: Session
    :param user_id: The `user_id` parameter is an integer that represents the ID of the user whose
    project details we want to retrieve
    :type user_id: int
    :param offset: The `offset` parameter is used to specify the number of records to skip before
    returning the results. It is used for pagination purposes, allowing you to retrieve a specific
    subset of records, defaults to 0
    :type offset: int (optional)
    :param limit: The `limit` parameter is used to specify the maximum number of projects to be returned
    in the response. By default, it is set to 10, but it cannot exceed 15
    :type limit: int
    :return: the project details of a user with the specified user_id. The returned value is a list of
    ProjectRead objects.
    """
    query_statement = (
        select(User).where(User.user_id == user_id).offset(offset).limit(limit)
    )
    user = session.exec(query_statement).one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User not Found")

    return user.project_details


@router.post("/", response_model=ProjectRead)
def create_user_project(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    user_project: ProjectCreate,
):
    """
    The function creates a new user project in the database and associates it with an existing user.

    :param session: The `session` parameter is of type `Session` and is used to interact with the
    database session. It is obtained using the `get_db_session` dependency
    :type session: Session
    :param user_id: The `user_id` parameter is an integer that represents the ID of the user for whom
    the project is being created
    :type user_id: int
    :param user_project: The `user_project` parameter is of type `ProjectCreate`, which is a Pydantic
    model representing the data required to create a new project for a user. It contains the necessary
    fields and their types for creating a project, such as project name, description, and any other
    relevant information
    :type user_project: ProjectCreate
    :return: an instance of the `ProjectRead` model.
    """
    # check if user exists
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")

    user_project.user_id = user_id
    user_project_db_create = Project.from_orm(user_project)

    session.add(user_project_db_create)
    session.commit()
    session.refresh(user_project_db_create)

    return user_project_db_create


@router.patch("/{project_id}", response_model=ProjectRead)
def update_user_project(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    project_id: int,
    update_project: ProjectUpdate,
):
    """
    The above function updates the details of a user's project in the database.

    :param session: The `session` parameter is of type `Session` and is used to interact with the
    database. It is obtained using the `get_db_session` dependency, which is responsible for creating a
    new database session for each request
    :type session: Session
    :param user_id: The `user_id` parameter represents the ID of the user whose project is being updated
    :type user_id: int
    :param project_id: The `project_id` parameter is the identifier of the project that needs to be
    updated. It is used to locate the specific project in the database for modification
    :type project_id: int
    :param update_project: The `update_project` parameter is of type `ProjectUpdate`, which is a
    Pydantic model representing the fields that can be updated for a project. It is used to specify the
    new values for the project fields that need to be updated
    :type update_project: ProjectUpdate
    :return: the updated user project details as a response with the `ProjectRead` model.
    """
    query_statement = (
        select(Project)
        .where(Project.user_id == user_id, Project.project_id == project_id)
        .limit(1)
    )
    user_project = session.exec(query_statement).one_or_none()
    if user_project is None:
        raise HTTPException(status_code=404, detail="User Project Details Not Found")

    new_user_project = update_project.dict(exclude_unset=True)
    for key, value in new_user_project.items():
        setattr(user_project, key, value)

    session.add(user_project)
    session.commit()
    session.refresh(user_project)

    return user_project


@router.delete("/{project_id}")
def delete_user_project(
    *, session: Session = Depends(get_db_session), user_id: int, project_id: int
):
    """
    The above function deletes a user project from the database.

    :param session: The `session` parameter is an instance of the database session that is used to
    interact with the database
    :type session: Session
    :param user_id: The `user_id` parameter represents the ID of the user whose project is being deleted
    :type user_id: int
    :param project_id: The `project_id` parameter in the `delete_user_project` function represents the
    unique identifier of the project that needs to be deleted. It is used to identify the specific
    project that the user wants to remove from their account
    :type project_id: int
    :return: a dictionary with the key "ok" and the value True.
    """
    query_statement = (
        select(Project)
        .where(Project.user_id == user_id, Project.project_id == project_id)
        .limit(1)
    )
    user_project = session.exec(query_statement).one_or_none()
    if user_project is None:
        raise HTTPException(status_code=404, detail="User Project Details Not Found")

    session.delete(user_project)
    session.commit()

    return {"ok": True}
