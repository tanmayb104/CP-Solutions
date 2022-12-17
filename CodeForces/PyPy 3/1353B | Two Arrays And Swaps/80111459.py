for _ in range(int(input())):
    n,k=map(int,input().split())
    l1=[int(x) for x in input().split()]
    l2=[int(x) for x in input().split()]
    l1.sort()
    l2.sort()
    l2.reverse()
    i=0
    while(i<n and k>0):
        if(l1[i]<l2[i]):
            l1[i]=l2[i]
            k-=1
        i+=1
    print(sum(l1))