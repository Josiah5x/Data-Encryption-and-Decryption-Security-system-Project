import socket
import threading

HEADER = 64
PORT = 5050
SERVER = "192.168.1.255"
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)