import heapq

def solve(A, n):
    p1 = A[0]

    minHeap = []
    for j in range(1, n):
        heapq.heappush(minHeap, (A[j], j+1))
    
    steps = []
    while len(minHeap) > 1:
        item = heapq.heappop(minHeap)
        if item[0] <= p1:
            p1 += item[0]
            steps.append([item[1], 1, item[0]])
        else:
            nextItem = heapq.heappop(minHeap)
            heapq.heappush(minHeap, (nextItem[0] + item[0] - p1, nextItem[1]))
            steps.append([item[1], nextItem[1], item[0] - p1])
            steps.append([item[1], 1, p1])
            p1 += p1            

    lastItem = heapq.heappop(minHeap)
    if lastItem[0] <= p1:
        steps.append([lastItem[1], 1, lastItem[0]])
    else:
        steps = []
    
    return steps


t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    result = solve(A, n)
    if len(result):
        print(len(result))
        for step in result:
            print(*step)
    else:
        print(-1)