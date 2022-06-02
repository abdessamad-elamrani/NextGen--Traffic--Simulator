
from scapy import *
import scapy.all as scapy
from scapy.layers.inet import TCP, UDP, IP
import psutil,os
from scapy.layers.l2 import Ether
from scapy.packet import Raw, Packet
from datetime import datetime
'''

# Kishore Firweall Server side interface MAC : 00:09:0f:09:01:04
# Kishore Firewall Client side interface MAC : 08:5b:0e:e2:d1:ee


'''
#os.remove("res.pcap")
mac_fw_client_side="00:09:0f:09:01:05"
mac_fw_server_side="08:5b:0e:e2:d1:ee"

i=0
j=2

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%H_%M_%S")

for ind in range(40000):
    packets = scapy.rdpcap("orig-clean.pcap")
    ip_client = '1.1.'+str(i)+'.'+str(j)

    print("generating session numb "+str(ind)+" for source "+ip_client)
    #ip_server1 = '172.31.201.69'
    #ip_server2 = '172.31.201.70'
    #print("CREATING  FLOW  FOR  ",ip_client," to " , ip_server)

    for x in range(47):
        xpkt=packets[x]
        if(xpkt[scapy.IP].src != '172.31.201.69' ) and (xpkt[scapy.IP].src != '172.31.201.70'):
            xpkt[scapy.IP].src = ip_client
            xpkt[Ether].dst = mac_fw_client_side
        else:
            xpkt[scapy.IP].dst = ip_client
            xpkt[Ether].dst = mac_fw_server_side

        del xpkt.chksum
        pkt1 = xpkt.__class__(bytes(xpkt))

        #filename="res_"+dt_string+".pcap"
        scapy.wrpcap("res_"+dt_string+".pcap", xpkt, append=True)

    j += 1
    if j == 255:
        j = 1
        i += 1
