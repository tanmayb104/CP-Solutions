# cook your dish here
for _ in range(int(input())):
    n,k=tuple([int(x) for x in input().split()])
    count=0
    a=0
    for i in range(k):
        f,d=tuple([int(x) for x in input().split()])
        if(f<d and a<=f):
            count+=(d-a)
            a=d
        elif( f<d and a>f ):
            count+=(a-f)
            count+=(d-f)
            a=d
        elif( d<f and a<=f ):
            count+=(f-a)
            count+=(f-d)
            a=d
        elif( d<f and f<a ):
            count+=(a-f)
            count+=(f-d)
            a=d
    print(count)
