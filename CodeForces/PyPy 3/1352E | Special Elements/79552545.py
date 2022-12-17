from collections import Counter
 
def subArraySum(arr, n, sum):
    curr_sum = arr[0]
    count = 1
    start = 0
    i = 1
    while i <= n:
        while (curr_sum > sum and start < i - 1):
            curr_sum = curr_sum - arr[start]
            count -= 1
            start += 1
        if (curr_sum == sum and count > 1):
            return 1
        if i < n:
            curr_sum = curr_sum + arr[i]
            count += 1
        i += 1
    return 0
 
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    s=set(a)
    co=Counter(a)
    c=0
    for i in s:
        if(subArraySum(a,n,i)):
            c+=co[i]
    print(c)