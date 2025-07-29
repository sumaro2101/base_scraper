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
    PROXIES_SIMPLE: ClassVar[list | None] = os.getenv('PROXIES_SIMPLE')
    PROXIES_AUTH: ClassVar[list | None] = os.getenv('PROXIES_AUTH')
    IPV4: ClassVar[bool] = False if os.getenv('IPV4_ENABLE') == 'False' else True

    @staticmethod
    def get_proxy_address(cls, type_browser: str) -> str:
        """
        Получение адресса прокси
        """



class Settings:
    """
    Базовая Конфигурация браузера
    """
    TYPE_BROWSER: ClassVar[str | None] = check_type_browser(os.getenv('TYPE_BROWSER'))
    PROXIES: ClassVar[dict[str, str]] = ProxySettings.get_proxy_address(TYPE_BROWSER)
