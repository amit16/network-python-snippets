#!/usr/bin/python
#A Simple http client (only get), using python requests, takes input arg : interface, domain 

import os
import sys
import requests
import datetime

def main():
    if len(sys.argv)<3:
        print "fewer arguements"
        sys.exit(1)
    else:
        tap_interface = sys.argv[1]
        domain = sys.argv[2]

    try:
        res = requests.get(domain, verify=False, timeout=1)
    except Exception as ex:
        print "ERROR: Not valid domain"
        sys.exit(-1)

    if res.status_code == 200:
        print "OK"

    sys.exit(0)

if __name__ == '__main__':
    main()

