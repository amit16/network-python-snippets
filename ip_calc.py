#!/usr/bin/env python

# Reference: http://netaddr.readthedocs.io/en/latest/tutorial_01.html

from netaddr import *
import pprint
import os
import sys
import json
promptString= ("\nThis script needs up to 2 arguments:"
	           "\n   ./ip_calc.py 10.1.1.0/24        To break down a given subnet"
	           "\n   ./ip_calc.py 10.1.1.0/24 28     To split a given subnet into smaller ones.\n")
### function to calculate subnet
def calc_subnet(Subnet1):
	ip = IPNetwork(Subnet1)
	firstHost = ip[+1]
	lasttHost = ip[-2]
	print "\n----------  {}     -----------".format(Subnet1)
	print "Netmask:                    {}".format(ip.netmask)
	print "Network Address:            {}".format(ip.network)
	print "Broadcast Address:          {}".format(ip.broadcast)
	print "Numbers of usable host:     {}".format(len(ip) - 2)
	print "   First usable host:       {}".format(firstHost)
	print "   Last usable host:        {}".format(lasttHost)
### function to ascertain subnet address and prefix input
def check_input(Subnet1, Prefix1='None'):
	if Prefix1 == 'None':
		try:
			ip = IPNetwork(Subnet1)
			if ip.prefixlen > 31:
				print "\nGiven subnet {} is invalid.".format(Subnet1)
				raise
		except:
			print(promptString)
			quit()
	else:
		try:
			ip = IPNetwork(Subnet1)
			thisPrefix = int(Prefix1)
			if ip.prefixlen > 31:
				print "\nGiven subnet {} is invalid.".format(Subnet1)
				raise
			if thisPrefix < ip.prefixlen or thisPrefix > 30:
				print "\nThe desired prefix '{}' is either invalid or already a superset of given prefix '{}'.".format(Prefix1, ip.prefixlen)
				raise
		except:
			print(promptString)
			quit()
###
if len(sys.argv) == 2:
	mySubnet      = sys.argv[1]
	check_input(mySubnet)
	calc_subnet(mySubnet)
	print""
elif len(sys.argv) == 3:
	bigSubnet     = sys.argv[1]
	myPrefix      = sys.argv[2]
	check_input(bigSubnet, myPrefix)
	bigSubnet     = IPNetwork(sys.argv[1])
	littleSubnets = list(bigSubnet.subnet(int(myPrefix)))
	for i in littleSubnets:
		calc_subnet(i)
	print "\nTotal of {} subnets\n".format(len(littleSubnets))
else:
	print(promptString)
	quit()
