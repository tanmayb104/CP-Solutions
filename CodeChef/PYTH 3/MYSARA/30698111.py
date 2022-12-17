def no_of_ones(n):
    
    c = 0
    while n:
        c += n & 1
        n >>= 1
    #print('c=',c)
    return c  
MOD = 10**9 + 7    
two = []
two.append(1)
for i in range(1,31):
    two.append(two[i-1] * 2)
for _ in range(int(input())):
    n=int(input())
    l=[(int(x)) for x in input().split()]
    a=1
    for i in range(n-1) :
        
        if l[i] > l[i+1] :
            a = 0
            break
        
        else :
            a = ( (a%MOD) * (two[no_of_ones(l[i]) ] %MOD))
            
    print(a%MOD)
    