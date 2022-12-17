# cook your dish here
from collections import Counter as co
for ii in range(int(input())):
    s=input().strip()
    d=co(s)
    a=0
    for i in d.keys():
        if(d[i]==1):
            a-=1
        elif(d[i]%2==0):
            a+=d[i]//2
        else:
            a+=(d[i]-3)//2
    if(a>=0):
        print("Yes")
    else:
        print("No")