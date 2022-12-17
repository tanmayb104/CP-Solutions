import sys
import math
input = lambda: sys.stdin.readline().rstrip()
#sys.setrecursionlimit(100000000)
 
for _ in range(int(input())):
 a,b,c=map(int,input().split())
 print(math.ceil(math.sqrt(a**2+(b-c)**2)))
 
 