# cook your dish here
for _ in range(int(input())):
  n=int(input())
  l=[int(x) for x in input().split()]
  l.sort()
  if(l[0]==0):
    print(len(set(l))-1)
  else:
      print(len(set(l)))