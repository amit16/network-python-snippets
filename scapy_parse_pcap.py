import scapy

def scpy_parse_pcap(pcapfile, src, dst, protocol=None, dst_port=None):
    pkt_count = 0
    packets = list()
    pcap = rdpcap(pcapfile)
    protocol = protocol.upper()
    for pkt in pcap:
        try:
            if dst_port is None:
                if pkt.haslayer(protocol) and pkt[IP].src == src and \
                        pkt[IP].dst == dst:
                    pkt_count = pkt_count + 1
                    packets.append(pkt.summary())
            else:
                if pkt.haslayer(protocol.upper()) and pkt[IP].src == src and \
                    pkt[IP].dst == dst and pkt[IP].dport == dst_port:
                    pkt_count = pkt_count + 1
                    packets.append(pkt.summary())
         except Scapy_Exception as ex:
            msg = 'Parsing pcap files failed: %s parse()' % (e)
            raise ValueError(msg=msg)
     
     #Returns packet summary and packet count                   
     return packets, pkt_count

