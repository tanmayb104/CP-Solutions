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
# from math import ceil,floor,sqrt,pow
# import bisect as bs
from collections import Counter
# from collections import defaultdict as dc 
 
for i in range(N()):
    n=N()
    l=RLL()
    if(len(set(l))==1):
        print(0)
    else:
        l1=[l[0]]
        for i in range(1,n):
            if(l[i]!=l[i-1]):
                l1.append(l[i])
        c=Counter(l1)
        mi=9999999
        for i in set(l1):
            mi=min(mi,c[i])
        ans=[]
        for i in set(l1):
            if(c[i]==mi or c[i]==mi+1 or c[i]==mi+2):
                ans.append([i,c[i]])
        mi=999999
        for j in ans:
            if(l1[0]==j[0] and l1[-1]==j[0]):
                mi=min(j[1]-1,mi)
            elif(l1[0]==j[0] or l1[-1]==j[0]):
                mi=min(j[1],mi)
            else:
                mi=min(j[1]+1,mi)
        print(mi)