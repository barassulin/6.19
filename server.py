from scapy.all import *

Timeout=0.5
PORT = 20
CIP = input("enter ip")

while PORT<1024:
    syn_segment = TCP(dport=PORT, seq=123, flags='S')
    syn_packet = IP(dst=CIP)/syn_segment
    syn_ack_packet = sr1(syn_packet, timeout = Timeout)
    F = syn_ack_packet['TCP'].flags  # this should give you an integer
    if F & SYN and F & ACK:
        print("port: " + PORT)
    else:
        print("closed")
    PORT=PORT+1
