from abc import ABC, abstractmethod
from typing import ClassVar, Any
from types import MappingProxyType

from common import TypeBrowser
from proxy import Proxy
from .options import OptionsGoogle, Options
from .d_types import ID_INSTANCE, ADAPT_ID_INSTANCE
from config import settings


class Adapter(ABC):
    """
    Базовый адаптер
    """
    distinctiveness: ClassVar[Any]
    security_distinctiveness: ClassVar[Any]
    type_browser: ClassVar[str]

    @classmethod
    @abstractmethod
    def adapt_proxy(self) -> dict[dict[str, ADAPT_ID_INSTANCE]] | str: ...


class GoggleChromeAdapter(Adapter):
    options: ClassVar[Options] = OptionsGoogle
    type_browser: ClassVar[str] = TypeBrowser.CHROME
    options: ClassVar[Options] = OptionsGoogle

    @classmethod
    def adapt_proxy(cls, proxy: Proxy[ID_INSTANCE]) -> dict[dict[str, ADAPT_ID_INSTANCE]] | str:
        if not proxy.is_secure:
            return cls.distinctiveness.format(proxy.full_address)
        return cls.security_distinctiveness.options({
            'https': proxy.full_address,
        })


class EdgeAdapter(Adapter):
    type_browser: ClassVar[str] = TypeBrowser.EDGE


class SafariAdapter(Adapter):
    type_browser: ClassVar[str] = TypeBrowser.SAFARI


class FirefoxAdapter(Adapter):
    type_browser: ClassVar[str] = TypeBrowser.FIREFOX


MenuAdapters = MappingProxyType({
    TypeBrowser.CHROME: GoggleChromeAdapter,
    TypeBrowser.EDGE: EdgeAdapter,
    TypeBrowser.FIREFOX: FirefoxAdapter,
    TypeBrowser.SAFARI: SafariAdapter,
})
