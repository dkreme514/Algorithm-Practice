# Greedy algorithm: Interval Partitioning

def minimumMeetingRooms(intervals):
    import heapq
    sortedIntervals = sorted(intervals,key=lambdax:x[0])
    pq=[]
    heapq.heappush(pq.sortedIntervals[0][1])

    for i in range(1,len(sortedIntervals)):
        cs = sortedIntervals[i][0]
        ce=sortedIntervals[i][1]
        ee=heapq.heappop(pq)
        if cs < ee:
            heapq.heappush(pq,ee)
        else:
            ee=ce
        heapq.heappush(pq,ee)

    return len(pq)