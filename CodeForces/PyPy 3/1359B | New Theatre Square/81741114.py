for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    l=[]
    for i in range(n):
        l.append([x for x in input()])
    if(x<=(y//2)):
        y=2*x
    c=0
    for i in range(n):
        j=0
        while(j<m):
            if(j<m-1):
                if(l[i][j]=="." and l[i][j+1]=="."):
                    c+=y
                    j+=1
                elif(l[i][j]=="."):
                    c+=x
            else:
                if(l[i][j]=="."):
                    c+=x
            j+=1
    print(c)