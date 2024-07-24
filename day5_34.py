#WAP to print all the consonents and vowels
check=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
count=0
c=0
n="hello wOrld"
n=n.lower()
for i in n:
    if(i in check):
        count+=1
print(count)
for i in n:
    if(i in abc):
        c+=1
print(c)             