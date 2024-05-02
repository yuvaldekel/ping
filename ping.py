from scapy.all import IP, ICMP, Raw, sr1, sr, send
from sys import argv

def is_ping(packet):
    return ICMP in packet

def alphabet_list(start = "A", end = 'z'):
    alphabet = []
    A_ascii = ord(start)
    Z_ascii = ord(end)

    for ascii_rep in range(A_ascii, Z_ascii + 1):
        letter = ascii_rep.to_bytes().decode('ascii')
        if letter.isalpha():
            alphabet.append(letter)
    
    return ''.join(alphabet)        

def sr_ping(n, data):
    packets = []
    for i in range(n):
        ping_request = IP(dst = 'www.google.com')/ICMP(type = 8, code = 0, id = n + 1, seq = n + 1)/Raw(data)
        packets.append(ping_request)

    ping_replies = sr(packets)

    return ping_replies

def main():
    ip = argv[1]
    n = int(argv[2])

    alphabet = alphabet_list(end= 'v')

    reply_packets = sr_ping(4, alphabet)[0]
    loads = [packet[1][Raw].load.decode() for packet in reply_packets if ICMP in packet[1]]

    received = len(loads)

    print(f"Sent {n} packets to {ip}")
    print(f"Received {received} reply packets from {ip}")
    [print(f'got data {load[1]} for packet {load[0]}') for load in enumerate(loads)]

if __name__ == "__main__":
    main()