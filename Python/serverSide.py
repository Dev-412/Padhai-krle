import socket
s=socket.socket()
s.bind(('<IP ADDRESS>',4567))
num=2
s.listen(num)
print("listening...")

while(True):
    count=0
    c,addr=s.accept()
    print(addr," Connected successfully!!!")
    count+=1

    break

while(True):
    packet=c.recv(1024).decode()
    print(packet)

    if '?' in packet:
        ans=input(": ")
        c.send(("Server: "+ans).encode())
    if(packet=='q'):
        break

s.close()