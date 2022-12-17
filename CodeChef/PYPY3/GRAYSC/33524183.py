from collections import Counter
n=int(input())
l=[int(x) for x in input().split()]
if(n>130):
    print("Yes")
else:
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for p in range(k+1,n):
                    if(l[i]^l[j]^l[k]^l[p]==0):
                        print("Yes")
                        exit()
    print("No")
        