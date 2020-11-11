import socket
import base64

PORT = 19876
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    client.send(b'helloiam avdasilvab.17')
    data = client.recv(1024)
    print(data)

send('helloiam avdasilvab.17')