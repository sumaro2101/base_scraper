from .common import TypeBrowser
from .exeptions import ClassBrowserNotProvideError


def check_type_browser(type_browser: str) -> None:
    if type_browser not in TypeBrowser:
        raise ClassBrowserNotProvideError(f'{type_browser} is not provide')
