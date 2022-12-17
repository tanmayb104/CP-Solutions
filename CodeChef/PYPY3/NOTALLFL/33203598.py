t = int(input())
while t:
    t-=1
    n,k = map(int,input().split())
    c = [0]*(k+1)
    a = list(map(int,input().split()))
    i = 0
    j = 0
    ans = 0
    cur_k = 0
    while j<n:
        if c[a[j]]==0:
            cur_k+=1
        c[a[j]]+=1
        j+=1
        while cur_k==k:
            c[a[i]]-=1
            if c[a[i]]==0:
                cur_k-=1
            i+=1
        ans = max(ans,j-i)
    print(ans)
