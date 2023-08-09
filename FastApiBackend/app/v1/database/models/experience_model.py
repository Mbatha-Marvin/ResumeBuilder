from sqlmodel import Column, SQLModel, Field, Relationship, ARRAY, String
import datetime
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.v1.database.models.language_model import UserV1


# The above class represents a base model for storing experience information, including job titles,
# company names, job descriptions, and dates.
class ExperienceV1Base(SQLModel):
    card_title: str
    job_title: str
    company_name: str
    company_url: str
    location: str
    job_description_title: str
    job_descriptions: List[str] = Field(default=None, sa_column=Column(ARRAY(String())))
    start_date: datetime.date
    end_date: datetime.date


# The class "ExperienceV1" represents a user's experience details and includes a foreign key
# relationship to the "User" class.
class ExperienceV1(ExperienceV1Base, table=True):
    experience_id: int = Field(primary_key=True, default=None)

    user_id: int = Field(foreign_key="userv1.user_id")
    user: Optional["UserV1"] = Relationship(back_populates="experience_details")


# The `ExperienceV1Create` class is a subclass of `ExperienceV1Base` that includes a `user_id` attribute
# and a `Config` class with an example schema for creating a new experience.
class ExperienceV1CreateRequest(ExperienceV1Base):
    # user_id: int
    pass

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "job_title": "Job title",
                "company_name": "Company Name",
                "company_url": "Company URL",
                "location": "Location",
                "job_description_title": "Job Description Title",
                "job_descriptions": ["Description 1", "Description 2"],
                "start_date": "yyyy-mm-dd",
                "end_date": "yyyy-mm-dd",
                # "user_id": 0,
            }
        }


class ExperienceV1Create(ExperienceV1Base):
    user_id: Optional[int] = None


# The `ExperienceV1Read` class is a subclass of `ExperienceV1Base` that includes additional attributes for
# `user_id` and `experience_id`, and it has a `Config` class with an example schema.
class ExperienceV1Read(ExperienceV1Base):
    user_id: int
    experience_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "job_title": "Job title",
                "company_name": "Company Name",
                "company_url": "Company URL",
                "location": "Location",
                "job_description_title": "Job Description Title",
                "job_descriptions": ["Description 1", "Description 2"],
                "start_date": "yyyy-mm-dd",
                "end_date": "yyyy-mm-dd",
                "user_id": 0,
                "experience_id": 0,
            }
        }


# The `ExperienceV1Update` class represents an update to a user's experience, including job title,
# company name, location, job descriptions, and dates.
class ExperienceV1Update(SQLModel):
    card_title: Optional[str] = None
    job_title: Optional[str] = None
    company_name: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = None
    job_description_title: Optional[str] = None
    job_descriptions: Optional[List[str]] = None
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None

    class Config:
        exclude = {"user_id"}
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "job_title": "Job title",
                "company_name": "Company Name",
                "company_url": "Company URL",
                "location": "Location",
                "job_description_title": "Job Description Title",
                "job_descriptions": ["Description 1", "Description 2"],
                "start_date": "yyyy-mm-dd",
                "end_date": "yyyy-mm-dd",
                # "user_id": 0,
            }
        }
