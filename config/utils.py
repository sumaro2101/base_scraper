from common import TypeBrowser, ErrorCodeProgram
from .exeptions import (
    ClassBrowserNotProvideError,
    RequiredEnviromentNotSetError,
    )


ENV_NAME_BROWSER = 'TYPE_BROWSER'


def check_type_browser(type_browser: str) -> None:
    """
    Функция проверка типа браузера.
    """
    if not type_browser:
        raise RequiredEnviromentNotSetError(
            ErrorCodeProgram.ENV_NOT_FOUND.format(ENV_NAME_BROWSER),
            )
    try:
        TypeBrowser[type_browser]
    except KeyError:
        raise ClassBrowserNotProvideError(
            ErrorCodeProgram.BROWSER_NOT_PROVIDE.format(type_browser),
            )
