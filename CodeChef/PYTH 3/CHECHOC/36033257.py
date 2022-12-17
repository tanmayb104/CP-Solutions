# cook your dish here
for _ in range(int(input())):
    m,n,x,y=map(int,input().split())
    if(n==1 and m==1):
        print(x)
    elif(n%2==0 or m%2==0):
        a=min(y,x*2)
        print(n*m*a//2)
    else:
        if(x<=y//2):
            print(n*m*x)
        elif(x<y):
            a=x
            b=y-x
            c=(n//2+1)*a+(n//2)*b
            d=(n//2)*a+(n//2+1)*b
            ans=max(c,d)*(m//2+1)+min(c,d)*(m//2)
            print(ans)
        else:
            a=y
            b=0
            c=(n//2+1)*a+(n//2)*b
            d=(n//2)*a+(n//2+1)*b
            ans=max(c,d)*(m//2+1)+min(c,d)*(m//2)
            print(ans)

