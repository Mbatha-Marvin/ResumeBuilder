from fastapi import HTTPException
from app.core.models import User, UserUpdate
from sqlmodel import Session, select
from pydantic import EmailStr
from typing import Optional


class UserEndpointValidations:
    def __init__(self, session: Session) -> None:
        self.session = session

    def email_exists(self, email: EmailStr):
        sql_statement = select(User).where(User.email == email)
        user_db_instance = self.session.exec(sql_statement)

        if user_db_instance:
            return True
        else:
            return False

    def user_id_exists(self, user_id: int):
        sql_statement = select(User).where(User.user_id == user_id)
        user_db_instance = self.session.exec(sql_statement)

        if user_db_instance:
            return True
        else:
            return False

    def user_exists(
        self, email: Optional[EmailStr] = None, user_id: Optional[int] = None
    ):
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
