import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return i
    return n
 
for _ in range(int(input())):
    a=int(input())
    b=prime(a)
    if(b==a):
        print(1,a-1)
    else:
        print(a//b,a-a//b)
 
    