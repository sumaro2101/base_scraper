from enum import Enum


class TypeBrowser(str, Enum):
    """
    Типы поддерживаемых браузеров
    """
    CHROME = 'Google Chrome'
    FIREFOX = 'Firefox'
    SAFARI = 'Sarari'
    EDGE = 'Edge'
