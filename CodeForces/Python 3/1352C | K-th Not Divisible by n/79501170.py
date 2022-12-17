for _ in range(int(input())):
    n,k=map(int,input().split())
    a=k//(n-1)
    b=n*a
    b+=(k%(n-1))
    if(b%n==0):
        b-=1
    print(b)