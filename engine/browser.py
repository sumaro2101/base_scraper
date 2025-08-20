from typing import ClassVar

from collections.abc import Generator

from proxy import Proxy, Proxies

from config import settings
from adapters import MenuAdapters, Adapter
from .processor import ServeProcess


class Browser:
    """
    Класс браузера (Основная рабочая единица)
    """
    type_browser: ClassVar[str] = settings.TYPE_BROWSER
    adapter: ClassVar[Adapter]

    def __init__(self, proxies: Proxies[Proxy]):
        self.adapter = MenuAdapters[self.type_browser]
        self._proxyes = proxies

    def __enter__(self) -> Generator[None, None, ServeProcess]:
        yield ServeProcess(self.adapter.get_options())
