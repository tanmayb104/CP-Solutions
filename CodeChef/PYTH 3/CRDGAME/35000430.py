# cook your dish here
def check(a):
    c=0
    while(a):
        c+=a%10
        a=a//10
    return c

for _ in range(int(input())):
    n=int(input())
    c1=0
    c2=0
    for i in range(n):
        a,b=map(int,input().split())
        a1=check(a)
        b1=check(b)
        if(a1>b1):
            c1+=1
        elif(a1<b1):
            c2+=1
        else:
            c1+=1
            c2+=1
    if(c1>c2):
        print(0,c1)
    elif(c2>c1):
        print(1,c2)
    else:
        print(2,c1)
        
