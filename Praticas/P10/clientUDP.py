import socket
import signal
import sys

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

n = 329 
e = 5 

ip_addr = "127.0.0.1"
udp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message=input("Message to send? ")
    encypted = str([pow(ord(char), e, n) for char in message]).encode()
    if len(message)>0:
        sock.sendto(encypted, (ip_addr, udp_port))
