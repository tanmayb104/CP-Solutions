# cook your dish here
from collections import Counter

n,m=map(int,input().split())
l1=[]
l2=[]
dict1={}
for i in range(n):
    a=[x for x in input().split()]
    l1.append(a)
for i in range(m):
    l2.append(input())
c=Counter(l2)
for i in range(n):
    if(l1[i][1] in dict1):
        dict1[l1[i][1]]=dict1[l1[i][1]]+c[l1[i][0]]
    else:
        dict1[l1[i][1]]=c[l1[i][0]]
temp1=dict1.items()
temp1=sorted(temp1,key=lambda x:x[1],reverse=True)
m=temp1[0][1]
ans1=[temp1[0][0]]
for i in range(1,len(temp1)):
    if(temp1[i][1]<m):
        break
    else:
        ans1.append(temp1[i][0])
ans1=sorted(ans1)
print(ans1[0])
dict1=dict(c)
temp1=dict1.items()
temp1=sorted(temp1,key=lambda x:x[1],reverse=True)
m=temp1[0][1]
ans1=[temp1[0][0]]
for i in range(1,len(temp1)):
    if(temp1[i][1]<m):
        break
    else:
        ans1.append(temp1[i][0])
ans1=sorted(ans1)
print(ans1[0])
