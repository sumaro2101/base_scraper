import pathlib
import os

from dotenv import load_dotenv

from pydantic import BaseModel, AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

from .utils import check_type_browser


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

ENV_NAME = '.env'
ENV_FILE = BASE_DIR / ENV_NAME

load_dotenv(ENV_FILE)


class GoogleChromeSettings(BaseModel):
    """
    Конфигурация Google Chrome
    """
    PROXY_DISTINCTIVENESS: str = '--proxy-server={0}'


class ProxySettings(BaseModel):
    """
    Конфигурация прокси
    """
    PROXIES_SIMPLE: list[AnyUrl] | None = os.getenv('PROXIES_SIMPLE')
    PROXIES_AUTH: list[AnyUrl] | None = os.getenv('PROXIES_AUTH')
    REGEX_PROXY_PATTERN: str = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{1,5}\b'
    IPV4: bool = False if os.getenv('IPV4_ENABLE') == 'False' else True


class Settings(BaseSettings):
    """
    Базовая Конфигурация браузера
    """
    model_config = SettingsConfigDict(
        extra='ignore',
    )

    TYPE_BROWSER: str | None = check_type_browser(os.getenv('TYPE_BROWSER'))
    PROXIES: ProxySettings = ProxySettings()
    GOOGLE_SETTINGS: GoogleChromeSettings = GoogleChromeSettings()


settings = Settings()
