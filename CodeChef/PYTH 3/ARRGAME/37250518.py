# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    flag=0
    c=0
    m=0
    arr=[]
    for i in range(n):
        if(l[i]==0 and not flag):
            flag=1
            c=1
        elif(l[i]==0 and flag):
            c+=1
        else:
            m=max(c,m)
            arr.append(c)
            flag=0
            c=0
    #print(m)
    arr.sort()
    if(len(arr)>1):
        m2=arr[-2]
    if(m%2==0):
        print("No")
        continue
    else:
        if(len(arr)==1):
            print("Yes")
        else:
            if(m//2<m2):
                print("No")
            else:
                print("Yes")