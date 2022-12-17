n=int(input())
l1=[int(x) for x in input().split()]
l2=[int(x) for x in input().split()]
ll1=[[l1[i],i] for i in range(n)]
ll2=[[l2[i],i] for i in range(n)]
ll1=sorted(ll1,key=lambda x:x[0])
ll2=sorted(ll2,key=lambda x:x[0])
s=[]
for i in range(n):
    s.append((ll1[i][1]-ll2[i][1])%n)
#print(s)
d={}
l=[0]*(max(s)+1)
for i in s:
    if(l[i]==1):
        d[i]+=1
    else:
        d[i]=1
        l[i]=1
se=set(s)
m=0
for i in se:
    m=max(m,d[i])
print(m)
 