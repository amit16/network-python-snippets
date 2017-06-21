#Send a dns query using scapy

from scapy.all import *

dns_query = sr1(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="www.gslab.com")),verbose=0)
print dns_query[DNS].summary()
