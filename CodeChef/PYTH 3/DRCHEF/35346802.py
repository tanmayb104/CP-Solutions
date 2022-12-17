import bisect
for _ in range(int(input())):
    n,x1=map(int,input().split())
    l=[int(x) for x in input().split()]
    l.sort()
    l2=l.copy()
    c1=0
    c2=0
    x2=x1
    if(x1>=l[-1]):
        print(len(l))
        continue
    while(len(l)):
        a=bisect.bisect(l,x1)
        #print(a,x,l)
        if(a==0):
            x1=x1*2
            c1+=1
        else:
            b=l[a-1]
            if(b>=3*x1//4 and b<=x1) or a==len(l):
                x1=b*2
                c1+=1
                l.pop(a-1)
            else:
                x1=x1*2
                c1+=1
        if(a>len(l)):
            break
    c1+=len(l)
    while(len(l2)):
        a=bisect.bisect(l2,x2)
        #print(a,x,l)
        if(a==0):
            x2=x2*2
            c2+=1
        else:
            b=l2[a-1]
            if(b>=x2//2 and b<=x2):
                x2=b*2
                c2+=1
                l2.pop(a-1)
            else:
                x2=x2*2
                c2+=1
        if(a>len(l2)):
            break
    c2+=len(l2)
        
        
        
    print(min(c1,c2))
