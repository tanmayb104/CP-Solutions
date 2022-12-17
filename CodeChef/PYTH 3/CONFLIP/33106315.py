# cook your dish here
import math
for _ in range(int(input())):
    for _ in range(int(input())):
        l=[int(x) for x in input().split()]
        if(l[0]==l[2]):
            print(l[1]//2)
        else:
            print(math.ceil(l[1]/2))