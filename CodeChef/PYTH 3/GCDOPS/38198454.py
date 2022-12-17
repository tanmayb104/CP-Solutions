# cook your dish here
import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    flag=0
    for i in range(1,n+1):
        if(i/l[i-1]!=i//l[i-1]):
            flag=1
    if(flag):
        print("NO")
    else:
        print("YES")

        