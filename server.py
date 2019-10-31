import socket
  
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('', UDP_PORT))
# address = ('localhost', UDP_PORT)

while True:
    data, address = sock.recvfrom(1024)
    if data.lower() == b"hi":
    	sock.sendto(b"Hello", address)
    	#print(data)

  
sock.close()