#leap year
#logic: year should be divisible by 400 or divisible by 4 not divisible by 100
inp=int(input())
for i in range(2000,2025):
    if(i%400==0 or (i%4==0) and i!=100):
        print(i)
