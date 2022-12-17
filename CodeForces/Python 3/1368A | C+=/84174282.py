for _ in range(int(input())):
    a,b,n=map(int,input().split())
    a1=min(a,b)
    b1=max(a,b)
    c=0
    while(max(a1,b1)<=n):
        a1=a1+b1
        t=a1
        a1=b1
        b1=t
        c+=1
    print(c)
 
    