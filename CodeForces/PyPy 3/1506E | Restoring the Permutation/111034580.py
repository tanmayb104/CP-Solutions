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
from heapq import *
from collections import deque as dq
from math import ceil,floor,sqrt,pow,factorial,log2
import bisect as bs
from collections import Counter
# from collections import defaultdict as dc 
 
for ii in range(N()):
    
    n=N()
    l=RLL()
    num=[i+1 for i in range(n)]
    a=[0 for i in l]
    c=0
    wq=[]
    for i in range(n):
        if(l[i]>c):
            a[i]=l[i]
            c=l[i]
            wq.append(c)
    wq_set=set(wq)
    set_left1=[]
    set_left2=[]
    for i in num:
        if(i not in wq_set):
            set_left1.append(i)
            set_left2.append(i)
 
    set_left1.sort()
    min_a=[i for i in a]
    c=1
    j=0
    for i in range(n):
        if(min_a[i]==0):
            min_a[i]=set_left1[j]
            j+=1
    print(*min_a)
    set_left2.sort()
    max_a=[i for i in a]
    le=1
    wq.sort()
    j=0
    h=[]
    heapify(h)
    vis=set()
    len_vis=0
    m=0
    prev=0
    for i in range(n):
        if(max_a[i]==0):
            a=heappop(h)
            max_a[i]=abs(a)
        else:
            for j in range(max_a[i]-1,prev,-1):
                heappush(h,-j)
            prev=max_a[i]
    print(*max_a)
        