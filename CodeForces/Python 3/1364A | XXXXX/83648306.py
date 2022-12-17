for _ in range(int(input())):
    n,x=map(int,input().split())
    l=[int(x) for x in input().split()]
    flag=0
    if(sum(l)%x!=0):
        print(n)
        continue
    index1=-1
    for i in range(n):
        if(l[i]%x!=0):
            flag=1
            index1=i
            break
    if(flag==0):
        print(-1)
        continue
    l.reverse()
    index2=-1
    for i in range(n):
        if(l[i]%x!=0):
            flag=1
            index2=i
            break
    print(max(n-index1-1,n-index2-1))