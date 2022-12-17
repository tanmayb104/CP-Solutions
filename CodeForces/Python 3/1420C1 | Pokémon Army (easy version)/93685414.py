for _ in range(int(input())):
    n,q=map(int,input().split())
    l=[int(x) for x in input().split()]
    ans=max(l)
    c=0
    stack_inc=[]
    stack_dec=[]
    flag=0
    for i in range(n):
        if(flag==0):
            if(len(stack_inc)==0):
                stack_inc.append(l[i])
            elif(stack_inc[-1]<=l[i]):
                stack_inc.append(l[i])
            else:
                c+=stack_inc[-1]
                stack_inc=[]
                flag=1
                stack_dec=[l[i]]
        else:
            if(len(stack_dec)==0):
                stack_dec.append(l[i])
            elif(stack_dec[-1]>=l[i]):
                stack_dec.append(l[i])
            else:
                c-=stack_dec[-1]
                stack_dec=[]
                flag=0
                stack_inc=[l[i]]
    if(flag==0):
        c+=stack_inc[-1]
    print(max(ans,c))