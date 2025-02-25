import netlib.network_lib as nl 

net = nl.Network(nl.IPAddress("192.168.1.1"),24)

# print(net.__str__())
ip_str: str = ""


# print(bin(net.ip.ip_to_binary()))

# print(len(str(bin(net.ip.ip_to_binary()))))


# print(net.ip._ip_int)
# print(net.ip._ip)
# print(net.ip.ip_bytearray)
# print(net.ip.binary_to_ip())
 
data = nl.IPAddress.int_to_binary(pow(2,32-24)-1)
negated_data = bytearray(~byte & 0xFF for byte in data)

print(nl.IPAddress.binary_to_str(negated_data))