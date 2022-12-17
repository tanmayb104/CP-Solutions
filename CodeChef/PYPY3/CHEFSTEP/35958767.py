# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=[int(x) for x in input().split()]
    for j in range(n):
        b=l[j]
        if(b%k==0):
            print("1",end="")
        else:
            print("0",end="")
    print()