for _ in range(int(input())):
    #l=[int(x) for x in input().split()]
    a1,b1=map(int,input().split())
    a=min(a1,b1)
    b=max(a1,b1)
    a=a*2
    print(max(a,b)*max(a,b))