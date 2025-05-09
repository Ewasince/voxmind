from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # secrets
    gigachat_token: str | None = Field(default=None)

    # recognizing settings
    key_phase: str = Field(default="jarvis")
    regexp: str = Field(default=r"[^A-Za-zА-ЯЁа-яё0-9 ]")
    language: str = "ru-RU"
