import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List
from sqlmodel import Session, select

from app import settings
from app.core.models import HealthCheck, UserRead, User, UserCreate, UserUpdate
from app.core.db import get_db_session, initialize_db

app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    openapi_url=f"{settings.api_v1_prefix}/openapi.json",
    debug=settings.debug,
)


@app.on_event("startup")
def on_startup():
    initialize_db()


@app.get("/", response_model=HealthCheck, tags=["status"])
def health_check() -> dict:
    return {
        "name": settings.project_name,
        "version": settings.version,
        "description": settings.description,
    }


@app.get("/users/", response_model=List[UserRead], tags=["Users"])
def read_users(
    *,
    session: Session = Depends(get_db_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@app.get("/user/{user_id}", response_model=UserRead, tags=["Users"])
def read_user(*, session: Session = Depends(get_db_session), user_id: int):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not Found")
    return user


@app.post("/users/", response_model=UserRead, tags=["Users"])
def create_user(*, session: Session = Depends(get_db_session), user: UserCreate):
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.patch("/users/{user_id}", response_model=UserRead, tags=["Users"])
def update_user(
    *, session: Session = Depends(get_db_session), user_id: int, user: UserUpdate
):
    db_user_instance = session.get(User, user_id)
    if not db_user_instance:
        raise HTTPException(status_code=404, detail="User not Found")
    new_user_data = user.dict(exclude_unset=True)
    for key, value in new_user_data.items():
        setattr(db_user_instance, key, value)

    session.add(db_user_instance)
    session.commit()
    session.refresh(db_user_instance)
    return db_user_instance


@app.delete("/users/{user_id}")
def delete_user(*, session: Session = Depends(get_db_session), user_id: int):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not Found")
    session.delete(user)
    session.commit()
    return {"ok": True}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=5000,
        host="0.0.0.0",
        reload=True,
        use_colors=True,
    )
