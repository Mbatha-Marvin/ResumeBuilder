from sqlmodel import Column, SQLModel, Field, Relationship, ARRAY, String
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.v1.database.models.language_model import UserV1


# The `ProjectV1Base` class is a SQLModel that represents a project with attributes such as card title,
# project name, project description title, project description, and project URL.
class ProjectV1Base(SQLModel):
    card_title: str
    project_name: str
    project_description_title: str
    project_description: List[str] = Field(
        default=None, sa_column=Column(ARRAY(String()))
    )
    project_url: Optional[str]


# The `ProjectV1` class represents a project with a unique project ID, associated with a user and a list
# of users.
class ProjectV1(ProjectV1Base, table=True):
    project_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="userv1.user_id")
    user: Optional["UserV1"] = Relationship(back_populates="project_details")


# The `ProjectV1Create` class is a subclass of `ProjectV1Base` and includes a `user_id` attribute.
class ProjectV1Create(ProjectV1Base):
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "project_name": "Project Name",
                "project_description_title": "Project Description Title",
                "project_description": ["Description 1", "Description 2"],
                "project_url": "project_url.com",
                "user_id": 0,
            }
        }


# The `ProjectV1Read` class is a subclass of `ProjectV1Base` and represents a project with additional
# properties for user ID and project ID.
class ProjectV1Read(ProjectV1Base):
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
                "user_id": 0,
                "project_id": 0,
            }
        }


# The `ProjectV1Update` class is a model for updating project information, including the card title,
# project name, project description title, project description, and project URL.
class ProjectV1Update(SQLModel):
    card_title: Optional[str] = None
    project_name: Optional[str] = None
    project_description_title: Optional[str] = None
    project_description: Optional[List[str]] = None
    project_url: Optional[str] = None

    class Config:
        exclude = {"user_id"}
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "project_name": "Project Name",
                "project_description_title": "Project Description Title",
                "project_description": ["Description 1", "Description 2"],
                "project_url": "project_url.com",
                # "user_id": 0,
            }
        }
