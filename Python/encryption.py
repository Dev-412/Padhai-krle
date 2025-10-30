s=input("Enter something: ")
key=int(input('Key: '))

for i in s.upper():
    ascii=ord(i)
    if ascii==32:
        print(i,end="")
    else:
        alpha=((ascii-ord("A"))+key)%26
        print(chr(alpha+ord("A")),end="")