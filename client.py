import socket

PORT = 19876
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_cmd(msg):
    encoded_msg = bytes(msg, encoding='utf-8')
    client.send(encoded_msg)
    data = client.recv(1024)
    print('Message received:', data.decode('utf-8'))

def request_msg():
    send_cmd('helloiam avdasilvab.17')
    send_cmd('msglen')
    # send_cmd('givememsg')
    # send_cmd('chkmsg')

# send_cmd('helloiam avdasilvab.17')
request_msg()