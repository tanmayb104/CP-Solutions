# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[int(x) for x in input().split()]
    a=99999999
    b=0
    for i in l:
        if(abs(i-k)%i==0):
            if(a>abs(i-k)//i):
                a=abs(i-k)//i
                b=i
    if(a==99999999):
        print(-1)
    else:
        print(b)

        