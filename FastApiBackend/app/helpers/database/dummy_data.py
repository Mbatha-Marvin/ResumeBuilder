from sqlmodel import create_engine, SQLModel, Session
from app.core.db import engine
from datetime import date
from app.core.models import (
    User,
    UserCreate,
    Education,
    EducationCreate,
    Experience,
    ExperienceCreate,
    UserContact,
    UserContactCreate,
    Language,
    LanguageCreate,
    ProjectCreate,
    Project,
)

start_date = date(year=2022, month=9, day=21)
end_date = date(year=2023, month=3, day=21)


def create_dummy_user(user_id: int):
    dummy_user = UserCreate(
        name="Test User", password="TestPass", email="test@email.com"
    )
    dummy_education_1 = EducationCreate(
        card_title="Education",
        school_name="University 1",
        education_level="Bachelors Degree",
        location="Location 1",
        course_title="Course Title 1",
        final_grade="Final Grade",
        start_date=start_date,
        finish_date=end_date,
        user_id=user_id,
    )
    dummy_education_2 = EducationCreate(
        card_title="Education",
        school_name="University 2",
        education_level="Masters Degree",
        location="Location 2",
        course_title="Course Title 2",
        final_grade="Final Grade 2",
        start_date=start_date,
        finish_date=end_date,
        user_id=user_id,
    )
    dummy_experience_1 = ExperienceCreate(
        card_title="Experience",
        job_title="Job title 1",
        company_name="Company Name 1",
        company_url="company_1_url.com",
        location="Location 1",
        job_description_title="Job Description Title 1",
        job_descriptions=[
            "some job description entry 1",
            "some job description entry 2",
            "some job description entry 3 that is slightly lengthy for variety",
            "some job description entry 4 that is longer than the rest to test text wrapping in the cards",
            "some job description entry 5 ",
        ],
        start_date=start_date,
        end_date=end_date,
        user_id=user_id,
    )
    dummy_experience_2 = ExperienceCreate(
        card_title="Experience",
        job_title="Job title 2",
        company_name="Company Name 2",
        company_url="company_2_url.com",
        location="Location 2",
        job_description_title="Job Description Title 2",
        job_descriptions=[
            "some job description entry 1",
            "some job description entry 2",
            "some job description entry 3 that is slightly lengthy for variety",
            "some job description entry 4 that is longer than the rest to test text wrapping in the cards",
            "some job description entry 5 just for fun",
        ],
        start_date=start_date,
        end_date=end_date,
        user_id=user_id,
    )
    dummy_user_contact = UserContactCreate(
        personal_website="personal_website.com",
        city="Some City",
        country="Some Country",
        phone_number="+12345678909",
        user_work_title="A short and concise profession title",
        user_id=user_id,
        user_summary="This is a summary of your skills strengths, things you think are important for the recruiter to see in a glipmes. An ideal length is two paragraphs",
    )
    dummy_language_1 = LanguageCreate(
        card_title="Language",
        language_name="First Language",
        profeciency_level=5,
        user_id=user_id,
    )
    dummy_language_2 = LanguageCreate(
        card_title="Language",
        language_name="Second Language",
        profeciency_level=4,
        user_id=user_id,
    )
    dummy_language_3 = LanguageCreate(
        card_title="Language",
        language_name="Third Language",
        profeciency_level=5,
        user_id=user_id,
    )
    dummy_language_4 = LanguageCreate(
        card_title="Language",
        language_name="Forth Language",
        profeciency_level=4,
        user_id=user_id,
    )
    dummy_project_1 = ProjectCreate(
        card_title="Projects",
        project_name="Project Name or title",
        project_description_title="First project decription title",
        project_description=[
            "Project description entry 1",
            "Project description entry 2",
            "Project description entry 3 that is slightly lengthy for variety",
            "Project description entry 4 that is longer than the rest to test text wrapping in the cards",
            "Project description entry 5 ",
        ],
        project_url="some_github_url.com",
        user_id=user_id,
    )
    dummy_project_2 = ProjectCreate(
        card_title="Projects",
        project_name="Project Name or title",
        project_description_title="Second project decription title",
        project_description=[
            "Project description entry 1",
            "Project description entry 2",
            "Project description entry 3 that is slightly lengthy for variety",
            "Project description entry 4 that is longer than the rest to test text wrapping in the cards",
            "Project description entry 5 ",
        ],
        project_url="some_gitlab_url.com",
        user_id=user_id,
    )
    with Session(engine) as session:
        db_user_instance = session.get(User, user_id)
        if not db_user_instance:
            # create user
            db_user_entry = User.from_orm(dummy_user)

            session.add(db_user_entry)
            session.commit()
            session.refresh(db_user_entry)

            # Add education fields to user
            user_education_db_create_1 = Education.from_orm(dummy_education_1)
            session.add(user_education_db_create_1)
            session.commit()
            session.refresh(user_education_db_create_1)

            user_education_db_create_2 = Education.from_orm(dummy_education_2)
            session.add(user_education_db_create_2)
            session.commit()
            session.refresh(user_education_db_create_2)

            # Add experience fields to user
            user_experience_db_create_1 = Experience.from_orm(dummy_experience_1)
            session.add(user_experience_db_create_1)
            session.commit()
            session.refresh(user_experience_db_create_1)

            user_experience_db_create_2 = Experience.from_orm(dummy_experience_2)
            session.add(user_experience_db_create_2)
            session.commit()
            session.refresh(user_experience_db_create_2)

            # Add project fields to user
            user_project_db_create_1 = Project.from_orm(dummy_project_1)
            session.add(user_project_db_create_1)
            session.commit()
            session.refresh(user_project_db_create_1)

            user_project_db_create_2 = Project.from_orm(dummy_project_2)
            session.add(user_project_db_create_2)
            session.commit()
            session.refresh(user_project_db_create_2)

            # Add language fields to user
            user_language_db_create_1 = Language.from_orm(dummy_language_1)
            session.add(user_language_db_create_1)
            session.commit()
            session.refresh(user_language_db_create_1)

            user_language_db_create_2 = Language.from_orm(dummy_language_2)
            session.add(user_language_db_create_2)
            session.commit()
            session.refresh(user_language_db_create_2)

            user_language_db_create_3 = Language.from_orm(dummy_language_3)
            session.add(user_language_db_create_3)
            session.commit()
            session.refresh(user_language_db_create_3)

            user_language_db_create_4 = Language.from_orm(dummy_language_4)
            session.add(user_language_db_create_4)
            session.commit()
            session.refresh(user_language_db_create_4)

            # Add user_contact fields to user
            user_user_contact_db_create_1 = UserContact.from_orm(dummy_user_contact)
            session.add(user_user_contact_db_create_1)
            session.commit()
            session.refresh(user_user_contact_db_create_1)

            return "Dummy_user with user_id {user_id} successfully created"
        else:
            return "Dummy_user or User with user_id {user_id} already exists"
