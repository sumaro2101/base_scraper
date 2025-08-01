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
    WRONG_PROXY_ERROR = 'Format Proxy IP is wrong - {0}. Check your ENV file.'
    JSON_DECODE_ENV_ERROR = 'JSON can not decode variable {0}, must to be list format data. Check your ENV file.'
    WRONG_FORMAT_LIST_ERROR = '{0}, must to be list format data. Check your ENV file.'
