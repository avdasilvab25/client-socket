import client

user = None
msg = None

def menu():
    print('1. Autenticarse con el servidor')
    
    if user:
        print('2. Solicitar mensaje')
        print('3. Solicitar longitud del mensaje')
        print('4. Validar contenido del mensaje')
        print('5. Desconectarse del servidor')

    print('0. Salir')

menu()

print()
option = int(input('Marque la opción que desee: '))

while option != 0:
    if option == 1:
        user = str(input('Ingrese su usuario: '))

        if "invalid" in client.authenticate(user):
            user = None
    elif option == 2:
        msg = client.req_msg()
        print('El mensaje recibido fue:', msg)
    elif option == 3:
        client.req_msg_length()
    elif option == 4:
        if msg:
            client.validate_msg(msg)
        else:
            print('Primero debe solicitar el mensaje al servidor')
    elif option == 5:
        client.logout()
        user = None

    print()
    menu()
    option = int(input('Marque la opción que desee: '))
    print()

print('¡Hasta luego!')