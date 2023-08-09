from pydantic import EmailStr
from sqlmodel import Session
from app.core.db import engine
from datetime import date
from app.v1.database.dummy_data.data import DummyUserData
from app.v1.database.models.user_model import UserV1
from app.v1.database.models.profile_model import ProfileV1
from app.v1.database.models.education_model import EducationV1
from app.v1.database.models.experience_model import ExperienceV1
from app.v1.database.models.language_model import LanguageV1
from app.v1.database.models.certification_model import CertificationV1

from app.v1.database.models.referee_model import RefereeV1
from app.v1.database.models.project_model import ProjectV1


class LoadDummyData(DummyUserData):
    def __init__(
        self, user_id: int, dummy_email: EmailStr, dummy_phone_number: str
    ) -> None:
        super().__init__(
            user_id=user_id,
            dummy_email=dummy_email,
            dummy_phone_number=dummy_phone_number,
        )

    def create_user(self):
        with Session(engine) as session:
            db_user_instance = session.get(UserV1, self.user_id)
            if not db_user_instance:
                # create user
                db_user_entry = UserV1.from_orm(self.dummy_user)

                session.add(db_user_entry)
                session.commit()
                session.refresh(db_user_entry)

                # Add education fields to user
                user_education_db_create_1 = EducationV1.from_orm(
                    self.dummy_education_1
                )
                session.add(user_education_db_create_1)
                session.commit()
                session.refresh(user_education_db_create_1)

                user_education_db_create_2 = EducationV1.from_orm(
                    self.dummy_education_2
                )
                session.add(user_education_db_create_2)
                session.commit()
                session.refresh(user_education_db_create_2)

                # Add experience fields to user
                user_experience_db_create_1 = ExperienceV1.from_orm(
                    self.dummy_experience_1
                )
                session.add(user_experience_db_create_1)
                session.commit()
                session.refresh(user_experience_db_create_1)

                user_experience_db_create_2 = ExperienceV1.from_orm(
                    self.dummy_experience_2
                )
                session.add(user_experience_db_create_2)
                session.commit()
                session.refresh(user_experience_db_create_2)

                # Add project fields to user
                user_project_db_create_1 = ProjectV1.from_orm(self.dummy_project_1)
                session.add(user_project_db_create_1)
                session.commit()
                session.refresh(user_project_db_create_1)

                user_project_db_create_2 = ProjectV1.from_orm(self.dummy_project_2)
                session.add(user_project_db_create_2)
                session.commit()
                session.refresh(user_project_db_create_2)

                # Add language fields to user
                user_language_db_create_1 = LanguageV1.from_orm(self.dummy_language_1)
                session.add(user_language_db_create_1)
                session.commit()
                session.refresh(user_language_db_create_1)

                user_language_db_create_2 = LanguageV1.from_orm(self.dummy_language_2)
                session.add(user_language_db_create_2)
                session.commit()
                session.refresh(user_language_db_create_2)

                user_language_db_create_3 = LanguageV1.from_orm(self.dummy_language_3)
                session.add(user_language_db_create_3)
                session.commit()
                session.refresh(user_language_db_create_3)

                user_language_db_create_4 = LanguageV1.from_orm(self.dummy_language_4)
                session.add(user_language_db_create_4)
                session.commit()
                session.refresh(user_language_db_create_4)

                # Add user_contact fields to user
                user_user_contact_db_create_1 = ProfileV1.from_orm(self.dummy_profile)
                session.add(user_user_contact_db_create_1)
                session.commit()
                session.refresh(user_user_contact_db_create_1)

                # Add Certification fields to user
                user_certification_db_create_1 = CertificationV1.from_orm(
                    self.dummy_certification_1
                )
                session.add(user_certification_db_create_1)
                session.commit()
                session.refresh(user_certification_db_create_1)

                user_certification_db_create_2 = CertificationV1.from_orm(
                    self.dummy_certification_2
                )
                session.add(user_certification_db_create_2)
                session.commit()
                session.refresh(user_certification_db_create_2)

                # Add Referee fields to user
                user_referee_db_create_1 = RefereeV1.from_orm(self.dummy_referee_1)
                session.add(user_referee_db_create_1)
                session.commit()
                session.refresh(user_referee_db_create_1)

                user_referee_db_create_2 = RefereeV1.from_orm(self.dummy_referee_2)
                session.add(user_referee_db_create_2)
                session.commit()
                session.refresh(user_referee_db_create_2)

                return "Dummy_user with user_id {user_id} successfully created"
            else:
                return "Dummy_user or User with user_id {user_id} already exists"
