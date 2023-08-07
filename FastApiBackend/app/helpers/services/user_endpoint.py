from fastapi import HTTPException
from app.core.models import User, UserUpdate
from sqlmodel import Session, select, or_
from pydantic import EmailStr
from typing import Optional
from app.core.models import UserRead, User, UserCreate, UserUpdate


class UserServices:
    def __init__(self, session: Session) -> None:
        self.session = session

    def email_exists(self, email: EmailStr) -> bool:
        user_db_instance = self.session.exec(
            select(User).where(User.email == email)
        ).one_or_none()

        if user_db_instance:
            return True
        else:
            return False

    def user_id_exists(self, user_id: int) -> bool:
        user_db_instance = self.session.exec(
            select(User).where(User.user_id == user_id)
        ).one_or_none()

        if user_db_instance:
            return True
        else:
            return False

    def phone_number_exists(self, phone_number: str):
        """Check that there are no duplicate phone numbers registered with us."""
        user_db_instance = self.session.exec(
            select(User).where(User.phone_number == phone_number)
        ).one_or_none()

        if user_db_instance:
            return True
        else:
            return False

    def user_exists(
        self, email: Optional[EmailStr] = None, user_id: Optional[int] = None
    ) -> bool:
        """Check whether a user exists in the database"""
        if email is None and user_id is None:
            raise HTTPException(
                status_code=401, detail="Please provide either a user_id or an email"
            )

        if email:
            # Check for existing users by their emails
            return self.email_exists(email=email)
        if user_id:
            # Check for existing users by their ids
            return self.user_id_exists(user_id=user_id)

    def get_user(
        self, email: Optional[EmailStr] = None, user_id: Optional[int] = None
    ) -> User | None:
        if self.user_exists(email=email, user_id=user_id):
            # fetch using email if email is provided
            if email:
                return self.session.exec(
                    select(User).where(User.email == email)
                ).one_or_none()
            # fetch using user if email is not provided
            elif user_id:
                return self.session.exec(
                    select(User).where(User.user_id == user_id)
                ).one_or_none()
        else:
            return None

    def create_user(self, new_user: UserCreate) -> UserRead:
        if self.email_exists(email=new_user.email):
            raise HTTPException(status_code=409, detail="Email already exists")

        elif self.phone_number_exists(phone_number=new_user.phone_number):
            raise HTTPException(status_code=409, detail="Phone Number already exists")

        new_user_instance = User.from_orm(new_user)
        self.session.add(new_user_instance)
        self.session.commit()
        self.session.refresh(new_user_instance)

        return new_user_instance

    def update_user(
        self,
        email: Optional[EmailStr] = None,
        user_id: Optional[int] = None,
        new_user: Optional[UserUpdate] = None,
    ):
        # check if user exists
        if self.user_exists(email=email, user_id=user_id):
            if new_user:
                db_user_instance = self.session.get(User, user_id)
                # save email so as to reset it incase user resets email
                prev_email = db_user_instance.email

                # Sanity checks, If password field is empty set to None
                if new_user.password == "":
                    new_user.password = None

                # Sanity checks, If user name field is empty set to None
                if new_user.name == "":
                    new_user.name = None

                new_user_data = new_user.dict(exclude_none=True)
                for key, value in new_user_data.items():
                    setattr(db_user_instance, key, value)

                # resetting email to email set before the update
                db_user_instance.email = prev_email

                self.session.add(db_user_instance)
                self.session.commit()
                self.session.refresh(db_user_instance)

                return db_user_instance
            else:
                raise HTTPException(
                    status_code=401, detail="Please provide data to update"
                )
        else:
            raise HTTPException(status_code=404, detail="User not Found")

    def delete_user(
        self, user_id: Optional[int] = None, email: Optional[EmailStr] = None
    ) -> bool:
        user_to_delete = self.get_user(email=email, user_id=user_id)
        if user_to_delete is None:
            return False
        else:
            self.session.delete(user_to_delete)
            self.session.commit()

            return True

    def get_full_profile(
        self, user_id: Optional[int] = None, email: Optional[EmailStr] = None
    ):
        """Get full profile of a User"""
        user = self.get_user(user_id=user_id, email=email)

        full_profile = {}
        user_profile = {
            "personal_website_url": user.profile_details[0].personal_website,
            "linkein_url": user.profile_details[0].linkedin_url,
            "github_url": user.profile_details[0].github_url,
            "work_title_highlight": user.profile_details[0].user_work_title,
            "first_name": user.profile_details[0].first_name,
            "last_name": user.profile_details[0].last_name,
            "middle_name": user.profile_details[0].middle_name,
            "email": user.email,
            "city": user.profile_details[0].city,
            "country": user.profile_details[0].country,
            "address": user.profile_details[0].address,
            "phone_number": user.phone_number,
        }
        summary = {
            "card_title": "string",
            "brief_description": user.profile_details[0].user_summary,
        }
        objectives = {
            "card_title": "string",
            "brief_description": user.profile_details[0].objectives,
        }
        hobbies = {"card_title": "string", "hobbies": user.profile_details[0].hobbies}

        education = {
            "card_title": user.education_details[0].card_title,
            "education_details": [
                {
                    "school_name": detail.school_name,
                    "education_level": detail.education_level,
                    "location": detail.location,
                    "course_title": detail.course_title,
                    "final_grade": detail.final_grade,
                    "start_date": detail.start_date,
                    "end_date": detail.finish_date,
                }
                for detail in user.education_details
            ],
        }

        experience = {
            "card_title": user.experience_details[0].card_title,
            "experience_details": [
                {
                    "job_title": detail.job_title,
                    "company_name": detail.company_name,
                    "company_url": detail.company_url,
                    "location": detail.location,
                    "job_description_title": detail.job_description_title,
                    "job_description": detail.job_descriptions,
                    "start_date": detail.start_date,
                    "end_date": detail.end_date,
                }
                for detail in user.experience_details
            ],
        }

        language = {
            "card_title": user.language_details[0].card_title,
            "language_details": [
                {
                    "language_name": detail.language_name,
                    "profeciency_level": detail.profeciency_level,
                }
                for detail in user.language_details
            ],
        }
        project = {
            "card_title": user.project_details[0].card_title,
            "project_details": [
                {
                    "project_title": detail.project_name,
                    "project_url": detail.project_url,
                    "project_description_list": detail.project_description,
                    "project_description_title": detail.project_description_title,
                }
                for detail in user.project_details
            ],
        }
        certification = {
            "card_title": user.certification_details[0].card_title,
            "certification_details": [
                {
                    "school_name": detail.school_name,
                    "school_type": detail.school_type,
                    "certified_on": detail.certified_on,
                    "start_date": detail.start_date,
                    "end_date": detail.end_date,
                }
                for detail in user.certification_details
            ],
        }

        referee = {
            "card_title": user.referee_details[0].card_title,
            "referee_details": [
                {
                    "full_name": detail.full_name,
                    "email": detail.email,
                    "phone_number": detail.phone_number,
                    "company_name": detail.company_name,
                    "occupation": detail.occupation,
                    "address": detail.address,
                }
                for detail in user.referee_details
            ],
        }

        full_profile["user_profile"] = user_profile
        full_profile["summary"] = summary
        full_profile["objectives"] = objectives
        full_profile["hobbies"] = hobbies
        full_profile["skills"] = user.profile_details[0].skills
        full_profile["education"] = education
        full_profile["experience"] = experience
        full_profile["language"] = language
        full_profile["project"] = project
        full_profile["certification"] = certification
        full_profile["referee"] = referee

        return full_profile
