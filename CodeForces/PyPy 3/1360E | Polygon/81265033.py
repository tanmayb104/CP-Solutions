for _ in range(int(input())):
    n=int(input())
    l=[]
    #n,k=map(int,input().split())
    for i in range(n):
        l.append([int(x) for x in input()])
    flag=0
    for i in range(n-1):
        for j in range(n-1):
            if(l[i][j]==1):
                if(l[i+1][j]!=1 and l[i][j+1]!=1):
                    flag=1
    if(flag==1):
        print("NO")
    else:
        print("YES")