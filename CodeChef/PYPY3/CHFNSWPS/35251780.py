from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l1=[int(x) for x in input().split()]
    l2=[int(x) for x in input().split()]
    l=l1+l2
    s=set(l)
    c=Counter(l)
    min_l=min(l)
    flag=0
    for i in s:
        if(c[i]%2==1):
            flag=1
    if(flag):
        print(-1)
    else:
        c1=Counter(l1)
        s1=set(l1)
        c2=Counter(l2)
        s2=set(l2)
        ans=0
        s3=s2-s1
        ele=[]
        for i in s1:
            if(c[i]//2!=c1[i]):
                ele+=[i]*abs(c[i]//2-c1[i])
        for i in s3:
            if(c[i]//2!=c2[i]):
                ele+=[i]*abs(c[i]//2-c2[i])
        #print(ele)
        if(len(ele)):
            ele.sort()
            s=0
            for i in range(len(ele)//2):
                s+=min(ele[i],2*min_l)
            print(s)
        else:
            print(0)


# 1 2 2 3 4 5 6 1 1 1 1
# 1 7 7 3 4 5 6 9 9 9 9
# c1=[1:5 2:2 3:1 4:1 5:1 6:1]           (1,2,3,4,5,6)
# c2=[1:1 7:2 3:1 4:1 5:1 6:1 9:4]       (1,3,4,5,6,7,9)
# c= [1:6 2:2 3:2 4:2 5:2 6:2 7:2 9:4]   (1,2,3,4,5,6,7,9)
