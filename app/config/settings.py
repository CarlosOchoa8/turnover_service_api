# """
# Settings for the project.
# """

# from pydantic import Extra
# from pydantic_settings import BaseSettings

# from app.config.common import CONFIG_FILE, AppSettings
# from app.config.database.settings import DatabaseSettings


# class Settings(BaseSettings):
#     """
#     Settings class for the project.
#     """
#     app_environment: str
#     database: AppSettings = DatabaseSettings()

#     class Config:
#         """
#         Settings class configuration.
#         """

#         env_file = CONFIG_FILE
#         extra = "allow"


# settings = Settings()
