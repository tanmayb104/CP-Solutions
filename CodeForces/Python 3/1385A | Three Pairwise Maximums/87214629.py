for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if(x==y and y==z):
        print("YES")
        print(x,y,z)
    elif(x!=y and y!=z and x!=z):
        print("NO")
    elif(x!=y and ((x==z and x>y) or (y==z and y>x))):
        print("YES")
        print(max(x,y),min(x,y),min(x,y))
    elif(x!=z and ((x==y and x>z) or (y==z and z>x))):
        print("YES")
        print(max(x,z),min(x,z),min(x,z))
    else:
        print("NO")