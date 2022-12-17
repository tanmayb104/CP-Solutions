# cook your dish here
for _ in range(int(input())):
    l=[int(x) for x in input().split()]
    p=l.pop()
    s=0
    for i in range(5):
        s+=l[i]*p
    if(s<=24*5):
        print("No")
    else:
        print("Yes")