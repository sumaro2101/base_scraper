from typing import Protocol, ClassVar


class SupportSetProxyProtocol(Protocol):
    """
    Протокол поддержки установки прокси
    """

    def set_proxies(self, ids_proxies): ...


class SupportTypeBrowserProtocol(Protocol):
    """
    Протокол поддержки протокола
    """
    type_browser: ClassVar[str]


class SupportBrowserProtocol(SupportSetProxyProtocol,
                             SupportTypeBrowserProtocol):
    """
    Протокол поддержки браузера
    """
