for _ in range(int(input())):
    l=[x for x in input()]
    ans=""
    ans+=l[0]
    i=1
    while(i<len(l)):
        ans+=l[i]
        i+=2
    print(ans)