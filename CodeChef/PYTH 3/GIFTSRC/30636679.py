# cook your dish here
for _ in range(int(input())):
    n=int(input())
    x=0
    y=0
    b=-1
    l=[x for x in input()]
    for i in range(n):
        a=l[i]
        if( (a=="L") and (b!=0)):
            x-=1
            b=0
        elif( (a=="R")and (b!=0)):
            x+=1
            b=0
        elif( (a=="U")and (b!=1)):
            y+=1
            b=1
        elif( (a=="D") and (b!=1)):
            y-=1
            b=1
    print(x,end=" ")
    print(y)