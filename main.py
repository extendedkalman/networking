import socket
import time

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "192.168.178.139"
print(SERVER)
ADDR = (SERVER, PORT)
#soc = socket.socket()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)

number = 0
while True:
    send(str(number))
    time.sleep(1)
    number += 1
#msg = s.recv(1024)
#print(msg.decode("utf-8"))