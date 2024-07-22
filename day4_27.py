#find LCM
a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=a*b
while b!=0:
    a,b= b,a%b
print("gcd of 2 number is: ",a)
lcm=c//a
print(lcm)    
     