#Tutorial https://medium.com/@jkishan421/chat-room-application-in-python-part-i-9193d768dc64


import socket



host = 'localhost'
port = 3000

# creating a socket with ipv4 protocol and binding socket for Sending
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port)) 


# server listens to accept the connecion. Socket listens for 1 client
sock.listen(1)
print("Server Running...")



#creates new socket instance for this connection and display attributes of new client
connection, address = sock.accept()


# print("Client Connected ", connection)
print("Client Connected", address)

#Send message or recieve
while 1:
    
    print("Waiting for message...")
    msg = connection.recv(1024).decode()
    print("Recieved:",msg)

    #Reply in byte array or quits
    message = input("Send Message:")
    if message == "/q":
        sock.close()
        break
    else:
        connection.send(message.encode())


print("Program End")