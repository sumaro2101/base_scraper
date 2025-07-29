from typing import TypeVar, Generic

T = TypeVar('T', bound=str)


class ProxyManagerBrowser(Generic[T]):
    """
    Менеджер прокси.

    Отдает правильные настройки для браузера исходя oт типа браузера.
    """
    def __init__(self,
                 type_browser: T,
                 proxies_simple: list[T] | None,
                 proxies_auth: list[T] | None,
                 ) -> None:
        self._type_browser = str(type_browser)
        self._proxies_simple = list(proxies_simple)
        self._proxies_auth = list(proxies_auth)

    @property
    def type_browser(self) -> T:
        return self._type_browser
