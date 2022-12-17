n=int(input())
l=[int(x) for x in input().split()]
l.sort()
j=1
flag=0
for i in l:
    if(i==j):
        j+=1
    else:
        print(j)
        flag=1
        break
else:
    print(j)