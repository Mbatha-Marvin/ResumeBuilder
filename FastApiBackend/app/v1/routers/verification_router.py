from fastapi import APIRouter, Depends, HTTPException
from app.core.db import get_db_session
from sqlmodel import Session, select
from app.v1.database.models.verification_model import (
    VerificationV1Read,
    PhoneVerificationV1Request,
)
from app.v1.database.models.user_model import UserV1
from app.v1.database.services.verification_services import CreateVerificationDetails

router = APIRouter(
    prefix="/user/{user_id}/verification", tags=["Verification Version 1"]
)


@router.post("/phone")
def verify_otp_code(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    phone_number_verification_request: PhoneVerificationV1Request,
):
    user = session.exec(select(UserV1).where(UserV1.user_id == user_id)).one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not Found")
    else:
        if (
            user.verification_details[0].otp_code
            == phone_number_verification_request.otp_code
        ):
            verification_details_service = CreateVerificationDetails(session=session)
            updated_successfully = (
                verification_details_service.update_phone_verified_field(
                    user_id=user_id
                )
            )
            if updated_successfully:
                return {"message": "OTP Code Verified"}
            else:
                raise HTTPException(status_code=409, detail="OTP invalid or expired")
        else:
            raise HTTPException(status_code=409, detail="OTP invalid or expired 2")
        pass
    pass
