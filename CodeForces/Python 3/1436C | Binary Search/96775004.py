# cook your dish here
import sys
import math
input = lambda: sys.stdin.readline().rstrip()
 
 
n,x,pos=map(int,input().split())
#l=[-1 for i in range(n)]
#l[pos]=x
less=x-1
more=n-x
 
l=0
r=n
c=1
avail=n-1
mod=10**9+7
 
while(l<r):
    mid=(l+r)//2
    if(mid==pos):
        l=mid+1
    elif(mid<pos):
        c*=less
        less-=1
        l=mid+1
        avail-=1
    else:
        c*=more
        more-=1
        r=mid
        avail-=1
 
less+=more
c*=math.factorial(less)
print(c%mod)