import socket
import time

UDP_IP = input("Enter the IP address: ")
UDP_PORT = int(input('Enter the port number: '))
request_string = "echo request"
receive_buffer_size = 1024

# Create socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RTT = [0, 0, 0, 0, 0]

for i in range(0, 5):
    t1 = time.time() * 1000000
    # Send request
    my_socket.sendto(request_string.encode('utf-8'), (UDP_IP, UDP_PORT))

    # Receive response
    request = my_socket.recvfrom(receive_buffer_size)

    t2 = time.time() * 1000000

    RTT[i] = t2 - t1
    print("RTT is ", RTT[i])

average_RTT = 0
for i in range(0, 5):
    average_RTT += RTT[i]

average_RTT = average_RTT / 5
print("average is ", average_RTT)

# Close socket
my_socket.close
