for _ in range(int(input())):
    n,s=map(int,input().split())
    l=[x for x in str(n)]
    su=sum([int(x) for x in str(n)])
    ans=0
    c=0
    for i in range(len(l)):
        c+=int(l[i])
        if(c>=s and su>s):
            p=10**(len(l)-i)
            ans=p-int("".join(l[i:]))
            break
    print(ans)
 
 