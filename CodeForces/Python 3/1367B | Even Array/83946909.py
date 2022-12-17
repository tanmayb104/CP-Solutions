for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    e=0
    o=0
    for i in range(n):
        if(i%2!=l[i]%2):
            if(l[i]%2==1):
                o+=1
            else:
                e+=1
    if(o==e and o!=0):
        print(o)
    elif(o==e and o==0):
        print(0)
    else:
        print(-1)