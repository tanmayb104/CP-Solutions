import os
import sys
from io import BytesIO, IOBase
# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline()
 
# ------------------------------
 
def RL(): return map(int, sys.stdin.readline().split())
def RLL(): return list(map(int, sys.stdin.readline().split()))
def N(): return int(input())
def print_list(l):
    print(' '.join(map(str,l)))
# sys.setrecursionlimit(300000)
# from heapq import *
# from collections import deque as dq
from math import ceil,floor,sqrt,pow,factorial
# import bisect as bs
# from collections import Counter
# from collections import defaultdict as dc 
 
def modInverse(a, m): 
  
    g = gcd(a, m) 
  
    # If a and m are relatively prime, 
    # then modulo inverse is a^(m-2) mode m 
    return power1(a, m - 2, m)
  
# To compute x^y under modulo m 
  
  
def power1(x, y, m): 
  
    if (y == 0): 
        return 1
  
    p = power1(x, y // 2, m) % m 
    p = (p * p) % m 
  
    if(y % 2 == 0): 
        return p 
    else: 
        return ((x * p) % m) 
  
# Function to return gcd of a and b 
  
  
def gcd(a, b): 
    if (a == 0): 
        return b 
  
    return gcd(b % a, a) 
 
def power(x, y, p) : 
    res = 1     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
      
    if (x == 0) : 
        return 0
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res 
 
n=N()
fi0=0
fi1=1
ans=1
for i in range(2,n+1):
    ans=fi0+fi1
    fi0=fi1
    fi1=ans
x=ans
y=power(2,n,998244353)
inv=modInverse(y,998244353)
print((x*inv)%998244353)
 
    
 
    
            
 
 