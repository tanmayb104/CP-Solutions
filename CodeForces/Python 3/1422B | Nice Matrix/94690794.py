import sys
import math
input = lambda: sys.stdin.readline().rstrip()
#sys.setrecursionlimit(100000000)
 
for _ in range(int(input())):
 n,m=map(int,input().split())
 l=[]
 for i in range(n):
  l1=[int(x) for x in input().split()]
  l.append(l1)
 ans=0
 for i in range(n//2):
  for j in range(m//2):
   arr=[l[i][j],l[n-i-1][j],l[i][m-j-1],l[n-i-1][m-j-1]]
   arr.sort()
   ans+=min( abs(arr[1]-l[i][j])+abs(arr[1]-l[n-i-1][j])+abs(arr[1]-l[i][m-j-1])+abs(arr[1]-l[n-i-1][m-j-1]),  abs(arr[2]-l[i][j])+abs(arr[2]-l[n-i-1][j])+abs(arr[2]-l[i][m-j-1])+abs(arr[2]-l[n-i-1][m-j-1]) )
 if(n%2==1 and m%2==1):
  for i in range(n//2):
   ans+=abs(l[i][m//2]-l[n-i-1][m//2])
  for i in range(m//2):
   ans+=abs(l[n//2][i]-l[n//2][m-i-1])
 elif(n%2==1):
  for i in range(m//2):
   ans+=abs(l[n//2][i]-l[n//2][m-i-1])
 elif(m%2==1):
  for i in range(n//2):
   ans+=abs(l[i][m//2]-l[n-i-1][m//2])
 print(ans)