#Does a tcp handshake
#Input - args : interface-name and domain(destination ip address/fqdn)

import sys
from scapy.all import*


def main():
    if len(sys.argv)<3:
        print "fewer arguements"
        sys.exit(1)
    else:
        tap_interface = sys.argv[1]
        domain = sys.argv[2]

    syn = IP(dst=domain) / TCP(dport=80, flags='S')
    syn_ack = sr1(syn)
    getStr = 'GET / HTTP/1.1\r\nHost: domain\r\n\r\n'
    request = IP(dst=domain) / TCP(dport=80, sport=syn_ack[TCP].dport,seq=syn_ack[TCP].ack,\
             ack=syn_ack[TCP].seq + 1, flags='A') / getStr
    reply = sr1(request)

if __name__ == '__main__':
    main()
