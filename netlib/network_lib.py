class IPAddress:

    _ip: str

    def __init__(self,ip: str):
        if(self.validate_addr(ip)):
            self._ip = ip
        else:
            raise ValueError("Incorrect ip address value")

    @staticmethod
    def validate_addr(ip: str) -> bool: 
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
    cidr: int #usunac zamiast tego w if wyliczac maske
    mask: int
    host_number: int
    first_address: IPAddress
    gateway: IPAddress
    broadcast: IPAddress

    def __init__(self, ip: IPAddress, cidr: int):
        if(self.validate_cidr(cidr)):
            self.cidr = cidr
        else:
            raise ValueError("Incorrect cidr value") 
        
        self.ip = ip
        self.host_number = self.calc_host_number()
        

    @staticmethod
    def validate_cidr(cidr: int):
        return 0 <= cidr <= 32

    def calc_host_number(self):
        return pow(2,32-self.cidr)-2