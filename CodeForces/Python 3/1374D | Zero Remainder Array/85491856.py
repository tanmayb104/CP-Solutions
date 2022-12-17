from collections import Counter
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[int(x)%k for x in input().split()]
    c=Counter(l)
    s=set(l)
    co=0
    m=0
    for i in s:
        if(i!=0):
            co=(c[i]-1)*k+k-i
            m=max(co,m)
    if(m!=0):
        print (m+1)
    else:
        print (0)