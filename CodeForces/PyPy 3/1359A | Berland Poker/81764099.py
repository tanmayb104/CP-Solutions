import math
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    card=n//k
    if(m<=card):
        print(m)
    else:
        m=m-card
        m=math.ceil(m/(k-1))
        print(card-m)