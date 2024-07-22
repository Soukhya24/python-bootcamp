my_list=list(map(str,input().split(",")))
print("enter the choice:\n1.append \n2.pop \n3.sort\n4.length")
choice=int(input())
if(choice==1):
    my_list.append(9)
    print(*my_list)
elif(choice==2):
    my_list.pop(2)
    print(my_list)
elif(choice==3):
    my_list.sort()
    print(my_list)   
else:
    print(len(my_list))  
       