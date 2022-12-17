from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    c=Counter(l)
    ans=[]
    for i in c.keys():
        ans+=[i]*(c[i]//2)
    print(*ans)