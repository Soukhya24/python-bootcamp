#peak element ****************************
print("enter elements")
peak=list(map(int,input().split( )))
for i in range(1,len(peak)-1):
    if(peak[i]>peak[i-1] and peak[i]>peak[i+1]):
        print(peak[i],end=" ")         


#
my_list=list(map(int,input().split( )))
count=0 
for i in ramge(1,len(my_list)-1):
    if (my_list[-i]>my_list[-2] and my_list[-1]>count):
        count=len(my_list)-1
print(my_list[count])        