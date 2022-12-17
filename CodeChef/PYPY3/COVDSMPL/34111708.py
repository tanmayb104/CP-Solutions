for _ in range(int(input())):
    n,p=map(int,input().split())
    #l=[int(x) for x in input().split()]
    #n=int(input())
    #l = [int(x) for x in input().split()]
    l=[]
    for i in range(n):
        l1=[]
        for j in range(n):
            l1.append(0)
        l.append(l1)
    i=1
    print(1,1,1,n,n)
    if(int(input())==0):
        for i in range(n):
            print(*l[i])
    else:
        while(i<=n):
            j=1
            while(j<=n):
                print(1,i,j,i,j)
                if(int(input())==1):
                    l[i-1][j-1]=1
                else:
                    l[i-1][j-1]=0
                j+=1
            i+=1
        print(2)
        for i in range(n):
            print(*l[i])
    if(int(input())==-1):
        break
