from sqlmodel import Session, select
from fastapi import HTTPException
from app.v1.database.services.user_services import UserCRUDService
from typing import List
from app.v1.database.models.project_model import (
    ProjectV1,
    ProjectV1Create,
    ProjectV1Read,
    ProjectV1Update,
)


class ProjectCRUDServices(UserCRUDService):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session)

    def read_user_project_details(self, user_id: int) -> List[ProjectV1Read]:
        user = self.get_user(user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        else:
            return user.project_details

    def create_user_project(
        self, user_id: int, user_project: ProjectV1Create
    ) -> ProjectV1Read:
        user = self.get_user(user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        else:
            user_project.user_id = user_id
            user_project_db_create = ProjectV1.from_orm(user_project)

            self.session.add(user_project_db_create)
            self.session.commit()
            self.session.refresh(user_project_db_create)

            return user_project_db_create

    def update_user_project(
        self, user_id: int, project_id: int, update_project: ProjectV1Update
    ) -> ProjectV1Read:
        user_project = self.session.exec(
            select(ProjectV1).where(
                ProjectV1.user_id == user_id, ProjectV1.project_id == project_id
            )
        ).one_or_none()

        if user_project is None:
            raise HTTPException(
                status_code=404, detail="User Project Details Not Found"
            )
        else:
            new_user_project = update_project.dict(exclude_unset=True)
            for key, value in new_user_project.items():
                setattr(user_project, key, value)

            self.session.add(user_project)
            self.session.commit()
            self.session.refresh(user_project)

            return user_project

    def delete_user_project(self, user_id: int, project_id: int) -> dict:
        user_project = self.session.exec(
            select(ProjectV1).where(
                ProjectV1.user_id == user_id, ProjectV1.project_id == project_id
            )
        ).one_or_none()

        if user_project is None:
            raise HTTPException(
                status_code=404, detail="User Project Details Not Found"
            )
        else:
            self.session.delete(user_project)
            self.session.commit()
            return {"Status": "Successfully deleted"}
