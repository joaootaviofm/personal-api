from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingConfigDict(
        env_file = "../.env",
        env_file_encoding = "utf-8",
        extra="ignore",
    )

    database_url : str

settings = Settings()