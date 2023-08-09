from sqlmodel import SQLModel, Field, Relationship
import datetime
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.v1.database.models.language_model import UserV1


# The class "EducationV1Base" represents educational information including card title, school name,
# education level, location, course title, final grade (optional), start date, and finish date.
class EducationV1Base(SQLModel):
    card_title: str
    school_name: str
    education_level: str
    location: str
    course_title: str
    final_grade: Optional[str] = Field(default=None)
    start_date: datetime.date
    end_date: datetime.date


# The class EducationV1 represents education details of a user with a foreign key relationship to the
# User class.
class EducationV1(EducationV1Base, table=True):
    education_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="userv1.user_id")
    user: Optional["UserV1"] = Relationship(back_populates="education_details")


# The `EducationV1Create` class is a subclass of `EducationV1Base` that includes a `user_id` attribute and
# a `Config` class with an example schema for creating an education record.
class EducationV1Create(EducationV1Base):
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "school_name": "School Name",
                "education_level": "Education Level",
                "course_title": "Course Title",
                "location": "Location",
                "final_grade": "Final Grade",
                "start_date": "yyyy-mm-dd",
                "end_date": "yyyy-mm-dd",
                "user_id": 0,
            }
        }


# The `EducationV1Read` class represents an education record with various attributes and includes an
# example schema for validation.
class EducationV1Read(EducationV1Base):
    user_id: int
    education_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "school_name": "School Name",
                "education_level": "Education Level",
                "course_title": "Course Title",
                "location": "Location",
                "final_grade": "Final Grade",
                "start_date": "yyyy-mm-dd",
                "end_date": "yyyy-mm-dd",
                "user_id": 0,
                "education_id": 0,
            }
        }


# The `EducationV1Update` class represents an update to a user's education information, including
# details such as card title, school name, education level, course title, location, final grade, start
# date, and finish date.
class EducationV1Update(SQLModel):
    card_title: Optional[str] = None
    school_name: Optional[str] = None
    education_level: Optional[str] = None
    location: Optional[str] = None
    course_title: Optional[str] = None
    final_grade: Optional[str] = None
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None

    class Config:
        exclude = {"user_id"}
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "school_name": "School Name",
                "education_level": "Education Level",
                "course_title": "Course Title",
                "location": "Location",
                "final_grade": "Final Grade",
                "start_date": "yyyy-mm-dd",
                "end_date": "yyyy-mm-dd",
                # "user_id": 0,
            }
        }
