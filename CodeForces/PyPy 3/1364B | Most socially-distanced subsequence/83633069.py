for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    s=[l[0]]
    for i in range(1,n-1):
        if( (l[i]>l[i-1] and l[i]<l[i+1]) or (l[i]<l[i-1] and l[i]>l[i+1]) ):
            continue
        else:
            s.append(l[i])
    s.append(l[-1])
    print(len(s))
    print(*s)