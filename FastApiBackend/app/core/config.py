from pydantic import BaseSettings


class Settings(BaseSettings):
    # Base
    api_v1_prefix: str
    debug: bool
    project_name: str
    version: str
    description: str
    africas_talking_username: str
    africas_talking_api_key: str
    test_phone_number: str
    # Database
    db_connection_str: str
