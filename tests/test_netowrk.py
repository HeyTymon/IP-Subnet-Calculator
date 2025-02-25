import unittest
from netlib import network_lib as nl

class TestNetwork(unittest.TestCase):

    # IPAddress class methods
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
    
    def test_conversion(self):
        
        ip1 = nl.IPAddress("169.254.0.1")
        ip_bytearray1 = nl.IPAddress.str_to_bytearray("169.254.0.1")
        ip_int1 = ip1.bytearray_to_int()

        self.assertEqual(nl.IPAddress.bytearray_to_str(ip_bytearray1), ip1.__str__())
        self.assertEqual(nl.IPAddress.int_to_bytearray(ip_int1),ip_bytearray1)
        self.assertEqual(ip1.int_to_bytearray_self(),ip_bytearray1)
        self.assertEqual(nl.IPAddress.int_to_bytearray(ip_int1),ip1.int_to_bytearray_self())

    # Network class methods
    def test_validate_cidr(self):

        self.assertTrue(nl.Network.validate_cidr(0))
        self.assertTrue(nl.Network.validate_cidr(8))
        self.assertTrue(nl.Network.validate_cidr(16))
        self.assertTrue(nl.Network.validate_cidr(24))
        self.assertTrue(nl.Network.validate_cidr(32))
        self.assertFalse(nl.Network.validate_cidr(-1))
        self.assertFalse(nl.Network.validate_cidr(33))

    def test_calc_host_number(self):

        ip = nl.IPAddress("10.0.0.1")
        
        self.assertEqual(nl.Network(ip,24).calc_host_number(24),254)
        self.assertEqual(nl.Network(ip,16).calc_host_number(16),65534)
        self.assertEqual(nl.Network(ip,8).calc_host_number(8),16777214)

    #CIDR is validated in Network constructor
    def test_calc_net_mask(self):

        ip = nl.IPAddress("10.0.0.1")
        
        self.assertEqual(nl.Network(ip,32).calc_net_mask(32).__str__(),"255.255.255.255")
        self.assertEqual(nl.Network(ip,30).calc_net_mask(30).__str__(),"255.255.255.252")
        self.assertEqual(nl.Network(ip,24).calc_net_mask(24).__str__(),"255.255.255.0")
        self.assertEqual(nl.Network(ip,16).calc_net_mask(16).__str__(),"255.255.0.0")
        self.assertEqual(nl.Network(ip,8).calc_net_mask(8).__str__(),"255.0.0.0")

if __name__ == '__main__':
    unittest.main()