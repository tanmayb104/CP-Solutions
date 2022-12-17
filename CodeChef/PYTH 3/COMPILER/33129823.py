# cook your dish here
for _ in range(int(input())):
    s=input()
    st=[]
    c=0
    for i in range(len(s)):
        if(s[i]=="<"):
            st.append(s[i])
        elif(s[i]==">"):
            if(len(st)==0):
                break
            st.pop()
        if(len(st)==0):
            c=i+1
    print(c)