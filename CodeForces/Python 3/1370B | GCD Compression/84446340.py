for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    odd=[]
    even=[]
    for i in range(2*n):
        if(l[i]%2==0):
            even.append(i+1)
        else:
            odd.append(i+1)
    #print(odd,even)
    if(len(odd)%2==1):
        odd.pop()
        even.pop()
    else:
        if(len(odd)>=2):
            odd.pop()
            odd.pop()
        else:
            even.pop()
            even.pop()
    #print(odd,even)
    while(len(odd)):
        a=odd.pop()
        b=odd.pop()
        print(b,a)
    while(len(even)):
        a=even.pop()
        b=even.pop()
        print(b,a)
 
            