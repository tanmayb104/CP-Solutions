for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    su=0
    d={0:0}
    flag=0
    for i in range(1,n+1):
        su+=l[i-1]
        su=su%n
        if(su not in d):
            d[su]=i
        else:
            print(i-d[su])
            flag=1
            for j in range(d[su]+1,i+1):
                print(j,end=" ")
            print()
            break
    if(flag==0):
        print(-1)