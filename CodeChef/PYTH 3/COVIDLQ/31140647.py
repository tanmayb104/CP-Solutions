# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    c=6
    flag=0
    for i in l:
        if(i==1):
            if(c>4):
                c=0
            else:
                flag=1
                break
        else:
            c+=1
    if(flag==0):
        print("YES")
    else:
        print("NO")