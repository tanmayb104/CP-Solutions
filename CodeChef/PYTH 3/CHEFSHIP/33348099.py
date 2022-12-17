# cook your dish here
for _ in range(int(input())):
    s=input()
    n=len(s)
    flag=0
    for i in range(2,n-1,2):
        if s[:i//2]==s[i//2:i] and s[i:i+(n-i)//2]==s[i+(n-i)//2:n]:
            flag+=1
    print(flag)