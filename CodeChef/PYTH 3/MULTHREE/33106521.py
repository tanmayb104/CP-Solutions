for _ in range(int(input())):
    k,d0,d1 = map(int,input().split())
    if k==2:
        if (d0+d1)%3==0:
            print("YES") 
        else:
            print("NO")
    elif k==3:
        if ((d0+d1) + (d0+d1)%10)%3==0:
            print("YES") 
        else:
            print("NO")
    else:
        d2=(d0+d1)%10
        n=k-3
        l=[(d2*2)%10]
        for i in range(1,4):
            l.append((l[i-1]*2)%10)
        n4=0
        if sum(l)==20:
            n4 = ((n//4)*2)%3
        sm = (d0+d1+d2 + sum(l[:n%4]))%3
        if (sm+n4)%3==0:
            print("YES") 
        else:
            print("NO")