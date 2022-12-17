n=int(input())
x=0
y=0
print(4+3*n)
print(x,y)
print(x+1,y)
print(x,y+1)
print(x+1,y+1)
x=1
y=1
for i in range(n):
    print(x+1,y)
    print(x,y+1)
    print(x+1,y+1)
    x+=1
    y+=1
 
    