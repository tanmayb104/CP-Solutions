for _ in range(int(input())):
    #n,k=map(int,input().split())
    #l=[int(x) for x in input().split()]
    #n=int(input())
    #l = [int(x) for x in input().split()]
    s=input()
    n=len(s)
    i=0
    c=0
    while(i<n-1):
        if((s[i]=="x" and s[i+1]=="y") or (s[i]=="y" and s[i+1]=="x")):
            c+=1
            i+=1
        i+=1
    print(c)