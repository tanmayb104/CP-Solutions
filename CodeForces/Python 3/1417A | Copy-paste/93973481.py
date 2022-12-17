import sys
import math
input = lambda: sys.stdin.readline().rstrip()
 
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[int(x) for x in input().split()]
    l.sort()
    a=0
    for i in range(1,n):
        if(l[i]>=k):
            break
        else:
            a+=(k-l[i])//l[0]
    print(a)
            
        
        
 
        