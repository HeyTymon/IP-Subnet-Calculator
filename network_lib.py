class IPAddress:

    _ip: str

    def __init__(self,ip: str):
        if(self.validate_addr(ip)):
            self._ip = ip
        else:
            raise ValueError("Incorrect ip address value")

    def validate_addr(self,ip: str) -> bool: 
        octets = ip.split(".")
        if(len(octets) == 4):
            in_threshold = lambda o: 0 <= int(o) <= 255
            return all(octet.isdigit() for octet in octets) and all(in_threshold(octet) for octet in octets)
        else: 
            return False
        
    def __str__(self):
        return self._ip

class Network:

    ip: IPAddress
    cidr: int 
    mask: int
    gateway: IPAddress
    broadcast: IPAddress


print(IPAddress.validate_addr(None, "192.168.1.1"))   # True
print(IPAddress.validate_addr(None, "256.168.1.1"))   # False
print(IPAddress.validate_addr(None, "192.168.-1.1"))  # False
print(IPAddress.validate_addr(None, "192.168.one.1")) # False
print(IPAddress.validate_addr(None, "300.10.10.10"))  # False
