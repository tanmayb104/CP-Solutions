for _ in range(int(input())):
    n=input()
    len_n=len(n)
    ans=[]
    count=0
    for i in range(len(n)):
        if(n[i]=="0"):
            len_n-=1
            continue
        else:
            str=n[i]+"0"*(len_n-1)
            ans.append(str)
            count+=1
            len_n-=1
    print(count)
    print(*ans)
    
            