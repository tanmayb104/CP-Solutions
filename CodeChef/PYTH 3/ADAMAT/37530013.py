# cook your dish here
for _ in range(int(input())):
  n=int(input())
  l=[[int(x) for x in input().split()] for i in range(n)]
  a=[]
  for i in range(1,n):
    if(l[0][i]<l[i][0]):
      a.append(0)
    else:
      a.append(1)
  c=0
  flag=a[0]
  for i in range(len(a)):
    if(flag==1 and a[i]==1):
      continue
    elif(flag==1 and a[i]==0):
      c+=1
      flag=0
    elif(flag==0 and a[i]==0):
      continue
    else:
      flag=1
      c+=1
  if(flag):
    c+=1
  print(c)
