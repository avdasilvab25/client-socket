import socket
import base64
from time import time, sleep
from hashlib import md5

tcp_client = None
udp_client = None
port_udp = None

### CLIENT ###
def connect(ip, tcp_port, udp_port):
    TCP_ADDR = (ip, tcp_port)
    global tcp_client
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect(TCP_ADDR)

    UDP_ADDR = (ip, udp_port)
    global udp_client
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_client.bind(UDP_ADDR)

    global port_udp
    port_udp = udp_port

def disconnect():
    tcp_client.close()
    udp_client.close()

def send_cmd(msg):
    print('Comando a ejecutar:', msg)
    encoded_msg = bytes(msg, encoding='utf-8')
    tcp_client.send(encoded_msg)
    data = tcp_client.recv(1024)
    print('Respuesta del servidor:', data.decode('utf-8'))
    return data.decode('utf-8')

def authenticate(user):
    return send_cmd('helloiam ' + str(user))

def req_msg():
    global port_udp
    send_cmd("givememsg " + str(port_udp))

    t_end = time() + 20
    msg_received = False
    msg_chksm = None

    while time() < t_end and not msg_received: # Wait for 20 sgs to receive the msg
        if not msg_received:
            try:
                data, address = udp_client.recvfrom(1024)
                if data:
                    msg_received = True
            except:
                print('An error occurred!')
        
        return data

def req_msg_length():
    send_cmd('msglen')

def validate_msg(msg):
    msg_chksm = md5(msg).hexdigest()
    send_cmd('chkmsg ' + msg_chksm)

def logout():
    send_cmd('bye')
