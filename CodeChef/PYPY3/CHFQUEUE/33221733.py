# cook your dish here
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
f=1
c=999999999
stack=[]
pos=[]
i=0
while(i<n):
    if(len(stack)==0 or stack[-1]<=l[i]):
        stack.append(l[i])
        pos.append(i)
        i+=1
    else:
        a=stack.pop()
        b=pos.pop()
        f*=(i-b+1)
        f%=1000000007
print(f)
        

