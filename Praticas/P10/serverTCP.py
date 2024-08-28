import socket
import threading
import signal
import sys

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

def handle_client_connection(client_socket,address):  # Para cada comunicacao client <--> server
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    try:
        while True:
            request = client_socket.recv(1024)
            if not request:
                client_socket.close()
            else:
                msg=request.decode()
                print('Received {}'.format(msg))
                msg=("ECHO: "+msg).encode()
                client_socket.send(msg)
    except (socket.timeout, socket.error):
        print('Client {} error. Done!'.format(address))

ip_addr = "0.0.0.0" # norma para associar a todos os enderecos ip's daquela maquina... (aberto)
tcp_port = 5005 

# AF_INET6 seria ipv6
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_addr, tcp_port)) # à escuta!
server.listen(5)  # max backlog of connections

print('Listening on {}:{}'.format(ip_addr, tcp_port))

while True:
    # Novo socket para cada cliente
    client_sock, address = server.accept() # Fica bloqueado ate alguem aparecer...
    client_handler = threading.Thread(target=handle_client_connection,args=(client_sock,address),daemon=True)
    client_handler.start()


