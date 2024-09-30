import threading
import socket

SIZE = 50
SERVER = 'localhost'
PORT = 4444
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
def handle_client(conn,addr):
    connected = True
    print("[CONNECT] get connection {}".format(addr))
    while connected:
        get_msg = conn.recv(SIZE).decode()
        print("[{addr}] msg : ",get_msg)
        server.send(b'True'+(b''*46))
        if get_msg == "disconnect":
            connected= False
    conn.close()

def main():
    print(f"[LISTENING] server on {ADDR} listening...")
    while True:
        server.listen()
        conn, addr = server.accept()
        t = threading.Thread(target=handle_client,args=(conn,addr))

main()