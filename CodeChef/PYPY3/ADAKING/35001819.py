for _ in range(int(input())):
    n=int(input())
    l=[["X" for i in range(8)] for i in range(8)]
    l[0][0]="O"
    j=0
    k=1
    while(n-1):
        l[j][k]="."
        n-=1
        k+=1
        if(k==8):
            k=0
            j+=1
    for i in range(8):
        for j in range(8):
            print(l[i][j],end="")
        print()


