class IPAddress:

    _ip: str
    ip_bytearray: bytearray
    _ip_int: int

    @staticmethod
    def validate_addr(ip: str) -> bool: 
        octets = ip.split(".")
        if(len(octets) == 4):
            in_threshold = lambda o: 0 <= int(o) <= 255
            return all(octet.isdigit() for octet in octets) and all(in_threshold(octet) for octet in octets)
        else: 
            return False
   
    @staticmethod
    def str_to_binary(ip: str) -> bytearray:
        octets = ip.split(".")
        return bytearray(int(octet) for octet in octets)
    
    @staticmethod
    def binary_to_str(ip: bytearray) -> str:
        return '.'.join(str(byte) for byte in ip)
                      
    @staticmethod
    def int_to_binary(num: int) -> bytearray:
        oct1 = (num >> 24) & 0xFF
        oct2 = (num >> 16) & 0xFF
        oct3 = (num >> 8) & 0xFF
        oct4 =  num & 0xFF
        return bytearray([oct1,oct2,oct3,oct4])
    
    def __init__(self,ip: str):
        if(self.validate_addr(ip)):
            self._ip = ip
            self.ip_bytearray = self.str_to_binary(ip)
            self._ip_int = self.ip_to_binary()
        else:
            raise ValueError("Incorrect ip address value")    
        
    def ip_to_binary(self) -> int:
        return self.ip_bytearray[0] << 24 | self.ip_bytearray[1] << 16 | self.ip_bytearray[2] << 8 | self.ip_bytearray[3]
    
    def binary_to_ip(self) -> bytearray:
        oct1 = (self._ip_int >> 24) & 0xFF
        oct2 = (self._ip_int >> 16) & 0xFF
        oct3 = (self._ip_int >> 8) & 0xFF
        oct4 =  self._ip_int & 0xFF
        return bytearray([oct1,oct2,oct3,oct4])

    def __str__(self):
        return self._ip

class Network:

    ip: IPAddress
    cidr: int 
    mask: int
    host_number: int
    first_address: IPAddress
    gateway: IPAddress
    broadcast: IPAddress

    @staticmethod
    def validate_cidr(cidr: int):
        return 0 <= cidr <= 32
    
    def __init__(self, ip: IPAddress, cidr: int):
        if(self.validate_cidr(cidr)):
            self.cidr = cidr
        else:
            raise ValueError("Incorrect cidr value") 
        
        self.ip = ip
        self.host_number = self.calc_host_number()
        self.mask = self.calc_net_mask(cidr)

    def calc_host_number(self):
        return pow(2,32-self.cidr)-2
    
    def calc_net_mask(self,cidr: int):
       negated_data = bytearray(~byte & 0xFF for byte in IPAddress.int_to_binary(pow(2,32-cidr)-1))
       self.mask = IPAddress(IPAddress.binary_to_str(negated_data)) 

    def __str__(self):
        return self.ip.__str__() + "/" + str(self.cidr)