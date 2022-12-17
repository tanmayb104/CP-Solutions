import sys
import math
input = lambda: sys.stdin.readline().rstrip()
 
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[int(x) for x in input().split()]
    ans=[0 for i in range(n)]
    if(k%2==1):
        for i in range(n):
            if(l[i]%2==0):
                ans[i]=1
 
    else:
        for i in range(n):
            if(l[i]<k/2):
                ans[i]=1
        a=l.count(k//2)
        if(a>1):
            b=a//2
            for i in range(n):
                if(l[i]==k//2):
                    ans[i]=1
                    b-=1
                if(b==0):
                    break
    print(*ans)
 
 
 
 
            
        
        
 
        