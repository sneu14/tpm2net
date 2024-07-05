import socket
from time import sleep

WLED_port = 65506
WLED_host = "10.16.1.90"
LEDS = 30

startbyte = 0x9c
packettype = 0xda
packetend = 0x36

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def tpmpacket(data):
        p = [ startbyte, packettype ]
        # Length High Byte
        p.append( len(data) & 0xff00 )
        # Length Low Byte
        p.append( len(data) & 0x00ff )
        # Frame 1
        p.append(1)
        # of 1
        p.append(1)
        for x in range(0,len(data)):
            p.append(data[x])
        # Endbyte
        p.append(packetend)
        # send Packet
        sock.sendto( bytes(p),(WLED_host, WLED_port))

for i in range(0,LEDS-1):
    leddata = []
    for j in range(0,LEDS-1):
        if i == j:
            leddata.append(255)
        else:
            leddata.append(0)
    tpmpacket(leddata)
    sleep(0.1)
             



