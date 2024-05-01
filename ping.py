from scapy.all import IP, ICMP, Raw, sr1, sniff
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

def sr_ping(ID, sq, data):
    ping_request = IP(dst = 'www.google.com')/ICMP(type = 8, code = 0, id = ID, seq = sq)/Raw(data)

    ping_reply = sr1(ping_request, timeout = 1)

    return ping_reply

def main():
    ip = argv[1]
    n = int(argv[2])

    received = 0
    alphabet = alphabet_list(end= 'v')

    for i in range(n):
        reply = sr_ping(n + 1, n + 1, alphabet)
        if reply != None:
            received = received + 1

    print(f"Sent {n} packets to {ip}")
    print(f"Received {received} reply packets from {ip}")

if __name__ == "__main__":
    main()