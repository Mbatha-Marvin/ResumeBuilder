from sqlmodel import Session, select
from fastapi import HTTPException
import pyotp, time, datetime
from app.v1.database.models.verification_model import (
    VerificationV1,
    VerificationV1Create,
    VerificationV1Read,
    PhoneVerificationV1Request,
)


class VerificationCRUDServices:
    def __init__(self, session: Session) -> None:
        self.session = session

    def generate_time_based_otp(self) -> int:
        otp_generator = pyotp.TOTP(s="U2ERQTKVMK7KKDJQSVS5T4LEK57VB24V", interval=1)
        return int(otp_generator.now())

    def create_phone_number_verification_details(self, user_id: int) -> bool:
        otp_code = self.generate_time_based_otp()
        otp_created_at = datetime.datetime.now()
        otp_expiry_at = otp_created_at + datetime.timedelta(minutes=5)

        verification_create = VerificationV1Create(
            otp_code=otp_code,
            otp_created_at=otp_created_at,
            otp_expiry_at=otp_expiry_at,
            number_verified=False,
            user_id=user_id,
        )

        verification_instance = VerificationV1.from_orm(verification_create)
        self.session.add(verification_instance)
        self.session.commit()
        self.session.refresh(verification_instance)

        return True

    # def verify_phone_number(self, user_id: int, otp_code: int) -> VerificationV1Read:
    #     user = self.get_user(user_id=user_id)
    #     if user is None:
    #         raise HTTPException(status_code=404, detail="User not Found")
    #     else:
    #         verification_instance = user.verification_details[
    #             (len(user.verification_details) - 1)
    #         ]
    #         if verification_instance.otp_code == otp_code:
    #             verification_instance.number_verified = True
    #             self.session.add(verification_instance)
    #             self.session.commit()
    #             self.session.refresh(verification_instance)

    #             response = VerificationV1Read(status=True)
    #             return response
    #         else:
    #             response = VerificationV1Read(status=True)
    #             raise HTTPException(status_code=409, detail=response)


class CreateVerificationDetails:
    def __init__(self, session: Session) -> None:
        self.session = session

    def generate_time_based_otp(self) -> int:
        otp_generator = pyotp.TOTP(s="U2ERQTKVMK7KKDJQSVS5T4LEK57VB24V", interval=1)
        return int(otp_generator.now())

    def create_phone_number_verification_details(self, user_id: int) -> bool:
        otp_code = self.generate_time_based_otp()
        otp_created_at = datetime.datetime.now()
        otp_expiry_at = otp_created_at + datetime.timedelta(minutes=5)

        verification_create = VerificationV1Create(
            otp_code=otp_code,
            otp_created_at=otp_created_at,
            otp_expiry_at=otp_expiry_at,
            number_verified=False,
            user_id=user_id,
        )

        verification_instance = VerificationV1.from_orm(verification_create)
        self.session.add(verification_instance)
        self.session.commit()
        self.session.refresh(verification_instance)

        return True
