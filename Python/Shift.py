s=int(input("Enter something: "))
shift=int(input("Enter Shift: "))
string=str(s)
num=s
if(shift>len(string)):
    for i in string[len(string)-1::-1]:
        print(i,end="")

else:
    for i in string[shift:len(string):1]:
        print(i,end="")
    for i in string[0:shift]:
        print(i,end="")        