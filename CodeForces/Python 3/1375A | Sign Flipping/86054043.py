for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    for i in range(0,n-1,2):
        print(abs(l[i]), end=" ")
        print(-abs(l[i+1]), end=" ")
    print(abs(l[n-1]))