# print the element in a particular index in a cyclic printing
# k=20
#ip: 70 54 36 72 99 888 76
#idx:1  2  3  4  5  6   7
#l=20,length=7
#index:6
#o/p: 888
my_list=list(map(int,input().split( )))
k=(int(input("enter k")))
idx=k%len(my_list)
print(my_list[idx])
       