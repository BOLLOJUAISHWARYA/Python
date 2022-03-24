#Socket program - You can send messages between two systems , has to be runned on two different systems

#server side program
import socket

server=socket.socket() #default ipv4 and tcp
HOST = ''
PORT = 65341
server.bind((HOST,PORT))
server.listen()
client, address = server.accept()
print('This is client address : {}'.format(address))
while True:
    print(client.recv(1024).decode())
    reply=input("office laptop : ")
    client.sendall(bytes(reply,'utf-8'))


#client side program
import socket

client=socket.socket()
client.connect(('ip',65341))#ip of the system in which server program is running
while True:
    msg=input("personal laptop:")
    client.send(bytes(msg,'utf-8'))
    print(client.recv(1024).decode())


