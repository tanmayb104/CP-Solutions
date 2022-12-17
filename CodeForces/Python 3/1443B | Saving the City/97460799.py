 
 
def RL(): return map(int, input().split())
def RLL(): return list(map(int, input().split()))
def N(): return int(input())
def print_list(l):
    print(' '.join(map(str,l)))
# sys.setrecursionlimit(300000)
# from heapq import *
# from collections import deque as dq
# from math import ceil,floor,sqrt,pow,factorial
# import bisect as bs
# from collections import Counter
# from collections import defaultdict as dc 
 
 
for _ in range(N()):
    a,b=RL()
    s=input()
    c=0
    blow=0
    num=0
    blow_1=0
    for i in range(len(s)):
        if(s[i]=="0"):
            if(blow==0):
                continue
            else:
                num+=1
        else:
            if(num>0):
                if(b*num<a):
                    c+=b*num
                    num=0
                else:
                    num=0
                    c+=a
                
            elif(blow==0):
                blow=1
                c+=a
    print(c)
 
        
 
 
 
    