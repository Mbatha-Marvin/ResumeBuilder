from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
import datetime
from typing import Optional, List


class HealthCheck(BaseModel):
    name: str
    version: str
    description: str


class UserBase(SQLModel):
    name: str
    password: str


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)

    education_details: List["Education"] = Relationship(back_populates="user")
    experience_details: List["Experience"] = Relationship(back_populates="user")
    language_details: List["Language"] = Relationship(back_populates="user")


class UserCreate(UserBase):
    pass


class EducationBase(SQLModel):
    card_title: str
    school_name: str
    education_level: str
    location: str
    course_title: str
    final_grade: Optional[str]
    start_date: datetime.date
    finish_date: datetime.date


class Education(EducationBase, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")

    user: Optional[User] = Relationship(back_populates="education_details")


class EducationCreate(EducationBase):
    pass


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
