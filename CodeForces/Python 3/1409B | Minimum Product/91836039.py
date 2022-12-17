for _ in range(int(input())):
    a,b,x,y,n=map(int,input().split())
    if(a+b-x-y<=n):
        print(x*y)
    else:
        ans=9999999999999999999999999999999999999
        if(n>a-x):
            n1=n-a+x
            y1=b-n1
            ans=min(ans,x*y1)
        else:
            ans=min(ans,(a-n)*b)
        if(n>b-y):
            n1=n-b+y
            x1=a-n1
            ans=min(ans,y*x1)
        else:
            ans=min(ans,(b-n)*a)
        print(ans)
        