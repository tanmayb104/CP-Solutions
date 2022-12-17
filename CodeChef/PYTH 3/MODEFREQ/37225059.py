from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    c=Counter(l)
    c1=Counter(list(c.values()))
    s=list(c.values())
    a=0
    b=0
    arr=[]
    for i in s:
        if(c1[i]>a):
            a=c1[i]
            b=i
    for i in s:
        if(c1[i]==a):
            arr.append(i)
    print(min(arr))


