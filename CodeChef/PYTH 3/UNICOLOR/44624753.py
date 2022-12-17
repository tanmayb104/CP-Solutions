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
from math import ceil,floor,sqrt,factorial,log2
# import bisect as bs
from collections import Counter
# from collections import defaultdict as dc 

for _ in range(N()):
    c,n,m=RLL()
    g={}
    for i in range(c):
        g[i]=set()
    intervals=[]
    for i in range(c):
        le=N()
        l=RLL()
        for j in range(0,2*le,2):
            intervals.append([l[j],l[j+1],i])

    intervals=sorted(intervals, key=lambda x:x[0])
    #print(intervals)
    unique=[intervals[0]]
    unique_club=[[intervals[0][2]]]
    j=0
    for k in range(1,len(intervals)):
        if(intervals[k][0]<=unique[j][1]):
            unique[j][1]=max(unique[j][1],intervals[k][1])
            unique_club[j].append(intervals[k][2])
        else:
            unique.append(intervals[k])
            unique_club.append([intervals[k][2]])
            j+=1
    #print(unique_club)
    #print(unique)
    for i in range(len(unique_club)):
        unique_club[i]=list(set(unique_club[i]))
    for j in range(len(unique_club)):
        for k in range(1,len(unique_club[j])):
            g[unique_club[j][k]].add(unique_club[j][k-1])
            g[unique_club[j][k-1]].add(unique_club[j][k])

    vis=[0 for i in range(c)]
    cont=n
    con=0
    for i in range(len(unique)):
        cont=cont-(unique[i][1]-unique[i][0]+1)
    #print(g)
    for i in range(c):
        if(vis[i]==0):
            con+=1
            st=[i]
            while(len(st)):
                a=st.pop()
                vis[a]=1
                for j in g[a]:
                    if(vis[j]==0):
                        st.append(j)
    a=n
    print(pow(m,con+cont,998244353))


    