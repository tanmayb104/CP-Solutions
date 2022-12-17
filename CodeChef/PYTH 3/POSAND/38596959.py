# cook your dish here
import sys
input = lambda: sys.stdin.readline().rstrip()
import sys
import math
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n=int(input())
    if(n==1):
        print(1)
    elif(math.log2(n)==int(math.log2(n))):
        print(-1)
    else:
        a=math.log2(n)
        a=int(a)
        l=[2**(a-1)]
        l1=[int(i) for i in range(2**a+1,n+1)]
        l1+=[2**a]
        a-=1
        while(a!=-1):
            l+=[int(i) for i in range(2**a+1,2**(a+1))]
            a-=1
            if(a!=-1):
                l+=[2**a]
        print(*(l+l1))


                

