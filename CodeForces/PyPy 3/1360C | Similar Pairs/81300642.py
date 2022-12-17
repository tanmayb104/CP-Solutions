for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    #a1,b1=map(int,input().split())
    if(len(l)==2):
        if(l[0]%2==l[1]%2 or abs(l[0]-l[1])==1):
            print("YES")
        else:
            print("NO")
    else:
        even=[]
        odd=[]
        for i in range(n):
            if(l[i]%2==0):
                even.append(l[i])
            else:
                odd.append(l[i])
        if(len(even)%2==0 and len(odd)%2==0):
            print("YES")
        else:
            l.sort()
            flag=0
            for i in range(1,n):
                if(l[i]-l[i-1]==1):
                    flag=1
                    break
            if(flag==1):
                print("YES")
            else:
                print("NO")