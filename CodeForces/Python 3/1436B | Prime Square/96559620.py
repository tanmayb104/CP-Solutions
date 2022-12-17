# cook your dish here
import sys
import math
input = lambda: sys.stdin.readline().rstrip()
 
def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
 
for _ in range(int(input())):
    n=int(input())
    l=[[1 for i in range(n)] for j in range(n)] 
    flag=0
    for i in range(n,10**5+n):
        if(isPrime(i)):
            if(not isPrime(i-n+1)):
                flag=1
                for j in range(n-1,-1,-1):
                    l[j][n-j-1]=i-n+1
                break
        if(flag):
            break
    for i in range(n):
        print(*l[i])
 
 
 
 
 
 
 
 
 
 
 