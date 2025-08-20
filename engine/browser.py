from typing import ClassVar

from proxy.proxy import Proxy, Proxies

from config import settings
from proxy.adapters import MenuAdapters, Adapter


class Browser:
    """
    Класс браузера (Основная рабочая единица)
    """
    type_browser: ClassVar[str] = settings.TYPE_BROWSER
    adapter: ClassVar[Adapter]

    def __init__(self):
        self.adapter = MenuAdapters[self.type_browser]

    def set_proxies(self, ids_proxies: Proxies[Proxy[str]]) -> None:
        ...
