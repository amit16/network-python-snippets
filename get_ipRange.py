
#Generates all possible ip ranges in a given network
#Input start and end ip of the network

def ipRange(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []

    ip_range.append(start_ip)
    while temp != end:
       start[3] += 1
       for i in (3, 2, 1):
          if temp[i] == 256:
             temp[i] = 0
             temp[i-1] += 1
       ip_range.append(".".join(map(str, temp)))

    return ip_range

ip_range = ipRange("20.20.20.3", "20.20.20.254")
for count in range(0, len(ip_range)-1, 2):
    s = str(ip_range[count] + '-' + ip_range[count+1])
    print s,',',

