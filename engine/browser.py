from proxy import Proxies, Proxy


class Browser:

    def set_proxies(self, ids_proxies: Proxies[Proxy[str]]) -> None:
        ...

    def set_auth_proxies(self, ids_auth_proxies: Proxies[Proxy[str]]) -> None:
        ...
