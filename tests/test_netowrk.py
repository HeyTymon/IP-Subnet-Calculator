import unittest
from netlib import network_lib as nl

class TestNetwork(unittest.TestCase):
    def test_validate_ip(self):
        
        self.assertTrue(nl.IPAddress.validate_addr("10.0.0.1"))
        self.assertTrue(nl.IPAddress.validate_addr("192.168.0.1"))
        self.assertTrue(nl.IPAddress.validate_addr("172.16.0.1"))
        self.assertTrue(nl.IPAddress.validate_addr("0.0.0.0"))
        self.assertTrue(nl.IPAddress.validate_addr("255.255.255.255"))
        self.assertFalse(nl.IPAddress.validate_addr("1.one.2.3"))
        self.assertFalse(nl.IPAddress.validate_addr("1.2.3"))
        self.assertFalse(nl.IPAddress.validate_addr("300.0.0.1"))
        self.assertFalse(nl.IPAddress.validate_addr("#.0.0.1"))

    def test_validate_cidr(self):

        self.assertTrue(nl.Network.validate_cidr(0))
        self.assertTrue(nl.Network.validate_cidr(8))
        self.assertTrue(nl.Network.validate_cidr(16))
        self.assertTrue(nl.Network.validate_cidr(24))
        self.assertTrue(nl.Network.validate_cidr(32))
        self.assertFalse(nl.Network.validate_cidr(-1))
        self.assertFalse(nl.Network.validate_cidr(33))

    def test_calc_host_number(self):
        
        self.assertEqual(nl.Network(nl.IPAddress("10.0.0.1"),24).calc_host_number(),254)
        self.assertEqual(nl.Network(nl.IPAddress("10.0.0.1"),16).calc_host_number(),65534)
        self.assertEqual(nl.Network(nl.IPAddress("10.0.0.1"),8).calc_host_number(),16777214)

if __name__ == '__main__':
    unittest.main()