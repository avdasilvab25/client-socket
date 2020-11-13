import socket
import base64
from time import time, sleep
from hashlib import md5

### SOCKET TCP PROTOCOL ###
PORT = 19876
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

### SOCKET UDP PROTOCOL ###
UDP_PORT = 9876
UDP_SERVER = '127.0.0.1'
UDP_ADDR = (UDP_SERVER, UDP_PORT)

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client.bind(UDP_ADDR)

### CLIENT ###
def send_cmd(msg):
    encoded_msg = bytes(msg, encoding='utf-8')
    client.send(encoded_msg)
    data = client.recv(1024)
    print('Respuesta del servidor:', data.decode('utf-8'))

def authenticate(user):
    send_cmd('helloiam ' + str(user))

def req_msg():
    send_cmd("givememsg " + str(UDP_PORT))

    t_end = time() + 20
    msg_received = False
    msg_chksm = None

    while time() < t_end and not msg_received: # Wait for 20 sgs to receive the msg
        if not msg_received:
            try:
                data, address = udp_client.recvfrom(1024)
                if data:
                    msg_received = True
                    data_decoded = base64.b64decode(data)
                    user_msg = data_decoded.decode('utf-8')
                    print('Received message:', user_msg)
            except:
                print('An error occurred!')
        else:
            print('Message received!', msg_received)
        
        return user_msg

def req_msg_length():
    send_cmd('msglen')

def validate_msg(msg):
    msg_chksm = md5(msg).hexdigest()
    send_cmd('chkmsg ' + msg_chksm)

def logout():
    send_cmd('bye')

# req_msg()
# print('The execution ended')