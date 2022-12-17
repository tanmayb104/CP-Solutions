# cook your dish here
import heapq
for _ in range(int(input())):
    n,z=map(int,input().split())
    l=[int(x)*-1 for x in input().split()]
    c=0
    heapq.heapify(l)
    while(z>0 and len(l)>0):
        a=heapq.heappop(l)
        a*=-1
        if(a<=0):
            break
        z-=a
        a=a//2*(-1)
        heapq.heappush(l,a)
        c+=1
    if(z>0):
        print("Evacuate")
    else:
        print(c)