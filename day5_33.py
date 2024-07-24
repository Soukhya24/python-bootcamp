#Ascii values
#check how many vowels are in a string
check=['a','e','i','o','u']
count=0
n="hello world"
for i in n:
    if(i in check):
        count+=1
print(count)        