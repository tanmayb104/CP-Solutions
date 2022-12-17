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
    l=[]
    string="abcde"
    for i in range(n):
        s=S()
        temp=[len(s)]
        c=Counter(s)
        for j in string:
            if(j in c):
                temp.append(c[j])
            else:
                temp.append(0)
        l.append(temp)
    ans=0
    for i in range(5):
        temp=l #sorted(l,key=lambda x:(x[1+i],-x[0]) if (x[0]-x[1+i])==0 else (x[1+i]/(x[0]-x[1+i]),-x[0]), reverse=True)
        te=0
        c1=0
        c2=0
        t2=[]
        for j in temp:
            if(j[1+i]>j[0]-j[1+i]):
                c1+=j[1+i]
                c2+=j[0]-j[1+i]
                te+=1
            else:
                t2.append(j)
        t2=sorted(t2, key=lambda x:x[0]-2*x[1+i])
        for j in t2:
            c1+=j[1+i]
            c2+=j[0]-j[1+i]
            te+=1
            if(c1<=c2):
                te-=1
                break
        ans=max(ans,te)
    print(ans)
            
 
 
 
    
    