from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE_NAME = '.env'


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE_NAME, env_file_encoding='utf-8')

    BOT_TOKEN: SecretStr


config = Config()
