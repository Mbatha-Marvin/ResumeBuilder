from sqlmodel import Session, select
from fastapi import HTTPException
from app.v1.database.services.user_services import UserCRUDService
from typing import List
from app.v1.database.models.referee_model import (
    RefereeV1,
    RefereeV1Create,
    RefereeV1CreateRequest,
    RefereeV1Read,
    RefereeV1Update,
)


class RefereeCRUDServices(UserCRUDService):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session)

    def read_user_referee_details(self, user_id: int) -> List[RefereeV1Read]:
        user = self.get_user(user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        else:
            return user.referee_details

    def create_user_referee(
        self, user_id: int, user_referee_request: RefereeV1CreateRequest
    ) -> RefereeV1Read:
        user = self.get_user(user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        else:
            user_referee = RefereeV1Create.parse_obj(user_referee_request)
            user_referee.user_id = user_id
            user_referee_db_create = RefereeV1.from_orm(user_referee)

            self.session.add(user_referee_db_create)
            self.session.commit()
            self.session.refresh(user_referee_db_create)

            return user_referee_db_create

    def update_user_referee(
        self, user_id: int, referee_id: int, update_referee: RefereeV1Update
    ) -> RefereeV1Read:
        user_referee = self.session.exec(
            select(RefereeV1).where(
                RefereeV1.user_id == user_id, RefereeV1.referee_id == referee_id
            )
        ).one_or_none()

        if user_referee is None:
            raise HTTPException(
                status_code=404, detail="User Referee Details Not Found"
            )
        else:
            new_user_referee = update_referee.dict(exclude_none=True)
            for key, value in new_user_referee.items():
                setattr(user_referee, key, value)

            self.session.add(user_referee)
            self.session.commit()
            self.session.refresh(user_referee)

            return user_referee

    def delete_user_referee(self, user_id: int, referee_id: int) -> dict:
        user_referee = self.session.exec(
            select(RefereeV1).where(
                RefereeV1.user_id == user_id, RefereeV1.referee_id == referee_id
            )
        ).one_or_none()

        if user_referee is None:
            raise HTTPException(
                status_code=404, detail="User Referee Details Not Found"
            )
        else:
            self.session.delete(user_referee)
            self.session.commit()

            return {"Status": "Successfully deleted"}
