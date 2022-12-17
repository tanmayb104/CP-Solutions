for _ in range(int(input())):
    s=[x for x in input()]
    res=len(s)
    c=0
    j=0
    l=[]
    prev=0
    for i in range(len(s)):
        if(s[i]=="+"):
            c+=1
        else:
            c-=1
        if(c<prev):
            prev=c
            l.append([c,i])
    prev=0
    #print(l)
    for i in range(len(l)):
        res+=abs((abs(l[i][0])-prev)*(l[i][1]+1))
        prev=abs(l[i][0])        
    print(res)
    