for _ in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    d={}
    for i in range(n):
        a=arr[i]
        b=bin(a)[2:]
        c=len(b)
        if(c in d.keys()):
            d[c]+=1
        else:
            d[c]=1
    ans=0
    for i in d.keys():
        ans+=d[i]*(d[i]-1)//2
    print(ans)
 
        