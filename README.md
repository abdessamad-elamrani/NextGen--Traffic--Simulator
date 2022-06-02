# SCTP--Simulator
SCTP--Simulator from typical SCTP ession, generates ~40k sessions, and send it through tcpreplay

This script **gen-40k-sctp.py**   will take a sample clean pcap  **orig-clean.pcap** and  generate 40k SCTP sessions from 1.1.x.y  Client ips  to 2 SCTP server.

it uses Scapy , and few libraries to achieve it via few loops to copy packets, modify ips, recalculate checksum, 

Then you can use the resulting pcap , see  orig-clean.pcap as an example , to Tcpreplay it via linux machine with 2 interfaces ,

You can use following commands to do that : 

1) Generate new Cache file:

#**tcpprep --cidr=1.1.0.0/16 --pcap=XXXXXXX --cachefile=cacheY // XXXXXXX = pcap file , Y : new cache version**

2) Send packets :

#**tcpreplay --loop=0 --topspeed --intf1=ens9 --intf2=ens10 --cachefile=cache2 res_15_10_52.pcap**

NOTES :
**
>> If you need Different IPs or MAC, then change MAC Addresses or IPs : either directly on the script, or via  tcprewrite linux binary (and fix checksum)
>> 1 VM with 1 linux core can generate up to 40k session, and 0.5 Gbps bandwidth, if you want more, think about manually forking more threads ( nohup ... &), 
   (as tcpreplay is not multihreaded by default)**
