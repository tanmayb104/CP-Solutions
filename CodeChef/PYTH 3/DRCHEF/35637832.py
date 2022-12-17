# cook your dish here
import bisect
for _ in range(int(input())):
    n,x=map(int,input().split())
    l=[int(x) for x in input().split()]
    l.sort()
    c=0
    if(x>=l[-1]):
        print(len(l))
    else:
        while(len(l)):
            a=bisect.bisect(l,x)
            #print(a,x,l)
            if(a==0):
                x=x*2
                c+=1
            else:
                b=l[a-1]
                if(b>x//2 and b<=x):
                    x=b*2
                    c+=1
                    l.pop(a-1)
                else:
                    x=x*2
                    c+=1
            if(a>len(l)):
                break
        c+=len(l)
        print(c)
