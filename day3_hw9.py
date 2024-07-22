n=12346
even_sum=0
odd_sum=0
for i in range(1,n):
    r=n%10
    if(n%2==0):
        even_sum=even_sum+r*r
    n=n//10
else:
    odd_sum=odd_sum+r*r
print (even_sum)
print(odd_sum)   
        


 