
cap,smll,spec,num,count=0,0,0,0,0
check=True

while(True):
    passwd=input("Enter Something: ")
    count+=1
    if len(passwd)>=8:
        for i in passwd:
            if i.isupper():
                cap+=1
            elif i.islower():
                smll+=1
            elif i.isnumeric():
                num+=1
            else:
                spec+=1
            if i.isspace():
                print("Password does not contains any space...")
                check=False
                break
            
        if check:
            if cap==0 or smll==0 or spec==0 or num==0:
                print('Invalid password...')
            else:
                print("Done!")
                break
        else:
            print("Invalid Password...")
    else:
        print("Invalid Password...")
        
    if count==3:
        print("you're blocked!!")
        break