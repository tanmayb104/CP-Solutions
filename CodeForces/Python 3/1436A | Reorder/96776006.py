# cook your dish here
import sys
import math
input = lambda: sys.stdin.readline().rstrip()
 
for _ in range(int(input())):
 n,m=map(int,input().split())
 l=[int(x) for x in input().split()]
 if(m==sum(l)):
  print("YES")
 else:
  print("NO")