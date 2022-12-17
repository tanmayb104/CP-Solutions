# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    min_num=999
    max_num=1
    count=1
    for i in range(1,n):
        if(l[i]-l[i-1]<=2):
            count+=1
        else:
            min_num=min(min_num,count)
            max_num=max(max_num,count)
            count=1
    min_num=min(min_num,count)
    max_num=max(max_num,count)
    if(min_num>max_num):
        min_num=max_num
    print(min_num,max_num)