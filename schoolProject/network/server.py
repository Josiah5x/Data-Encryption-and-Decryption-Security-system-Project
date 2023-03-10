import socket
import threading


HEADER = 64
PORT =  5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = ('utf-8')
DISCONNETION_MESSAGE = "!DISCONECT" 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION], {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).deccode(FORMAT)
            if msg == DISCONNETION_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()



def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION ], {threading.activeCount() -1}")

print('[STARTING], server is connected.')
start()
