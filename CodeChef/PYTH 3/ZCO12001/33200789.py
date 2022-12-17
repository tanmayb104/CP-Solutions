# cook your dish here
max_dep=0
max_dep_ind=0
max_sym=0
max_sym_ind=0
c=0
stack=[]
n=int(input())
l=[int(x) for x in input().split()]
for i in range(n): 
    
    if(l[i]==1):
        stack.append(1)
    else:
        if(len(stack)>max_dep):
            max_dep=len(stack)
            max_dep_ind=i
        stack.pop()
    
    
    if(len(stack)>0):
        c+=1
    else:
        if(max_sym<c):
            max_sym=c+1
            max_sym_ind=i-max_sym+2
        c=0
        
print(max_dep,max_dep_ind,max_sym,max_sym_ind)