# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    if(k<=n):
        a=(k-1)//9+1
        print(1,a)
    else:
        a1=(n-1)//9+1
        a2=(k-1)//9+1
        if(a1==a2):
            print(1,a1)
        else:
            print(0,a1)