# cook your dish here

def binsearchx (arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l) // 2
        if (arr[mid] == x): 
            return mid 
        elif(r-l==1):
            if(mid+1<r):
                if(arr[mid+1]<x):
                    return mid+1
            return mid
        elif arr[mid] > x: 
            return binsearchx(arr, l, mid, x) 
        else: 
            return binsearchx(arr, mid, r, x) 

def binsearchy (arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l) // 2
        if (arr[mid] == x): 
            return mid 
        elif(r-l==1):
            if(arr[mid]>x):
                return mid
            else:
                return mid+1
        elif arr[mid] > x: 
            return binsearchy(arr, l, mid, x) 
        else: 
            return binsearchy(arr, mid, r, x) 

n,x,y=map(int,input().split())
l=[]
for i in range(n):
    l.append([int(x) for x in input().split()])
x_t=[int(x) for x in input().split()]
y_t=[int(x) for x in input().split()]
x_t.sort()
y_t.sort()
m=9999999
for i in range(n):
    x1=l[i][0]
    y1=l[i][1]
    if(x1<x_t[0] or y1>y_t[-1]):
        continue
    a=binsearchx(x_t,0,x,x1)
    b=binsearchy(y_t,0,y,y1)
    m=min(m,y_t[b]-x_t[a]+1)
print(m)
