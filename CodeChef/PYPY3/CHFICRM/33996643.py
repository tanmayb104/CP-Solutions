for _ in range(int(input())):
    n=int(input())
    l = [int(x) for x in input().split()]
    m=[0,0]
    flag=0
    for i in range(n):
        if(l[i]==5):
            m[0]+=1
        else:
            if(l[i]==15):
                if(m[1]>0):
                    m[1]-=1
                elif(m[0]>1):
                    m[0]-=2
                else:
                    flag=1
                    break
            else:
                if(m[0]>0):
                    m[0]-=1
                    m[1]+=1
                else:
                    flag=1
                    break
    if(flag):
        print("NO")
    else:
        print("YES")