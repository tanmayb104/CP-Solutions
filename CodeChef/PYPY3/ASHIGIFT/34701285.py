for _ in range(int(input())):
    n=int(input())
    l1=[int(x) for x in input().split()]
    n1=l1.pop(0)
    l2=[int(x) for x in input().split()]
    n2=l2.pop(0)
    s=1
    for i in range(n1):
        s+=l1[2*i+1]
    l=1
    r=s
    while(l<=r):
        flag=0
        mid=(l+r)//2
        cur=mid
        p1=0
        p2=0
        while(p1<len(l1) and p2<len(l2)):
            if(l1[p1]<l2[p2]):
                cur-=l1[p1+1]
                p1+=2
                if(cur<0):
                    flag=1
                    break
            else:
                if(l2[p2+1]<=cur):
                    cur+=l2[p2+2]
                p2+=3
        while(p1<len(l1)):
            cur-=l1[p1+1]
            p1+=2
            if(cur<0):
                flag=1
                break
        while(p2<len(l2)):
            if(l2[p2+1]<=cur):
                cur+=l2[p2+2]
            p2+=3
        if(cur>0 and not flag):
            r=mid-1
        else:
            l=mid+1
    print(l)