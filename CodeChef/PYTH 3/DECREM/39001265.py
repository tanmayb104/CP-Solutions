# cook your dish here
import sys
import math
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
	l,r=map(int,input().split())
	if(l<=(r-l)):
		print(-1)
	else:
		print(r)


