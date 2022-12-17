# cook your dish here
import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    s=sum(l)
    if(s<0):
        print("NO")
    else:
        print("YES")

        