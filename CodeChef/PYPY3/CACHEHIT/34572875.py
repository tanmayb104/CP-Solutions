for _ in range(int(input())):
    n,b,m=map(int,input().split())
    l1=[int(x) for x in input().split()]
    cur=-1
    i=0
    c=0
    while(i<len(l1)):
        now=(l1[i])//b
        if(now!=cur):
            cur=now
            c+=1
        i+=1
    print(c)

    