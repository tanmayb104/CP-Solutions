for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input()]
    stack=[]
    i=0
    while(i<n):
        if(not len(stack) or l[i]==1):
            stack.append([l[i],0])
            i+=1
        elif(stack[-1][0]==0):
            stack.append([l[i],0])
            i+=1
        else:
            a=stack.pop()
            if(len(stack)):
                if(stack[-1][0]==1):
                    stack[-1][1]+=1
                else:
                    stack.append([1,1])
                    i+=1
            else:
                stack.append([1,1])
                i+=1
    for i in range(len(stack)):
        if(stack[i][0]==0):
            print("0",end="")
        else:
            if(stack[i][1]>0):
                print("0",end="")
            else:
                print("1",end="")
    print()
    