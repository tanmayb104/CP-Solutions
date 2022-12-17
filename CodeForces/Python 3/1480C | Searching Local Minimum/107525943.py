 
def RL(): return map(int, sys.stdin.readline().split())
def RLL(): return list(map(int, sys.stdin.readline().split()))
def N(): return int(input())
def print_list(l):
 print(' '.join(map(str,l)))
# sys.setrecursionlimit(300000)
# from heapq import *
import sys
from collections import deque as dq
from math import ceil,floor,sqrt,pow,factorial
# import bisect as bs
from collections import Counter
# from collections import defaultdict as dc 
 
n=N()
l=[-1 for i in range(n+2)]
l[0]=9999999
l[-1]=9999999
low=1
high=n+1
while(low<=high):
 mid=(low+high)//2
 if(l[mid]==-1):
  print("? "+str(mid))
  a=N()
  l[mid]=a
  sys.stdout.flush()
 if(l[mid-1]==-1):
  print("? "+str(mid-1))
  a=N()
  l[mid-1]=a
  sys.stdout.flush()
 if(l[mid+1]==-1):
  print("? "+str(mid+1))
  a=N()
  l[mid+1]=a
  sys.stdout.flush()
 if(l[mid-1]<l[mid] and l[mid]<l[mid+1]):
  high=mid
 elif(l[mid]<l[mid-1] and l[mid]<l[mid+1]):
  print("! "+str(mid))
  exit()
 elif(l[mid-1]>l[mid] and l[mid]>l[mid+1]):
  low=mid
 else:
  high=mid