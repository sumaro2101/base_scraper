from abc import ABC, abstractmethod
from typing import ClassVar, Any
from types import MappingProxyType

from common import TypeBrowser


class Adapter(ABC):
    """
    Базовый адаптер
    """
    distinctiveness: ClassVar[Any]
    type_browser: ClassVar[str]

    @abstractmethod
    def adapt(self) -> str: ...


class GoggleChromeAdapter(Adapter):
    type_browser: ClassVar[str] = TypeBrowser.CHROME


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
