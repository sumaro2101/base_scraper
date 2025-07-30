from typing import TypeVar, Generic

from engine import Browser

T_co = TypeVar('T', bound=Browser, covariant=True)


class ProxyIPSSetter(Generic[T_co]):
    """
    Менеджер прокси.

    Отдает правильные настройки для браузера.
    """
    def __init__(self,
                 type_browser: T_co,
                 proxies_simple: list[str] | None,
                 proxies_auth: list[str] | None,
                 ) -> None:
        self._type_browser = type_browser
        self._proxies_simple = list(proxies_simple)
        self._proxies_auth = list(proxies_auth)

    def set_ips_proxy(self) -> T_co:
        """
        Устанавливает ``Необходимые прокси адреса`` для браузера
        """
        self._type_browser.set_proxies(self._proxies_simple)
        self._type_browser.set_auth_proxies(self._proxies_auth)
        return self._type_browser
