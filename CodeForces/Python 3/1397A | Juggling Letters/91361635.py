from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=""
    for i in range(n):
        a+=input()
    c=Counter(a)
    flag=0
    for i in set(a):
        if(c[i]%n!=0):
            flag=1
    if(flag):
        print("NO")
    else:
        print("YES")