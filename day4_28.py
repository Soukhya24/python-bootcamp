#find whether the given number is prime or not
a=int(input("enter a number: "))
r=a**0.5
count=0
if a==1:
    print("not aprime number")
elif a==2:
    print("prime number")    
for i in range(a,int(r+1)):
    if a%i==0:
        count=1
        break
if count==0:
    print("it is a prime number")
else:
    print("it is not a prime number")    


