# find the element that is present in k+n  index
# k=3,n=2
# i/p :3 6 8  4 61 2
# o/p:2
#k=3,n=4
#i/p:80 70 54 36 72
#o/p:error
my_list=list(map(int,input().split( )))
n=(int(input("enter n")))
k=(int(input("enter k")))
if(len(my_list)<k+n):
    print("error")
else:
     for i in range(0,len(my_list)) :
          print(my_list[k+n],end=" ")
          break

