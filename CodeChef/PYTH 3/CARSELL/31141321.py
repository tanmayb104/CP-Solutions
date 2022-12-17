# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    l.sort()
    l=l[::-1]
    c=0
    for i in range(n):
        if((l[i]-i)>0):
            c+=(l[i]-i)
            c=c%1000000007
    print(c)