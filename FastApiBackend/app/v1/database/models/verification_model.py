from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime


if TYPE_CHECKING:
    from app.v1.database.models.language_model import UserV1


class VerificationV1BaseModel(SQLModel):
    otp_code: Optional[int] = Field(default=None)
    otp_created_at: Optional[datetime] = Field(default=None)
    otp_expiry_at: Optional[datetime] = Field(default=None)
    number_verified: Optional[bool] = Field(default=False)


class PhoneVerificationV1Request(SQLModel):
    otp_code: int

    class Config:
        schema_extra = {"example": {"otp_code": "valid OTP code"}}


class VerificationV1Read(SQLModel):
    status: bool


class VerificationV1Create(VerificationV1BaseModel):
    user_id: Optional[int] = None


class VerificationV1(VerificationV1BaseModel, table=True):
    verification_id: int = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="userv1.user_id")
    user: Optional["UserV1"] = Relationship(back_populates="verification_details")
