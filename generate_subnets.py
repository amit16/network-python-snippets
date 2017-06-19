import ipaddress
import random
import os

my_net = ipaddress.ip_network(u'10.0.0.0/8')

#Generates all possible subnets in the above network, in this 2000 subnets
subnet_list = list(my_net.subnets(prefixlen_diff=11))

print subnet_list
