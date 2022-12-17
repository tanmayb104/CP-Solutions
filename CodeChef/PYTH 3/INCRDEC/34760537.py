# cook your dish here
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    c=Counter(l)
    l1=list(c.values())
    #print(l1)
    flag=0
    for i in l1:
        if(i>2):
            print("NO")
            flag=1
            break
    if(flag):
        continue
    if(c[max(l)]>1):
        print("NO")
        continue
    l.sort()
    s1=[]
    s2=[]
    s1.append(l[0])
    prev=l[0]
    for i in range(1,n):
        if(prev==l[i]):
            s2.append(l[i])
        else:
            s1.append(l[i])
            prev=l[i]
    print("YES")
    print(*(s1+s2[::-1]))    
