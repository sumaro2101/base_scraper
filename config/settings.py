import os
import json
import pathlib
import re

from pydantic import BaseModel, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import load_dotenv

from loguru import logger

from .utils import check_type_browser
from .exeptions import WrongProxyError, WrongFormatListError
from common import ErrorCodeProgram


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

ENV_NAME = '.env'
ENV_FILE = BASE_DIR / ENV_NAME

load_dotenv(ENV_FILE)


class GoogleChromeSettings(BaseModel):
    """
    Конфигурация Google Chrome
    """
    PROXY_ARGUMENT: str = '--proxy-server={0}'


class ProxySettings(BaseModel):
    """
    Конфигурация прокси
    """
    try:
        PROXIES_URLS: list[str] = json.loads(os.getenv('PROXIES_URLS', default='[]'))
    except json.decoder.JSONDecodeError:
        raise WrongFormatListError(ErrorCodeProgram.JSON_DECODE_ENV_ERROR.format('PROXIES_URLS'))
    REGEX_ENTER_DATA_PATTERN: str = r'(.{1,}:.{1,}@)'
    REGEX_IP_PORT_PATTERN: str = r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{1,4})(:[0-9]{1,4})?'
    REGEX_PROXY_PATTERN: str = r'^' + REGEX_ENTER_DATA_PATTERN + r'{0,1}' + REGEX_IP_PORT_PATTERN + r'$'
    IPV4: bool = False if os.getenv('IPV4', default=True) == 'False' else True
    ALONE_PROXY: bool = False if os.getenv('IPV4', default=True) == 'False' else True

    @model_validator(mode='after')
    def check_proxy_list(self):
        list_of_proxy: str | list = self.PROXIES_URLS
        logger.debug(f'Get list from env {list_of_proxy}')
        if not isinstance(list_of_proxy, list):
            raise WrongFormatListError(ErrorCodeProgram.WRONG_FORMAT_LIST_ERROR.format('PROXIES_URLS'))
        for proxy in list_of_proxy:
            if re.match(self.REGEX_PROXY_PATTERN, proxy) is None:
                logger.debug(f'Enter Wrong data {proxy} in regex {self.REGEX_PROXY_PATTERN}')
                raise WrongProxyError(ErrorCodeProgram.WRONG_PROXY_ERROR.format(proxy))
        return self


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
