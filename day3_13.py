# replace the elements in an arrays with avg of maximum and minimum elements 

my_list=list(map(int,input().split()))
mini=my_list[0]
maxi=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
    else:
         my_list[i]<mini
         mini=my_list[i]
avg=(maxi+mini)//2
for i in range(len(my_list)):
    my_list[i]=avg
print(my_list)             



