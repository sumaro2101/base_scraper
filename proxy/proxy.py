import re
import operator
import reprlib

from typing import Generic, TypeVar, ClassVar

from collections import abc

from loguru import logger

from .adapters import MenuAdapters, Adapter
from .d_types import (ID_INSTANCE,
                      ADAPT_ID_INSTANCE,
                      USERNAME_DATA,
                      PASSWORD_DATA,
                      IP_DATA,
                      PORT_DATA,
                      )
from config import settings
from engine import SupportBrowserProtocol


T = TypeVar('T', bound=ID_INSTANCE)


class Proxy(Generic[T]):
    """
    Прокси тип
    """
    adapters: ClassVar[dict[str, Adapter]] = MenuAdapters

    def __init__(self,
                 ip_proxy: T | None,
                 ) -> None:
        self._ip_proxy = ip_proxy
        self._username = None
        self._password = None
        self._ip = None
        self._port = None
        if self._ip_proxy:
            self._get_username_password(self._ip_proxy)
            self._get_ip_port(self._ip_proxy)
            self._secure = self._check_secure(self._ip_proxy)

    @property
    def full_address(self) -> T:
        return self._ip_proxy

    @property
    def is_secure(self) -> bool:
        return self._secure

    @property
    def with_auth(self) -> bool:
        return bool(self._username or self._password)

    @property
    def username(self) -> USERNAME_DATA:
        return self._username

    @property
    def password(self) -> PASSWORD_DATA:
        return self._password

    @property
    def ip(self) -> IP_DATA:
        return self._ip

    @property
    def port(self) -> PORT_DATA:
        return self._port

    def _get_username_password(self, value: str) -> None:
        enter_data: re.Match[str] | None = re.search(
            settings.PROXIES.REGEX_ENTER_DATA_PATTERN,
            value,
            )
        if enter_data:
            cleared_data = enter_data.group().rstrip('@')
            logger.debug(cleared_data)
            self._username, self._password = cleared_data.split(':')

    def _get_ip_port(self, value: str) -> None:
        socket: re.Match[str] = re.search(
            settings.PROXIES.REGEX_IP_PORT_PATTERN,
            value,
        )
        if socket:
            self._ip, self._port = socket.group().split(':')

    def _check_secure(self, value: str) -> bool:
        scheme: re.Match[str] = re.search(
            settings.PROXIES.REGEX_SCHEME_PATTERN,
            value,
        )
        if scheme:
            return scheme.group().rstrip('://') == 'https'

    def adapt_to_browser(self, browser: SupportBrowserProtocol) -> ADAPT_ID_INSTANCE | dict[dict[str, T]]:
        adapter = self.adapters[browser.type_browser]
        return adapter(self).adapt_proxy()

    def __eq__(self, value):  # type: ignore[override]
        if isinstance(self, value.__class__):
            return str(self) == str(value)

    def __str__(self) -> str:
        return str(self._ip_proxy)

    def __repr__(self):
        return repr(self._ip_proxy)


P = TypeVar('P', bound=Proxy)


class Proxies(Generic[P], abc.Sequence):
    """
    Свой тип прокси
    """
    def __init__(self,
                 proxies: list[P],
                 ) -> None:
        """
        Args:
            ids_proxies (list[P]): Список ``IDs`` для ``Proxy``
        """
        self._ids_proxies = list(proxies)
        self._empty = bool(proxies)

    @property
    def empty(self) -> bool:
        return self._empty

    def __len__(self) -> int:
        return len(self._ids_proxies)

    def __getitem__(self, position: int) -> P:  # type: ignore[override]
        index = operator.index(position)
        return self._ids_proxies[index]

    def __eq__(self, other: abc.Sequence) -> bool:  # type: ignore[override]
        if isinstance(other, self.__class__):
            return False
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))

    def __str__(self) -> str:
        return str(list(self))

    def __repr__(self) -> str:
        ids = reprlib.repr(self._ids_proxies)
        ids = ids[ids.find('['):-1]
        return f'Proxies({ids})'
