import socket
hostname =socket.gethostname()
ips = socket.gethostbyname(hostname)
print("my ip address: " + ips )