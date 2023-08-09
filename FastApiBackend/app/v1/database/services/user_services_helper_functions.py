from app.v1.database.models.user_model import UserV1


def get_full_profile(user: UserV1) -> dict:
    full_profile = {}

    # check if profile details has data before trying to access them
    if len(user.profile_details) > 0:
        user_profile = {
            "personal_website_url": user.profile_details[0].personal_website,
            "linkein_url": user.profile_details[0].linkedin_url,
            "github_url": user.profile_details[0].github_url,
            "work_title_highlight": user.profile_details[0].user_work_title,
            "first_name": user.profile_details[0].first_name,
            "last_name": user.profile_details[0].last_name,
            "middle_name": user.profile_details[0].middle_name,
            "email": user.email,
            "city": user.profile_details[0].city,
            "country": user.profile_details[0].country,
            "address": user.profile_details[0].address,
            "phone_number": user.phone_number,
        }
        summary = {
            "card_title": "string",
            "brief_description": user.profile_details[0].user_summary,
        }

        objectives = {
            "card_title": "string",
            "brief_description": user.profile_details[0].objectives,
        }
        hobbies = {
            "card_title": "string",
            "hobbies": user.profile_details[0].hobbies,
        }
        skills = user.profile_details[0].skills

    else:
        user_profile = {
            "personal_website_url": "",
            "linkein_url": "",
            "github_url": "",
            "work_title_highlight": "",
            "first_name": "",
            "last_name": "",
            "middle_name": "",
            "email": user.email,
            "city": "",
            "country": "",
            "address": "",
            "phone_number": user.phone_number,
        }
        summary = {
            "card_title": "string",
            "brief_description": "",
        }
        objectives = {
            "card_title": "string",
            "brief_description": "",
        }
        hobbies = {
            "card_title": "string",
            "hobby_details": "",
        }
        skills = ""

    # check if education details has data before trying to access them
    if len(user.education_details) > 0:
        education = {
            "card_title": user.education_details[0].card_title,
            "education_details": [
                {
                    "school_name": detail.school_name,
                    "education_level": detail.education_level,
                    "location": detail.location,
                    "course_title": detail.course_title,
                    "final_grade": detail.final_grade,
                    "start_date": detail.start_date,
                    "end_date": detail.finish_date,
                }
                for detail in user.education_details
            ],
        }
    else:
        education = {"card_title": "", "education_details": []}

    # check if experience details has data before trying to access them
    if len(user.experience_details) > 0:
        experience = {
            "card_title": user.experience_details[0].card_title,
            "experience_details": [
                {
                    "job_title": detail.job_title,
                    "company_name": detail.company_name,
                    "company_url": detail.company_url,
                    "location": detail.location,
                    "job_description_title": detail.job_description_title,
                    "job_description": detail.job_descriptions,
                    "start_date": detail.start_date,
                    "end_date": detail.end_date,
                }
                for detail in user.experience_details
            ],
        }
    else:
        experience = {"card_title": "", "experience_details": []}

    # check if language details has data before trying to access them
    if len(user.language_details) > 0:
        language = {
            "card_title": user.language_details[0].card_title,
            "language_details": [
                {
                    "language_name": detail.language_name,
                    "profeciency_level": detail.profeciency_level,
                }
                for detail in user.language_details
            ],
        }
    else:
        language = {"card_title": "", "language_details": []}

    # check if project details has data before trying to access them
    if len(user.project_details) > 0:
        project = {
            "card_title": user.project_details[0].card_title,
            "project_details": [
                {
                    "project_title": detail.project_name,
                    "project_url": detail.project_url,
                    "project_description_list": detail.project_description,
                    "project_description_title": detail.project_description_title,
                }
                for detail in user.project_details
            ],
        }
    else:
        project = {"card_title": "", "project_details": []}

    # check if certification details has data before trying to access them
    if len(user.certification_details) > 0:
        certification = {
            "card_title": user.certification_details[0].card_title,
            "certification_details": [
                {
                    "school_name": detail.school_name,
                    "school_type": detail.school_type,
                    "certified_on": detail.certified_on,
                    "start_date": detail.start_date,
                    "end_date": detail.end_date,
                }
                for detail in user.certification_details
            ],
        }
    else:
        certification = {"card_title": "", "certification_details": []}

    # check if referee details has data before trying to access them
    if len(user.referee_details) > 0:
        referee = {
            "card_title": user.referee_details[0].card_title,
            "referee_details": [
                {
                    "full_name": detail.full_name,
                    # "email": detail.email,
                    "phone_number": detail.phone_number,
                    "company_name": detail.company_name,
                    "occupation": detail.occupation,
                    "address": detail.address,
                }
                for detail in user.referee_details
            ],
        }
    else:
        referee = {"card_title": "", "referee_details": []}

    full_profile["user_profile"] = user_profile
    full_profile["summary"] = summary
    full_profile["objectives"] = objectives
    full_profile["hobbies"] = hobbies
    full_profile["skills"] = skills
    full_profile["education"] = education
    full_profile["experience"] = experience
    full_profile["language"] = language
    full_profile["project"] = project
    full_profile["certification"] = certification
    full_profile["referee"] = referee

    return full_profile
