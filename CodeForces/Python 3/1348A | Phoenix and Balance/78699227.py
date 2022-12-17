l1=[2]
for i in range(14):
    l1.append(l1[-1]*2+2)
for _ in range(int(input())):
    n=int(input())
    print(l1[n//2-1])