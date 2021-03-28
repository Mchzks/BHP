import socket

target_host = "127.0.0.1"
target_port = 9997

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(b"AABBBCCC",(target_host, target_port))

# recieve some data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()