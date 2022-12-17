# cook your dish here
from collections import Counter

for _ in range(int(input())):
    n,q=map(int,input().split())
    s=input()
    counter=Counter(s)
    set_s=set(s)
    for i in range(q):
        c=int(input())
        count=0
        for i in set_s:
            if(counter[i]>c):
                count+=(counter[i]-c)
        print(count)