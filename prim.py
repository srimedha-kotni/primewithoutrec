n=int(input("enter a psitive number:"))
flag=0
for i in range(1,n+1):
    if(n%i==0):
        flag=flag+1
if(flag==2):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
