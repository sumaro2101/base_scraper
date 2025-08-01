import unittest

from proxy.proxy import Proxy
from config import settings


class TestProxy(unittest.TestCase):
    """
    Тесты прокси
    """
    def setUp(self):
        self.settings = settings.model_copy()
        self.settings.PROXIES.PROXIES_URLS = ['138.128.91.65:8000', 'login:password@138.128.91.65:8100']

    def test_proxy_simple(self):
        proxy = Proxy(self.settings.PROXIES.PROXIES_URLS[0])
        proxy_2 = Proxy(self.settings.PROXIES.PROXIES_URLS[0])
        self.assertFalse(proxy.is_secure)
        self.assertEqual(proxy, proxy_2)

    def test_proxy_auth(self):
        proxy = Proxy(self.settings.PROXIES.PROXIES_URLS[-1])
        proxy_2 = Proxy(self.settings.PROXIES.PROXIES_URLS[-1])
        self.assertTrue(proxy.is_secure)
        self.assertEqual(proxy, proxy_2)
