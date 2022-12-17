for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    l=0
    r=n
    moves=0
    sum_l=0
    sum_r=0
    cur_l=0
    cur_r=0
    prev=0
    flag=0
    while(l<r):
        if(flag==0):
            moves += 1
            cur_l = 0
            while(cur_l <= prev and l < r):
                cur_l += a[l]
                l += 1
            prev = cur_l
            sum_l += cur_l
            flag = 1
        else:
            moves += 1
            cur_r = 0
            while (cur_r <= prev and l < r):
                r -= 1
                cur_r += a[r]
            prev = cur_r
            sum_r += cur_r
            flag = 0
    print(moves,sum_l,sum_r)