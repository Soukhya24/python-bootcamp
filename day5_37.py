# print the sum of numbers in a given i/p
n="hello 123"
sum=0
num="0123456789"
for i in n:
    if(i in num):
        sum+=int(i)
print(sum)
