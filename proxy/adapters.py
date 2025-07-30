from abc import ABC, abstractmethod
from typing import ClassVar, Any
from types import MappingProxyType

from common import TypeBrowser
from .proxy import Proxy
from config import settings


class Adapter(ABC):
    """
    Базовый адаптер
    """
    distinctiveness: ClassVar[Any]
    security_distinctiveness: ClassVar[Any]
    type_browser: ClassVar[str]

    @abstractmethod
    def __init__(self, proxy: Proxy) -> None:
        self._proxy = proxy

    @abstractmethod
    def adapt_proxy(self) -> Proxy[str]: ...


class GoggleChromeAdapter(Adapter):
    distinctiveness: ClassVar[str] = settings.GOOGLE_SETTINGS.PROXY_DISTINCTIVENESS
    type_browser: ClassVar[str] = TypeBrowser.CHROME

    def __init__(self, proxy: Proxy):
        super().__init__(proxy)

    def adapt_proxy(self):
        return super().adapt_proxy()


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
