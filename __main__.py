import sys, getopt

username = ''
port = ''
ipserv = ''

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "u:p:ipserv:", ["username=", "port=", "ipservice="])
    except getopt.GetoptError:
        print("client.py -u <username> -p <port> -ipserv <ipservice>")
    
    for opt, arg in opts:
        if opt in ('-u', '--username'):
            username = arg
            print('Username:', username)
        elif opt in ('-p', '--port'):
            port = arg
            print('Port:', port)
        elif opt in ('-ipserv', '--ipservice'):
            ipserv = arg
            print('IP Service:', ipserv)

if __name__ == "__main__":
    main(sys.argv[1:])
