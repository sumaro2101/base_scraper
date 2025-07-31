from typing import Protocol, TypeVar

from .d_types import ID_INSTANCE


T = TypeVar('T', bound=ID_INSTANCE)


class SupportAddaterProtocol(Protocol):
    """
    Протокол поддерживающий Адаптор
    """

    def adapt_proxy(self): ...


class SupportAddaptBrowserProtocol(Protocol):
    """
    Протокол поддерживающий Адаптацию для Браузера
    """

    def adapt_to_browser(self, browser): ...


class SupportSecureProtocol(Protocol):
    """
    Протокол поддерживающий Secure
    """

    @property
    def is_secure(self) -> bool: ...


class SupportIDProxyProtocol(Protocol[T]):
    """
    Протокол поддерживающий ID Proxy
    """

    @property
    def id_proxy(self) -> T: ...


class SupportProxyProtocol(SupportSecureProtocol,
                           SupportAddaptBrowserProtocol,
                           SupportIDProxyProtocol,
                           ):
    """
    Протокол прокси
    """
