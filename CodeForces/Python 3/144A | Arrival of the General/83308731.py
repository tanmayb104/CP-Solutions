n=int(input())
l=[int(x) for x in input().split()]
ma=max(l)
mi=min(l)
mai=l.index(ma)
l.reverse()
mii=l.index(mi)
if(mai>n-1-mii):
    print(mai-1+mii)
else:
    print(mai+mii)