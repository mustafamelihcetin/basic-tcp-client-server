import socket
SIZE = 50
SERVER = 'localhost'
PORT = 4444
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
def send():
    send_data = input("[client] veri girin: ")
    send_length = len(send_data)
    client.send(send_data.encode() + (b'' * (50 - send_length)))
    get_data = client.recv(50)
    print("[Data] GET Data: {}".format(get_data))

send()