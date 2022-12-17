n=int(input())
l=[int(x) for x in input().split()]
if(l[0]>1 or l[-1]>n):
    print(-1)
else:
    flag=0
    dup=0
    for i in range(n):
        if(l[i]-i>1):
            flag=1
            break
    if(flag==1):
        print(-1)
    else:
        s1=set(l)
        s2=set([int(x) for x in range(0,n+2)])
        s3=s2.difference(s1)
        l1=list(s3)
        l1.sort()
        ans=[]
        if(l[0]==0):
            ans.append(l1.pop(0))
        else:
            l1.pop(0)
            ans.append(0)
        prev=l[0]
        for i in range(1,n):
            if(l[i]==prev):
                ans.append(l1.pop(0))
            else:
                ans.append(prev)
                prev=l[i]
        print(*ans)
 
            