# cook your dish here
for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    l1=[i for i in l]
    l1=sorted(l1,reverse=True)
    if(l==l1):
        print("No")
    else:
        print("Yes")