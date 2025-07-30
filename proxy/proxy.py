import operator
import reprlib

from typing import Generic, TypeVar

from collections import abc


T = TypeVar('T', bound=str)


class Proxy(Generic[T]):
    """
    Прокси тип
    """
    def __init__(self,
                 id_proxy: T,
                 ) -> None:
        self._id_proxy = id_proxy

    @property
    def id_proxy(self) -> T:
        return self._id_proxy


P = TypeVar('P', bound=Proxy)


class Proxies(Generic[P], abc.Sequence):
    """
    Свой тип прокси
    """
    def __init__(self,
                 ids_proxies: list[P],
                 ) -> None:
        """
        Args:
            ids_proxies (list[P]): Список ``IDs`` для ``Proxy``
        """
        self._ids_proxies = list(ids_proxies)
        self._empty = bool(ids_proxies)

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
