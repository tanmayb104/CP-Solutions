# cook your dish here
import sys
import math
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
	n=int(input())
	ans=[]
	while(True):
		
		if(n>10**5-2):
			ans.append(10**5)
			ans.append(10**5-1)
			ans.append(1)
			n-=10**5-2

		else:

			ans.append(n+2)
			ans.append(n+1)
			break
	print(len(ans))	
	print(*ans)








