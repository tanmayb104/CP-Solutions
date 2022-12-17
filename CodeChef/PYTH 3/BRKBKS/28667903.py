# cook your dish here
for k in range(int(input())):
    l=[int(x) for x in input().split()]
    s=l[0]
    l.remove(s)
    c=0
    while(len(l)!=0):
        if(sum(l)>s):
            for i in range(1,len(l)+1):
                l1=l[:i]
                r1=sum(l1)
                if(r1>s):
                    break
            sum1=sum(l[:(i-1)])
            l.reverse()
            for j in range(1,len(l)+1):
                l2=l[:j]
                r2=sum(l2)
                if(r2>s):
                    break
            sum2=sum(l[:(j-1)])
            if(sum1>sum2):
                l.reverse()
                c+=1
                for k in range(i-1):
                    l.pop(0)
            else:
                c+=1
                for k in range(j-1):
                    l.pop(0)  
        else:
            l.clear()
            c+=1        
    print(c)