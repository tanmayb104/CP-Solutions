import sys
import math
input = lambda: sys.stdin.readline().rstrip()
#sys.setrecursionlimit(100000000)

for _ in range(int(input())):
	n,k,x,y=map(int,input().split())
	flag=1
	l=[0]*n
	while(flag):
		if(l[x]!=1):
			l[x]=1
			x=(x+k)%n
		else:
			flag=0

	if(l[y]==1):
		print("YES")
	else:
		print("NO")
	
