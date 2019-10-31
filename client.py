import socket
from time import sleep
import threading
import sys


  
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(('localhost', UDP_PORT))

def check_output():
    while True:
        data = sock.recv(1024)
        print ("Response > ", (data))

th = threading.Thread(target = check_output)
th.daemon = True
th.start()

while True:
    # txt = b""
    txt = input("> ")
    sock.send(bytes(txt, encoding='utf8'))

