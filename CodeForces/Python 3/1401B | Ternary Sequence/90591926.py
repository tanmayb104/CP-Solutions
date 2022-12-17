for _ in range(int(input())):
    a,b,c=map(int,input().split())
    x,y,z=map(int,input().split())
    f=0
    a1=min(a,z)
    a-=a1
    z-=a1
    a1=min(c,y)
    f+=2*a1
    c-=a1
    y-=a1
    if(z==0 and y==0):
        print(f)
    elif(z==0 and c==0):
        print(f)
    elif(a==0 and c==0):
        f-=2*z
        print(f)
    elif(a==0 and y==0):
        a1=min(z,c)
        z-=a1
        c-=a1
        if(c):
            print(f)
        else:
            f-=2*z
            print(f)
    else:
        print(f)
 
    
    