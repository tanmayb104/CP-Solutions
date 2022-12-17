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
# from math import ceil,floor,sqrt,pow,factorial
# import bisect as bs
# from collections import Counter
# from collections import defaultdict as dc 
 

for _ in range(N()):
    n,u=RL()
    s=input().upper()
    l=s.split("X")
    ans=0
    for i in l:
        a=[0 for j in range(len(i))]
        for j in range(len(i)):
            if(i[j]==":"):
                a[j]=1
        for j in range(1,len(i)):
            a[j]+=a[j-1]
        iron=dq()
        m=dq()
        li_i=[]
        li_m=[]
        c=0
        for j in range(len(i)):
            if(i[j]=="I"):
                if(len(m)==0):
                    iron.append(j)
                else:
                    li_m=list(m)
                    flag=0
                    for k in li_m:
                        if(abs(int(k)-int(j))<int(u)+1-(int(a[j])-int(a[k]))):
                            c+=1
                            flag=1
                            m.popleft()
                            break
                        else:
                            m.popleft()
                    if(not flag):
                        iron.append(j)

            elif(i[j]=="M"):
                if(len(iron)==0):
                    m.append(j)
                else:
                    li_i=list(iron)
                    flag=0
                    for k in li_i:
                        if(abs(int(k)-int(j))<int(u)+1-(int(a[j])-int(a[k]))):
                            c+=1
                            iron.popleft()
                            flag=1
                            break
                        else:
                            iron.popleft()
                    if(not flag):
                        m.append(j)

        ans+=c
    print(ans)



    