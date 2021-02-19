import socket
import datetime

receive_buffer_size = 1024

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 7))

while True:
    request = server_socket.recvfrom(receive_buffer_size)
    server_socket.sendto(request[0], request[1])
    print('Message is received: ', request[0].decode('utf-8'),  ' Date and time: ', datetime.datetime.now())
