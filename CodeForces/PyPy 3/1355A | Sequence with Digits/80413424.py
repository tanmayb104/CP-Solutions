for _ in range(int(input())):
    n,k=map(int,input().split())
    for _ in range(k-1):
        min_n=min(str(n))
        if(int(min_n)==0):
            break
        max_n=max(str(n))
        n+=int(min_n)*int(max_n)
    print(int(n))