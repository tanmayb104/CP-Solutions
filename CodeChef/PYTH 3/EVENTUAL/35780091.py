from collections import Counter
for _ in range(int(input())):
    n=int(input())
    s=input()
    c=Counter(s)
    #print(c)
    flag=0
    for i in list(c.keys()):
        if(c[i]%2!=0):
            flag=1
    if(flag):
        print("NO")
    else:
        print("YES")
# cook your dish here
