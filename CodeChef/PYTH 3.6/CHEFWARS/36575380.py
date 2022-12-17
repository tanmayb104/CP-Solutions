# cook your dish here
for _ in range(int(input())):
    h,p=map(int,input().split())
    while(p!=0 and h>0):
        h-=p
        p=p//2
    if(h>0):
        print(0)
    else:
        print(1)