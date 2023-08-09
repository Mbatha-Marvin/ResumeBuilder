from sqlmodel import Session, select
from fastapi import HTTPException
from app.v1.database.services.user_services import UserCRUDService
from pydantic import EmailStr
from typing import Optional, List
from app.v1.database.models.education_model import (
    EducationV1,
    EducationV1Update,
    EducationV1Read,
    EducationV1Create,
)


class EducationCRUDService(UserCRUDService):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session)

    def read_user_education_details(
        self, user_id: int, email: Optional[EmailStr] = None
    ) -> List[EducationV1Read]:
        user = self.get_user(user_id=user_id, email=email)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        else:
            return user.education_details

    def create_user_education(
        self,
        user_id: int,
        user_education: EducationV1Create,
    ) -> EducationV1Read:
        user = self.get_user(user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        else:
            user_education.user_id = user_id
            user_education_db_create = EducationV1.from_orm(user_education)

            self.session.add(user_education_db_create)
            self.session.commit()
            self.session.refresh(user_education_db_create)

            return user_education_db_create

    def update_user_Education(
        self, user_id: int, education_id: int, education_update: EducationV1Update
    ) -> EducationV1Read:
        user_education_instance = self.session.exec(
            select(EducationV1).where(
                EducationV1.education_id == education_id, EducationV1.user_id == user_id
            )
        ).one_or_none()

        if user_education_instance is None:
            raise HTTPException(
                status_code=404, detail="User Education Details Not Found"
            )
        else:
            new_user_education = education_update.dict(exclude_none=True)
            for key, value in new_user_education.items():
                setattr(user_education_instance, key, value)

            self.session.add(user_education_instance)
            self.session.commit()
            self.session.refresh(user_education_instance)

            return user_education_instance

    def delete_user_education(self, user_id: int, education_id: int):
        user_education_instance = self.session.exec(
            select(EducationV1).where(
                EducationV1.education_id == education_id, EducationV1.user_id == user_id
            )
        ).one_or_none()

        if user_education_instance is None:
            raise HTTPException(
                status_code=404, detail="User Education Details Not Found"
            )
        else:
            self.session.delete(user_education_instance)
            self.session.commit()

            return {"Status": "Successfully deleted"}
