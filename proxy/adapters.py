from abc import ABC, abstractmethod
from typing import ClassVar, Any
from types import MappingProxyType

from common import TypeBrowser
from .protocols import SupportProxyProtocol
from .options import ProxyOptionsGoogle
from .d_types import ID_INSTANCE, ADAPT_ID_INSTANCE
from config import settings


class Adapter(ABC):
    """
    Базовый адаптер
    """
    distinctiveness: ClassVar[Any]
    security_distinctiveness: ClassVar[Any]
    type_browser: ClassVar[str]

    @abstractmethod
    def __init__(self, proxy: SupportProxyProtocol[ID_INSTANCE]) -> None:
        self._proxy = proxy

    @abstractmethod
    def adapt_proxy(self) -> dict[dict[str, ADAPT_ID_INSTANCE]] | str: ...


class GoggleChromeAdapter(Adapter):
    distinctiveness: ClassVar[str] = settings.GOOGLE_SETTINGS.PROXY_ARGUMENT
    security_distinctiveness: ClassVar[ProxyOptionsGoogle] = ProxyOptionsGoogle
    type_browser: ClassVar[str] = TypeBrowser.CHROME

    def __init__(self, proxy: SupportProxyProtocol):
        super().__init__(proxy)

    def adapt_proxy(self) -> dict[dict[str, ADAPT_ID_INSTANCE]] | str:
        if not self._proxy.is_secure:
            return self.distinctiveness.format(self._proxy.id_proxy)
        return self.security_distinctiveness.options({
            'https': self._proxy.id_proxy,
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
