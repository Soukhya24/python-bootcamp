# you are given with a , separated natural numbers 1-10 print even numbers
my_list=list(map(int,input().split(",")))
for i in range(1,len(my_list),2):
    print(my_list[i])