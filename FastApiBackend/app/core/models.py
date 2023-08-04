from pydantic import BaseModel, EmailStr, validator
from sqlmodel import Column, SQLModel, Field, Relationship, ARRAY, String
import datetime
from typing import Optional, List


class HealthCheck(BaseModel):
    name: str
    version: str
    description: str


# The class `UserBase` represents a user with attributes such as name, password, and email.
class UserBase(SQLModel):
    name: str = Field(index=True)
    password: str = Field(index=True, nullable=False)
    email: EmailStr = Field(nullable=False, unique=True, index=True)


# The User class represents a user with various details such as education, experience, language,
# projects, and contact information.
class User(UserBase, table=True):
    user_id: int = Field(default=None, primary_key=True)
    education_details: List["Education"] = Relationship(back_populates="user")
    experience_details: List["Experience"] = Relationship(back_populates="user")
    language_details: List["Language"] = Relationship(back_populates="user")
    project_details: List["Project"] = Relationship(back_populates="user")
    user_contact_details: List["UserContact"] = Relationship(back_populates="user")


# The `UserCreate` class is a subclass of `UserBase` and includes a `Config` class with an `example`
# attribute that provides an example JSON schema for creating a user.
class UserCreate(UserBase):
    class Config:
        schema_extra = {
            "example": {
                "name": "UserName",
                "password": "Password",
                "email": "Email",
            }
        }


# The `UserRead` class is a subclass of `UserBase` that includes a `user_id` attribute and a `Config`
# class with an example schema.
class UserRead(UserBase):
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "name": "UserName - type(string)",
                "password": "Password  - type(string)",
                "email": "user_email - type(email)",
                "user_id": "user_id",
            }
        }


# The `UserUpdate` class is a subclass of `UserBase` that allows for updating user information such as
# name and password.
class UserUpdate(UserBase):
    name: Optional[str] = None
    password: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "New UserName",
                "password": "New Password",
                "user_id": "User_id",
            }
        }


# The class "EducationBase" represents educational information including card title, school name,
# education level, location, course title, final grade (optional), start date, and finish date.
class EducationBase(SQLModel):
    card_title: str
    school_name: str
    education_level: str
    location: str
    course_title: str
    final_grade: Optional[str] = Field(default=None)
    start_date: datetime.date
    finish_date: datetime.date


# The class Education represents education details of a user with a foreign key relationship to the
# User class.
class Education(EducationBase, table=True):
    education_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.user_id")
    user: Optional[User] = Relationship(back_populates="education_details")


# The `EducationCreate` class is a subclass of `EducationBase` that includes a `user_id` attribute and
# a `Config` class with an example schema for creating an education record.
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
                "user_id": "valid id",
            }
        }


# The `EducationRead` class represents an education record with various attributes and includes an
# example schema for validation.
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
                "user_id": "valid id",
                "education_id": 0,
            }
        }


# The `EducationUpdate` class represents an update to a user's education information, including
# details such as card title, school name, education level, course title, location, final grade, start
# date, and finish date.
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
                "user_id": "valid id",
            }
        }


# The above class represents a base model for storing experience information, including job titles,
# company names, job descriptions, and dates.
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


# The class "Experience" represents a user's experience details and includes a foreign key
# relationship to the "User" class.
class Experience(ExperienceBase, table=True):
    experience_id: int = Field(primary_key=True, default=None)

    user_id: int = Field(foreign_key="user.user_id")
    user: Optional[User] = Relationship(back_populates="experience_details")


# The `ExperienceCreate` class is a subclass of `ExperienceBase` that includes a `user_id` attribute
# and a `Config` class with an example schema for creating a new experience.
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
                "user_id": "valid id",
            }
        }


# The `ExperienceRead` class is a subclass of `ExperienceBase` that includes additional attributes for
# `user_id` and `experience_id`, and it has a `Config` class with an example schema.
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
                "user_id": "valid id",
                "experience_id": 0,
            }
        }


# The `ExperienceUpdate` class represents an update to a user's experience, including job title,
# company name, location, job descriptions, and dates.
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
                "user_id": "valid id",
            }
        }


# The above class represents a base model for a language with attributes such as card title, language
# name, and proficiency level.
class LanguageBase(SQLModel):
    card_title: str
    language_name: str
    profeciency_level: int


