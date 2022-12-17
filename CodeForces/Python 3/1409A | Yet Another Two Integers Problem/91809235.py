for _ in range(int(input())):
    a,b=map(int,input().split())
    c=min(a,b)
    d=max(a,b)
    cd=abs(c-d)
    if(cd/10==cd//10):
        print(cd//10)
    else:
        print(cd//10+1)