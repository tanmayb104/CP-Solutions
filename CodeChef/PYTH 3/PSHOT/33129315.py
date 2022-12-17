# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    sla=n
    slb=n
    ga=0
    gb=0
    for i in range(2*n):
        if(i%2==0):
            sla-=1
            if(s[i]=="1"):
                ga+=1
                if(ga>(slb+gb)):
                    print((n-sla)*2-1)
                    break
            else:
                if(gb>(sla+ga)):
                    print((n-sla)*2-1)
                    break
        else:
            slb-=1
            if(s[i]=="1"):
                gb+=1
                if(gb>(sla+ga)):
                    print((n-slb)*2)
                    break
            else:
                if(ga>(slb+gb)):
                    print((n-slb)*2)
                    break
            if(i==(2*n-1)):
                print(2*n)
    