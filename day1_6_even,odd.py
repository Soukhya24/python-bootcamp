n=int(input("enter a number \n"))
if(n>0 and n%2==0):
    print("the n is positive and even")
elif(n<0 and n%2==0):
    print("the n is negative and even")
elif(n>0 and n%2==1):
    print("the n is positive and odd")
else:
    print("the n is negative and odd")
