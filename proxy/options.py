from typing import ClassVar


class ProxyOptionsGoogle:
    """
    Опции прокси для Google
    """
    proxy_options: ClassVar[dict[dict[str, str]]]

    def __init__(cls):
        cls.proxy_options = dict()

    @property
    def options(cls):
        if cls.proxy_options:
            return cls.proxy_options

    @options.setter
    def options(cls, value: dict[str, str]):
        cls.proxy_options = dict(dict(**value))
