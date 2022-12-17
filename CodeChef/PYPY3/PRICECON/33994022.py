for _ in range(int(input())):
    n,k=map(int,input().split())
    l = [int(x) for x in input().split()]
    s=sum(l)
    c=0
    for i in range(n):
        if(l[i]>k):
            c+=k
        else:
            c+=l[i]
    print(s-c)