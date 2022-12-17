for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    #n, k = map(int, input().split())
    #n, m = map(int, input().split())
    a.sort()
    c=1
    l=0
    r=0
    while(r<n):
        if(c>=a[l]):
            c+=1
            l+=1
            r+=1
        else:
            if(a[r]<=c+r-l):
                c+=(r-l+1)
                l=r+1
                r=l
            else:
                r+=1
    print(c)