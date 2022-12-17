# cook your dish here
for _ in range(int(input())):
    n=int(input())
    ans1=0
    ans2=0
    for _ in range(n):
        g,a,b=map(int,input().split())
        ans1+=b*(g/(a+b))
        ans2+=a*(g/(a+b))
    print(ans1,ans2)
