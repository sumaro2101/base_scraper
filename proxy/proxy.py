import operator
import reprlib

from collections import abc


class Proxies(abc.Sequence):
    """
    Свой тип прокси
    """
    def __init__(self,
                 ids_proxies: list[str],
                 ) -> None:
        """
        Args:
            ids_proxies (list[str]): Список ``IDs`` для ``Proxy``
        """
        self._ids_proxies = list(ids_proxies)

    def __len__(self):
        return len(self._ids_proxies)

    def __getitem__(self, position: int) -> str:
        index = operator.index(position)
        return self._ids_proxies[index]

    def __eq__(self, other):
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        ids = reprlib.repr(self._ids_proxies)
        ids = ids[ids.find('['):-1]
        return f'Proxies({ids})'
