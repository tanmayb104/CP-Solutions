# cook your dish here
def lcm(a,b):
    if(a==0):
        return b
    else:
        return lcm(min(b-a,a),max(b-a,a))
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=lcm(min(a,b),max(a,b))
    print(c)
    