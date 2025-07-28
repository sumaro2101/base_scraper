import unittest

from .utils import check_type_browser


class TestUtils(unittest.TestCase):

    def test_check_browser(self):
        type_browser = 'CHROME'
        self.assertIsNone(check_type_browser(type_browser))
