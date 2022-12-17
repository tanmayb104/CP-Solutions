from sys import stdout
 
n=int(input())
s=[-1 for x in range(n)]
r=2
l=1
 
while(r<=n):
  print("? "+str(l)+" "+str(r))
  stdout.flush()
  a=int(input())
 
  print("? "+str(r)+" "+str(l))
  stdout.flush()
  b=int(input())
 
  if(a==-1 or b==-1):
    exit()
 
  if(a>b):
    s[l-1]=a
    l=r
    r+=1
  else:
    s[r-1]=b
    r+=1
 
used = [False]*(n+1)
yet = -1
for i in range(n):
    if s[i] != -1:
        used[s[i]] = True
    else:
        yet = i
 
s[yet] = n
print("!",*s)
  
 