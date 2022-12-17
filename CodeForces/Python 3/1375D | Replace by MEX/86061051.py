def mex(l):
    global s
    s1=set(l)
    s2=s-s1
    l2=list(s2)
    l2.sort()
    return l2[0]
 
 
for _ in range(int(input())):
    ans=[]
    n=int(input())
    l=[int(x) for x in input().split()]
    c=l.copy()
    c.sort()
    s=set([int(i) for i in range(n+1)])
    for i in range(2*n):
        a=mex(l)
        if(a>=n):
            for i in range(n):
                if(l[i]!=i):
                    ans.append(i+1)
                    l[i]=a
                    break
        else:
            l[a]=a
            ans.append(a+1)
    #print(l)
    print(len(ans))
    print(*ans)
 