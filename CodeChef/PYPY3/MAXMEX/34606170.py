for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[int(x) for x in input().split()]
    l.sort()
    c=0
    j=0
    cur=1
    flag=0
    for i in range(len(l)):
        if(l[i]>=m):
            j=i
            break
        elif(l[i]==cur):
            cur+=1
            c+=1
        elif(l[i]<cur):
            c+=1
        else:
            flag=1
    if(flag==1):
        print(-1)
    elif(j==0 and l[-1]==m-1):
        print(len(l))
    elif(j==0):
        print(-1)
    else:
        while(l[j]==m and j<len(l)):
            j+=1
        c+=(len(l)-j)
        print(c)
    

        


    