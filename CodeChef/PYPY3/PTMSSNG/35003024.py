from collections import Counter
for _ in range(int(input())):
    n=int(input())
    x=[]
    y=[]
    for i in range(4*n-1):
        l=[int(xi) for xi in input().split()]
        x.append(l[0])
        y.append(l[1])
    c1=Counter(x)
    c2=Counter(y)
    s1=set(x)
    s2=set(y)
    for i in s1:
        if(c1[i]%2==1):
            print(i,end=" ")
    for i in s2:
        if(c2[i]%2==1):
            print(i)
    


