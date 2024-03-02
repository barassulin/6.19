"""

Author: Bar Assulin
Date: 2/3/24

Description:
This program gets an ip from the client and finds if the ports are open or not.

"""

# imports:
from scapy.all import *
from scapy.layers.inet import TCP, IP

# constants:
Timeout = 0.5
SYN = 0x02
ACK = 0x10
STARTING_PORT = 20
ENDING_PORT = 1025


# funcs:
def main():
    cip = input("enter ip")
    port = STARTING_PORT
    while port < ENDING_PORT:
        syn_segment = TCP(dport=port, seq=123, flags='S')
        syn_packet = IP(dst=cip) / syn_segment
        syn_ack_packet = sr1(syn_packet, timeout=Timeout)
        if syn_ack_packet is not None:
            try:
                if syn_ack_packet['TCP'].flags & SYN and syn_ack_packet['TCP'].flags & ACK:
                    print("port: ", port, " is open")
                else:
                    print("port: ", port, " is closed")
            except Exception as err:
                print("error: ", err)
        else:
            print("port: ", port, " is not responding")
        port = port+1


if __name__ == "__main__":
    main()
