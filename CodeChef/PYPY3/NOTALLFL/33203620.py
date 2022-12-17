# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[int(x) for x in input().split()]
    i=0
    j=0
    new_k=0
    c=[0]*(k+1)
    m=0
    while(j<n):
        if(c[l[j]]==0):
            new_k+=1
        c[l[j]]+=1
        j+=1
        while(k==new_k):
            c[l[i]]-=1
            if(c[l[i]]==0):
                new_k-=1
            i+=1
        m=max(m,j-i)
    print(m)
