# cook your dish here
for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    c=1
    for j in range(1,n):
        if(l[j-1]>=l[j]):
            c+=1
        else:
            l[j]=l[j-1]
    print(c)