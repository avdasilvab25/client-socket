import client
import base64

connected = False
user = None
msg_decoded = None

print('')

def menu():
    print('---------- GETMYMSG CLIENT ----------')
    if not connected:
        print('1. Conectarse al servidor')
    
    if connected:
        print('2. Autenticarse')

        if user:
            print('3. Solicitar mensaje')
            print('4. Solicitar longitud del mensaje')
            print('5. Validar contenido del mensaje')
        
        print('6. Desconectarse del servidor')

    print('0. Salir')
    print('-------------------------------------')

menu()

print('')
option = int(input('Marque la opción que desee: '))
print('')

while option != 0:
    print('')
    if option == 1:
        server_ip = str(input('Ingrese la IP del servidor (ej. 127.0.0.1): '))
        client_ip = str(input('Ingrese la IP del cliente (ej. 127.0.0.1): '))
        tcp_port = int(input('Ingrese el puerto TCP (ej. 19876): '))
        udp_port = int(input('Ingrese el puerto UDP (ej. 9876): '))
        client.connect(server_ip, client_ip, tcp_port, udp_port)
        connected = True
    elif option == 2:
        user = str(input('Ingrese su usuario: '))
        if "invalid" in client.authenticate(user):
            user = None  
    elif option == 3:
        msg = client.req_msg()
        msg_decoded = base64.b64decode(msg)
        user_msg = msg_decoded.decode('utf-8')
        print('El mensaje recibido es:', user_msg)
    elif option == 4:
        client.req_msg_length()
    elif option == 5:
        if msg_decoded:
            client.validate_msg(msg_decoded)
        else:
            print('Primero debe solicitar el mensaje al servidor')
    elif option == 6:
        client.logout()
        client.disconnect()
        connected = False
        user = None
        msg_decoded = None

    print('')
    menu()
    print('')
    option = int(input('Marque la opción que desee: '))

print('¡Hasta luego!')