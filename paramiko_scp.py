import paramiko
from scp import SCPClient


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()


print "Starting SCP get ..."
ssh.connect("192.168.2.5",
            username="amit",
            password="test@123")

scp = SCPClient(ssh.get_transport())
scp.get('google.pcap', '/home/autotester')
#scp.put('google.pcap', '/home/autotester')
scp.close()


~
~
