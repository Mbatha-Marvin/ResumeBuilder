from fastapi import HTTPException
from sqlmodel import Session, select
from pydantic import EmailStr
from typing import Optional, List
from app.v1.database.services.user_services import UserCRUDService
from app.v1.database.models.certification_model import (
    CertificationV1,
    CertificationV1Update,
    CertificationV1Read,
    CertificationV1Create,
    CertificationV1CreateRequest,
)


class CertificationCRUDService(UserCRUDService):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session)

    def read_user_certifications(
        self, user_id: int, email: Optional[EmailStr] = None
    ) -> List[CertificationV1Read]:
        user = self.get_user(email=email, user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        else:
            return user.certification_details

    def create_user_certifications(
        self,
        user_certification_request: CertificationV1CreateRequest,
        user_id: int,
        email: Optional[EmailStr] = None,
    ) -> CertificationV1Read:
        user = self.get_user(user_id=user_id, email=email)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        else:
            user_certification = CertificationV1Create.parse_obj(
                user_certification_request
            )
            user_certification.user_id = user.user_id
            user_certification_db_create = CertificationV1.from_orm(user_certification)

            self.session.add(user_certification_db_create)
            self.session.commit()
            self.session.refresh(user_certification_db_create)

            return user_certification_db_create

    def update_user_certifications(
        self,
        user_id: int,
        certification_id: int,
        update_certification: CertificationV1Update,
    ) -> CertificationV1Read:
        user_certification = self.session.exec(
            select(CertificationV1).where(
                CertificationV1.certification_id == certification_id,
                CertificationV1.user_id == user_id,
            )
        ).one_or_none()
        if user_certification is None:
            raise HTTPException(
                status_code=404, detail="User Certification Details Not Found"
            )
        else:
            new_user_certification = update_certification.dict(exclude_none=True)
            for key, value in new_user_certification.items():
                setattr(user_certification, key, value)

            self.session.add(user_certification)
            self.session.commit()
            self.session.refresh(user_certification)

            return user_certification

    def delete_user_certifications(
        self,
        user_id: int,
        certification_id: int,
    ) -> CertificationV1Read:
        user_certification = self.session.exec(
            select(CertificationV1).where(
                CertificationV1.certification_id == certification_id,
                CertificationV1.user_id == user_id,
            )
        ).one_or_none()
        if user_certification is None:
            raise HTTPException(
                status_code=404, detail="User Certification Details Not Found"
            )
        else:
            self.session.delete(user_certification)
            self.session.commit()

            return {"Status": "Successfully deleted"}
