for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    #a1,b1=map(int,input().split())
    l.sort()
    m=99999999999
    for i in range(1,n):
        m=min(m,l[i]-l[i-1])
    print(m)