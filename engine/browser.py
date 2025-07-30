from proxy import Proxies


class Browser:

    def set_proxies(self, ids_proxies: Proxies[str]) -> None:
        ...

    def set_auth_proxies(self, ids_auth_proxies: Proxies[str]) -> None:
        ...
