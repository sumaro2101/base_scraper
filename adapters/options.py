from abc import ABC

from typing import ClassVar

from config import settings
from .d_types import ID_INSTANCE, ADAPT_ID_INSTANCE
from proxy import Proxy


class Options(ABC):
    """
    Абстрактный класс опций браузера
    """


class OptionsGoogle(Options):
    """
    Настройки для Google Браузера
    """
    proxy_options: ClassVar[dict[dict[str, str]]]
    distinctiveness: ClassVar[str] = settings.GOOGLE_SETTINGS.PROXY_ARGUMENT

    def __init__(cls):
        cls.proxy_options = dict()

    @property
    def options(cls):
        if cls.proxy_options:
            return cls.proxy_options

    @options.setter
    def options(cls, value: dict[str, str]):
        cls.proxy_options = dict(dict(**value))

    @classmethod
    def get_proxy_options(cls, proxy_address: Proxy[ID_INSTANCE]) -> dict[dict[str, ADAPT_ID_INSTANCE]] | ADAPT_ID_INSTANCE:
        """
        """
        if not proxy_address.is_secure:
            return cls.distinctiveness.format(proxy_address.full_address)
        cls.options({
            'https': proxy.full_address,
        })
