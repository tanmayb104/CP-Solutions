for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[x for x in input()]
    ans=[]
    c=0
    for i in range(len(l)):
        if(l[i]=="1"):
            ans.append(i)
    if(len(ans)!=0):
        if(ans[0]-k>0):
            ans.insert(0,0)
            c+=1
    else:
        ans.append(0)
        c+=1
    while(True):
        if(ans[-1]+k<(len(l)-1)):
            ans.append(len(l)-1)
            c+=1
        else:
            break
    for i in range(1,len(ans)):
        a=(ans[i]-ans[i-1]-k-1)//(k+1)
        if(a>0):
            c+=a
    print(c)
    