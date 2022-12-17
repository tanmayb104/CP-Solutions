# cook your dish here
import math
for i in range(int(input())):
    a=input()
    if(sorted(a[:len(a)//2])==sorted(a[math.ceil(len(a)/2):])):
        print("YES")
    else:
        print("NO")