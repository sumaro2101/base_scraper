class ClassBrowserNotProvideError(Exception):
    """
    Исключение не поддерживаемого типа браузера
    """


class RequiredEnviromentNotSetError(Exception):
    """
    Исключение не установленной переменной
    """


class WrongProxyError(ValueError):
    """
    Исключение не верного прокси адреса
    """


class WrongFormatListError(ValueError):
    """
    Исключение не верного формата данных
    """
