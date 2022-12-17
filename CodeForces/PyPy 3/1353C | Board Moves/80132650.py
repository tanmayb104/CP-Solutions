for _ in range(int(input())):
    n=int(input())
    if(n==1):
        print(0)
    else:
        s=0
        for i in range(3,n+1,2):
            s+=(i-1)*4*(i//2)
        print(s)