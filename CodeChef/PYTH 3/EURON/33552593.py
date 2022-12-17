# cook your dish here

def mergesort(arr):
    global c
    if(len(arr)==1):
        return arr
    l=mergesort(arr[:len(arr)//2])
    r=mergesort(arr[len(arr)//2:])
    a=[]
    i=0
    j=0
    while(i<len(l) and j<len(r)):
        if(l[i]<=r[j]):
            a.append(l[i])
            i+=1
        else:
            a.append(r[j])
            c+=len(l)-i
            j+=1
    while(i<len(l)):
        a.append(l[i])
        i+=1
    while(j<len(r)):
        a.append(r[j])
        j+=1
    return a
    

n=int(input())
l=[int(x) for x in input().split()]
c=0
a=mergesort(l)
print(c)