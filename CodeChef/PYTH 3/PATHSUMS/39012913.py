# cook your dish here
import sys
import math
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
	n=int(input())
	g={}
	for i in range(n-1):
		u,v=map(int,input().split())
		if(u in g):
			g[u].append(v)
		else:
			g[u]=[v]
		if(v in g):
			g[v].append(u)
		else:
			g[v]=[u]
	queue=[]
	queue.append(1)
	queue.append(-1)
	arr=[0]*(n+1)
	visited = [False] * (n+1)
	visited[1]=True
	flag=1
	while(len(queue)):
		s=queue.pop(0)
		if(s==-1):
			flag=1^flag
			try:
				if(queue[0]!=-1):
					queue.append(-1)
			except:
				pass
			continue
		if(flag):
			arr[s]=2
		else:
			arr[s]=1
		for i in g[s]:
			if visited[i]==False:
				queue.append(i)
				visited[i]=True
	arr.pop(0)
	print(*arr)






