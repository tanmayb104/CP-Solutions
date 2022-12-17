import math
for _ in range(int(input())):
    n=int(input())
    k=1
    l=[]
    for i in range(n):
        l1=[]
        for j in range(n):
            l1.append(k)
            k+=1
        l.append(l1)
    if(n%2==1):
        for i in range(n):
            print(*l[i])
    else:
        for i in range(0,n,2):
            print(*l[i])
            a=l[i+1]
            a.reverse()
            print(*a)
