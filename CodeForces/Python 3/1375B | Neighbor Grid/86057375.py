for _ in range(int(input())):
    r,c=map(int,input().split())
    l=[[int(x) for x in input().split()] for i in range(r)]
    flag=0
    for i in range(r):
        for j in range(c):
            if(l[i][j]>4):
                flag=1
                break
            else:
                c1=0
                if(i-1>-1):
                    c1+=1
                if(j-1>-1):
                    c1+=1
                if(i+1<r):
                    c1+=1
                if(j+1<c):
                    c1+=1
                if(l[i][j]>c1):
                    flag=1
                    break
                l[i][j]=c1
    if(flag):
        print("NO")
    else:
        print("YES")
        for i in range(r):
            print(*l[i])
    