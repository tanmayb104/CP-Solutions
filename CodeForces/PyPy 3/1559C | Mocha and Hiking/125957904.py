# cook your dish here
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
        self.writable = "a1" in file.mode or "r" not in file.mode
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
def S(): return input().strip()
def print_list(l):
    print(' '.join(map(str,l)))
# sys.setrecursionlimit(300000)
from heapq import *
from collections import deque as dq
from math import ceil,floor,sqrt,pow,factorial,log2
import bisect as bs
from collections import Counter
from itertools import permutations
# from collections import defaultdict as dc 
 
for _ in range(N()):
    n=N()
    l=RLL()
    if(l[0]==1):
        ans=[n+1]
        for i in range(1,n+1):
            ans.append(i)
        print(*ans)
    elif(l[-1]==0):
        ans=[]
        for i in range(1,n+2):
            ans.append(i)
        print(*ans)
    else:
        flag=0
        for i in range(1,n):
            if(l[i]==1 and l[i-1]==0):
                flag=1
                break
        if(flag):
            ans=[]
            j=i
            for i in range(1,n+1):
                if(i==j+1):
                    ans.append(n+1)
                ans.append(i)
            print(*ans)
        else:
            print(-1)
 
 
 
    