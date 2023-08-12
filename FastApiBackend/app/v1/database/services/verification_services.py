from typing import List
from sqlmodel import Session, select
from fastapi import HTTPException
import africastalking
import pyotp, datetime
from app.v1.database.models.verification_model import (
    VerificationV1,
    VerificationV1Create,
)
from app import settings


class CreateVerificationDetails:
    def __init__(self, session: Session) -> None:
        self.session = session

    def generate_time_based_otp(self) -> int:
        otp_generator = pyotp.TOTP(s="U2ERQTKVMK7KKDJQSVS5T4LEK57VB24V", interval=1)
        return int(otp_generator.now())

    def send_otp_to_number(self, otp_code: int, phone_number: List[str]):
        # Initialize SDK
        username = settings.africas_talking_username
        api_key = settings.africas_talking_api_key
        africastalking.initialize(username, api_key)

        # Initialize a service e.g. SMS
        sms = africastalking.SMS
        phone_number_test = [settings.test_phone_number]

        # Use the service synchronously
        response = sms.send(
            f"Your OTP code is {otp_code} for Number: {phone_number}", phone_number_test
        )
        print(response)

    def create_phone_number_verification_details(self, user_id: int) -> int:
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

        return otp_code

    def update_phone_verified_field(self, user_id: int) -> bool:
        verification_instance = self.session.exec(
            select(VerificationV1).where(VerificationV1.user_id == user_id)
        ).one_or_none()

        verification_instance.number_verified = True

        self.session.add(verification_instance)
        self.session.commit()
        self.session.refresh(verification_instance)

        return True

        pass
