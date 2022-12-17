# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    s=list(set(l))
    a=l.count(s[0])
    for i in range(1,len(s)):
        b=l.count(s[i])
        if(a<b):
            a=b
    print(n-a)