for _ in range(int(input())):
    x,y,n=map(int,input().split())
    a=n//x
    b=x*a
    b+=y
    while(b>n):
        b-=x
    print(b)