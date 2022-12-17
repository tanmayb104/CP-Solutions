for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    a=l.copy()
    a.sort()
    m=min(l)
    flag=0
    for i in range(n):
        if(l[i]%m!=0 and l[i]!=a[i]):
            flag=1
    if(flag):
        print("NO")
    else:
        print("YES") 