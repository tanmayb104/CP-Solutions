for _ in range(int(input())):
    n,x=map(int,input().split())
    c=0
    for i in range(n-1):
        a, b = map(int, input().split())
        if(a==x or b==x):
            c+=1
    f=0
    if(c==1 or c==0):
        print("Ayush")
        continue
    elif (n-c-1)%2==0:
        f=0
    else:
        f=1
    if ((c-1)%2==0 and f==0) or ((c-1)%2==1 and f==1) :
        print("Ayush")
    elif ((c-1)%2==0 and f==1) or ((c-1)%2==1 and f==0):
        print("Ashish")