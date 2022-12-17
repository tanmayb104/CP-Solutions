for _ in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    s=sorted(arr,reverse=True)
    if(arr==s and len(set(arr))==n):
        print("NO")
    else:
        print("YES")