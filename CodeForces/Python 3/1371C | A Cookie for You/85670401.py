for _ in range(int(input())):
    a,b,n,m=map(int,input().split())
    if(a+b<n+m):
        print("No")
    elif(min(a,b)>=m and (a+b-m)>=n):
        print("Yes")
    else:
        print("No")