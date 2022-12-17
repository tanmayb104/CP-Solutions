# cook your dish here
for _ in range(int(input())):
    n=int(input())
    ma=0
    for i in range(n):
        l=[int(x) for x in input().split()]
        ma=max(ma,(l[1]//(l[0]+1))*l[2])
    print(ma)