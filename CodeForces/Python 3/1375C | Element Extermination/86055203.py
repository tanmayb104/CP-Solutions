for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    if(l[0]<l[-1]):
        print("YES")
    else:
        print("NO")
    