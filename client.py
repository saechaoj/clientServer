import socket

host = 'localhost'
port = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))


#Get message from server
msg = sock.recv(1024).decode()

#Continuous chat
while msg:
    print("Message : ", msg)
    msg = sock.recv(1024).decode()

    #Check for quit message
    if msg == '/q':
        sock.close()