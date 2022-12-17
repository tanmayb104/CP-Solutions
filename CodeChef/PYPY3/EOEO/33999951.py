import math
#from collections import *
for _ in range(int(input())):
    #n,k=map(int,input().split())
    #l=[int(x) for x in input().split()]
    n=int(input())
    #l = [int(x) for x in input().split()]
    if(n%2==1):
        print(n//2)
    else:
        c=0
        m=n
        while(n%2==0):
            n=n//2
            c+=1
        a=pow(2,c)
        a=a+a
        print(m//a)
