for _ in range(int(input())):
    a,b=map(int,input().split())
    c=0
    if(a<b):
        c+=(b-a)
        a=b
    if (a%2==0 and b%2==0) or (a%2==1 and b%2==1):
        print(c)
    else:
        print(c+1)