# The `Language` class represents a programming language and its relationship with a user.
class Language(LanguageBase, table=True):
    language_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.user_id")
    user: List[User] = Relationship(back_populates="language_details")


# The `LanguageCreate` class is a subclass of `LanguageBase` that includes a `user_id` attribute and a
# `Config` class with an example schema.
class LanguageCreate(LanguageBase):
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "language_name": "Language Name",
                "profeciency_level": 5,
                "user_id": "valid id",
            }
        }


# The `LanguageRead` class represents a language read operation and includes properties for user ID
# and language ID.
class LanguageRead(LanguageBase):
    user_id: int
    language_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "language_name": "Language Name",
                "profeciency_level": 5,
                "user_id": "valid id",
                "language_id": 0,
            }
        }


# The `LanguageUpdate` class represents an update to a language entry in a database, including the
# card title, language name, and proficiency level.
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
                "user_id": "valid id",
            }
        }


# The `ProjectBase` class is a SQLModel that represents a project with attributes such as card title,
# project name, project description title, project description, and project URL.
class ProjectBase(SQLModel):
    card_title: str
    project_name: str
    project_description_title: str
    project_description: List[str] = Field(
        default=None, sa_column=Column(ARRAY(String()))
    )
    project_url: Optional[str]


# The `Project` class represents a project with a unique project ID, associated with a user and a list
# of users.
class Project(ProjectBase, table=True):
    project_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.user_id")
    user: List[User] = Relationship(back_populates="project_details")


# The `ProjectCreate` class is a subclass of `ProjectBase` and includes a `user_id` attribute.
class ProjectCreate(ProjectBase):
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "project_name": "Project Name",
                "project_description_title": "Project Description Title",
                "project_description": ["Description 1", "Description 2"],
                "project_url": "project_url.com",
                "user_id": "valid id",
            }
        }


# The `ProjectRead` class is a subclass of `ProjectBase` and represents a project with additional
# properties for user ID and project ID.
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
                "project_url": "project_url.com",
                "user_id": "valid id",
                "project_id": 0,
            }
        }


# The `ProjectUpdate` class is a model for updating project information, including the card title,
# project name, project description title, project description, and project URL.
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
                "project_url": "project_url.com",
                "user_id": "valid id",
            }
        }


# The class `UserContactBase` represents a user's contact information and work details.
class UserContactBase(SQLModel):
    personal_website: Optional[str]
    city: str
    country: str
    phone_number: str
    user_work_title: str
    user_summary: str


class UserContact(UserContactBase, table=True):
    user_contact_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.user_id")
    user: List[User] = Relationship(back_populates="user_contact_details")


class UserContactCreate(UserContactBase):
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "personal_website": "personal_website",
                "city": "City",
                "country": "Country of residence",
                "phone_number": "Phone Number",
                "user_work_title": "User Work Title",
                "user_summary": "User Summary",
                "user_id": "valid id",
            }
        }


class UserContactRead(UserContactBase):
    user_id: int
    user_contact_id: int

    class Config:
        schema_extra = {
            "example": {
                "personal_website": "personal_website",
                "city": "City",
                "country": "Country of residence",
                "phone_number": "Phone Number",
                "user_work_title": "User Work Title",
                "user_summary": "User Summary",
                "user_id": "valid id",
                "user_contact_id": 0,
            }
        }


class UserContactUpdate(SQLModel):
    personal_website: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    phone_number: Optional[str] = None
    user_work_title: Optional[str] = None
    user_summary: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "personal_website": "personal_website",
                "city": "City",
                "country": "Country of residence",
                "phone_number": "Phone Number",
                "user_work_title": "User Work Title",
                "user_summary": "User Summary",
                "user_id": "valid id",
            }
        }


# The class UserProfileRead is a subclass of UserBase and represents a user profile with optional
# education, experience, language, project, and contact details.
class UserProfileRead(UserBase):
    education_details: Optional[List[EducationBase]] = None
    experience_details: Optional[List[Experience]] = None
    language_details: Optional[List[Language]] = None
    project_details: Optional[List[Project]] = None
    user_contact_details: Optional[List[UserContact]] = None
