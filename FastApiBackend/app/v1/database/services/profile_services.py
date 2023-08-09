from sqlmodel import Session, select
from fastapi import HTTPException
from app.v1.database.services.user_services import UserCRUDService
from typing import List
from app.v1.database.models.profile_model import (
    ProfileV1,
    ProfileV1Create,
    ProfileV1Read,
    ProfileV1Update,
    ProfileV1CreateRequest,
)


class ProfileCRUDServices(UserCRUDService):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session)

    def read_user_profile(self, user_id: int) -> List[ProfileV1Read]:
        user = self.get_user(user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        else:
            return user.profile_details

    def create_user_profile(
        self, user_id: int, profile_request: ProfileV1CreateRequest
    ) -> ProfileV1Read:
        user = self.get_user(user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        elif len(user.profile_details) >= 1:
            raise HTTPException(
                status_code=404, detail="A profile already exists for this User"
            )

        else:
            profile = ProfileV1Create.parse_obj(profile_request)
            profile.user_id = user_id
            new_profile = ProfileV1.from_orm(profile)

            self.session.add(new_profile)
            self.session.commit()
            self.session.refresh(new_profile)

            return new_profile

    def update_user_profile(
        self, user_id: int, profile_id: int, update_profile: ProfileV1Update
    ) -> ProfileV1Read:
        profile_in_db = self.session.exec(
            select(ProfileV1).where(
                ProfileV1.user_id == user_id, ProfileV1.profile_id == profile_id
            )
        ).one_or_none()

        if profile_in_db is None:
            raise HTTPException(status_code=404, detail="Profile Not found")
        else:
            new_profile = update_profile.dict(exclude_none=True)
            for key, value in new_profile.items():
                setattr(profile_in_db, key, value)

            self.session.add(profile_in_db)
            self.session.commit()
            self.session.refresh(profile_in_db)

            return profile_in_db

    def delete_user_profile(self, user_id: int, profile_id: int) -> dict:
        profile_in_db = self.session.exec(
            select(ProfileV1).where(
                ProfileV1.user_id == user_id, ProfileV1.profile_id == profile_id
            )
        ).one_or_none()

        if profile_in_db is None:
            raise HTTPException(status_code=404, detail="Profile Not found")
        else:
            self.session.delete(profile_in_db)
            self.session.commit()

            return {"Status": "Successfully deleted"}
