# cook your dish here
t=int(input())
for _ in range(t):
    n= int(input())
    exp=input().strip()
    precedence={"^":3,"*":2,"/":2,"+":1,"-":1}
    oprts=[]
    ans=[]
    for s in exp:
        if s.isalnum():
            ans.append(s)
        elif s=='(':
            oprts.append(s)
        elif s==')':
            top=oprts.pop()
            while top!='(':
                ans.append(top)
                top=oprts.pop()
        else:
            while len(oprts)>0 and oprts[-1]!='(' and (precedence[oprts[-1]]>=precedence[s]):
                ans.append(oprts.pop())
            oprts.append(s)
    while len(oprts)>0:
        ans.append(oprts.pop())
    print("".join(ans))