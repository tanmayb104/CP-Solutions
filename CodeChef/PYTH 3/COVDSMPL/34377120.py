# cook your dish here
for _ in range(int(input())):
    n,p=map(int,input().split())
    #l=[int(x) for x in input().split()]
    #n=int(input())
    #l = [int(x) for x in input().split()]
    i=1
    l=[]
    while(i<=n):
        l1=[]
        j=1
        while(j<=n):
            print(1,i,j,i,j)
            if(int(input())==1):
                l1.append(1)
            else:
                l1.append(0)
            j+=1
        l.append(l1)
        i+=1
    print(2)
    for i in range(n):
        print(*l[i])
    if(int(input())==-1):
        break
