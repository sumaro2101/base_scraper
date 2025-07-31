import unittest

from pydantic import AnyUrl

from proxy import Proxy


class TestProxy(unittest.TestCase):
    """
    Тесты прокси
    """
    def setUp(self):
        self.ADDRESS_PROXY = AnyUrl('127.0.0.1:9081')
        self.ADDRESS_PROXY_SECURE = AnyUrl('user:password@127.0.0.1:9081')

    def test_proxy_simple(self):
        proxy = Proxy(self.ADDRESS_PROXY)
        proxy_2 = Proxy(self.ADDRESS_PROXY)
        self.assertEqual(proxy.id_proxy.port, 9081)
        self.assertFalse(proxy.is_secure)
        self.assertEqual(proxy, proxy_2)

    def test_proxy_auth(self):
        proxy = Proxy(self.ADDRESS_PROXY_SECURE)
        proxy_2 = Proxy(self.ADDRESS_PROXY_SECURE)
        self.assertEqual(proxy.id_proxy.port, 9081)
        self.assertTrue(proxy.is_secure)
        self.assertEqual(proxy, proxy_2)
