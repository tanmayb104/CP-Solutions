for _ in range(int(input())):
    n=int(input())
    l1=[int(x) for x in input().split()]
    l2=[int(x) for x in input().split()]
    s1=0
    s2=0
    c=0
    for i in range(n):
        if(s1==s2 and l1[i]==l2[i]):
            c+=l1[i]
        s1+=l1[i]
        s2+=l2[i]
    print(c)