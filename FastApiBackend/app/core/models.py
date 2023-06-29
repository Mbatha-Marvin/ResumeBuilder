from pydantic import BaseModel
from sqlmodel import Column, SQLModel, Field, Relationship, ARRAY, String
import datetime
from typing import Optional, List


class HealthCheck(BaseModel):
    name: str
    version: str
    description: str


class UserBase(SQLModel):
    name: str = Field(index=True)
    password: str


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)

    education_details: List["Education"] = Relationship(back_populates="user")
    experience_details: List["Experience"] = Relationship(back_populates="user")
    language_details: List["Language"] = Relationship(back_populates="user")
    project_details: List["Project"] = Relationship(back_populates="user")
    user_contact_details: List["UserContact"] = Relationship(back_populates="user")


class UserCreate(UserBase):
    class Config:
        schema_extra = {
            "example": {
                "name": "UserName",
                "password": "Password",
            }
        }


class UserRead(UserBase):
    id: int

    class Config:
        schema_extra = {
            "example": {
                "name": "UserName - type(string)",
                "password": "Password  - type(string)",
                "id": "user_id - type(int)",
            }
        }


class UserUpdate(UserBase):
    name: Optional[str] = None
    password: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "New UserName",
                "password": "New Password",
            }
        }


class EducationBase(SQLModel):
    card_title: str
    school_name: str
    education_level: str
    location: str
    course_title: str
    final_grade: Optional[str] = Field(default=None)
    start_date: datetime.date
    finish_date: datetime.date


class Education(EducationBase, table=True):
    education_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="education_details")


class EducationCreate(EducationBase):
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
                "start_date": "2023-06-29",
                "finish_date": "2023-06-29",
                "user_id": 0,
            }
        }


class EducationRead(EducationBase):
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
                "start_date": "2023-06-29",
                "finish_date": "2023-06-29",
                "user_id": 0,
                "education_id": 0,
            }
        }


class EducationUpdate(SQLModel):
    card_title: Optional[str] = None
    school_name: Optional[str] = None
    education_level: Optional[str] = None
    location: Optional[str] = None
    course_title: Optional[str] = None
    final_grade: Optional[str] = None
    start_date: Optional[datetime.date] = None
    finish_date: Optional[datetime.date] = None

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "school_name": "School Name",
                "education_level": "Education Level",
                "course_title": "Course Title",
                "location": "Location",
                "final_grade": "Final Grade",
                "start_date": "2023-06-29",
                "finish_date": "2023-06-29",
                "user_id": 0,
            }
        }


class ExperienceBase(SQLModel):
    card_title: str
    job_title: str
    company_name: str
    company_url: str
    location: str
    job_description_title: str
    job_descriptions: List[str] = Field(default=None, sa_column=Column(ARRAY(String())))
    start_date: datetime.date
    end_date: datetime.date


class Experience(ExperienceBase, table=True):
    experience_id: int = Field(primary_key=True, default=None)

    user_id: int = Field(foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="experience_details")


class ExperienceCreate(ExperienceBase):
    user_id: int

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
                "start_date": "2023-06-29",
                "end_date": "2023-06-29",
                "user_id": 0,
            }
        }


class ExperienceRead(ExperienceBase):
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
                "start_date": "2023-06-29",
                "end_date": "2023-06-29",
                "user_id": 0,
                "experience_id": 0,
            }
        }


class ExperienceUpdate(SQLModel):
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
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "job_title": "Job title",
                "company_name": "Company Name",
                "company_url": "Company URL",
                "location": "Location",
                "job_description_title": "Job Description Title",
                "job_descriptions": ["Description 1", "Description 2"],
                "start_date": "2023-06-29",
                "end_date": "2023-06-29",
                "user_id": 0,
            }
        }


class LanguageBase(SQLModel):
    card_title: str
    language_name: str
    profeciency_level: int


class Language(LanguageBase, table=True):
    language_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.id")
    user: List[User] = Relationship(back_populates="language_details")


class LanguageCreate(LanguageBase):
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "language_name": "Language Name",
                "profeciency_level": 5,
                "user_id": 0,
            }
        }


class LanguageRead(LanguageBase):
    user_id: int
    language_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "language_name": "Language Name",
                "profeciency_level": 5,
                "user_id": 0,
                "language_id": 0,
            }
        }


class LanguageUpdate(SQLModel):
    card_title: Optional[str] = None
    language_name: Optional[str] = None
    profeciency_level: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "language_name": "Language Name",
                "profeciency_level": 5,
                "user_id": 0,
            }
        }


class ProjectBase(SQLModel):
    card_title: str
    project_name: str
    project_description_title: str
    project_description: List[str]
    project_url: Optional[str]


class Project(ProjectBase, table=True):
    project_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.id")
    user: List[User] = Relationship(back_populates="project_details")


class ProjectCreate(ProjectBase):
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "project_name": "Project Name",
                "project_description_title": "Project Description Title",
                "project_description": ["Description 1", "Description 2"],
                "user_id": 0,
            }
        }


class ProjectRead(ProjectBase):
    user_id: int
    project_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "project_name": "Project Name",
                "project_description_title": "Project Description Title",
                "project_description": ["Description 1", "Description 2"],
                "user_id": 0,
                "project_id": 0,
            }
        }


class ProjectUpdate(SQLModel):
    card_title: Optional[str] = None
    project_name: Optional[str] = None
    project_description_title: Optional[str] = None
    project_description: Optional[List[str]] = None
    project_url: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "project_name": "Project Name",
                "project_description_title": "Project Description Title",
                "project_description": ["Description 1", "Description 2"],
                "user_id": 0,
            }
        }


class UserContactBase(SQLModel):
    email: str
    personal_website: Optional[str]
    city: str
    country: str
    phone_number: str
    user_work_title: str
    user_summary: str


class UserContact(UserContactBase, table=True):
    user_contact_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.id")
    user: List[User] = Relationship(back_populates="user_contact_details")


class UserContactCreate(UserContactBase):
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "email": "Uesr Email",
                "personal_website": "personal_website",
                "city": "City",
                "country": "Country of residence",
                "phone_number": "Phone Number",
                "user_work_title": "User Work Title",
                "user_summary": "User Summary",
                "user_id": 0,
            }
        }


class UserContactRead(UserContactBase):
    user_id: int
    user_contact_id: int

    class Config:
        schema_extra = {
            "example": {
                "email": "Uesr Email",
                "personal_website": "personal_website",
                "city": "City",
                "country": "Country of residence",
                "phone_number": "Phone Number",
                "user_work_title": "User Work Title",
                "user_summary": "User Summary",
                "user_id": 0,
                "user_contact_id": 0,
            }
        }


class UserContactUpdate(SQLModel):
    email: Optional[str] = None
    personal_website: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    phone_number: Optional[str] = None
    user_work_title: Optional[str] = None
    user_summary: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "email": "Uesr Email",
                "personal_website": "personal_website",
                "city": "City",
                "country": "Country of residence",
                "phone_number": "Phone Number",
                "user_work_title": "User Work Title",
                "user_summary": "User Summary",
                "user_id": 0,
            }
        }
