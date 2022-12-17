import sys

def div1(arr):
    global x_coord
    if(len(arr)==1):
        x_coord=arr[0]
        return arr
    y_cord=0
    x_cord=arr[len(arr)//2]
    print("?",x_cord,y_cord)
    sys.stdout.flush()
    ans=input()
    if(ans=="YES"):
        div1(arr[len(arr)//2:])
    else:
        div1(arr[:len(arr)//2])

def div2(arr):
    global y_coord
    if(len(arr)==1):
        y_coord=arr[0]
        return arr
    x_cord=0
    y_cord=arr[len(arr)//2]
    print("?",x_cord,y_cord)
    sys.stdout.flush()
    ans=input()
    if(ans=="YES"):
        div2(arr[len(arr)//2:])
    else:
        div2(arr[:len(arr)//2])
        
def div3(arr):
    global tri_coord
    global x_coord
    if(len(arr)==1):
        tri_coord=arr[0]
        return arr
    y_cord=x_coord
    x_cord=arr[len(arr)//2]
    print("?",x_cord,2*y_cord)
    sys.stdout.flush()
    ans=input()
    if(ans=="YES"):
        div3(arr[len(arr)//2:])
    else:
        div3(arr[:len(arr)//2])

x=[int(i) for i in range(0,1000+1)]
y=x.copy()
tri=x.copy()
x_coord=0
y_coord=0
tri_base=0
div1(x)
div2(y)
div3(tri)
a=2*x_coord
a=a*a
a+=(tri_coord)*(y_coord-2*x_coord)
print("!",a)