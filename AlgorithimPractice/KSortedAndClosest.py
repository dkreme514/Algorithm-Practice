import heapq
def kclosest(x, k, arr):
    maxPQ = []
    size = 0
    for v in arr:
        heapq.heappush(maxPQ, (-abs(x-v),v))
        if len(maxPQ) > k:
            heapq.heappop(maxPQ)

    return sorted(list(map(lambda x: x[1], maxPQ)))

def ksorted(k, arr):
    minPQ = arr[:k+1]
    heapq.heapify(minPQ(k))
    answer = []

    for i in range(k + 1, len(arr)):
        minPQ.heappush((arr[i]))
        answer.append(minPQ.heappop)

    while minPQ:
        answer.append(minPQ.heappop())

    return answer
