for _ in range(int(input())):
  n=int(input())
  l=[int(x) for x in input().split()]
  c0=0
  c1=0
  for i in range(n):
    if(l[i]==1):
      c1+=1
    else:
      c0+=1
  if(c0>=c1):
    print(c0)
    print(*([0]*c0))
  else:
    if(c1%2!=0):
      c1-=1
    print(c1)
    print(*([1]*c1))