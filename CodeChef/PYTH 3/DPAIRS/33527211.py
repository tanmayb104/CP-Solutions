# cook your dish here
n,m=map(int,input().split())
s1=[int(x) for x in input().split()]
s2=[int(x) for x in input().split()]
l1=[[s1[i],i] for i in range(n)]
l2=[[s2[i],i] for i in range(m)]
l1.sort()
l2.sort()
for i in range(m):
    print(l1[-1][1],l2[i][1])
for i in range(n-1):
    print(l1[i][1],l2[0][1])