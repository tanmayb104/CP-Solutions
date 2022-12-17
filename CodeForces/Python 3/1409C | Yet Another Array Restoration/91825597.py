for _ in range(int(input())):
  n,x,y=map(int,input().split())
  dif=y-x
  for i in range(n-1,-1,-1):
    if(dif%i==0):
      a=dif//i
      break
  print(y,end=" ")
  c=1
  for i in range(1,n):
    if(y-i*a>0):
      print(y-i*a,end=" ")
      c+=1
    else:
      break
  if(c!=n):
    for i in range(1,n-c+1):
      print(y+i*a,end=" ")
  print()