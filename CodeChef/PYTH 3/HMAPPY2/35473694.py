from math import gcd
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    q=0
    q+=a//b
    q+=a//c
    q-=2*(a//((b*c)//gcd(b,c)))
    if(q>=d):
        print("Win")
    else:
        print("Lose")