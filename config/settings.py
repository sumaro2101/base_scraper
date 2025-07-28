import pathlib

from pydantic_settings import BaseSettings
from pydantic import BaseModel


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


class ProxySettings(BaseModel):
    ...


class Settings(BaseSettings):
    """
    Базовая Конфигурация браузера
    """
    ...
