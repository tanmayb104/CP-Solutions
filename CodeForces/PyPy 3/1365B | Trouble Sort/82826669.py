import math
for _ in range(int(input())):
    #n,m=map(int,input().split())
    #l=[int(x) for x in input().split()]
    n=int(input())
    l1 = [int(x) for x in input().split()]
    l=l1.copy()
    l.sort()
    l2 = [int(x) for x in input().split()]
    s=set(l2)
    if(len(set(s))==1 and l1!=l):
        print("No")
    else:
        print("Yes")