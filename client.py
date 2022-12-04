#Tutorial https://medium.com/@jkishan421/chat-room-application-in-python-part-i-9193d768dc64


import socket

host = 'localhost'
port = 3000

#Create Socket and connect connect to local host 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))


#Continuous chat
while 1:

    #Send Message in byte array or quit
    sendMsg = input("Send Message:")
    if sendMsg == "/q":
        sock.close()
        break
    else:
        sock.send(sendMsg.encode())


    #Recieves message from Server
    print("Waiting for message...")
    msg = sock.recv(1024).decode()
    print("Recieved: ", msg)


    
print("Program End")