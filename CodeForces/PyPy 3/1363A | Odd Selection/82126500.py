import math
for _ in range(int(input())):
    n,x=map(int,input().split())
    l=[int(x) for x in input().split()]
    #n=int(input())
    odd=0
    even=0
    for i in range(n):
        if(l[i]%2==0):
            even+=1
        else:
            odd+=1
    if(odd==0):
        print("No")
    elif(x==n and odd%2==0):
        print("No")
    elif(x%2==0 and even==0):
        print("No")
    else:
        print("Yes")