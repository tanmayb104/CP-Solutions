# cook your dish here
l=[]
for i in range(int(input())):
    l.append(int(input()))
l.sort()
m=0
n=len(l)
for i in l:
    m=max(m,i*n)
    n-=1
print(m)