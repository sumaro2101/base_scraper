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
                      SOCKET_INSTANCE,
                      )
from config import settings
from engine import SupportBrowserProtocol


T = TypeVar('T', bound=ID_INSTANCE)


class Proxy(Generic[T]):
    """
    Прокси тип
    """
    adapters: ClassVar[dict[str, Adapter]] = MenuAdapters
    secure: ClassVar[bool]

    def __init__(self,
                 id_proxy: T,
                 ) -> None:
        self._id_proxy = id_proxy
        self._username = None
        self._password = None
        self._socket = None
        self._get_username_password(self._id_proxy)
        self.secure = self._check_secure()

    @property
    def id_proxy(self) -> T:
        return self._id_proxy

    @property
    def is_secure(self) -> bool:
        return self.secure

    @property
    def username(self) -> USERNAME_DATA:
        return self._username

    @property
    def password(self) -> PASSWORD_DATA:
        return self._password

    def _get_username_password(self, value: str) -> None:
        enter_data: re.Match[str] | None = re.search(
            settings.PROXIES.REGEX_ENTER_DATA_PATTERN,
            value,
            )
        if enter_data:
            cleared_data = enter_data.group().rstrip('@')
            self._username, self._password = cleared_data.split(':')

    def _check_secure(self) -> bool:
        logger.debug(self._id_proxy)
        return self.username or self.password

    def adapt_to_browser(self, browser: SupportBrowserProtocol) -> ADAPT_ID_INSTANCE | dict[dict[str, T]]:
        adapter = self.adapters[browser.type_browser]
        return adapter(self).adapt_proxy()

    def __eq__(self, value):  # type: ignore[override]
        return self._id_proxy.__eq__(value)

    def __str__(self) -> str:
        return str(self._id_proxy)

    def __repr__(self):
        return repr(self._id_proxy)


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
