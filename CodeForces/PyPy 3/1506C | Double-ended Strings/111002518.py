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
# import bisect as bs
from collections import Counter
# from collections import defaultdict as dc 
 
def printSubArrays(arr, start, end):  
    l=[]
    if end == len(arr):
        return
    elif start > end:
        return printSubArrays(arr, 0, end + 1)
    else:
        l.append("".join(arr[start:end + 1]))
        return printSubArrays(arr, start + 1, end)
 
for ii in range(N()):
    l1=input().strip()
    l2=input().strip()
    a=[i for i in l1]
    b=[i for i in l2]
    m=len(a)+len(b)
    sub_a=[]
    sub_b=[]
    for i in range(len(a)):
        temp=""
        for j in range(i,len(a)):
            temp=temp+a[j]
            sub_a.append(temp)
 
    for i in range(len(b)):
        temp=""
        for j in range(i,len(b)):
            temp=temp+b[j]
            sub_b.append(temp)
 
    sub_a=set(sub_a)
    sub_b=set(sub_b)
    inter=sub_a.intersection(sub_b)
    for i in inter:
        c=len(i)
        m=min(m,len(a)+len(b)-2*c)
    print(m)
    
    
 