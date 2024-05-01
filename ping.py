from scapy.all import IP, ICMP, Raw, sr1, sniff

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

def main():
    alphabet = alphabet_list(end= 'v')

    ping_request = IP(dst = 'www.google.com')/ICMP(type = 8, code = 0, id = 1, seq = 1)/Raw(alphabet)
    #ping_request.show()

    ping_reply = sr1(ping_request)
    #print(ping_reply.show())

    print(ping_reply[Raw].load.decode())

if __name__ == "__main__":
    main()