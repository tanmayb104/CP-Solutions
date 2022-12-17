import sys
import math
input = lambda: sys.stdin.readline().rstrip()
 
for _ in range(int(input())):
 n=int(input())
 l1=[int(x) for x in input().split()]
 l2=[int(x) for x in input().split()]
 l3=[int(x) for x in input().split()]
 a=[l1[0]]
 for i in range(1,n):
  if(i==n-1):
   if(l1[i]!=a[0] and l1[i]!=a[-1]):
    a.append(l1[i])
   elif(l2[i]!=a[0]and l2[i]!=a[-1]):
    a.append(l2[i])
   else:
    a.append(l3[i])
  else:
   if(l1[i]!=a[-1]):
    a.append(l1[i])
   elif(l2[i]!=a[-1]):
    a.append(l2[i])
   else:
    a.append(l3[i])
 print(*a)
 
 
 
 
 
 
 
   
        
        
 
        