# cook your dish here
for _ in range(int(input())):
    l1=input().split()
    c=0
    for _ in range(int(l1[0])):
        l=input().split()
        if(l[0]=="CONTEST_WON"):
            c+=300
            if(int(l[1])<20):
                c+=(20-int(l[1]))
        elif(l[0]=="TOP_CONTRIBUTOR"):
            c+=300
        elif(l[0]=="BUG_FOUND"):
            c+=int(l[1])
        else:
            c+=50
    #print(c)
    if(l1[1]=="INDIAN"):
        print(c//200)
    else:
        print(c//400)