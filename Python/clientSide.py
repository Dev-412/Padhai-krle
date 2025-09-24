import socket
s=socket.socket()
s.connect(('<SERVER\'s IP>',4567))
while(True):

    packet=input("NOTE: \'?\' is compulsory and type \'quit()\' for exit.\nEnter something: ")
    s.send(packet.encode())

    if '?' in packet:
        print("Server: ",s.recv(1024).decode())

    if 'quit()' in packet:
        break