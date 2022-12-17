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
    n,m,k=RL()
    rows=n
    cols=m
    h=k
    v=n*m//2-k
    if(n%2==1):
        k-=m//2
    if(m%2==1):
        v-=n//2
    if(v>=0 and k>=0 and k%2==0 and v%2==0):
        print("YES")
        v=n*m//2-h
        mat=[["" for i in range(m)] for j in range(n)]
        if(n%2==1):
            row=["x","x","y","y"]
            point=0
            h-=m//2
            for i in range(m):
                mat[-1][i]=row[point]
                point+=1
                point=point%4
            n-=1
        if(m%2==1):
            v-=n//2
            col=["x","x","y","y"]
            point=0
            for i in range(n):
                mat[i][-1]=col[point]
                point+=1
                point=point%4
            m-=1
        choice1=["a","b"]
        choice2=["c","d"]
        flag1=1
        for i in range(0,n,2):
            flag2=1
            if(flag1):
                for j in range(0,m,2):
                    if(flag2):
                        if(h):
                            mat[i][j]="a"
                            mat[i][j+1]="a"
                            mat[i+1][j]="b"
                            mat[i+1][j+1]="b"
                            h-=2
                        else:
                            mat[i][j]="a"
                            mat[i][j+1]="b"
                            mat[i+1][j]="a"
                            mat[i+1][j+1]="b"
                            v-=2
                    else:
                        if(h):
                            mat[i][j]="c"
                            mat[i][j+1]="c"
                            mat[i+1][j]="d"
                            mat[i+1][j+1]="d"
                            h-=2
                        else:
                            mat[i][j]="c"
                            mat[i][j+1]="d"
                            mat[i+1][j]="c"
                            mat[i+1][j+1]="d"
                            v-=2
                    flag2= not flag2
            else:
                for j in range(0,m,2):
                    if(flag2):
                        if(h):
                            mat[i][j]="c"
                            mat[i][j+1]="c"
                            mat[i+1][j]="d"
                            mat[i+1][j+1]="d"
                            h-=2
                        else:
                            mat[i][j]="c"
                            mat[i][j+1]="d"
                            mat[i+1][j]="c"
                            mat[i+1][j+1]="d"
                            v-=2
                    else:
                        if(h):
                            mat[i][j]="a"
                            mat[i][j+1]="a"
                            mat[i+1][j]="b"
                            mat[i+1][j+1]="b"
                            h-=2
                        else:
                            mat[i][j]="a"
                            mat[i][j+1]="b"
                            mat[i+1][j]="a"
                            mat[i+1][j+1]="b"
                            v-=2
                    flag2= not flag2
            flag1=not flag1
        for i in range(rows):
            print("".join(mat[i]))
    else:
        print("NO")