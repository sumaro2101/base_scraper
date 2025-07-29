import unittest

from .exeptions import (
    ClassBrowserNotProvideError,
    RequiredEnviromentNotSetError,
)
from .utils import check_type_browser, ENV_NAME_BROWSER
from .common import ErrorCodeProgram


class TestUtils(unittest.TestCase):

    def test_check_browser(self):
        type_browser = 'CHROME'
        self.assertIsNone(check_type_browser(type_browser))

    def test_fake_browser(self):
        type_browser = 'undefind'
        with self.assertRaises(ClassBrowserNotProvideError) as e:
            check_type_browser(type_browser)
        self.assertEqual(e.exception.args[0],
                         ErrorCodeProgram.BROWSER_NOT_PROVIDE.format(type_browser),
                         )

    def test_none_browser(self):
        with self.assertRaises(RequiredEnviromentNotSetError) as e:
            check_type_browser(None)
        self.assertEqual(e.exception.args[0],
                         ErrorCodeProgram.ENV_NOT_FOUND.format(ENV_NAME_BROWSER),
                         )
