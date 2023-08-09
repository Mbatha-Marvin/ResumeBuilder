from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING


if TYPE_CHECKING:
    from app.v1.database.models.user_model import UserV1


# The above class represents a base model for a language with attributes such as card title, language
# name, and proficiency level.
class LanguageV1Base(SQLModel):
    card_title: str
    language_name: str
    profeciency_level: int


# The `Language` class represents a programming language and its relationship with a user.
class LanguageV1(LanguageV1Base, table=True):
    language_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="userv1.user_id")
    user: Optional["UserV1"] = Relationship(back_populates="language_details")


# The `LanguageCreate` class is a subclass of `LanguageV1Base` that includes a `user_id` attribute and a
# `Config` class with an example schema.
class LanguageV1CreateRequest(LanguageV1Base):
    # user_id: int
    pass

    class Config:
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "language_name": "Language Name",
                "profeciency_level": 5,
                # "user_id": "valid id",
            }
        }


class LanguageV1Create(LanguageV1Base):
    user_id: Optional[int] = None


# The `LanguageRead` class represents a language read operation and includes properties for user ID
# and language ID.
class LanguageV1Read(LanguageV1Base):
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
class LanguageV1Update(SQLModel):
    card_title: Optional[str] = None
    language_name: Optional[str] = None
    profeciency_level: Optional[int] = None

    class Config:
        exclude = {"user_id"}
        schema_extra = {
            "example": {
                "card_title": "Card Title",
                "language_name": "Language Name",
                "profeciency_level": 5,
                # "user_id": "valid id",
            }
        }
