from app.v1.database.models.user_model import UserV1Create
from app.v1.database.models.profile_model import ProfileV1Create
from app.v1.database.models.education_model import EducationV1Create
from app.v1.database.models.experience_model import ExperienceV1Create
from app.v1.database.models.language_model import LanguageV1Create
from app.v1.database.models.certification_model import CertificationV1Create
from app.v1.database.models.referee_model import RefereeV1Create
from app.v1.database.models.project_model import ProjectV1Create
from datetime import date
from pydantic import EmailStr

start_date = date(year=2017, month=9, day=21)
end_date = date(year=2021, month=3, day=24)


class DummyUserData:
    def __init__(
        self, user_id: int, dummy_email: EmailStr, dummy_phone_number: str
    ) -> None:
        self.user_id = user_id
        self.dummy_user = UserV1Create(
            password="TestPass",
            email=dummy_email,
            phone_number=dummy_phone_number,
        )
        self.dummy_education_1 = EducationV1Create(
            card_title="Education",
            school_name="University 1",
            education_level="Bachelors Degree",
            location="Location 1",
            course_title="Course Title 1",
            final_grade="Final Grade",
            start_date=start_date,
            end_date=end_date,
            user_id=user_id,
        )
        self.dummy_education_2 = EducationV1Create(
            card_title="Education",
            school_name="University 2",
            education_level="Masters Degree",
            location="Location 2",
            course_title="Course Title 2",
            final_grade="Final Grade 2",
            start_date=start_date,
            end_date=end_date,
            user_id=user_id,
        )
        self.dummy_experience_1 = ExperienceV1Create(
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
        self.dummy_experience_2 = ExperienceV1Create(
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
        self.dummy_profile = ProfileV1Create(
            first_name="first_name",
            last_name="last_name",
            middle_name="middle_name",
            image_url="image_url.com",
            linkedin_url="linkedin_url.com",
            github_url="github_url.com",
            personal_website="personal_website_url.com",
            city="some city",
            country="some country",
            address="some address",
            skills=[
                "skill 1",
                "skill 2",
                "skill 3",
                "skill 4",
                "skill 5",
                "skill 6",
                "skill 7 slighly longer",
                "skill 8",
            ],
            hobbies=[
                "hobby 1",
                "hobby 2",
                "hobby 3",
                "hobby 4",
                "hobby 5",
                "hobby 6",
                "hobby 7 slighly longer",
                "hobby 8",
            ],
            user_work_title="some work title",
            user_id=user_id,
            user_summary="some user summary description that is longer than the rest to test text wrapping in the cards",
            objectives="some user objective description that is longer than the rest to test text wrapping in the cards",
        )
        self.dummy_language_1 = LanguageV1Create(
            card_title="Language",
            language_name="First Language",
            profeciency_level=5,
            user_id=user_id,
        )
        self.dummy_language_2 = LanguageV1Create(
            card_title="Language",
            language_name="Second Language",
            profeciency_level=4,
            user_id=user_id,
        )
        self.dummy_language_3 = LanguageV1Create(
            card_title="Language",
            language_name="Third Language",
            profeciency_level=5,
            user_id=user_id,
        )
        self.dummy_language_4 = LanguageV1Create(
            card_title="Language",
            language_name="Forth Language",
            profeciency_level=4,
            user_id=user_id,
        )
        self.dummy_project_1 = ProjectV1Create(
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
        self.dummy_project_2 = ProjectV1Create(
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
        self.dummy_certification_1 = CertificationV1Create(
            card_title="Certification",
            school_name="Maseno",
            school_type="University",
            certified_on="Engineering",
            start_date="2023-06-29",
            end_date="2023-06-29",
            user_id=user_id,
        )
        self.dummy_certification_2 = CertificationV1Create(
            card_title="Certification",
            school_name="Moringa",
            school_type="BootCamp",
            certified_on="Software Engineering",
            start_date="2023-07-29",
            end_date="2023-10-29",
            user_id=user_id,
        )

        self.dummy_referee_1 = RefereeV1Create(
            card_title="Referee",
            full_name=f"Full_Name_1",
            phone_number="A phone number",
            company_name=f"Some_Company_Name_1",
            occupation=f"Some_Job_Title_1",
            address=f"Some_Address_1",
            user_id=user_id,
        )
        self.dummy_referee_2 = RefereeV1Create(
            card_title="Referee",
            full_name=f"Full_Name_2",
            phone_number="A phone number",
            company_name=f"Some_Company_Name_2",
            occupation=f"Some_Job_Title_2",
            address=f"Some_Address_2",
            user_id=user_id,
        )
