from typing import TypeVar, Generic

from engine import Browser
from .proxy import Proxy, Proxies


T_co = TypeVar('T_co', bound=Browser, covariant=True)


class ProxyIPSSetter(Generic[T_co]):
    """
    Менеджер прокси.

    Отдает правильные настройки для браузера.
    """
    def __init__(self,
                 type_browser: T_co,
                 proxies: list[str] | None,
                 ) -> None:
        self._type_browser = type_browser
        self._proxies = list(proxies) if proxies else list()

    def convert_str_to_proxy_type(self, id_proxy: str) -> Proxy[str]:
        """
        Помещает ``ID`` в тип ``Proxy``
        """
        return Proxy(id_proxy)

    def get_proxies(self) -> Proxies[Proxy[str]]:
        """
        Получение списка прокси
        """
        return Proxies([self.convert_str_to_proxy_type(proxy)
                        for proxy
                        in self._proxies])

    def set_ips_proxy(self) -> T_co:
        """
        Устанавливает ``Необходимые прокси адреса`` для браузера
        """
        self._type_browser.set_proxies(self._proxies)
        return self._type_browser
