# db refers to database in this file

from app import settings
import subprocess, time
from sqlmodel import create_engine, SQLModel, Session


DATABASE_URL = settings.db_connection_str
engine = create_engine(url=DATABASE_URL, echo=True)


def upgrade_to_alembic_head():
    time.sleep(2)
    result = subprocess.run(
        ["alembic", "upgrade", "head"],
        shell=True,
        capture_output=True,
        text=True,
    )
    print(result.stdout)


def initialize_db():
    time.sleep(5)
    SQLModel.metadata.create_all(bind=engine)


def get_db_session():
    with Session(engine) as session:
        yield session
