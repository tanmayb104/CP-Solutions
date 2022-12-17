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
 
n,m1,m2=RL()
m={}
d={}
for i in range(1,n+1):
    m[i]=[]
    d[i]=[]
for i in range(m1):
    u,v=RL()
    m[u].append(v)
    m[v].append(u)
for i in range(m2):
    u,v=RL()
    d[u].append(v)
    d[v].append(u)
cm={}
cd={}
vis=[False for i in range(n+1)]
c1=0
for i in range(1,n+1):
    if(not vis[i]):
        st=[i]
        while(st):
            a=st.pop()
            cm[a]=c1
            vis[a]=True
            for i in m[a]:
                if(not vis[i]):
                    st.append(i)
        c1+=1
vis=[False for i in range(n+1)]
c2=0
for i in range(1,n+1):
    if(not vis[i]):
        st=[i]
        while(st):
            a=st.pop()
            cd[a]=c2
            vis[a]=True
            for i in d[a]:
                if(not vis[i]):
                    st.append(i)
        c2+=1
ans=[]
# print(cm,cd)
flag=0
for i in range(1,n):
    for j in range(i+1,n+1):
        if(cm[i]!=cm[j] and cd[i]!=cd[j]):
            ans.append([i,j])
            com1=cm[i]
            com2=cm[j]
            for k in range(1,n+1):
                if(cm[k]==com1 or cm[k]==com2):
                    cm[k]=c1
            c1+=1
            com1=cd[i]
            com2=cd[j]
            for k in range(1,n+1):
                if(cd[k]==com1 or cd[k]==com2):
                    cd[k]=c2
            c2+=1
            if(len(cm.values())==1 or len(cd.values())==1):
                flag=1
                break
    if(flag):
        break
print(len(ans))
for i in ans:
    print(*i)                
 
 
 
 