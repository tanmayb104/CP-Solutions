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
 
for _ in range(N()):
    s=input().strip()
    na=s.count("A")
    nb=s.count("B")
    nc=s.count("C")
    if(na==nb+nc or nb==na+nc or nc==na+nb):
        l=[["A",na],["B",nb],["C",nc]]
        l=sorted(l,key=lambda x:x[1])
        ns1=l[0][0]
        ns2=l[1][0]
        ns3=l[2][0]
        n1=l[0][1]
        n2=l[1][1]
        n3=l[2][1]
        s1=[]
        s2=[]
        flag1=0
        flag2=0
        for i in range(len(s)):
            if(s[i]==ns3):
                s1.append("(")
                try:
                    s2.pop()
                except:
                    flag2=0
            else:
                s2.append("(")
                try:
                    s1.pop()
                except:
                    flag1=0
        if(len(s1)==0 or len(s2)==0):
            print("YES")
        else:
            print("NO")
 
 
 
        
    else:
        print("NO")
 
 