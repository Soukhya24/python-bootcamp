#print a unique characters in a string
#unique characters means not repeating characters
vowels="aeiou"
consonant="bcdfghjklmnpqrstvwxy"
ans=""
i="hello wOrld"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)
