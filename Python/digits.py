s=input("Enter something: ")
count,sum=0,0

for i in s:
    if i.isdigit():
        sum=sum+int(i)
        count+=1

print(f"sum: {sum}")
print(f"Average: {sum/count}")