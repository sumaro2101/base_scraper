from typing import ClassVar, Literal

from proxy import Proxies, Proxy

from common import TypeBrowser


class Browser:
    type_browser: ClassVar[Literal[TypeBrowser.CHROME,
                                   TypeBrowser.EDGE,
                                   TypeBrowser.FIREFOX,
                                   TypeBrowser.SAFARI]]

    def set_proxies(self, ids_proxies: Proxies[Proxy[str]]) -> None:
        ...
