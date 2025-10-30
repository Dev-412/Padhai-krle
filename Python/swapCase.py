s=input("Enter somethig: ")

for i in s:
    if ord(i)>=65 and ord(i)<=90:
        print(chr(ord(i)+32),end="")
    elif ord(i)>=97 and ord(i)<=122:
        print(chr(ord(i)-32),end="")
    else:
        print(i,end="")