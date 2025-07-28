from enum import Enum


class TypeBrowser(str, Enum):
    """
    Типы поддерживаемых браузеров
    """
    CHROME = 'Goggle Chrome'
    FIREFOX = 'Firefox'
    SAFARI = 'Sarari'
    EDGE = 'Edge'
