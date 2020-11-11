import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.2.126.2', 19876))
