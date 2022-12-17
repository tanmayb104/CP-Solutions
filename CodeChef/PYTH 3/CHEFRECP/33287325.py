# cook your dish here
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    #a,b=map(int,input().split())
    co=Counter(l)
    s1=set(l)
    s2=[]
    flag=0
    s=[]
    for i in range(n):
        if(len(s)==0):
            s.append(l[i])
        else:
            if(l[i]==s[-1]):
                continue
            else:
                if(l[i] in s):
                    flag=1
                    break
                else:
                    s.append(l[i])
    for i in s1:
        if(co[i] in s2):
            flag=1
        else:
            s2.append(co[i])
    if(flag==0):
        print("YES")
    else:
        print("NO")