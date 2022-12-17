# cook your dish here
from bisect import bisect_right as br
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    stack=[l[0]]
    for i in range(1,n):
        a=br(stack,l[i])
        if(a==len(stack)):
            stack.append(l[i])
        else:
            stack[a]=l[i]
    print(len(stack),end=" ")
    print(*stack)