#skip 4 alphabets after a selected alphabet and print the next alphabet in capital letter
#sample i/p:ABC selected "A"
#sample o/p:E
t=input()
n=int(input())
for i in t:
    print(chr(ord(i)+n))
