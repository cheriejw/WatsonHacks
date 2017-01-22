import socket
from cmdparse import command

sock = socket.socket()  
host = 'localhost'   
port = 8080          
sock.bind((host, port)) 

sock.listen(5) 
while True:
    connection, addr = sock.accept()
    print 'Got connection from', addr
    while True:
        data = connection.recv(1024)
        print data
	command(data)
    connection.close()
