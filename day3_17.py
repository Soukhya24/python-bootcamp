#find the sum of squares of a digit in a given number
n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r*r # important line 
    n=n//10
print(sum)