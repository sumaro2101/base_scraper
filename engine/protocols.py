from typing import Protocol, ClassVar

from proxy.adapters import Adapter


class SupportSetProxyProtocol(Protocol):
    """
    Протокол поддержки установки прокси
    """

    def set_proxies(self, ids_proxies): ...


class SupportTypeBrowserProtocol(Protocol):
    """
    Протокол поддержки типа браузера
    """
    type_browser: ClassVar[str]


class SupportAdapterProtocol(Protocol):
    """
    Протокол поддержки адаптеров
    """
    adapter: ClassVar[Adapter]


class SupportBrowserProtocol(SupportSetProxyProtocol,
                             SupportTypeBrowserProtocol,
                             SupportAdapterProtocol):
    """
    Протокол поддержки браузера
    """
