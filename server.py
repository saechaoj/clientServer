import socket



host = 'localhost'
port = 3000

# creating a socket with ipv4 protocol and binding socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port)) 




# server listens to accept the connecion. Socket listens for 1 client
sock.listen(1)
print("Server Listening on Port: ", port)

connection, address = sock.accept()
print("Client Connected ", connection)
print("Client Address", address)


# create message on server-side
message = "This is the server, Hellooooooo"


# send message to the client in form of bytes array.
connection.send(message.encode())
connection.close()