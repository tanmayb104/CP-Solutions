for _ in range(int(input())):
    N = int(input())
    X = 10**9
    i = 1
    #find the factors of N
    while i * i < N: 
        if N % i == 0:
            a,b = i,N//i
            m = abs(a-b)
            if m % 2 == 0 and a!=b:
                X = min(X,abs(a-b)//2)
        i+=1
        
    if X == 10**9:
        print(-1)
    else:
        print(X*X)