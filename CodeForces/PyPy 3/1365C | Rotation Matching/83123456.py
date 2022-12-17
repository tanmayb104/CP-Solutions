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
s.sort()
#print(s)
c=1
m=0
a=s[0]
for i in range(1,len(s)):
    if(a==s[i]):
        c+=1
    else:
        m = max(m, c)
        c=1
        a=s[i]
m=max(m,c)
print(m)