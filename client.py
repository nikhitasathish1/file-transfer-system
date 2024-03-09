import socket 
import ssl

# Creating Client Socket 
host = '10.1.16.176'
port = 8080	
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.load_verify_locations("server.crt") #loads server certificate
sock = ssl_context.wrap_socket(sock, server_hostname="snauman")# wraps socket in ssl

sock.connect((host, port)) 

while True: 

    filename = input('Input filename you want to send: ') 
    try: 
    # Reading file and sending data to server 
        fi = open(filename, "r") 
        data = fi.read() 
        if not data: 
            break
        while data: 
            sock.send(str(data).encode()) 
            data = fi.read() 
        # File is closed after data is sent 
        fi.close() 

    except:
        print('You entered an invalid filename!Please enter a valid name') 

