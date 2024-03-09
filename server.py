import socket
import ssl

if __name__ == '__main__':
    # Defining Socket 
    host = '10.1.16.176'  
    port = 8080
    totalclient = int(input('Enter number of clients: ')) 

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.bind((host, port)) 
    sock.listen(totalclient)  
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile="server.crt", keyfile="server.key") #certificate

    sock = ssl_context.wrap_socket(sock, server_side=True)

    # Establishing Connections 
    connections = [] 
    print('Initiating clients') 
    for i in range(totalclient): 
        conn = sock.accept() 
        connections.append(conn) 
        print('Connected with client', i+1) 

    fileno = 0
    idx = 0
    for conn in connections: 
        # Receiving File Data 
        idx += 1
        data = conn[0].recv(1024).decode() 

        if not data: 
            continue
        # Creating a new file at server end and writing the data 
        filename = 'output'+str(fileno)+'.txt'
        fileno = fileno+1
        fo = open(filename, "w") 
        while data: 
            if not data: 
                break
            else: 
                fo.write(data) 
                data = conn[0].recv(1024).decode() 

        print() 
        print('Receiving file from client', idx) 
        print() 
        print('Received successfully! New filename is:', filename) 
        fo.close() 
    # Closing all Connections 
    for conn in connections: 
        conn[0].close() 
