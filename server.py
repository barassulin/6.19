from scapy.all import *
from scapy.layers.inet import TCP, IP

Timeout = 0.5
PORT = 20


def main():
    cip = input("enter ip")
    while PORT < 1024:
        syn_segment = TCP(dport=PORT, seq=123, flags='S')
        syn_packet = IP(dst=cip) / syn_segment
        syn_ack_packet = sr1(syn_packet, timeout=Timeout)
        if syn_ack_packet[TCP].flags & TCP.SYN == TCP.SYN and \
                syn_ack_packet[TCP].flags & TCP.ACK == TCP.ACK:
            print("port: " + PORT)
        else:
            print("closed")
        PORT = PORT + 1


if __name__ == "__main__":
    main()
