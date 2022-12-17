from collections import Counter
for _ in range(int(input())):
    n,m=map(int,input().split())
    s1=set([int(x) for x in input().split()])
    s2=set([int(x) for x in input().split()])
    s3=s1.intersection(s2)
    if(len(s3)):
        print("YES")
        print(1,list(s3)[0])
    else:
        print("NO")