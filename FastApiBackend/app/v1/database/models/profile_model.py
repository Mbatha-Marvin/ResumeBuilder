from sqlmodel import SQLModel, Field, Relationship, ARRAY, String, Column
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.v1.database.models.language_model import UserV1


# The class `ProfileV1Base` represents a user's contact information and work details.
class ProfileV1Base(SQLModel):
    first_name: str
    last_name: str
    middle_name: str
    image_url: Optional[str]
    linkedin_url: Optional[str]
    github_url: Optional[str]
    personal_website: Optional[str]
    city: str
    country: str
    address: Optional[str]
    user_work_title: str
    user_summary: str
    objectives: Optional[str]
    skills: List[str] = Field(default=None, sa_column=Column(ARRAY(String())))
    hobbies: List[str] = Field(default=None, sa_column=Column(ARRAY(String())))


class ProfileV1(ProfileV1Base, table=True):
    profile_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="userv1.user_id")
    user: Optional["UserV1"] = Relationship(back_populates="profile_details")


class ProfileV1CreateRequest(ProfileV1Base):
    # user_id: int

    class Config:
        schema_extra = {
            "example": {
                "first_name": "First Name",
                "last_name": "Last Name",
                "middle_name": "Middle Name",
                "image_url": "image_url",
                "linkedin_url": "valid_url",
                "github_url": "valid_url",
                "personal_website": "personal_website",
                "city": "City",
                "country": "Country of residence",
                "address": "address",
                "skills": ["Description 1", "Description 2"],
                "hobbies": ["Description 1", "Description 2"],
                "user_work_title": "User Work Title",
                "user_summary": "User Summary",
                "objectives": "objective summary",
                # "user_id": 0,
            }
        }


class ProfileV1Create(ProfileV1Base):
    user_id: Optional[int] = None


class ProfileV1Read(ProfileV1Base):
    user_id: int
    profile_id: int

    class Config:
        schema_extra = {
            "example": {
                "first_name": "First Name",
                "last_name": "Last Name",
                "middle_name": "Middle Name",
                "image_url": "image_url",
                "linkedin_url": "valid_url",
                "github_url": "valid_url",
                "personal_website": "personal_website",
                "city": "City",
                "country": "Country of residence",
                "address": "address",
                "skills": ["Description 1", "Description 2"],
                "hobbies": ["Description 1", "Description 2"],
                "user_work_title": "User Work Title",
                "user_summary": "User Summary",
                "objectives": "objective summary",
                "user_id": 0,
                "profile_id": 0,
            }
        }


class ProfileV1Update(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    image_url: Optional[str]
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    personal_website: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    address: Optional[str] = None
    skills: Optional[List[str]] = None
    hobbies: Optional[List[str]] = None
    user_work_title: Optional[str] = None
    user_summary: Optional[str] = None
    objectives: Optional[str] = None

    class Config:
        exclude = {"user_id"}
        schema_extra = {
            "example": {
                "first_name": "First Name",
                "last_name": "Last Name",
                "middle_name": "Middle Name",
                "image_url": "image_url",
                "linkedin_url": "valid_url",
                "github_url": "valid_url",
                "personal_website": "personal_website",
                "city": "City",
                "country": "Country of residence",
                "address": "address",
                "skills": ["Description 1", "Description 2"],
                "hobbies": ["Description 1", "Description 2"],
                "user_work_title": "User Work Title",
                "user_summary": "User Summary",
                "objectives": "objective summary",
                # "user_id": 0,
            }
        }
