from enum import Enum


class TypeBrowser(str, Enum):
    """
    Типы поддерживаемых браузеров
    """
    CHROME = 'Google Chrome'
    FIREFOX = 'Firefox'
    SAFARI = 'Sarari'
    EDGE = 'Edge'


class ErrorCodeProgram(str, Enum):
    """
    Значения кодов ошибок (программное)
    """
    ENV_NOT_FOUND = 'Env {0} not found.'
    BROWSER_NOT_PROVIDE = '{0} is not provide.'
