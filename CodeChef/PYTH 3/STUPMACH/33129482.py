# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    c=0
    s=l[0]
    for i in range(n):
        if(s>=l[i]):
            c+=l[i]
            s=l[i]
        else:
            c+=s
    print(c)