# from pydantic import EmailStr
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.v1.database.models.language_model import UserV1


class RefereeV1Base(SQLModel):
    card_title: str
    full_name: str
    # email: EmailStr
    phone_number: str
    company_name: str
    occupation: str
    address: str


class RefereeV1(RefereeV1Base, table=True):
    referee_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="userv1.user_id")
    user: Optional["UserV1"] = Relationship(back_populates="referee_details")


class RefereeV1Create(RefereeV1Base):
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Referee",
                "full_name": "Full_Name",
                # "email": "referee@email.com",
                "phone_number": "A phone number",
                "company_name": "Some_Company_Name",
                "occupation": "Some_Job_Title",
                "address": "Some_Address",
                "user_id": 0,
            }
        }


class RefereeV1Read(RefereeV1Base):
    user_id: int
    referee_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Referee",
                "full_name": "Full_Name",
                # "email": "referee@email.com",
                "phone_number": "A phone number",
                "company_name": "Some_Company_Name",
                "occupation": "Some_Job_Title",
                "address": "Some_Address",
                "user_id": 0,
                "referee_id": 0,
            }
        }


class RefereeV1Update(SQLModel):
    card_title: Optional[str] = None
    full_name: Optional[str] = None
    # email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    company_name: Optional[str] = None
    occupation: Optional[str] = None
    address: Optional[str] = None

    class Config:
        exclude = {"user_id"}
        schema_extra = {
            "example": {
                "card_title": "Referee",
                "full_name": "Full_Name",
                # "email": "referee@email.com",
                "phone_number": "A phone number",
                "company_name": "Some_Company_Name",
                "occupation": "Some_Job_Title",
                "address": "Some_Address",
                # "user_id": 0,
            }
        }
