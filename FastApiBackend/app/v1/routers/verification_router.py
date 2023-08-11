from fastapi import APIRouter, Depends
from app.core.db import get_db_session
from sqlmodel import Session
from app.v1.database.services.verification_services import VerificationCRUDServices
from app.v1.database.models.verification_model import (
    PhoneVerificationV1Request,
    VerificationV1Read,
)

router = APIRouter(
    prefix="/user/{user_id}/verification", tags=["Verification Version 1"]
)


@router.post("/", response_model=VerificationV1Read)
def create_user_referee(
    *,
    session: Session = Depends(get_db_session),
    user_id: int,
    otp_code: PhoneVerificationV1Request
):
    verification_crud_services = VerificationCRUDServices(session=session)
    return verification_crud_services.verify_phone_number(
        user_id=user_id, otp_code=otp_code.opt_code
    )
