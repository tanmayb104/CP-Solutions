# cook your dish here
for _ in range(int(input())):
    n,s=map(int,input().split())
    c=0
    if(n%2==1):
        c+=1
        n-=1
    c+=n//s
    if(n%s):
        c+=1
    print(c)
