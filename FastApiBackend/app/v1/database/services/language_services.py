from sqlmodel import Session, select
from fastapi import HTTPException
from app.v1.database.services.user_services import UserCRUDService
from typing import List
from app.v1.database.models.language_model import (
    LanguageV1,
    LanguageV1Create,
    LanguageV1Read,
    LanguageV1Update,
)


class LanguageCRUDServices(UserCRUDService):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session)

    def read_user_lanngauge_details(self, user_id: int) -> List[LanguageV1Read]:
        user = self.get_user(user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        else:
            return user.language_details

    def create_user_language(
        self, user_id: int, user_language: LanguageV1Create
    ) -> LanguageV1Read:
        user = self.get_user(user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not Found")
        else:
            user_language.user_id = user_id
            user_language_db_create = LanguageV1.from_orm(user_language)

            self.session.add(user_language_db_create)
            self.session.commit()
            self.session.refresh(user_language_db_create)

            return user_language_db_create

    def update_user_language(
        self, user_id: int, langauge_id: int, update_language: LanguageV1Update
    ) -> LanguageV1Read:
        user_language = self.session.exec(
            select(LanguageV1).where(
                LanguageV1.user_id == user_id, LanguageV1.language_id == langauge_id
            )
        ).one_or_none()

        if user_language is None:
            raise HTTPException(
                status_code=404, detail="User Language Details Not Found"
            )
        else:
            new_user_langauge = update_language.dict(exclude_unset=True)
            for key, value in new_user_langauge.items():
                setattr(user_language, key, value)

            self.session.add(user_language)
            self.session.commit()
            self.session.refresh(user_language)

            return user_language

    def delete_user_language(self, user_id: int, language_id: int) -> LanguageV1Read:
        user_language = self.session.exec(
            select(LanguageV1).where(
                LanguageV1.user_id == user_id, LanguageV1.language_id == language_id
            )
        ).one_or_none()

        if user_language is None:
            raise HTTPException(
                status_code=404, detail="User Language Details Not Found"
            )
        else:
            self.session.delete(user_language)
            self.session.commit()

            return {"Status": "Successfully deleted"}
