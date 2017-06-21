#!/usr/bin/env python
import time
import sys
import re
import os

lxc_name = sys.argv[1]
"""
cr_rc = os.system("sudo lxc-create -t ubuntu -n u1").execute()
print cr_rc

vi_rc = os.system("sudo virt-install --connect lxc:/// --name u1 --ram 512 --vcpu 1 --filesystem /var/lib/lxc/u1/rootfs/,/ --noautoconsole --network=network,source=PAC_T1S2_MGMT --network=network,source=PAC_T1S2_SL1,portgroup=port-group1").execute()
print vi_rc
"""

virsh_rc = os.system("sudo virsh -c lxc:// destroy {0}".format(lxc_name)).execute()
data = virsh_rc

match_o = re.search(r"error: Failed to kill process (\d+):", data)
if match_o:
    lxc_dhcp_pid =  match_o.group(1)
    print lxc_dhcp_pid

    kill_rc = os.system("sudo kill -9 {0}".format(lxc_dhcp_pid)).execute()
    print kill_rc
else:
    print "no match"

des_rc = os.system("sudo virsh -c lxc:// destroy {0}".format(lxc_name)).execute()
print des_rc

undef_rc = os.system("sudo virsh -c lxc:// undefine {0}".format(lxc_name)).execute()
print undef_rc

ldes_rc = os.system("sudo lxc-destroy -n {0}".format(lxc_name)).execute()
print ldes_rc
