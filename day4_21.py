#password verifier mr x is trying to create a new password for is instagram account these are the required conditions for creating a new password
#cond 1:minimum length is 8 maximum length is 15
#cond 2:must include @,/ is allowed in a password
#cond 3:no spaces are allowed
#cond 4:only alpha numerics are allowed
#you are supposed to print weak if length is exact 8
# if length is b/w 8-12 medium
#if length is b/w 12-15 strong
pswd=str(input("enter a password"))
n=len(pswd)
count=0
str[0]='@'
str[1]='/ '
if(n<8):
    print("please follow the conditions")
for i in pswd:
    if(i in str[0] or str[1] and i end=""):
        count+=1
        break;

