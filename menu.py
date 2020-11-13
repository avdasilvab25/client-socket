import client
import base64

connected = False
user = None
msg_decoded = None

def menu():
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

menu()

print()
option = int(input('Marque la opción que desee: '))

while option != 0:
    if option == 1:
        ip = str(input('Ingrese la IP del servidor: '))
        tcp_port = int(input('Ingrese el puerto TCP: '))
        udp_port = int(input('Ingrese el puerto UDP: '))
        client.connect(ip, tcp_port, udp_port)
        connected = True
    elif option == 2:
        user = str(input('Ingrese su usuario: '))
        if "invalid" in client.authenticate(user):
            user = None  
    elif option == 3:
        msg = client.req_msg()
        msg_decoded = base64.b64decode(msg)
        user_msg = msg_decoded.decode('utf-8')
        print('El mensaje recibido fue:', user_msg)
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

    print()
    menu()
    option = int(input('Marque la opción que desee: '))
    print()

print('¡Hasta luego!')