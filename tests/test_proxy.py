import unittest

from pydantic import AnyUrl, BaseModel

from proxy.proxy import Proxy


class TestProxy(unittest.TestCase):
    """
    Тесты прокси
    """
    def setUp(self):
        class Addresses(BaseModel):
            address_proxy: AnyUrl
            address_proxy_secure: AnyUrl

        self.address = Addresses(
            address_proxy="138.128.91.65:8000",
            address_proxy_secure="login:password@138.128.91.65:8100",
            )

    def test_proxy_simple(self):
        proxy = Proxy(self.address.address_proxy)
        proxy_2 = Proxy(self.address.address_proxy)
        self.assertFalse(proxy.is_secure)
        self.assertEqual(proxy, proxy_2)

    def test_proxy_auth(self):
        proxy = Proxy(self.address.address_proxy_secure)
        proxy_2 = Proxy(self.address.address_proxy_secure)
        self.assertTrue(proxy.is_secure)
        self.assertEqual(proxy, proxy_2)
