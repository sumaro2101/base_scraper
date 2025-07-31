import pathlib

from environs import Env

from pydantic import BaseModel, AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

from .utils import check_type_browser


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

ENV_NAME = '.env'
ENV_FILE = BASE_DIR / ENV_NAME

env = Env()
env.read_env(ENV_FILE)


class GoogleChromeSettings(BaseModel):
    """
    Конфигурация Google Chrome
    """
    PROXY_DISTINCTIVENESS: str = '--proxy-server={0}'


class ProxySettings(BaseModel):
    """
    Конфигурация прокси
    """
    PROXIES_URLS: set[AnyUrl]
    REGEX_PROXY_PATTERN: str = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{1,5}\b'
    IPV4: bool = False if env.str('IPV4', default=False) == 'False' else True


class Settings(BaseSettings):
    """
    Базовая Конфигурация браузера
    """
    model_config = SettingsConfigDict(
        extra='ignore',
    )

    TYPE_BROWSER: str | None = check_type_browser(env.str('TYPE_BROWSER'))
    PROXIES: ProxySettings = ProxySettings(PROXIES_URLS=env.list('PROXIES_URLS', default=list()))
    GOOGLE_SETTINGS: GoogleChromeSettings = GoogleChromeSettings()


settings = Settings()
