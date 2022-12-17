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
from collections import deque as dq
from math import ceil,floor,sqrt,pow,factorial,log2
# import bisect as bs
from collections import Counter
# from collections import defaultdict as dc 

MAX = 1000001; 
  
factor = [0]*(MAX + 1); 
def generatePrimeFactors(): 
    factor[1] = 1; 
    for i in range(2,MAX): 
        factor[i] = i; 
    for i in range(4,MAX,2): 
        factor[i] = 2; 
  
    i = 3; 
    while(i * i < MAX): 
        if (factor[i] == i): 
            j = i * i; 
            while(j < MAX):  
                if (factor[j] == j): 
                    factor[j] = i; 
                j += i; 
        i+=1; 
  
def calculateNoOFactors(n): 
    if (n == 1): 
        return 1; 
    ans = 1; 
    dup = factor[n]; 
  
    c = 1; 
    j = int(n / factor[n]); 
  
    while (j > 1): 
        if (factor[j] == dup): 
            c += 1; 
  
        else: 
            dup = factor[j]; 
            ans = ans * (c + 1); 
            c = 1; 
        j = int(j / factor[j]); 
  
    ans = ans * (c + 1); 
  
    return ans; 

generatePrimeFactors() 
l=[]
for i in range(1,10**6+1):
    a=calculateNoOFactors(i)
    if(a%2==1):
        l.append(i)

for _ in range(N()):
    for i in l:
        print(i)
        sys.stdout.flush()
        a=N()  
        if(a==1):
            break
