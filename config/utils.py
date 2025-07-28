from .common import TypeBrowser
from .exeptions import ClassBrowserNotProvideError


def check_type_browser(type_browser: str) -> None:
    try:
        TypeBrowser[type_browser]
    except KeyError:
        raise ClassBrowserNotProvideError(f'{type_browser} is not provide')
