# cook your dish here
import sys
import math
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
	n=int(input())
	s=input()
	a=s[:n-1]
	b=s[-1]
	if(b in a):
		print("YES")
	else:
		print("NO")


