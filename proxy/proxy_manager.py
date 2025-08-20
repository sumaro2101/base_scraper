from typing import TypeVar, Generic

from engine.browser import Browser
from .proxy import Proxy, Proxies
from .d_types import ID_INSTANCE


T_co = TypeVar('T_co', bound=Browser, covariant=True)


class ProxyIPSSetter(Generic[T_co]):
    """
    Менеджер прокси.

    Отдает правильные настройки для браузера.
    """
    def __init__(self,
                 type_browser: T_co,
                 proxies: list[ID_INSTANCE] | None,
                 ) -> None:
        self._type_browser = type_browser
        self._proxies = list(proxies) if proxies else list()

    def put_to_proxy_type(self, ip_proxy: ID_INSTANCE) -> Proxy[ID_INSTANCE]:
        """
        Помещает ``ID`` в тип ``Proxy``
        """
        return Proxy(ip_proxy)

    def get_proxies(self) -> Proxies[Proxy[ID_INSTANCE]]:
        """
        Получение списка прокси
        """
        return Proxies([self.put_to_proxy_type(proxy)
                        for proxy
                        in self._proxies])

    def set_ips_proxy(self) -> T_co:
        """
        Устанавливает ``Необходимые прокси адреса`` для браузера
        """
        proxies = self.get_proxies()
        self._type_browser.set_proxies(proxies)
