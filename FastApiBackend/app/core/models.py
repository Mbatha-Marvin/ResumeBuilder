from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
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
    pass


class UserRead(UserBase):
    id: int


class UserUpdate(UserBase):
    name: Optional[str] = None
    password: Optional[str] = None


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
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")

    user: Optional[User] = Relationship(back_populates="education_details")


class EducationCreate(EducationBase):
    pass


class EducationRead(EducationBase):
    id: int


class EducationUpdate(SQLModel):
    card_title: Optional[str] = None
    school_name: Optional[str] = None
    education_level: Optional[str] = None
    location: Optional[str] = None
    course_title: Optional[str] = None
    final_grade: Optional[str] = None
    start_date: Optional[datetime.date] = None
    finish_date: Optional[datetime.date] = None


class ExperienceBase(SQLModel):
    card_title: str
    job_title: str
    company_name: str
    company_url: str
    location: str
    job_description_title: str
    job_descriptions: List[str]
    start_date: datetime.date
    end_date: datetime.date


class Experience(ExperienceBase, table=True):
    id: int = Field(primary_key=True, default=None)

    user_id: int = Field(foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="experience_details")


class ExperienceCreate(ExperienceBase):
    pass


class ExperienceRead(ExperienceBase):
    id: int


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


class LanguageBase(SQLModel):
    card_title: str
    language_name: str
    profeciency_level: int


class Language(LanguageBase, table=True):
    id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.id")
    user: List[User] = Relationship(back_populates="language_details")


class LanguageCreate(LanguageBase):
    pass


class LanguageRead(LanguageBase):
    id: int


class LanguageUpdate(SQLModel):
    card_title: Optional[str] = None
    language_name: Optional[str] = None
    profeciency_level: Optional[int] = None


class ProjectBase(SQLModel):
    card_title: str
    project_name: str
    project_description_title: str
    project_description: List[str]
    project_url: Optional[str]


class Project(ProjectBase, table=True):
    id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.id")
    user: List[User] = Relationship(back_populates="project_details")


class ProjectCreate(ProjectBase):
    pass


class ProjectRead(ProjectBase):
    id: int


class ProjectUpdate(SQLModel):
    card_title: Optional[str] = None
    project_name: Optional[str] = None
    project_description_title: Optional[str] = None
    project_description: Optional[List[str]] = None
    project_url: Optional[str] = None


class UserContactBase(SQLModel):
    email: str
    personal_website: Optional[str]
    city: str
    country: str
    phone_number: str
    user_work_title: str
    user_summary: str


class UserContact(UserContactBase, table=True):
    id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key=True)
    user: List[User] = Relationship(back_populates="user_contact_details")


class UserContactCreate(UserContactBase):
    pass


class UserContactRead(UserContactBase):
    id: int


class UserContactUpdate(SQLModel):
    email: Optional[str] = None
    personal_website: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    phone_number: Optional[str] = None
    user_work_title: Optional[str] = None
    user_summary: Optional[str] = None
