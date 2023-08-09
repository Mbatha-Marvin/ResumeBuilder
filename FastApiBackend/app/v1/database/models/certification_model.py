from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
import datetime

if TYPE_CHECKING:
    from app.v1.database.models.language_model import UserV1


class CertificationV1Base(SQLModel):
    card_title: str
    school_name: str
    school_type: str
    certified_on: str
    start_date: datetime.date
    end_date: datetime.date


class CertificationV1(CertificationV1Base, table=True):
    certification_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="userv1.user_id")
    user: Optional["UserV1"] = Relationship(back_populates="certification_details")


class CertificationV1CreateRequest(CertificationV1Base):
    # user_id: int
    pass

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Certification",
                "school_name": "School_Name",
                "school_type": "School_Type",
                "certified_on": "Discipline",
                "start_date": "yyyy-mm-dd",
                "end_date": "yyyy-mm-dd",
                # "user_id": 0,
            }
        }


class CertificationV1Create(CertificationV1Base):
    user_id: Optional[int] = None
    # user_id: int


class CertificationV1Read(CertificationV1Base):
    user_id: int
    certification_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Certification",
                "school_name": "School_Name",
                "school_type": "School_Type",
                "certified_on": "Discipline",
                "start_date": "yyyy-mm-dd",
                "end_date": "yyyy-mm-dd",
                "user_id": 0,
                "certification_id": 0,
            }
        }


class CertificationV1Update(SQLModel):
    card_title: Optional[str] = None
    school_name: Optional[str] = None
    school_type: Optional[str] = None
    certified_on: Optional[str] = None
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None

    class Config:
        exclude = {"user_id"}
        schema_extra = {
            "example": {
                "card_title": "Certification",
                "school_name": "School_Name",
                "school_type": "School_Type",
                "certified_on": "Discipline",
                "start_date": "yyyy-mm-dd",
                "end_date": "yyyy-mm-dd",
                # "user_id": 0,
            }
        }
