import pathlib
import os

from typing import ClassVar

from dotenv import load_dotenv

from .utils import check_type_browser


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

ENV_NAME = '.env'
ENV_FILE = BASE_DIR / ENV_NAME

load_dotenv(ENV_FILE)


class ProxySettings:
    """
    Конфигурация прокси
    """
    PROXY_ID: ClassVar[str | None] = os.getenv('PROXY_ID')
    PROXY_PORT: ClassVar[str | None] = os.getenv('PROXY_PORT')
    PROXY_USERNAME: ClassVar[str | None] = os.getenv('PROXY_USERNAME')
    PROXY_PASSWORD: ClassVar[str | None] = os.getenv('PROXY_PASSWORD')
    IPV4: ClassVar[bool] = False if os.getenv('IPV4_ENABLE') == 'False' else True

    @staticmethod
    def get_proxy_address(cls, type_browser: str) -> str:
        """
        Получение адресса прокси
        """
        check_type_browser(type_browser)


class Settings:
    """
    Базовая Конфигурация браузера
    """
    TYPE_BROWSER: ClassVar[str | None] = os.getenv('TYPE_BROWSER')
    PROXY: ClassVar[str] = ProxySettings.get_proxy_address(os.getenv('TYPE_BROWSER'))
