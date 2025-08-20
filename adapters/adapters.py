from abc import ABC, abstractmethod
from typing import ClassVar, Any
from types import MappingProxyType

from selenium import webdriver

from common import TypeBrowser
from proxy import Proxy
from config import settings
from .options import Options
from .d_types import ID_INSTANCE, ADAPT_ID_INSTANCE


class Adapter(ABC):
    """
    Базовый адаптер
    """
    distinctiveness: ClassVar[Any]
    security_distinctiveness: ClassVar[Any]
    type_browser: ClassVar[str]

    @abstractmethod
    def adapt_proxy(self) -> dict[dict[str, ADAPT_ID_INSTANCE]] | str: ...


class GoggleChromeAdapter(Adapter):
    type_browser: ClassVar[str] = TypeBrowser.CHROME
    distinctiveness: ClassVar[str] = settings.GOOGLE_SETTINGS.PROXY_ARGUMENT

    def __init__(self, proxy: Proxy[ID_INSTANCE]):
        self._proxy = proxy
        self._options = webdriver.ChromeOptions()
        self._secure_options = None
        if not proxy.is_secure:
            adapt_proxy = self.distinctiveness.format(proxy.full_address)
            self._options.add_argument(adapt_proxy)
        else:
            self._secure_options = dict(proxy=dict(https=proxy.full_address))

    def wire_options(self) -> bool:
        return self._proxy.is_secure


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
