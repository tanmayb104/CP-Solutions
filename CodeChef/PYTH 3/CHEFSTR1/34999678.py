for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    c=0
    for i in range(1,n):
        c+=abs(l[i]-l[i-1])-1
    print(c)