for _ in range(int(input())):
    s=[int(x) for x in input()]
    one=s.count(1)
    zero=s.count(0)
    if(min(one,zero)%2==0):
        print("NET")
    else:
        print("DA")
    